import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the "规划中需求" section
planning_section = soup.find(lambda tag: tag.name == "h2" and "规划中需求" in tag.get_text())
if planning_section:
    tbody = planning_section.find_parent('div', class_='bg-white').find('tbody')
    
    task1_html = """
<tr class="table-row-hover bg-white border-l-4 border-[#8B5CF6]">
<td class="px-5 py-4 font-medium text-gray-900 whitespace-nowrap">官网模块</td>
<td class="px-5 py-4 font-bold text-gray-800 whitespace-nowrap">商品购买引流入口</td>
<td class="px-5 py-4 text-gray-500">在官网双端新增“商品购买”按钮，支持重定向至CRM登录页，并在登录后自动跳转至增值服务商品列表页。</td>
<td class="px-5 py-4">
<div class="flex flex-col gap-1">
<span class="inline-block px-2 py-0.5 text-[11px] rounded tag-group w-max">Group</span>
<span class="inline-block px-2 py-0.5 text-[11px] rounded tag-hk w-max">CRM-HK</span>
</div>
</td>
<td class="px-5 py-4 text-center font-medium text-gray-800 relative group whitespace-nowrap">
<div class="view-mode flex items-center justify-center gap-2">
<span class="date-text" data-task="商品购买引流入口">待定</span>
<button class="text-blue-500 hover:text-blue-700 opacity-0 group-hover:opacity-100 transition-opacity" onclick="toggleEdit('商品购买引流入口')" title="修改时间"><i class="fas fa-edit"></i></button>
</div>
<div class="edit-mode hidden items-center justify-center gap-1" id="edit-商品购买引流入口">
<input class="border border-gray-300 rounded px-2 py-1 w-24 text-sm date-input text-center font-normal" data-task="商品购买引流入口" type="text" value="待定"/>
<button class="text-green-500 hover:text-green-700" onclick="saveDate('商品购买引流入口')" title="保存"><i class="fas fa-check"></i></button>
<button class="text-gray-400 hover:text-gray-600" onclick="cancelEdit('商品购买引流入口')" title="取消"><i class="fas fa-times"></i></button>
</div>
</td>
<td class="px-5 py-4">
<div class="flex flex-col gap-2">
<div class="flex flex-wrap gap-2 items-center">
<a href="Group-Gw/index.html" target="_blank" class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-50 hover:bg-blue-100 rounded transition-colors flex items-center gap-1 border border-blue-200">
<i class="fas fa-globe"></i> Group 官网
</a>
<a href="Hk-Gw/index.html" target="_blank" class="px-3 py-1.5 text-xs font-medium text-blue-700 bg-blue-50 hover:bg-blue-100 rounded transition-colors flex items-center gap-1 border border-blue-200">
<i class="fas fa-globe"></i> HK 官网
</a>
</div>
</div>
</td>
</tr>
    """
    
    task2_html = """
<tr class="table-row-hover bg-white border-l-4 border-[#8B5CF6]">
<td class="px-5 py-4 font-medium text-gray-900 whitespace-nowrap">商品展示</td>
<td class="px-5 py-4 font-bold text-gray-800 whitespace-nowrap">商品展示及购买流程</td>
<td class="px-5 py-4 text-gray-500">
    <p>新增独立的商品详情页。支持未登录/未注册用户通过官网导流，强关联 CRM 登录/注册环节实现购买闭环。</p>
    <p class="mt-1 text-xs text-gray-400">本次新增：商品列表页、CRM钱包扣款支付结果页</p>
</td>
<td class="px-5 py-4">
<div class="flex flex-col gap-1">
<span class="inline-block px-2 py-0.5 text-[11px] rounded tag-group w-max">Group(含HK)/官网</span>
</div>
</td>
<td class="px-5 py-4 text-center font-medium text-gray-800 relative group whitespace-nowrap">
<div class="view-mode flex items-center justify-center gap-2">
<span class="date-text" data-task="商品展示及购买流程">待定</span>
<button class="text-blue-500 hover:text-blue-700 opacity-0 group-hover:opacity-100 transition-opacity" onclick="toggleEdit('商品展示及购买流程')" title="修改时间"><i class="fas fa-edit"></i></button>
</div>
<div class="edit-mode hidden items-center justify-center gap-1" id="edit-商品展示及购买流程">
<input class="border border-gray-300 rounded px-2 py-1 w-24 text-sm date-input text-center font-normal" data-task="商品展示及购买流程" type="text" value="待定"/>
<button class="text-green-500 hover:text-green-700" onclick="saveDate('商品展示及购买流程')" title="保存"><i class="fas fa-check"></i></button>
<button class="text-gray-400 hover:text-gray-600" onclick="cancelEdit('商品展示及购买流程')" title="取消"><i class="fas fa-times"></i></button>
</div>
</td>
<td class="px-5 py-4">
<div class="flex flex-col gap-2">
<div class="flex flex-wrap gap-2 items-center">
<a href="Crm-Group/prd-product-orders.html" target="_blank" class="px-3 py-1.5 text-xs font-medium text-gray-600 bg-gray-100 hover:bg-gray-200 rounded transition-colors flex items-center gap-1 border border-gray-200">
    <i class="fas fa-project-diagram text-gray-400"></i> PRD
</a>
<a href="Crm-Group/client-product-list.html" target="_blank" class="px-3 py-1.5 text-xs font-medium text-purple-700 bg-purple-50 hover:bg-purple-100 rounded transition-colors flex items-center gap-1 border border-purple-200">
    <i class="fas fa-desktop"></i> 商品列表
</a>
<a href="Crm-Group/product-detail.html" target="_blank" class="px-3 py-1.5 text-xs font-medium text-purple-700 bg-purple-50 hover:bg-purple-100 rounded transition-colors flex items-center gap-1 border border-purple-200">
    <i class="fas fa-desktop"></i> 商品详情
</a>
</div>
</div>
</td>
</tr>
    """

    task1_soup = BeautifulSoup(task1_html, 'html.parser')
    task2_soup = BeautifulSoup(task2_html, 'html.parser')
    
    # Check if they are already in tbody
    if "商品购买引流入口" not in str(tbody):
        tbody.insert(0, task2_soup.tr)
        tbody.insert(0, task1_soup.tr)
        
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Tasks added successfully.")
else:
    print("Could not find 规划中需求 section.")
