import re

with open('Crm-Group/admin-product-orders.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 筛选状态变更
content = content.replace('<option value="active">生效中</option>', '<option value="processing">处理中 (待交付)</option>')
content = content.replace('<option value="expired">已过期</option>', '<option value="delivered">已交付</option>')

# 2. 修改业务说明
banner_old = "客户通过 CRM 主钱包余额购买增值商品，扣款成功后，对应资金将自动转入平台指定的 MT 账号（如：MT-9999999）进行统一归集。若涉及代理返佣，将基于此资金流水独立计算。"
banner_new = "【代购交付模式】客户使用余额购买后，资金将自动转入指定MT账号（如：MT-9999999）归集。扣款成功仅代表代购请求成立，需运营人员线下开通业务后，在此处点击「交付」录入账号/激活信息，订单方可生效。"
content = content.replace(banner_old, banner_new)

# 3. 表格列头调整：服务周期 -> 交付信息
content = content.replace('<th class="px-4 py-3 font-medium whitespace-nowrap">服务周期</th>', '<th class="px-4 py-3 font-medium whitespace-nowrap">交付信息</th>')

# 4. 订单1：生效中 -> 处理中（待交付）
row1_old = """<td class="px-4 py-3 text-xs text-gray-600">
                                <div>起：2026-06-23</div>
                                <div>止：2026-07-23</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="px-2 py-1 bg-green-100 text-green-700 text-xs font-medium rounded">生效中</span>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-primary hover:text-primaryHover text-sm font-medium">查看</button>
                            </td>"""
row1_new = """<td class="px-4 py-3 text-xs text-gray-400 italic">
                                待运营线下人工开通
                            </td>
                            <td class="px-4 py-3">
                                <span class="px-2 py-1 bg-blue-100 text-blue-700 text-xs font-medium rounded">待交付</span>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-white bg-primary hover:bg-primaryHover px-3 py-1.5 rounded text-xs font-medium shadow-sm transition-colors">去交付</button>
                            </td>"""
content = content.replace(row1_old, row1_new)

# 5. 订单2：已过期 -> 已交付
row2_old = """<td class="px-4 py-3 text-xs text-gray-600">
                                <div>起：2025-12-10</div>
                                <div>止：2026-03-10</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="px-2 py-1 bg-gray-100 text-gray-600 text-xs font-medium rounded">已过期</span>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-primary hover:text-primaryHover text-sm font-medium">查看</button>
                            </td>"""
row2_new = """<td class="px-4 py-3 text-xs text-gray-600">
                                <div>账号：lisi_vip001</div>
                                <div class="text-gray-400 mt-0.5" title="有效期：2025-12-11 至 2026-03-11">期限：3个月</div>
                            </td>
                            <td class="px-4 py-3">
                                <span class="px-2 py-1 bg-green-100 text-green-700 text-xs font-medium rounded">已交付</span>
                            </td>
                            <td class="px-4 py-3 text-right">
                                <button class="text-primary hover:text-primaryHover text-sm font-medium">详情</button>
                            </td>"""
content = content.replace(row2_old, row2_new)

with open('Crm-Group/admin-product-orders.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 翻译繁体
tc_content = content
replacements = {
    '处理中 (待交付)': '處理中 (待交付)',
    '已交付': '已交付',
    '【代购交付模式】客户使用余额购买后，资金将自动转入指定MT账号（如：MT-9999999）归集。扣款成功仅代表代购请求成立，需运营人员线下开通业务后，在此处点击「交付」录入账号/激活信息，订单方可生效。': '【代購交付模式】客戶使用餘額購買後，資金將自動轉入指定MT賬號（如：MT-9999999）歸集。扣款成功僅代表代購請求成立，需運營人員線下開通業務後，在此處點擊「交付」錄入賬號/激活信息，訂單方可生效。',
    '交付信息': '交付信息',
    '待运营线下人工开通': '待運營線下人工開通',
    '待交付': '待交付',
    '去交付': '去交付',
    '账号：': '賬號：',
    '期限：': '期限：',
    '有效期：': '有效期：',
    '至': '至',
    '详情': '詳情'
}

for k, v in replacements.items():
    tc_content = tc_content.replace(k, v)

with open('CRM-HK/admin-product-orders.html', 'w', encoding='utf-8') as f:
    f.write(tc_content)

print("Admin orders updated for manual delivery logic.")