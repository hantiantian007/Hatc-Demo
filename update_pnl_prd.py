import re

# Read the equity PRD to get the global structure
with open('/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/prd-report-equity.html', 'r', encoding='utf-8') as f:
    equity_html = f.read()

# Read the pnl PRD
with open('/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/prd-report-pnl-1.html', 'r', encoding='utf-8') as f:
    pnl_html = f.read()

# We want to replace the whole body content of pnl_html with the structure from equity, but tailored for PnL.
# Extract the body from equity_html
body_match = re.search(r'<body[^>]*>(.*?)</body>', equity_html, re.DOTALL)
if not body_match:
    print("Could not find body in equity_html")
    exit(1)

equity_body = body_match.group(1)

# Modify the equity_body for PnL
pnl_body = equity_body.replace('风控与运营报表 PRD (净值报表)', '风控与运营报表 PRD (盈亏报表)')
pnl_body = pnl_body.replace('净值报表 (Equity Report)', '盈亏报表 (P/L Report)')
pnl_body = pnl_body.replace('admin-report-equity.html', 'admin-report-pnl-1.html')
pnl_body = pnl_body.replace('QA_TestCases_Equity.md', 'QA_TestCases_PnL.md') # Just in case
pnl_body = pnl_body.replace('核心风控与资产监控页面，用于实时查看伞下代理及客户的账户资产状况、净值结余及持仓盈亏表现。', '核心业绩监控页面，用于多维度（历史平仓+实时浮动）查看伞下代理及客户的整体盈亏状况及交易成本。')

# Replace the fields table
fields_table_html = """
            <h3 class="font-medium text-gray-800 mb-2 text-sm">核心字段与计算公式</h3>
            <div class="overflow-x-auto mb-4">
                <table class="w-full text-sm text-left border border-gray-200">
                    <thead class="bg-gray-50 text-gray-600">
                        <tr>
                            <th class="border-b py-2 px-3">页面显示字段</th>
                            <th class="border-b py-2 px-3">数据来源</th>
                            <th class="border-b py-2 px-3">定义与计算方式 (遵循 MT5 标准)</th>
                        </tr>
                    </thead>
                    <tbody class="text-gray-700 divide-y divide-gray-100">
                        <tr>
                            <td class="py-2 px-3 font-medium">账号/名称</td>
                            <td class="py-2 px-3">CRM 账户系统</td>
                            <td class="py-2 px-3">MT5 交易账号及其在 CRM 中绑定的客户/代理真实姓名。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">净值 (Equity)</td>
                            <td class="py-2 px-3">MT5 API</td>
                            <td class="py-2 px-3">账户当前的绝对清算价值。<br>计算公式：<code>结余 + 信用 + 浮动盈亏 + 过夜利息 + 平台佣金</code>。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">结余 (Balance)</td>
                            <td class="py-2 px-3">MT5 API</td>
                            <td class="py-2 px-3">账户的实际可用现金余额（已结平仓盈亏，但不含未平仓浮动数据与信用赠金）。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium text-primary">浮动盈亏 (Profit)</td>
                            <td class="py-2 px-3">MT5 API</td>
                            <td class="py-2 px-3">当前所有未平仓订单基于实时市场行情的纯价格波动盈亏总和。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">信用 (Credit)</td>
                            <td class="py-2 px-3">MT5 API</td>
                            <td class="py-2 px-3">账户当前拥有的信用额度（通常为入金赠金、信用补点等）。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">平仓手数 (Closed Lots)</td>
                            <td class="py-2 px-3">MT5 历史订单</td>
                            <td class="py-2 px-3">选定时间范围内，所有已平仓订单的交易总手数。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">平仓笔数 (Closed Deals)</td>
                            <td class="py-2 px-3">MT5 历史订单</td>
                            <td class="py-2 px-3">选定时间范围内，所有已平仓订单的总笔数。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">手续费 (Fee)</td>
                            <td class="py-2 px-3">MT5 历史订单</td>
                            <td class="py-2 px-3">选定时间范围内，所有已平仓订单产生的手续费总计。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">佣金 (Commission)</td>
                            <td class="py-2 px-3">MT5 历史订单</td>
                            <td class="py-2 px-3">选定时间范围内，所有已平仓订单产生的代理佣金总计。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium">过夜利息 (Swap)</td>
                            <td class="py-2 px-3">MT5 历史/实时订单</td>
                            <td class="py-2 px-3">选定时间范围内，订单因跨日持仓而产生的隔夜利息总和。</td>
                        </tr>
                        <tr>
                            <td class="py-2 px-3 font-medium text-primary">平仓盈亏 (Closed Profit)</td>
                            <td class="py-2 px-3">MT5 历史订单</td>
                            <td class="py-2 px-3">选定时间范围内，所有已平仓订单的纯价格波动盈亏总和。</td>
                        </tr>
                    </tbody>
                </table>
            </div>
"""

# Find the fields table in pnl_body and replace it
pnl_body = re.sub(r'<h3 class="font-medium text-gray-800 mb-2 text-sm">核心字段与计算公式</h3>.*?</div>\s*</div>', fields_table_html + '\n        </div>', pnl_body, flags=re.DOTALL)

# Reconstruct the full HTML
new_pnl_html = re.sub(r'(<body[^>]*>).*?(</body>)', r'\1' + pnl_body + r'\2', pnl_html, flags=re.DOTALL)

# Also fix the title
new_pnl_html = new_pnl_html.replace('<title>风控与运营报表 PRD - 净值报表</title>', '<title>风控与运营报表 PRD - 盈亏报表</title>')

with open('/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/prd-report-pnl-1.html', 'w', encoding='utf-8') as f:
    f.write(new_pnl_html)

with open('/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/prd-report-pnl-2.html', 'w', encoding='utf-8') as f:
    f.write(new_pnl_html)

print("Updated PnL PRDs")
