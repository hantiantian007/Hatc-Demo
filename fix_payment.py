import os

# 1. 强制写入 product-detail.html
dirs = ['Crm-Group', 'CRM-HK', 'Group-Gw', 'Hk-Gw']
old_payment_section = """<!-- 支付方式与余额 -->
                <div class="bg-blue-50/50 p-4 rounded-lg border border-blue-100">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-sm font-medium text-blue-900">主钱包余额扣款</span>
                        <span class="text-sm font-bold text-blue-700">9,999.00 USD</span>
                    </div>
                    <p class="text-xs text-blue-600/80 mt-1"><i class="fa-solid fa-circle-info mr-1"></i>购买成功后，对应金额将直接从您的CRM主钱包中扣除。</p>
                </div>"""

new_payment_section_sc = """<!-- 选择支付 MT 账号 -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">选择付款 MT 账号 <span class="text-red-500">*</span></label>
                    <div class="space-y-2 max-h-40 overflow-y-auto no-scrollbar pr-1">
                        <!-- 账号 1 -->
                        <label class="relative flex items-center justify-between p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors has-[:checked]:border-primary has-[:checked]:bg-primary/5">
                            <div class="flex items-center gap-3">
                                <input type="radio" name="pay_mt_account" value="667788" checked class="text-primary focus:ring-primary h-4 w-4">
                                <div>
                                    <div class="text-sm font-bold text-gray-900">MT5 - 667788</div>
                                    <div class="text-xs text-gray-500 mt-0.5">标准账户</div>
                                </div>
                            </div>
                            <div class="text-right">
                                <div class="text-sm font-bold text-gray-900">$1,500.00</div>
                                <div class="text-[10px] text-gray-400">可用余额</div>
                            </div>
                        </label>
                        <!-- 账号 2 -->
                        <label class="relative flex items-center justify-between p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors has-[:checked]:border-primary has-[:checked]:bg-primary/5">
                            <div class="flex items-center gap-3">
                                <input type="radio" name="pay_mt_account" value="556677" class="text-primary focus:ring-primary h-4 w-4">
                                <div>
                                    <div class="text-sm font-bold text-gray-900">MT5 - 556677</div>
                                    <div class="text-xs text-gray-500 mt-0.5">零点账户</div>
                                </div>
                            </div>
                            <div class="text-right">
                                <div class="text-sm font-bold text-gray-900">$300.00</div>
                                <div class="text-[10px] text-gray-400">可用余额</div>
                            </div>
                        </label>
                    </div>
                    <p class="text-xs text-gray-500 mt-2"><i class="fa-solid fa-circle-info mr-1 text-blue-500"></i>购买成功后，对应金额将直接从您选定的 MT 账号余额中扣除。</p>
                </div>"""

new_payment_section_tc = new_payment_section_sc.replace('选择付款 MT 账号', '選擇付款 MT 賬號').replace('标准账户', '標準賬戶').replace('零点账户', '零點賬戶').replace('可用余额', '可用餘額').replace('购买成功后，对应金额将直接从您选定的 MT 账号余额中扣除。', '購買成功後，對應金額將直接從您選定的 MT 賬號餘額中扣除。')

for d in dirs:
    filepath = os.path.join(d, 'product-detail.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        is_tc = '商品介紹' in content
        new_sec = new_payment_section_tc if is_tc else new_payment_section_sc
        content = content.replace(old_payment_section, new_sec)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 2. 强制写入 client-orders.html
for d in ['Crm-Group', 'CRM-HK']:
    filepath = os.path.join(d, 'client-orders.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        is_tc = '訂單號' in content
        lbl = '付款賬號' if is_tc else '付款账号'
        
        old_1 = '<span class="text-red-500 font-bold">$300.00</span>'
        new_1 = f'<span class="text-red-500 font-bold">$300.00</span> <span class="text-gray-400 text-xs ml-2 font-normal">({lbl}: MT5-667788)</span>'
        if new_1 not in content:
            content = content.replace(old_1, new_1)
            
        old_2 = '<span class="text-red-500 font-bold">$150.00</span>'
        new_2 = f'<span class="text-red-500 font-bold">$150.00</span> <span class="text-gray-400 text-xs ml-2 font-normal">({lbl}: MT5-556677)</span>'
        if new_2 not in content:
            content = content.replace(old_2, new_2)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 3. 强制写入 admin-product-orders.html
for d in ['Crm-Group', 'CRM-HK']:
    filepath = os.path.join(d, 'admin-product-orders.html')
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        is_tc = '商品訂單' in content
        lbl_pay = '付款賬號' if is_tc else '付款账号'
        lbl_transfer = '歸集至' if is_tc else '归集至'
        
        # 匹配第一个转入（ORD-20260623-8891）
        old_transfer_1 = '<div class="text-[10px] text-gray-500 mt-0.5" title="资金转入 MT-9999999"><i class="fa-solid fa-arrow-right-arrow-left text-gray-400 mr-1"></i>转入: MT-9999999</div>'
        if is_tc:
            old_transfer_1 = '<div class="text-[10px] text-gray-500 mt-0.5" title="资金转入 MT-9999999"><i class="fa-solid fa-arrow-right-arrow-left text-gray-400 mr-1"></i>歸集至: MT-9999999</div>'
            # Check if already replaced partially
            if old_transfer_1 not in content:
                 old_transfer_1 = '<div class="text-[10px] text-gray-500 mt-0.5" title="資金轉入 MT-9999999"><i class="fa-solid fa-arrow-right-arrow-left text-gray-400 mr-1"></i>轉入: MT-9999999</div>'
            if old_transfer_1 not in content:
                 old_transfer_1 = '<div class="text-[10px] text-gray-500 mt-0.5" title="资金转入 MT-9999999"><i class="fa-solid fa-arrow-right-arrow-left text-gray-400 mr-1"></i>转入: MT-9999999</div>'
                 
        parts = content.split(old_transfer_1)
        if len(parts) == 3: # 正好出现两次
            new_1 = f'<div class="text-[10px] text-gray-500 mt-1"><i class="fa-solid fa-wallet text-gray-400 mr-1"></i>{lbl_pay}: 667788</div>\n                                <div class="text-[10px] text-gray-500 mt-0.5" title="资金转入 MT-9999999"><i class="fa-solid fa-arrow-right-arrow-left text-gray-400 mr-1"></i>{lbl_transfer}: MT-9999999</div>'
            new_2 = f'<div class="text-[10px] text-gray-500 mt-1"><i class="fa-solid fa-wallet text-gray-400 mr-1"></i>{lbl_pay}: 556677</div>\n                                <div class="text-[10px] text-gray-500 mt-0.5" title="资金转入 MT-9999999"><i class="fa-solid fa-arrow-right-arrow-left text-gray-400 mr-1"></i>{lbl_transfer}: MT-9999999</div>'
            if is_tc:
                new_1 = new_1.replace('资金转入', '資金轉入')
                new_2 = new_2.replace('资金转入', '資金轉入')
                
            content = parts[0] + new_1 + parts[1] + new_2 + parts[2]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("All done.")