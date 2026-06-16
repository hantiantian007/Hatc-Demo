import re
import glob

files = glob.glob('**/prd-contact*.html', recursive=True)

new_focus_block = """
        <!-- 本期需求重点板块 (致产研测) -->
        <div class="mb-8 border border-red-200 rounded-lg overflow-hidden shadow-sm prd-focus-block">
            <div class="bg-red-50 px-5 py-3 border-b border-red-100 flex items-center">
                <i class="fa-solid fa-bullseye text-red-600 mr-2 text-lg"></i>
                <h2 class="text-red-600 font-bold text-base m-0">本期需求重点 (致产研测)</h2>
            </div>
            <div class="p-5 bg-white text-sm text-gray-700 leading-relaxed focus-content">
                <p class="mb-3 font-medium text-gray-900">本次迭代核心为在官网新增“留资入口”，用于收集无邀请码的散客线索。请重点关注以下业务与交互逻辑：</p>
                
                <div class="space-y-4 mt-4">
                    <!-- 变更点 1 -->
                    <div class="flex items-start">
                        <span class="flex-shrink-0 flex items-center justify-center w-5 h-5 rounded-full bg-red-100 text-red-600 font-bold text-xs mr-3 mt-0.5">1</span>
                        <div>
                            <h4 class="font-bold text-gray-800 mb-1">新增「联系我们」入口</h4>
                            <p class="text-gray-600">在官网页面（如顶部导航栏等全局显著位置）新增<span class="font-semibold text-gray-800">“联系我们”</span>按钮，作为散客留资的统一触发入口。</p>
                        </div>
                    </div>

                    <!-- 变更点 2 -->
                    <div class="flex items-start">
                        <span class="flex-shrink-0 flex items-center justify-center w-5 h-5 rounded-full bg-red-100 text-red-600 font-bold text-xs mr-3 mt-0.5">2</span>
                        <div>
                            <h4 class="font-bold text-gray-800 mb-1">表单弹窗交互（Modal）</h4>
                            <p class="text-gray-600">点击“联系我们”按钮后，不进行页面跳转，而是直接采用<span class="font-semibold text-blue-600">当前页弹窗（Modal）</span>形式弹出「留下资料」表单，以降低用户的操作阻力与流失率。</p>
                        </div>
                    </div>

                    <!-- 变更点 3 -->
                    <div class="flex items-start">
                        <span class="flex-shrink-0 flex items-center justify-center w-5 h-5 rounded-full bg-red-100 text-red-600 font-bold text-xs mr-3 mt-0.5">3</span>
                        <div>
                            <h4 class="font-bold text-gray-800 mb-1">表单必填项强校验</h4>
                            <p class="text-gray-600">弹窗内的表单字段需进行严格的非空校验，所有带有<span class="font-semibold text-red-600">红色星号（*）</span>的字段均为必填项。提交前需确保必填项已完善，否则前端予以拦截并进行标红提示。</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

# 正则匹配目前的占位符区块
pattern = re.compile(r'<!-- 本期需求重点板块 \(致产研测\) -->.*?<p class="text-gray-400 italic">待补充：请等待产品经理描述本期具体的变更与新增点\.\.\.</p>.*?</div>\s*</div>', re.DOTALL)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(new_focus_block.strip(), content, count=1)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Contact PRDs updated.")