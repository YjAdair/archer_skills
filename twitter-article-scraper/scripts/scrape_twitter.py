import os
import time
import re
import argparse
import random
import sys
from datetime import datetime, time as dtime
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import markdownify

# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- CONFIGURATION ---
CONFIG = {
    # 1. List of Bloggers (Twitter Handle -> Custom Folder Name)
    # Format: {"handle": "Custom Name"} or just "handle" (will use handle as name)
    # Example: {"dotey": "宝玉", "elonmusk": "Elon Musk"}
    "usernames": [
        {"dotey": "宝玉"}, 
        {"op7418": "歸藏"},
        {"RookieRicardoR": "耳朵"}
        # Add more usernames here
    ],

    # 2. Scheduled Time Windows (List of Start and End times in 24h format)
    # The script will only execute scraping if current time is within ANY of these windows.
    # Format: [{"start": "HH:MM", "end": "HH:MM"}, ...]
    "schedule_windows": [
        {"start": "07:30", "end": "12:00"}, # 晨读时间
        {"start": "12:00", "end": "18:30"}, # 午休时间
        {"start": "19:00", "end": "23:00"}  # 晚间阅读
    ],
    
    # 3. Reading Behavior Simulation
    # Articles per session: Randomly pick between min and max articles to scrape per blogger
    "articles_per_session_range": (5, 10),
    
    # Reading Speed (Words per minute)
    # Used to calculate dynamic waiting time based on article length
    "reading_speed_wpm": 250, 
    # Minimum reading time (seconds) - even for short articles
    "min_reading_time": 15,
    # Maximum reading time (seconds) - cap for very long articles to avoid timeouts
    "max_reading_time": 180,

    # 4. Time Interval Ranges (Seconds)
    # Random wait between scraping individual articles (Transition time)
    "scrape_interval_range": (5, 15), 
    # Random wait between processing different bloggers
    "blogger_interval_range": (30, 90),
    
    # 5. Storage Path
    # Articles will be saved in: output_dir/{username}/{date}_{title}.md
    # Default: 'articles' folder in the script directory
    
    # "output_dir": os.path.join(SCRIPT_DIR, "articles"),
    "output_dir": "/Users/yadmin/Library/Mobile Documents/com~apple~CloudDocs/Knowledge/03 资源/01 待归档/AI/Twitter博主",
    
    # Google Chrome Profile Path
    # Use a persistent user data directory to save login state.
    # Default: 'chrome_profile' folder in the script directory
    "user_data_dir": os.path.join(SCRIPT_DIR, "chrome_profile"),
    
    # Browser Channel
    # "chrome" for Google Chrome, "msedge" for Edge, or None for bundled Chromium
    "channel": "chrome"
}
# ---------------------

def clean_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title).strip()

def load_local_history(blogger_dir):
    """
    Loads local article history for deduplication.
    Returns a set of filenames (or identifier keys) that already exist.
    """
    if not os.path.exists(blogger_dir):
        return set()
        
    files = os.listdir(blogger_dir)
    history = set()
    for f in files:
        if f.endswith(".md"):
            history.add(f)
    return history

def get_latest_local_date(blogger_dir):
    """
    Finds the latest date among the markdown files in the blogger's directory.
    Assumes filename format: YYYY-MM-DD_Title.md
    """
    if not os.path.exists(blogger_dir):
        return None
        
    files = os.listdir(blogger_dir)
    dates = []
    for f in files:
        if f.endswith(".md"):
            match = re.match(r"(\d{4}-\d{2}-\d{2})_", f)
            if match:
                dates.append(match.group(1))
    
    if dates:
        dates.sort(reverse=True)
        return dates[0]
    return None

def is_within_schedule(windows):
    """
    Checks if current time is within any of the provided start and end time windows.
    windows: List of dicts, e.g. [{"start": "08:00", "end": "12:00"}]
    """
    now = datetime.now().time()
    
    for window in windows:
        start_str = window.get("start")
        end_str = window.get("end")
        
        try:
            start = datetime.strptime(start_str, "%H:%M").time()
            end = datetime.strptime(end_str, "%H:%M").time()
        except ValueError:
            print(f"Invalid time format in config: {start_str} - {end_str}")
            continue
            
        is_in_window = False
        if start <= end:
            is_in_window = start <= now <= end
        else: # Crosses midnight
            is_in_window = start <= now or now <= end
            
        if is_in_window:
            return True
            
    return False

def human_like_delay(min_sec, max_sec, description="等待中"):
    delay = random.uniform(min_sec, max_sec)
    print(f"[{description}] 随机等待 {delay:.2f} 秒...")
    time.sleep(delay)

def human_like_scroll(page):
    """
    Simulates human-like scrolling.
    """
    try:
        # Scroll down a bit
        for _ in range(random.randint(2, 5)):
            page.mouse.wheel(0, random.randint(100, 500))
            time.sleep(random.uniform(0.5, 1.5))
        # Maybe scroll up a tiny bit
        if random.random() > 0.7:
             page.mouse.wheel(0, -random.randint(50, 200))
             time.sleep(random.uniform(0.5, 1.0))
    except Exception:
        pass

def scrape_article_content(page, url=None):
    if url:
        print(f"正在加载文章: {url}")
        page.goto(url)
    else:
        print("正在解析当前页面内容...")
    
    try:
        page.wait_for_selector('article', state='attached', timeout=15000)
        human_like_delay(2, 4, "加载动态内容")
        human_like_scroll(page) # Simulate reading
    except Exception as e:
        print(f"等待文章内容加载失败: {e}")
        return None

    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')
    
    article_node = soup.find('article')
    if not article_node:
        print("未找到 <article> 标签。")
        return None

    # Extract Title
    title = page.title().replace(" / X", "").strip()
    h1 = article_node.find('h1')
    if h1:
        title = h1.get_text(strip=True)

    # Extract Date
    date_str = datetime.now().strftime('%Y-%m-%d')
    time_node = article_node.find('time')
    if time_node and hasattr(time_node, 'has_attr') and time_node.has_attr('datetime'):
        dt_str = time_node['datetime']
        if isinstance(dt_str, list):
            dt_str = dt_str[0]
        try:
            dt = datetime.fromisoformat(str(dt_str).replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d')
        except ValueError:
            pass

    # Process Video/Images
    if hasattr(article_node, 'find_all'):
        videos = article_node.find_all('video')
        for video in videos:
            poster = video.get('poster')
            src = video.get('src')
            video_md = f"\n\n**[视频内容]**\n"
            if poster:
                video_md += f"![视频封面]({poster})\n"
            if src:
                video_md += f"[视频链接]({src})\n"
            
            new_tag = soup.new_tag("div")
            new_tag.string = video_md
            video.replace_with(new_tag)

    md_content = markdownify.markdownify(str(article_node), heading_style="ATX")
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    # Calculate word count for reading time simulation
    # Simple estimation: split by spaces
    word_count = len(md_content.split())
    
    return {
        'title': title,
        'date': date_str,
        'content': md_content,
        'url': page.url,
        'word_count': word_count
    }

def ensure_login(page):
    """
    Checks if user is logged in. If not, waits for manual login.
    Uses wait_for_selector for efficiency instead of polling loops.
    """
    print("正在检查登录状态...")
    
    # 1. Fast check: Are we already logged in?
    try:
        # Check for Account Switcher (bottom left usually) which indicates login
        page.wait_for_selector('[data-testid="SideNav_AccountSwitcher_Button"]', state='attached', timeout=5000)
        print("状态: 已登录。")
        return True
    except:
        pass # Not found, proceed to wait
        
    # 2. Not logged in: Wait for user action
    print(">>> 需要登录 <<<")
    print("请在弹出的浏览器窗口中手动登录 Twitter。")
    print("脚本正在等待登录完成 (最长等待 5 分钟)...")
    
    try:
        # Efficiently wait for the element to appear. 
        # This pushes the waiting to the browser driver, avoiding CPU/Memory spinning in Python.
        page.wait_for_selector('[data-testid="SideNav_AccountSwitcher_Button"]', state='attached', timeout=300000)
        print("检测到登录成功！继续执行...")
        return True
    except Exception as e:
        print(f"登录等待超时。请重试。错误信息: {e}")
        return False

def process_blogger(context, page, blogger_info):
    # Parse blogger info
    if isinstance(blogger_info, dict):
        handle = list(blogger_info.keys())[0]
        display_name = list(blogger_info.values())[0]
    else:
        handle = str(blogger_info)
        display_name = str(blogger_info)

    target_url = f"https://x.com/{handle}/articles"
    blogger_dir = os.path.join(CONFIG["output_dir"], display_name)
    
    if not os.path.exists(blogger_dir):
        os.makedirs(blogger_dir)
        
    print(f"--- 正在处理博主: {display_name} (@{handle}) ---")
    print(f"目标 URL: {target_url}")
    print(f"输出目录: {blogger_dir}")
    
    try:
        page.goto(target_url)
        human_like_delay(2, 5, "页面加载")
    except Exception as e:
        print(f"页面加载失败: {e}")
        return

    # Check for "Articles" tab or content.
    # Note: Login check is now handled globally in main(), so we assume we are logged in.
    # But sometimes session might expire or navigation fails.
    
    # Fetch list
    try:
        print("正在等待文章列表加载...")
        page.wait_for_selector('article', timeout=15000)
    except:
        print(f"未找到博主 {display_name} 的文章或页面加载失败。")
        # Optional: Double check if we were logged out?
        if page.locator('[data-testid="login"]').count() > 0:
             print("检测到登录失效。停止处理。")
             return
        return

    # Load local history for deduplication
    local_history = load_local_history(blogger_dir)
    print(f"本地已归档 {len(local_history)} 篇文章。")

    # Scroll & Scan Loop
    # We need to find N *new* articles.
    # We will scroll and collect potential targets until we have enough NEW ones.
    
    min_arts, max_arts = CONFIG["articles_per_session_range"]
    session_target_count = random.randint(min_arts, max_arts)
    print(f"计划本轮寻找并阅读 {session_target_count} 篇新文章。")
    
    scraped_count = 0
    consecutive_duplicates = 0
    max_scroll_attempts = 20 # Prevent infinite scroll
    
    # We'll maintain a list of visited/checked article IDs (or indices) to avoid reprocessing in this session
    # But since DOM changes on scroll, index is unreliable.
    # We'll use a set of seen text content or timestamp as session-dedup key.
    session_seen_keys = set()
    
    scroll_attempts = 0
    consecutive_no_new = 0 # Count scrolls that produced NO new candidates
    
    while scraped_count < session_target_count and scroll_attempts < max_scroll_attempts:
        # Get all visible articles
        articles = page.locator('article').all()
        
        new_candidates = []
        found_new_on_screen = False
        
        for article in articles:
            # Extract key info to check against history without clicking
            # Time element is the best identifier
            try:
                time_el = article.locator('time').first
                if time_el.count() == 0:
                    continue
                    
                dt_str = time_el.get_attribute('datetime')
                # Parse date to match filename format YYYY-MM-DD
                # This is an approximation. Filename also has title.
                # Ideally we check if we have a file starting with this date.
                # But title is cleaner. Let's try to get title text.
                
                # Title often in a specific span or role="heading"? 
                # Twitter structure varies. Usually checking if we have *processed* this exact element is hard.
                # Let's assume we click it.
                
                # Better approach:
                # We can't easily know the full title without entering.
                # BUT we can check if the article date is very old compared to our latest local date?
                # Or we just assume we need to process it.
                
                # To support "Scroll until new", we need to know if it's old.
                # Let's use the timestamp.
                
                if not dt_str:
                    continue
                    
                dt = datetime.fromisoformat(str(dt_str).replace('Z', '+00:00'))
                date_str = dt.strftime('%Y-%m-%d')
                
                # Unique key for this session (to avoid clicking same element twice in current run)
                # Using timestamp + some text content as key
                text_preview = article.inner_text()[:50]
                session_key = f"{date_str}_{text_preview}"
                
                if session_key in session_seen_keys:
                    continue
                
                # Check if we already have files with this date?
                # This is a loose check. Multiple articles can be on same day.
                # If we have a file with this date, we might have read it.
                # But to be safe (since title check is hard), we might have to click it?
                # Optimization: If date_str is older than latest_local_date, and we trust chronological order,
                # we can skip.
                # But user asked to skip "already read".
                
                # Let's proceed to click if we haven't seen it this session.
                # We will do strict deduplication AFTER scraping title.
                
                session_seen_keys.add(session_key)
                new_candidates.append(article)
                found_new_on_screen = True
                
            except Exception as e:
                continue
        
        if found_new_on_screen:
            consecutive_no_new = 0
        else:
            consecutive_no_new += 1
            
        if consecutive_no_new >= 3:
            print("连续 3 次滚动未发现新内容，可能已到达列表底部。")
            break
        
        if not new_candidates:
            print("当前屏幕未发现更多新候选文章，向下滚动...")
            human_like_scroll(page)
            page.wait_for_timeout(2000)
            scroll_attempts += 1
            continue
            
        print(f"当前屏幕发现 {len(new_candidates)} 个潜在未处理文章。")
        
        # Process candidates
        for article_locator in new_candidates:
            if scraped_count >= session_target_count:
                break
                
            print(f"\n正在处理第 {scraped_count + 1}/{session_target_count} 篇新文章...")
            
            # Scroll into view
            try:
                article_locator.scroll_into_view_if_needed()
                time.sleep(1)
                
                # Click logic
                clickable = article_locator.locator("time")
                if clickable.count() > 0:
                    clickable.first.click()
                else:
                    article_locator.click()
                    
                page.wait_for_load_state("domcontentloaded")
                
                # Scrape
                data = scrape_article_content(page)
                
                if data:
                    article_date = data['date']
                    safe_title = clean_filename(data['title'])
                    filename = f"{article_date}_{safe_title}.md"
                    
                    if filename in local_history:
                        print(f"文章已存在本地历史中: {filename}。跳过并返回。")
                        consecutive_duplicates += 1
                    else:
                        # New article!
                        print("发现新文章！")
                        # Simulate reading only for NEW articles
                        
                        # Calculate dynamic reading time
                        wpm = CONFIG["reading_speed_wpm"]
                        word_count = data.get('word_count', 500)
                        base_reading_time = (word_count / wpm) * 60
                        min_time = CONFIG["min_reading_time"]
                        max_time = CONFIG["max_reading_time"]
                        variance = random.uniform(0.8, 1.2)
                        actual_reading_time = base_reading_time * variance
                        actual_reading_time = max(min_time, min(actual_reading_time, max_time))
                        
                        human_like_delay(actual_reading_time, actual_reading_time, f"模拟阅读 ({word_count} 字)")
                        
                        # Save
                        filepath = os.path.join(blogger_dir, filename)
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(f"# {data['title']}\n\n")
                            f.write(f"**日期:** {article_date}\n")
                            f.write(f"**URL:** {data['url']}\n\n")
                            f.write(data['content'])
                        
                        print(f"已保存: {filename}")
                        local_history.add(filename) # Add to current history
                        scraped_count += 1
                        consecutive_duplicates = 0
                
                # Back to list
                print("返回文章列表...")
                page.go_back()
                page.wait_for_selector('article', timeout=15000)
                
                # If we hit too many duplicates in a row, maybe we reached old history?
                # But user wants to "find unread", so we should keep looking until we find N new ones or hit limit.
                # We'll just continue.
                
            except Exception as e:
                print(f"处理文章时发生错误: {e}")
                if "articles" not in page.url:
                    page.go_back()
                continue
        
        # After processing candidates, scroll down to find more if needed
        if scraped_count < session_target_count:
            print("本轮目标尚未达成，继续向下滚动寻找新文章...")
            human_like_scroll(page)
            page.wait_for_timeout(2000)
            scroll_attempts += 1

    if scraped_count >= session_target_count:
        print(f"已完成本轮阅读目标 ({scraped_count} 篇新文章)。")
    elif consecutive_no_new >= 3:
        print(f"警告：未达到阅读目标 (目标: {session_target_count}, 实际: {scraped_count})，因为已到达列表底部或无法找到更多新文章。")
    else:
        print(f"已达到最大滚动次数，本次共找到 {scraped_count} 篇新文章。")

def main():
    # 1. Schedule Check
    if not is_within_schedule(CONFIG["schedule_windows"]):
        print(f"当前时间不在允许的运行时间段内: {CONFIG['schedule_windows']}。程序退出。")
        return

    # 2. Setup output
    if not os.path.exists(CONFIG["output_dir"]):
        os.makedirs(CONFIG["output_dir"])

    # 3. Launch Browser with Persistent Context
    print("正在启动浏览器 (加载用户配置文件)...")
    print(f"用户数据目录: {CONFIG['user_data_dir']}")
    
    with sync_playwright() as p:
        # Ensure user data dir exists
        if not os.path.exists(CONFIG["user_data_dir"]):
            os.makedirs(CONFIG["user_data_dir"])
            
        browser_args = [
            "--disable-blink-features=AutomationControlled", # Reduce detection
            "--start-maximized",
            "--disable-extensions", # Reduce memory usage
            "--no-sandbox", # Sometimes improves stability
            "--disable-dev-shm-usage" # Prevent memory crashes in some envs
        ]
        
        try:
            context = p.chromium.launch_persistent_context(
                user_data_dir=CONFIG["user_data_dir"],
                headless=False,
                channel=CONFIG["channel"],
                args=browser_args,
                viewport=None # Use window size
            )
            
            # Anti-detection script
            js = """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            """
            context.add_init_script(js)
            
        except Exception as e:
            print(f"启动 Chrome 失败: {e}")
            print("请确保没有其他 Chrome 窗口正在使用此配置文件。")
            return

        page = context.pages[0] if context.pages else context.new_page()
        
        # 5. Global Login Check
        # Perform login check once before processing any bloggers.
        # This is more efficient than checking inside the loop.
        try:
            page.goto("https://x.com/home")
            if not ensure_login(page):
                print("登录失败或超时。程序退出。")
                context.close()
                return
        except Exception as e:
            print(f"初始登录检查期间发生错误: {e}")
            context.close()
            return

        # 6. Process Bloggers
        blogger_list = CONFIG["usernames"]
        for i, blogger_info in enumerate(blogger_list):
            process_blogger(context, page, blogger_info)
            
            # Wait between bloggers
            if i < len(blogger_list) - 1:
                human_like_delay(*CONFIG["blogger_interval_range"], "切换博主间隙")
        
        print("所有任务已完成。")
        # context.close() # Optional: keep open if you want to inspect, but script ends here.
        context.close()

if __name__ == "__main__":
    main()
