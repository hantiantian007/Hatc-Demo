import re
import os

files_sc = [
    '/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/client-orders.html',
    '/Users/joker/Desktop/Ai/AI/1.2.0/Group-Gw/client-orders.html'
]

files_tc = [
    '/Users/joker/Desktop/Ai/AI/1.2.0/CRM-HK/client-orders.html',
    '/Users/joker/Desktop/Ai/AI/1.2.0/Hk-Gw/client-orders.html'
]

html_sc = """
            <div class="flex items-center gap-3 bg-white p-1 rounded-lg border border-gray-200 shadow-sm">
                <button class="px-4 py-1.5 text-sm font-medium rounded-md bg-gray-100 text-gray-900 transition-colors">全部订单</button>
                <button class="px-4 py-1.5 text-sm font-medium rounded-md text-gray-500 hover:text-gray-900 transition-colors">处理中</button>
                <button class="px-4 py-1.5 text-sm font-medium rounded-md text-gray-500 hover:text-gray-900 transition-colors">已交付</button>
                <button class="px-4 py-1.5 text-sm font-medium rounded-md text-gray-500 hover:text-gray-900 transition-colors">已过期</button>
            </div>
        </div>

        <!-- 订单列表区 -->
        <div class="space-y-4">
            
            <!-- 订单卡片 1：刚购买的处理中订单 -->
            <div class="bg-white rounded-xl shadow-sm border border-brandYellow overflow-hidden hover:shadow-md transition-shadow relative">
                <div class="absolute top-0 left-0 w-1 h-full bg-brandYellow"></div>
                <!-- 订单头部 -->
                <div class="bg-gray-50 px-6 py-3 border-b border-gray-100 flex flex-wrap justify-between items-center gap-4">
                    <div class="flex items-center gap-4 text-sm">
                        <span class="font-medium text-gray-900">订单号：ORD-20260623-8892</span>
                        <span class="text-gray-500">下单时间：2026-06-23 10:45:12</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 bg-yellow-100 text-yellow-700 text-xs font-bold rounded-md flex items-center gap-1">
                            <i class="fa-solid fa-clock-rotate-left fa-spin"></i> 处理中
                        </span>
                    </div>
                </div>
                <!-- 订单内容 -->
                <div class="p-6 flex flex-col md:flex-row items-center gap-6">
                    <div class="w-24 h-24 bg-gradient-to-br from-indigo-900 to-purple-800 rounded-lg shadow-inner flex flex-col items-center justify-center text-white flex-shrink-0 relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-8 h-8 bg-white/10 rounded-full blur-md transform translate-x-1/2 -translate-y-1/2"></div>
                        <i class="fa-solid fa-robot text-2xl mb-1 text-brandYellow"></i>
                        <span class="text-[10px] font-bold tracking-wider">先锋一号</span>
                    </div>
                    
                    <div class="flex-1 min-w-0">
                        <h3 class="text-lg font-bold text-gray-900 mb-1 truncate">【APP 版本】星启先锋一号智能交易系统</h3>
                        <div class="flex items-center gap-4 text-sm text-gray-500 mb-2">
                            <span><i class="fa-regular fa-clock mr-1"></i> 套餐：1个月</span>
                            <span><i class="fa-solid fa-wallet mr-1"></i> 付款账号：MT5 - 667788</span>
                        </div>
                        <div class="bg-yellow-50 text-yellow-700 text-xs p-2 rounded border border-yellow-100 inline-block">
                            <i class="fa-solid fa-circle-info mr-1"></i> 平台正在为您进行人工代购与账号开通，请耐心等待...
                        </div>
                    </div>
                    
                    <div class="flex flex-col items-end gap-3 min-w-[120px]">
                        <div class="text-right">
                            <div class="text-sm text-gray-500">实付金额</div>
                            <div class="text-xl font-bold text-gray-900">$300.00</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 订单卡片 2：已交付的订单 -->
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-shadow">
                <!-- 订单头部 -->
                <div class="bg-gray-50 px-6 py-3 border-b border-gray-100 flex flex-wrap justify-between items-center gap-4">
                    <div class="flex items-center gap-4 text-sm">
                        <span class="font-medium text-gray-900">订单号：ORD-20260623-8891</span>
                        <span class="text-gray-500">下单时间：2026-06-23 10:30:45</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-bold rounded-md flex items-center gap-1">
                            <i class="fa-solid fa-circle-check"></i> 已交付
                        </span>
                    </div>
                </div>
                <!-- 订单内容 -->
                <div class="p-6 flex flex-col md:flex-row items-center gap-6">
                    <div class="w-24 h-24 bg-gradient-to-br from-indigo-900 to-purple-800 rounded-lg shadow-inner flex flex-col items-center justify-center text-white flex-shrink-0 relative overflow-hidden">
                        <div class="absolute top-0 right-0 w-8 h-8 bg-white/10 rounded-full blur-md transform translate-x-1/2 -translate-y-1/2"></div>
                        <i class="fa-solid fa-robot text-2xl mb-1 text-brandYellow"></i>
                        <span class="text-[10px] font-bold tracking-wider">先锋一号</span>
                    </div>
                    
                    <div class="flex-1 min-w-0">
                        <h3 class="text-lg font-bold text-gray-900 mb-1 truncate">【APP 版本】星启先锋一号智能交易系统</h3>
                        <div class="flex items-center gap-4 text-sm text-gray-500 mb-2">
                            <span><i class="fa-regular fa-clock mr-1"></i> 套餐：1个月</span>
                            <span><i class="fa-solid fa-wallet mr-1"></i> 付款账号：MT5 - 556677</span>
                        </div>
                        <div class="bg-green-50 text-green-800 text-xs p-3 rounded border border-green-100 flex flex-col gap-1">
                            <div><span class="text-green-600 mr-2">交付账号:</span> <span class="font-bold font-mono">EA-882193</span> <button class="ml-2 text-green-600 hover:text-green-800" title="复制账号"><i class="fa-regular fa-copy"></i></button></div>
                            <div><span class="text-green-600 mr-2">有效期至:</span> <span class="font-medium">2026-07-23</span></div>
                        </div>
                    </div>
                    
                    <div class="flex flex-col items-end gap-3 min-w-[120px]">
                        <div class="text-right">
                            <div class="text-sm text-gray-500">实付金额</div>
                            <div class="text-xl font-bold text-gray-900">$300.00</div>
                        </div>
                        <button class="px-4 py-1.5 border border-gray-200 hover:border-primary hover:text-primary rounded text-sm font-medium transition-colors">
                            查看详情
                        </button>
                    </div>
                </div>
            </div>

            <!-- 订单卡片 3：已过期的历史订单 -->
            <div class="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden opacity-75 hover:opacity-100 transition-opacity">
                <!-- 订单头部 -->
                <div class="bg-gray-50 px-6 py-3 border-b border-gray-100 flex flex-wrap justify-between items-center gap-4">
                    <div class="flex items-center gap-4 text-sm">
                        <span class="font-medium text-gray-900">订单号：ORD-20251210-3342</span>
                        <span class="text-gray-500">下单时间：2025-12-10 14:20:11</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 bg-gray-200 text-gray-600 text-xs font-bold rounded-md flex items-center gap-1">
                            <i class="fa-solid fa-clock-rotate-left"></i> 已过期
                        </span>
                    </div>
                </div>
                <!-- 订单内容 -->
                <div class="p-6 flex flex-col md:flex-row items-center gap-6">
                    <div class="w-24 h-24 bg-gray-800 rounded-lg shadow-inner flex flex-col items-center justify-center text-white flex-shrink-0 relative overflow-hidden grayscale">
                        <i class="fa-solid fa-chart-line text-2xl mb-1 text-gray-400"></i>
                        <span class="text-[10px] font-bold tracking-wider text-gray-400">行情助手</span>
                    </div>
                    
                    <div class="flex-1 min-w-0">
                        <h3 class="text-lg font-bold text-gray-900 mb-1 truncate">VIP 专属行情分析助手</h3>
                        <div class="flex items-center gap-4 text-sm text-gray-500 mb-2">
                            <span><i class="fa-regular fa-clock mr-1"></i> 套餐：3个月</span>
                            <span><i class="fa-solid fa-wallet mr-1"></i> 付款账号：MT5 - 667788</span>
                        </div>
                        <div class="bg-gray-50 text-gray-500 text-xs p-3 rounded border border-gray-100 flex flex-col gap-1">
                            <div><span class="mr-2">交付账号:</span> <span class="font-mono">EA-112233</span></div>
                            <div><span class="mr-2">有效期至:</span> <span class="line-through">2026-03-10</span></div>
                        </div>
                    </div>
                    
                    <div class="flex flex-col items-end gap-3 min-w-[120px]">
                        <div class="text-right">
                            <div class="text-sm text-gray-500">实付金额</div>
                            <div class="text-xl font-bold text-gray-900">$150.00</div>
                        </div>
                        <button class="px-4 py-1.5 bg-brandYellow hover:bg-brandYellowHover text-gray-900 rounded text-sm font-medium transition-colors shadow-sm">
                            再次购买
                        </button>
                    </div>
                </div>
            </div>

        </div>"""

html_tc = html_sc.replace('全部订单', '全部訂單') \
    .replace('处理中', '處理中') \
    .replace('已交付', '已交付') \
    .replace('已过期', '已過期') \
    .replace('订单列表区', '訂單列表區') \
    .replace('订单卡片', '訂單卡片') \
    .replace('刚购买的处理中订单', '剛購買的處理中訂單') \
    .replace('订单头部', '訂單頭部') \
    .replace('订单号', '訂單號') \
    .replace('下单时间', '下單時間') \
    .replace('订单内容', '訂單內容') \
    .replace('套餐：1个月', '套餐：1個月') \
    .replace('套餐：3个月', '套餐：3個月') \
    .replace('付款账号', '付款賬號') \
    .replace('平台正在为您进行人工代购与账号开通，请耐心等待', '平台正在為您進行人工代購與賬號開通，請耐心等待') \
    .replace('实付金额', '實付金額') \
    .replace('已交付的订单', '已交付的訂單') \
    .replace('交付账号', '交付賬號') \
    .replace('复制账号', '複製賬號') \
    .replace('有效期至', '有效期至') \
    .replace('查看详情', '查看詳情') \
    .replace('历史订单', '歷史訂單') \
    .replace('再次购买', '再次購買') \
    .replace('专属行情分析助手', '專屬行情分析助手')

def replace_content(filepath, new_html):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找到筛选区的开头
    start_idx = content.find('<div class="flex items-center gap-3 bg-white p-1 rounded-lg border border-gray-200 shadow-sm">')
    # 找到分页区的开头
    end_idx = content.find('<!-- 分页 -->')
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + new_html + '\n        \n        ' + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

for filepath in files_sc:
    replace_content(filepath, html_sc)

for filepath in files_tc:
    replace_content(filepath, html_tc)

print("Orders page updated")
