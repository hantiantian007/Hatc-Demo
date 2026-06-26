import glob
import re

files = glob.glob("Crm-Group/admin-*.html")
menu_item = """
                <div class="px-4 py-2 mt-2 text-xs font-semibold text-gray-400 uppercase tracking-wider">
                    系统设置
                </div>
                <a href="admin-tag-management.html" class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors group">
                    <i class="fa-solid fa-tags w-5 text-center mr-3 group-hover:text-blue-400 transition-colors"></i>
                    <span class="font-medium text-sm">标签管理</span>
                </a>
"""

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "标签管理" not in content and "</nav>" in content:
        content = content.replace("</nav>", menu_item + "        </nav>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

