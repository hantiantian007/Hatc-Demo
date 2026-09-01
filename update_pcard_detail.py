import re

with open('Crm-Group/admin-activity-pcard-detail.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 取消编辑活动、结束活动按钮
content = re.sub(r'<div class="flex items-center gap-2">\s*<button class="h-8 px-4 rounded-md border border-gray-200 bg-white text-gray-600 hover:bg-gray-50 transition-colors text-xs font-medium">\s*<i class="fa-solid fa-pen mr-1\.5"><\/i> 编辑活动\s*<\/button>\s*<button class="h-8 px-4 rounded-md bg-red-50 text-red-600 border border-red-200 hover:bg-red-100 transition-colors text-xs font-medium">\s*<i class="fa-solid fa-stop mr-1\.5"><\/i> 结束活动\s*<\/button>\s*<\/div>', '', content)

# 2. 取消图片内的状态tab
content = re.sub(r'<!-- Tab 切换 -->\s*<div class="px-5 pt-3 border-b border-gray-100 bg-gray-50\/60">\s*<div class="flex items-center gap-2 text-xs overflow-x-auto no-scrollbar pb-2">[\s\S]*?<\/div>\s*<\/div>', '', content)

# 3. 活动状态仅保留：参与中、已达标
content = re.sub(r'<div class="bg-white rounded-xl card-shadow border border-gray-100 p-5">\s*<div class="flex items-center justify-between mb-2">\s*<span class="text-xs text-gray-500">即将达标 ≥80%<\/span>[\s\S]*?<\/div>\s*<p class="text-2xl font-bold text-amber-600">246<\/p>\s*<p class="text-xs text-gray-400 mt-1">建议主动营销 🔥<\/p>\s*<\/div>', '', content)
content = content.replace('<div class="grid grid-cols-2 md:grid-cols-4 gap-4">', '<div class="grid grid-cols-2 md:grid-cols-3 gap-4">')
content = re.sub(r'<tr class="table-row border-b border-gray-100">[\s\S]*?test-魏佳用[\s\S]*?即将达标[\s\S]*?<\/tr>', '', content)
content = content.replace('<option>$500~$999（接近）</option>', '')
content = content.replace('<option>3~4.99 Lot（接近）</option>', '')

# 4. 取消左侧复选框
content = re.sub(r'<th class="font-medium py-3 px-3 w-12">\s*<input type="checkbox" class="rounded border-gray-300 text-primary focus:ring-primary text-xs">\s*<\/th>', '', content)
content = re.sub(r'<td class="py-3 px-3"><input type="checkbox" class="rounded border-gray-300 text-primary focus:ring-primary text-xs"><\/td>', '', content)

# 5. 取消批量营销、提醒按钮
content = re.sub(r'<button onclick="openMarketingModal\(\)" class="h-8 px-4 rounded-md bg-amber-50 text-amber-600 border border-amber-200 hover:bg-amber-100 transition-colors text-xs font-medium">\s*<i class="fa-solid fa-bullhorn mr-1\.5"><\/i> 批量营销\s*<\/button>', '', content)
content = re.sub(r'<button class="px-2\.5 h-6 rounded-md text-\[11px\] bg-amber-50 text-amber-600 border border-amber-200 hover:bg-amber-100 transition-colors">\s*<i class="fa-solid fa-bullhorn mr-1"><\/i> 提醒\s*<\/button>', '', content)

with open('Crm-Group/admin-activity-pcard-detail.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated admin-activity-pcard-detail.html successfully.")
