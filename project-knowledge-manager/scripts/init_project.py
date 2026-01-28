#!/usr/bin/env python3
import os
import shutil
import sys

def init_project(target_dir=None):
    if target_dir is None:
        target_dir = os.getcwd()
    
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 模板文件路径 (假设 assets 在 scripts 的上一级的 assets 目录)
    template_path = os.path.join(script_dir, '..', 'assets', 'cloudy_template.md')
    
    target_path = os.path.join(target_dir, 'cloudy.md')
    
    if os.path.exists(target_path):
        print(f"Warning: {target_path} already exists. Skipping initialization.")
        return
    
    try:
        shutil.copy2(template_path, target_path)
        print(f"Successfully initialized cloudy.md at {target_path}")
    except Exception as e:
        print(f"Error initializing cloudy.md: {e}")
        sys.exit(1)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else None
    init_project(target_dir)
