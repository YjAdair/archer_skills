import json
import sys
import os
import argparse
from datetime import datetime

def get_color(name):
    if "巴菲特" in name or "Buffett" in name:
        return "green"
    elif "盖茨" in name or "Gates" in name:
        return "blue"
    elif "马斯克" in name or "Musk" in name:
        return "red"
    elif "乔布斯" in name or "Jobs" in name:
        return "purple"
    else:
        return "gray"

def get_icon(name):
    if "巴菲特" in name: return "🎩"
    if "盖茨" in name: return "💻"
    if "马斯克" in name: return "🚀"
    if "乔布斯" in name: return "🍎"
    return "👤"

def generate_html_snippets(data):
    snippets = {}

    # 1. Advisors HTML (Cover Page)
    advisors_html = ""
    for advisor in data.get('advisors', []):
        color = get_color(advisor['name'])
        advisors_html += f"""
            <div class="flex items-center gap-2">
                <div class="w-2 h-2 rounded-full bg-{color}-600"></div>
                <span class="text-sm text-gray-600">{advisor['name']}</span>
            </div>
        """
    snippets['advisors_html'] = advisors_html

    # 2. Problem Background HTML
    # Converting paragraphs to <p> tags
    bg_text = data.get('problem_overview', {}).get('background', '')
    snippets['problem_background_html'] = "".join([f'<p class="mb-6">{p.strip()}</p>' for p in bg_text.split('\n') if p.strip()])

    # 3. Goals HTML
    goals_html = ""
    for goal in data.get('problem_overview', {}).get('goals', []):
        goals_html += f"""
            <li class="flex items-start gap-3">
                <span class="text-green-600 mt-1">◆</span>
                <span>{goal}</span>
            </li>
        """
    snippets['goals_html'] = goals_html

    # 4. Insights HTML
    insights_html = ""
    insights = data.get('key_insights', [])
    icons = ["💡", "🔍", "⚡", "🌟"]
    for i, insight in enumerate(insights):
        icon = icons[i % len(icons)]
        insights_html += f"""
        <div class="p-6 bg-white rounded-lg shadow-sm border border-gray-100">
            <div class="flex items-center gap-3 mb-4">
                <span class="text-2xl">{icon}</span>
                <h3 class="text-lg font-semibold text-gray-800">{insight.get('title', '洞察')}</h3>
            </div>
            <p class="text-gray-600 breathing-space">{insight.get('content', '')}</p>
        </div>
        """
    snippets['insights_html'] = insights_html

    # 5. Advisor Pages HTML
    advisor_pages_html = ""
    for advisor in data.get('advisor_suggestions', []):
        name = advisor.get('name', '幕僚')
        color = get_color(name)
        icon = get_icon(name)
        title = advisor.get('title', '私董会幕僚')
        
        # Suggestions list
        suggestions_html = ""
        for i, sugg in enumerate(advisor.get('suggestions', [])):
            suggestions_html += f"""
            <div class="flex items-start gap-3">
                <span class="bg-{color}-600 text-white text-xs px-2 py-1 rounded font-medium">{i+1}</span>
                <p class="text-gray-600">{sugg}</p>
            </div>
            """

        advisor_pages_html += f"""
        <!-- 幕僚建议页 - {name} -->
        <article class="magazine-page shadow-2xl mx-auto mb-12 p-16">
            <header class="mb-8 pb-6 border-b-2 border-{color}-600">
                <div class="flex items-center gap-4">
                    <div class="w-12 h-12 rounded-full bg-{color}-100 flex items-center justify-center">
                        <span class="text-2xl">{icon}</span>
                    </div>
                    <div>
                        <h2 class="text-2xl font-bold text-gray-800">{name}</h2>
                        <p class="text-sm text-gray-500">{title}</p>
                    </div>
                </div>
            </header>

            <!-- 名言金句 -->
            <blockquote class="border-l-4 border-{color}-600 pl-6 my-8 bg-{color}-50 py-4 rounded-r-lg">
                <p class="text-xl font-medium italic text-gray-700">
                    「{advisor.get('quote', '')}」
                </p>
            </blockquote>

            <!-- 问题定性 -->
            <div class="my-8">
                <h3 class="text-lg font-semibold text-gray-700 mb-3 flex items-center gap-2">
                    <span class="text-{color}-600">◎</span> 问题定性
                </h3>
                <p class="text-gray-600 breathing-space pl-6">
                    {advisor.get('definition', '')}
                </p>
            </div>

            <!-- 经历分享 -->
            <div class="my-8 p-6 bg-gray-50 rounded-lg">
                <h3 class="text-lg font-semibold text-gray-700 mb-3">📖 经历分享</h3>
                <p class="text-gray-600 breathing-space">
                    {advisor.get('experience', '')}
                </p>
            </div>

            <!-- 具体建议 -->
            <div class="my-8">
                <h3 class="text-lg font-semibold text-gray-700 mb-4 flex items-center gap-2">
                    <span class="text-{color}-600">◎</span> 具体建议
                </h3>
                <div class="space-y-3 pl-6">
                    {suggestions_html}
                </div>
            </div>
        </article>
        """
    snippets['advisor_pages_html'] = advisor_pages_html

    # 6. Reflections HTML
    reflections_html = ""
    for reflection in data.get('reflections', []):
        name = reflection.get('name', '')
        color = get_color(name)
        reflections_html += f"""
        <div class="p-6 bg-white rounded-lg shadow-sm border-l-4 border-{color}-600">
            <h3 class="text-lg font-bold text-gray-800 mb-2">{name}的反思</h3>
            <div class="text-gray-600 breathing-space space-y-2">
               {reflection.get('content', '').replace(chr(10), '<br>')}
            </div>
        </div>
        """
    snippets['reflections_html'] = reflections_html

    # 7. Action Items HTML
    action_items_html = ""
    for item in data.get('action_plan', {}).get('action_items', []):
        action_items_html += f"""
        <div class="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-200">
            <div class="w-6 h-6 rounded border-2 border-gray-300"></div>
            <div class="flex-1">
                <p class="text-gray-700 font-medium">{item.get('item', '')}</p>
                <p class="text-sm text-gray-500">截止日期：{item.get('deadline', '立即执行')}</p>
            </div>
        </div>
        """
    snippets['action_items_html'] = action_items_html

    # 8. Timeline HTML
    timeline_html = ""
    for item in data.get('action_plan', {}).get('timeline', []):
        timeline_html += f"""
        <div class="flex items-center gap-4 p-4 bg-white rounded-lg border border-gray-200">
            <div class="w-6 h-6 rounded border-2 border-gray-300"></div>
            <div class="flex-1">
                <p class="text-gray-700 font-medium">{item.get('milestone', '')}</p>
                <p class="text-sm text-gray-500">截止日期：{item.get('date', '')}</p>
            </div>
        </div>
        """
    snippets['timeline_html'] = timeline_html

    # 9. Golden Sentences HTML
    golden_sentences_html = ""
    for item in data.get('golden_sentences', []):
        name = item.get('advisor', '')
        color = get_color(name)
        golden_sentences_html += f"""
        <div class="text-center">
            <p class="text-2xl font-serif italic text-gray-700 mb-4">"{item.get('sentence', '')}"</p>
            <div class="inline-block px-3 py-1 bg-{color}-100 text-{color}-700 text-sm rounded-full">
                {name}
            </div>
        </div>
        """
    snippets['golden_sentences_html'] = golden_sentences_html

    return snippets

def generate_report(data_path, output_path):
    # Resolve paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, '..', 'assets', 'report_template.html')
    
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        sys.exit(1)
        
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        sys.exit(1)

    # Read data
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading data file: {e}")
        sys.exit(1)

    # Generate HTML Snippets
    snippets = generate_html_snippets(data)

    # Read template
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except Exception as e:
        print(f"Error reading template file: {e}")
        sys.exit(1)

    # Replace placeholders
    content = template
    
    # Simple strings
    content = content.replace('{{ topic }}', data.get('topic', '私董会报告'))
    content = content.replace('{{ sub_topic }}', data.get('sub_topic', ''))
    content = content.replace('{{ date }}', data.get('date', datetime.now().strftime('%Y年%m月%d日')))
    content = content.replace('{{ problem_quote }}', data.get('problem_overview', {}).get('quote', ''))
    content = content.replace('{{ core_takeaway }}', data.get('action_plan', {}).get('core_takeaway', ''))
    content = content.replace('{{ user_name }}', data.get('user_name', '案主'))
    content = content.replace('{{ closing_message }}', data.get('closing_message', '感谢您的参与'))

    # HTML Snippets
    for key, html in snippets.items():
        content = content.replace(f'{{{{ {key} }}}}', html)

    # Write output
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Report generated successfully at {output_path}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Private Board of Directors Report')
    parser.add_argument('--data', required=True, help='Path to JSON data file')
    parser.add_argument('--output', required=True, help='Path to output HTML file')
    
    args = parser.parse_args()
    generate_report(args.data, args.output)
