import re

with open('Crm-Group/admin-home.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove left activity block
start_marker = '<!-- ⚡ 活动卡片 (多活动切换) -->'
end_marker = '<!-- Row 1: 三个统计卡片 -->'
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]

# 2. Add Pcard to right sidebar
sidebar_marker = '<div class="w-[320px] xl:w-[360px] flex flex-col gap-6 flex-shrink-0">'
new_card = """
                <!-- Pcard 进度卡 -->
                <div class="bg-white rounded-xl card-shadow border border-[#C19B5E] p-5">
                    <div class="flex justify-between items-center mb-4">
                        <div class="flex items-center gap-2">
                            <h3 class="font-bold text-gray-800 text-sm">Pcard 活动进度</h3>
                            <span class="inline-flex px-2 py-0.5 rounded text-[10px] font-medium bg-[#fef3c7] text-[#B45309]">进行中</span>
                        </div>
                        <a href="admin-activity-pcard-detail.html" class="text-xs text-[#C19B5E] hover:underline font-medium">查看详情</a>
                    </div>
                    
                    <div class="space-y-4">
                        <!-- 净入金 -->
                        <div>
                            <div class="flex justify-between items-center text-xs mb-1.5">
                                <span class="text-gray-500 font-medium">净入金</span>
                                <span class="font-bold text-gray-700">
                                    $1,013.00 <span class="text-gray-400 font-normal">/ $1,000</span>
                                </span>
                            </div>
                            <div class="h-1.5 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full w-full bg-[#C19B5E] rounded-full" style="width: 100%"></div>
                            </div>
                            <p class="text-[10px] text-[#C19B5E] mt-1 font-medium">已达标</p>
                        </div>
                        
                        <!-- 交易手数 -->
                        <div>
                            <div class="flex justify-between items-center text-xs mb-1.5">
                                <span class="text-gray-500 font-medium">交易手数</span>
                                <span class="font-bold text-gray-700">
                                    5.0 <span class="text-gray-400 font-normal">/ 5 Lot</span>
                                </span>
                            </div>
                            <div class="h-1.5 bg-gray-100 rounded-full overflow-hidden">
                                <div class="h-full w-full bg-[#C19B5E] rounded-full" style="width: 100%"></div>
                            </div>
                            <p class="text-[10px] text-[#C19B5E] mt-1 font-medium">已达标</p>
                        </div>
                    </div>
                    
                    <div class="mt-4 p-2 bg-[#fef3c7]/30 border border-[#fef3c7] rounded text-xs text-[#B45309] font-medium text-center">
                        双条件已达标，请联系客服免费办理 Pcard。
                    </div>
                </div>
"""

if 'Pcard 活动进度' not in content:
    content = content.replace(sidebar_marker, sidebar_marker + new_card)

# 3. Remove bank card icons
content = re.sub(r'<i class="[^"]*fa-credit-card[^"]*"><\/i>', '', content)

with open('Crm-Group/admin-home.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated admin-home.html")
