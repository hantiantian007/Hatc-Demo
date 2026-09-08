import re
import glob
import os

new_nav_content = """
            <a href="admin-home.html" class="flex items-center px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                <i class="fa-solid fa-house w-6 text-center text-lg group-hover:text-white transition-colors"></i><span class="ml-3 font-medium text-[15px]">首页</span>
            </a>
            
            <!-- 出入金 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-braille w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">出入金</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="client-deposit-record-cent-account.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">入金</a>
                    <a href="client-withdraw-record-cent-account.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">出金</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">返佣提现</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">我的赠金</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">待审核入金</a>
                    <a href="admin-withdraw-pending-review.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">待审核出金</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">赠金审核</a>
                    <a href="admin-bankcard-add.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">待审核银行卡</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">内部转账</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">转账审核</a>
                </div>
            </div>

            <!-- 财务对账 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-file-invoice-dollar w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">财务对账</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="admin-reconciliation-daily-record.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">每日对账日志</a>
                    <a href="admin-reconciliation-internal.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">对账异常看板</a>
                </div>
            </div>

            <!-- 佣金管理 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-border-all w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">佣金管理</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">基础分佣模版</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">佣金配置</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">基础分佣配置</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">加点分佣配置</a>
                </div>
            </div>

            <!-- 活动管理 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-file-alt w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">活动管理</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="admin-activity-list.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">活动列表</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">成长计划</a>
                    <a href="client-activity-ib-plan.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">IB 计划</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">活动审核</a>
                </div>
            </div>

            <!-- 动态公告 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-bullhorn w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">动态公告</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">集团动态</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">最新公告</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">推送消息</a>
                </div>
            </div>

            <!-- 客户管理 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-user-group w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">客户管理</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="admin-client-list.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">客户列表</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">账户管理</a>
                    <a href="admin-audit-list.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">账户审核</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">客户变动详情</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">分组管理</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">分享链接</a>
                    <a href="admin-sales-list.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">销售列表</a>
                    <a href="admin-leads-list.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">留资列表</a>
                </div>
            </div>
            
            <!-- 报表中心 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-chart-pie w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">报表中心</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="admin-report-commission-stats.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">佣金统计</a>
                    <a href="admin-report-trading.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">交易报表</a>
                    <a href="admin-report-position.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">持仓报表</a>
                    <a href="admin-report-close-position.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">平仓交易记录</a>
                    <a href="admin-report-finance-cent-account.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">财务报表</a>
                    <a href="admin-report-commission-cent-account.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">佣金报表</a>
                    <a href="admin-report-position-stats.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">持仓统计</a>
                    <a href="admin-report-trade-record-cent-account.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">交易记录</a>
                    <a href="admin-report-sales-trading.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">销售交易奖励报表</a>
                    <a href="admin-report-sales-deposit.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">销售入金奖励统计</a>
                    <a href="admin-report-equity.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">盈亏报表</a>
                </div>
            </div>

            <!-- 委托交易 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-handshake-angle w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">委托交易</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="admin-trust-phase1.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">委托交易一期</a>
                    <a href="admin-trust-account-management.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">委托交易账户管理</a>
                    <a href="admin-trust-rule-config.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">查看规则配置</a>
                </div>
            </div>

            <!-- 系统管理 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-gear w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">系统管理</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors flex justify-between items-center">系统设置 <i class="fa-solid fa-chevron-right text-[8px] mr-2"></i></a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors flex justify-between items-center">MT设置 <i class="fa-solid fa-chevron-right text-[8px] mr-2"></i></a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors flex justify-between items-center">群发管理 <i class="fa-solid fa-chevron-right text-[8px] mr-2"></i></a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors flex justify-between items-center">消息管理 <i class="fa-solid fa-chevron-right text-[8px] mr-2"></i></a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors flex justify-between items-center">日志管理 <i class="fa-solid fa-chevron-right text-[8px] mr-2"></i></a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">配置参数</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">支付币种</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">支付管理</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">提现设置</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">返佣设置</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">验证码记录</a>
                    <a href="admin-tag-management.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">标签管理</a>
                </div>
            </div>

            <a href="#" class="flex items-center px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                <i class="fa-solid fa-download w-6 text-center text-lg group-hover:text-white transition-colors"></i><span class="ml-3 font-medium text-[15px]">交易工具</span>
            </a>

            <!-- 财务管理 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-wallet w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">财务管理</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">财务报表明细</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">客户信息表</a>
                </div>
            </div>

            <!-- 风控管理 -->
            <div class="menu-group">
                <button onclick="toggleSubmenu(this)" class="w-full flex items-center justify-between px-3 py-3 text-menuText hover:text-white hover:bg-menuHover rounded-lg transition-colors group">
                    <div class="flex items-center">
                        <i class="fa-solid fa-shield w-6 text-center text-lg group-hover:text-white transition-colors"></i>
                        <span class="ml-3 font-medium text-[15px]">风控管理</span>
                    </div>
                    <i class="fa-solid fa-chevron-right text-[10px] arrow-transition"></i>
                </button>
                <div class="submenu-transition pl-11 pr-3 space-y-1 mt-1">
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">客户登录日志</a>
                    <a href="admin-risk-login-alert.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">登录 IP 一致性比对</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">黑名单管理</a>
                    <a href="#" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">平仓间隔统计</a>
                </div>
            </div>
"""

pattern = r'(<nav class="[^"]*flex-1 overflow-y-auto no-scrollbar py-4 px-3 space-y-2">).*?(</nav>)'

html_files = glob.glob('Crm-Group/admin-*.html') + glob.glob('Crm-Group/client-*.html')

count = 0
for file in html_files:
    if 'prd' in file:
        continue
        
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, n = re.subn(pattern, r'\1' + '\n' + new_nav_content + '\n        \2', content, flags=re.DOTALL)
        if n > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Updated {count} files.")
