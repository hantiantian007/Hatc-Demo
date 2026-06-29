import re
from bs4 import BeautifulSoup
import os

# 1. Update prd-product-orders.html
def update_prd(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_section = """
            <div class="p-8 border-b border-gray-100">
                <h3 class="text-lg font-bold text-gray-900 mb-4 border-l-4 border-primary pl-3">4. 商业化闭环核心逻辑 (新增)</h3>
                <table class="w-full text-sm text-left border-collapse border border-gray-200">
                    <thead class="bg-gray-50 text-gray-700">
                        <tr>
                            <th class="px-4 py-3 border border-gray-200 w-1/4">逻辑模块 / 指标</th>
                            <th class="px-4 py-3 border border-gray-200 w-1/2">计算公式与规则定义</th>
                            <th class="px-4 py-3 border border-gray-200 w-1/4">数据来源与特殊逻辑</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-200 text-gray-600">
                        <tr>
                            <td class="px-4 py-3 border border-gray-200 font-medium">MT5 交易账户强绑定</td>
                            <td class="px-4 py-3 border border-gray-200">客户在下单支付时，必须下拉选择其名下状态正常的 MT5 交易账号。订单生成后，该商品（如 EA 策略）的履约动作仅针对该指定账号生效。</td>
                            <td class="px-4 py-3 border border-gray-200">获取客户同名下的真实 MT5 账户列表。</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-3 border border-gray-200 font-medium">代理 (IB) 返佣机制</td>
                            <td class="px-4 py-3 border border-gray-200">后台可为每个商品单独设置“是否参与返佣”及“返佣比例”。当客户购买该商品且订单状态流转为“已通过(已完成)”时，系统自动按照实付金额 × 返佣比例计算佣金。</td>
                            <td class="px-4 py-3 border border-gray-200">佣金直接结算至该客户直属上级代理的返佣钱包中。</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-3 border border-gray-200 font-medium">余额不足断点挽回 (引导入金)</td>
                            <td class="px-4 py-3 border border-gray-200">支付确认弹窗内实时校验钱包余额。当余额 < 商品售价时，原“确认扣款”按钮变更为“余额不足，去入金”并支持跳转。</td>
                            <td class="px-4 py-3 border border-gray-200">引导跳转入金页时，需在 URL 中携带当前商品 ID（如 ?redirect=product&id=123）以便入金后回跳。</td>
                        </tr>
                        <tr>
                            <td class="px-4 py-3 border border-gray-200 font-medium">防重复购买与订阅到期</td>
                            <td class="px-4 py-3 border border-gray-200">
                                <ul class="list-disc pl-4 space-y-1">
                                    <li><strong>防重复购买</strong>：若商品为“一次性买断”，客户一旦购买成功，商品列表及详情页按钮置灰展示“已拥有”，禁止再次下单。</li>
                                    <li><strong>订阅到期降级</strong>：订阅制套餐到期前 3 天发送站内信预警；过期后系统自动撤销 MT5 账号的相关权限，订单状态变更为“已失效”。</li>
                                </ul>
                            </td>
                            <td class="px-4 py-3 border border-gray-200">系统定时任务每日凌晨扫描订阅到期时间。</td>
                        </tr>
                    </tbody>
                </table>
            </div>
"""
    if "4. 商业化闭环核心逻辑" not in html:
        html = re.sub(r'(<div class="p-8 border-b border-gray-100">[\s\S]*?)(</div>\s*</div>\s*</div>\s*</body>)', r'\1' + new_section + r'\2', html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

# 2. Update admin-product-management.html (Add IB commission)
def update_admin_management(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    ib_html = """
                        <!-- 代理返佣设置 -->
                        <div class="space-y-2 mt-4 bg-gray-50 p-4 rounded-lg border border-gray-200">
                            <label class="block text-sm font-medium text-gray-700">代理返佣 (IB Commission) 设置</label>
                            <div class="flex items-center justify-between">
                                <label class="flex items-center gap-2 cursor-pointer">
                                    <input type="checkbox" class="rounded text-[#C19B5E] focus:ring-[#C19B5E] h-4 w-4" checked>
                                    <span class="text-sm text-gray-600">允许上级代理获得分润</span>
                                </label>
                                <div class="flex items-center gap-2">
                                    <span class="text-sm text-gray-500">返佣比例</span>
                                    <input type="number" placeholder="0" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-20 focus:ring-2 focus:ring-[#C19B5E] focus:border-[#C19B5E]" value="10">
                                    <span class="text-sm text-gray-500">%</span>
                                </div>
                            </div>
                        </div>
"""
    if "代理返佣 (IB Commission) 设置" not in html:
        html = re.sub(r'(<label class="block text-sm font-medium text-gray-700 mb-1">上架时间[\s\S]*?</select>\s*</div>)', r'\1' + ib_html, html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

# 3. Update admin-product-orders.html (Show MT5 account)
def update_admin_orders(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if "MT5: 8881234" not in html:
        html = re.sub(r'(<div class="text-sm font-medium text-gray-900">张三</div>\s*<div class="text-xs text-gray-500">zhangsan@example.com</div>)', r'\1\n                                            <div class="text-xs text-[#C19B5E] mt-1"><i class="fas fa-wallet mr-1"></i>MT5: 8881234 (USD)</div>', html)
        html = re.sub(r'(<div class="text-sm font-medium text-gray-900">赵六</div>\s*<div class="text-xs text-gray-500">zhaoliu@example.com</div>)', r'\1\n                                            <div class="text-xs text-[#C19B5E] mt-1"><i class="fas fa-wallet mr-1"></i>MT5: 8885678 (USD)</div>', html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

# 4. Update product-detail.html (MT5 Binding & Insufficient Balance)
def update_product_detail(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    mt5_html = """
                    <!-- MT5 账户绑定 -->
                    <div class="mb-4">
                        <label class="block text-sm font-medium text-gray-700 mb-2">应用交易账户 (强绑定)</label>
                        <select class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-[#C19B5E] focus:border-[#C19B5E]">
                            <option value="">请选择需挂载策略的 MT5 账户...</option>
                            <option value="1">8881234 (USD) - 标准账户</option>
                            <option value="2">8885678 (USD) - VIP账户</option>
                        </select>
                    </div>
"""
    if "应用交易账户 (强绑定)" not in html:
        html = re.sub(r'(<div class="flex justify-between items-center mb-4 text-sm">\s*<span class="text-gray-500">钱包余额</span>\s*<span class="font-medium">\$10,000.00</span>\s*</div>)', mt5_html + r'\1', html)
    
    if "余额不足，去入金" not in html:
        html = re.sub(r'(<button class="w-full bg-\[#C19B5E\] text-white py-3 rounded-lg font-medium hover:bg-\[#A8864D\] transition-colors" onclick="confirmPurchase\(\)">)\s*(确认扣款.*?)\s*(</button>)', 
            r"""
                    <!-- 正常状态按钮 -->
                    <button id="btnNormalPurchase" class="w-full bg-[#C19B5E] text-white py-3 rounded-lg font-medium hover:bg-[#A8864D] transition-colors mb-2" onclick="confirmPurchase()">
                        \2
                    </button>
                    <!-- 余额不足状态按钮 (演示用) -->
                    <button id="btnInsufficientBalance" class="w-full bg-red-50 text-red-600 border border-red-200 py-3 rounded-lg font-medium hover:bg-red-100 transition-colors hidden" onclick="window.location.href='client-deposit.html'">
                        余额不足，去入金
                    </button>
                    
                    <div class="text-center mt-3">
                        <a href="#" onclick="toggleBalanceState(); return false;" class="text-xs text-gray-400 hover:text-[#C19B5E] underline">切换演示: 模拟余额不足</a>
                    </div>
            """, html)
        
        script_html = """
    <script>
        function toggleBalanceState() {
            const btnNormal = document.getElementById('btnNormalPurchase');
            const btnInsuf = document.getElementById('btnInsufficientBalance');
            if (btnNormal.classList.contains('hidden')) {
                btnNormal.classList.remove('hidden');
                btnInsuf.classList.add('hidden');
            } else {
                btnNormal.classList.add('hidden');
                btnInsuf.classList.remove('hidden');
            }
        }
    </script>
</body>"""
        html = html.replace("</body>", script_html)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

# 5. Update client-product-list.html (Duplicate Purchase)
def update_product_list(file_path):
    if not os.path.exists(file_path): return
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if "已拥有" not in html:
        html = re.sub(r'(<h3 class="text-lg font-bold text-gray-900 mb-1">先锋二号</h3>[\s\S]*?)<button class="w-full py-2 rounded font-medium transition-colors bg-\[#C19B5E\] text-white hover:bg-\[#A8864D\]" onclick="window\.location\.href=\'product-detail\.html\'">\s*立即购买\s*</button>', 
            r'\1<button class="w-full py-2 rounded font-medium transition-colors bg-gray-100 text-gray-400 cursor-not-allowed border border-gray-200" disabled><i class="fas fa-check-circle mr-1"></i>已拥有 (一次性买断)</button>', html)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

for base_dir in ['Crm-Group', 'CRM-HK']:
    update_prd(f"{base_dir}/prd-product-orders.html")
    update_admin_management(f"{base_dir}/admin-product-management.html")
    update_admin_orders(f"{base_dir}/admin-product-orders.html")
    update_product_detail(f"{base_dir}/product-detail.html")
    update_product_list(f"{base_dir}/client-product-list.html")

print("All updates applied.")
