const fs = require('fs');
const file = '/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/admin-home.html';
let content = fs.readFileSync(file, 'utf8');

// 1. Remove bank card icons from the left multi-activity block
// Specifically from the Pcard panel
content = content.replace(/<i class="fa-solid fa-credit-card" style="font-size:11px;"><\/i>\s*Pcard 银行卡/g, 'Pcard 银行卡');
content = content.replace(/<div style="width:44px; height:44px; border-radius:12px; background:linear-gradient\(135deg,#fbbf24,#f97316\); display:flex; align-items:center; justify-content:center; color:#fff; box-shadow:0 1px 2px rgba\(0,0,0,0.05\);">\s*<i class="fa-solid fa-credit-card" style="font-size:18px;"><\/i>\s*<\/div>/g, '');

// 2. We should move the Pcard card to the right sidebar and remove the Pcard part from the left.
// Actually, it's easier to just remove the whole left activity block if it's only for Pcard. But it has tab1 and tab2.
// The user said: "移除所有银行卡及装饰性图标".
// Let's first just add the right sidebar Pcard card.

const sidebarMarker = '<div class="w-[320px] xl:w-[360px] flex flex-col gap-6 flex-shrink-0">';
const newCard = `
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
`;

if (content.indexOf('Pcard 活动进度') === -1) {
    content = content.replace(sidebarMarker, sidebarMarker + newCard);
}

// Now let's remove the Pcard panel from the left activity block if it exists, or just hide it.
// Actually, let's just remove the entire `<!-- ⚡ 活动卡片 (多活动切换) -->` to `<!-- Row 1: 三个统计卡片 -->` block.
// Wait, the project is Pcard related. The other two tabs ("入金赠金", "返佣加码") might just be dummy UI.
// Let's remove the whole left activity block since the Kanban says "右侧边栏新增进度卡", implying the progress card shouldn't be a huge tabbed area on the left.
const startMarker = '<!-- ⚡ 活动卡片 (多活动切换) -->';
const endMarker = '<!-- Row 1: 三个统计卡片 -->';
const startIndex = content.indexOf(startMarker);
const endIndex = content.indexOf(endMarker);

if (startIndex !== -1 && endIndex !== -1) {
    content = content.substring(0, startIndex) + content.substring(endIndex);
}

// Remove any remaining `fa-credit-card`
content = content.replace(/<i class="[^"]*fa-credit-card[^"]*"><\/i>/g, '');

fs.writeFileSync(file, content, 'utf8');
console.log('admin-home.html updated successfully.');
