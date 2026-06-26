import glob
import re
import os

def update_menu():
    old_tag_menu_pattern = r'<div class="px-4 py-2 mt-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">\s*系统设置\s*</div>\s*<a href="admin-tag-management\.html" class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors group">\s*<i class="fa-solid fa-tags w-5 text-center mr-3 group-hover:text-blue-400 transition-colors"></i>\s*<span class="font-medium text-sm">标签管理</span>\s*</a>'
    insert_target_pattern = r'(<a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">验证码记录</a>)'
    new_tag_menu_item = r'\1\n                    <a href="admin-tag-management.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">标签管理</a>'

    files = glob.glob('CRM-HK/admin-*.html')
    for filepath in files:
        if filepath == 'CRM-HK/admin-leads-list.html':
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Remove old tag menu
        content = re.sub(old_tag_menu_pattern, '', content, flags=re.DOTALL)
        
        # Insert new tag menu
        if '标签管理</a>' not in content:
            content = re.sub(insert_target_pattern, new_tag_menu_item, content, flags=re.DOTALL)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes needed for {filepath}")

if __name__ == '__main__':
    update_menu()
