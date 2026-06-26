import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_task_html = """
<!-- 需求: CRM-HK 账户审核 -->
<tr class="table-row-hover bg-white border-l-4 border-[#3B82F6]">
<td class="px-5 py-4 font-medium text-gray-900 whitespace-nowrap">客户管理</td>
<td class="px-5 py-4 font-bold text-gray-800 whitespace-nowrap">账户审核 (HK)</td>
<td class="px-5 py-4 text-gray-500">HK 端专属开户审核详情页，包含身份证与银行卡等附件资料审核。</td>
<td class="px-5 py-4">
<div class="flex flex-col gap-1">
<span class="inline-block px-2 py-0.5 text-[11px] rounded tag-hk w-max">CRM-HK</span>
</div>
</td>
<td class="px-5 py-4 text-center font-medium text-gray-800 relative group whitespace-nowrap">
<div class="view-mode flex items-center justify-center gap-2">
<span class="date-text" data-task="账户审核 (HK)">2026-6-24</span>
<button class="text-blue-500 hover:text-blue-700 opacity-0 group-hover:opacity-100 transition-opacity" onclick="toggleEdit('账户审核 (HK)')" title="修改时间"><i class="fas fa-edit"></i></button>
</div>
<div class="edit-mode hidden items-center justify-center gap-1" id="edit-账户审核 (HK)">
<input class="border border-gray-300 rounded px-2 py-1 w-24 text-sm date-input text-center font-normal" data-task="账户审核 (HK)" type="text" value="2026-6-24"/>
<button class="text-green-500 hover:text-green-700" onclick="saveDate('账户审核 (HK)')" title="保存"><i class="fas fa-check"></i></button>
<button class="text-gray-400 hover:text-gray-600" onclick="cancelEdit('账户审核 (HK)')" title="取消"><i class="fas fa-times"></i></button>
</div>
</td>
<td class="px-5 py-4">
<div class="flex flex-col gap-2">
<div class="flex flex-wrap gap-2 items-center">
<a class="inline-flex items-center gap-1 bg-gray-100 hover:bg-gray-200 text-gray-700 px-3 py-1.5 rounded text-xs transition-colors border border-gray-200" href="CRM-HK/prd-audit.html" target="_blank">
<i class="fas fa-project-diagram text-gray-400"></i> PRD
                                        </a>
<a class="inline-flex items-center gap-1 bg-teal-50 hover:bg-teal-100 theme-text px-3 py-1.5 rounded text-xs transition-colors theme-border border" href="CRM-HK/admin-audit.html" target="_blank">
<i class="fas fa-laptop-code"></i> 原型
                                        </a>
</div>
</div>
</td>
</tr>
"""

soup = BeautifulSoup(html, 'html.parser')
in_progress_tbody = soup.find_all('tbody')[0]

missing_tr = BeautifulSoup(missing_task_html, 'html.parser').tr

# Insert it before the "开户申请 (HK)" task
for tr in in_progress_tbody.find_all('tr', recursive=False):
    tds = tr.find_all('td')
    if len(tds) >= 2 and '开户申请' in tds[1].get_text():
        tr.insert_before(missing_tr)
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Task restored successfully!")
