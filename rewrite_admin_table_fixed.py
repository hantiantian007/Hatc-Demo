import re
import os

def rewrite_table(filepath, is_tc):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define language specific terms
    l_order = '訂單編號' if is_tc else '订单编号'
    l_time = '購買時間' if is_tc else '购买时间'
    l_client = '客戶姓名' if is_tc else '客户姓名'
    l_email = '電子郵箱' if is_tc else '电子邮箱'
    l_product = '商品名稱' if is_tc else '商品名称'
    l_spec = '套餐規格' if is_tc else '套餐规格'
    l_amount = '實付金額' if is_tc else '实付金额'
    l_pay_acc = '付款 MT 賬號' if is_tc else '付款 MT 账号'
    l_collect = '歸集 MT 賬號' if is_tc else '归集 MT 账号'
    l_deliver_acc = '交付賬號' if is_tc else '交付账号'
    l_deliver_time = '有效期限' if is_tc else '有效期限'
    l_status = '狀態' if is_tc else '状态'
    l_action = '操作' if is_tc else '操作'

    new_thead = f"""<thead>
                        <tr class="bg-gray-50 text-gray-500 text-xs uppercase tracking-wider border-b border-gray-200">
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_order}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_time}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_client}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_email}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_product}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_spec}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_amount}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_pay_acc}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_collect}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_deliver_acc}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_deliver_time}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-left">{l_status}</th>
                            <th class="px-4 py-3 font-medium whitespace-nowrap text-right">{l_action}</th>
                        </tr>
                    </thead>"""
                        
    content = re.sub(r'<thead[\s\S]*?</thead>', new_thead, content)

    l_pending = '處理中 (待交付)' if is_tc else '处理中 (待交付)'
    l_delivered = '已交付' if is_tc else '已交付'
    l_btn_deliver = '去交付' if is_tc else '去交付'
    l_btn_view = '查看' if is_tc else '查看'
    l_product_name = '先鋒一號智能交易系統' if is_tc else '先锋一号智能交易系统'
    l_spec_name = '1個月' if is_tc else '1个月'
    l_spec_name2 = '3個月' if is_tc else '3个月'
    l_pending_desc = '待運營線下人工開通' if is_tc else '待运营线下人工开通'
    l_zhangsan = '張三' if is_tc else '张三'
    l_lisi = '李四' if is_tc else '李四'

    tbody_content = f"""<tbody class="text-sm divide-y divide-gray-100">
                        <!-- 订单 1: 待交付 -->
                        <tr class="hover:bg-gray-50 transition-colors">
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">ORD-20260623-8891</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500 text-xs">2026-06-23<br>14:30:22</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">{l_zhangsan}</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500">zhangsan@email.com</td>
                            <td class="px-4 py-3 whitespace-nowrap font-medium text-blue-600">{l_product_name}</td>
                            <td class="px-4 py-3 whitespace-nowrap"><span class="px-2 py-1 bg-gray-100 rounded text-xs">{l_spec_name}</span></td>
                            <td class="px-4 py-3 whitespace-nowrap font-bold text-red-500">$300.00</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">667788</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500">MT-9999999</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-400 italic">-</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-400 italic text-xs">{l_pending_desc}</td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800 border border-blue-200">
                                    <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mr-1.5 animate-pulse"></span>
                                    {l_pending}
                                </span>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap text-right">
                                <button onclick="openDeliveryModal('ORD-20260623-8891', '{l_zhangsan}', '{l_product_name}')" class="px-4 py-1.5 rounded text-xs font-bold shadow-md transition-colors transform hover:-translate-y-0.5" style="background-color: #FCD574; color: #111827;" onmouseover="this.style.backgroundColor='#fbc94e'" onmouseout="this.style.backgroundColor='#FCD574'">{l_btn_deliver}</button>
                            </td>
                        </tr>
                        
                        <!-- 订单 2: 已交付 -->
                        <tr class="hover:bg-gray-50 transition-colors bg-gray-50/30">
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">ORD-20260621-1024</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500 text-xs">2026-06-21<br>09:15:00</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">{l_lisi}</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500">lisi_fx@email.com</td>
                            <td class="px-4 py-3 whitespace-nowrap font-medium text-blue-600">{l_product_name}</td>
                            <td class="px-4 py-3 whitespace-nowrap"><span class="px-2 py-1 bg-gray-100 rounded text-xs">{l_spec_name2}</span></td>
                            <td class="px-4 py-3 whitespace-nowrap font-bold text-red-500">$150.00</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">556677</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500">MT-9999999</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-900">lisi_vip001</td>
                            <td class="px-4 py-3 whitespace-nowrap text-gray-500 text-xs">2026-06-21 至<br>2026-09-21</td>
                            <td class="px-4 py-3 whitespace-nowrap">
                                <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-green-100 text-green-800 border border-green-200">
                                    <span class="w-1.5 h-1.5 bg-green-500 rounded-full mr-1.5"></span>
                                    {l_delivered}
                                </span>
                            </td>
                            <td class="px-4 py-3 whitespace-nowrap text-right">
                                <button class="text-primary hover:text-primary-dark font-medium text-sm transition-colors">{l_btn_view}</button>
                            </td>
                        </tr>
                    </tbody>"""

    content = re.sub(r'<tbody[\s\S]*?</tbody>', tbody_content, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

rewrite_table('Crm-Group/admin-product-orders.html', False)
rewrite_table('CRM-HK/admin-product-orders.html', True)

print("Table successfully rewritten.")