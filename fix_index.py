import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the three tbodys
tbodys = soup.find_all('tbody')
in_progress_tbody = tbodys[0]
backlog_tbody = tbodys[1]
completed_tbody = tbodys[2]

# Function to extract task name from a tr
def get_task_name(tr):
    tds = tr.find_all('td')
    if len(tds) >= 2:
        return tds[1].get_text(strip=True).replace('\n', '').replace('\r', '')
    return None

all_tasks = {}

def process_tbody(tbody, source_list):
    for tr in tbody.find_all('tr', recursive=False):
        name = get_task_name(tr)
        if name:
            base_name = name.split(' ')[0] if ' ' in name else name
            # Handle specifics
            if '客户详情' in name: base_name = '客户详情'
            if '标签管理' in name: base_name = '标签管理'
            if '后台商品管理' in name: base_name = '后台商品管理'
            if '商品展示及购买流程' in name: base_name = '商品展示'
            if '商品购买引流入口' in name: base_name = '商品购买'
            if '商品订单管理' in name: base_name = '商品订单管理'
            
            if base_name not in all_tasks:
                all_tasks[base_name] = {'tr': tr, 'list': source_list, 'original_name': name}

process_tbody(in_progress_tbody, 'in_progress')
process_tbody(backlog_tbody, 'backlog')

# Tasks that must be in backlog
backlog_keywords = ['客户详情', '标签管理', '后台商品管理', '商品展示', '商品购买', '商品订单管理', '留资管理二期', '关系树统计', '净值报表', '销售入金奖励报表二期', '新增销售', 'logo跳转']

for base_name, data in all_tasks.items():
    # If it matches backlog keywords, force it to backlog
    for kw in backlog_keywords:
        if kw in base_name or kw in data['original_name']:
            data['list'] = 'backlog'
            
            tr = data['tr']
            # update border color to purple
            classes = tr.get('class', [])
            new_classes = []
            for c in classes:
                if 'border-orange-400' in c:
                    new_classes.append('border-[#8B5CF6]')
                else:
                    new_classes.append(c)
            if 'border-[#8B5CF6]' not in new_classes:
                new_classes.extend(['border-l-4', 'border-[#8B5CF6]'])
            tr['class'] = new_classes
                
            date_span = tr.find('span', class_='date-text')
            if date_span:
                date_span.string = '待定'
            date_input = tr.find('input', class_='date-input')
            if date_input:
                date_input['value'] = '待定'
            break

# Clear the tbodys
in_progress_tbody.clear()
backlog_tbody.clear()

in_progress_added = set()
backlog_added = set()

for base_name, data in all_tasks.items():
    if data['list'] == 'in_progress':
        if base_name not in in_progress_added:
            in_progress_tbody.append(data['tr'])
            in_progress_added.add(base_name)
    else:
        if base_name not in backlog_added:
            backlog_tbody.append(data['tr'])
            backlog_added.add(base_name)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("HTML processing complete!")
