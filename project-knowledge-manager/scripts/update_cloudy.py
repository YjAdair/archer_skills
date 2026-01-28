#!/usr/bin/env python3
import os
import sys
import argparse
import re

def update_cloudy(section, content, file_path='cloudy.md'):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please run project initialization first.")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    # 简单的章节匹配逻辑：查找 "## [Section Name]" 或 "## [Index]. [Section Name]"
    # 例如 "## 1. 项目规范" 或 "## 项目规范"
    section_pattern = re.compile(fr'^##\s+(\d+\.\s+)?{re.escape(section)}')
    
    insert_idx = -1
    for i, line in enumerate(lines):
        if section_pattern.match(line):
            # 找到章节头
            # 继续寻找下一个章节头或文件结束
            for j in range(i + 1, len(lines)):
                if line.startswith('## '):
                    insert_idx = j
                    break
            else:
                # 文件结束
                insert_idx = len(lines)
            break
            
    if insert_idx == -1:
        print(f"Error: Section '{section}' not found in {file_path}.")
        sys.exit(1)
        
    # 在下一章节之前插入内容
    # 如果前一行不是空行，插入一个换行符
    new_lines = []
    if not content.endswith('\n'):
        content += '\n'
    
    # 如果插入点前一行不是空行，加一个空行
    if insert_idx > 0 and lines[insert_idx-1].strip() != '':
        new_lines.append('\n')
        
    new_lines.append(content)
    
    lines[insert_idx:insert_idx] = new_lines
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
        
    print(f"Successfully updated section '{section}' in {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update cloudy.md sections')
    parser.add_argument('--section', required=True, help='Section name to update (e.g., "项目规范")')
    parser.add_argument('--content', required=True, help='Content to append')
    parser.add_argument('--file', default='cloudy.md', help='Path to cloudy.md file')
    
    args = parser.parse_args()
    update_cloudy(args.section, args.content, args.file)
