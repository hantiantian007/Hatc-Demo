const fs = require('fs');
const path = require('path');

function processDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        if (file.endsWith('.html')) {
            const filePath = path.join(dir, file);
            let content = fs.readFileSync(filePath, 'utf8');
            
            // This is the active deposit item
            const depositActivePattern = `<a href="admin-report-sales-deposit.html" class="block py-2 text-sm text-white font-medium bg-white/10 px-3 -ml-3 rounded transition-colors relative">
                        销售入金奖励统计
                        <span class="absolute left-0 top-1/2 -translate-y-1/2 w-1 h-4 bg-menuActive rounded-r"></span>
                    </a>`;
            
            // This is the inactive deposit item
            const depositInactivePattern = `<a href="admin-report-sales-deposit.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">销售入金奖励统计</a>`;
            
            const newItemInactive = `\n                    <a href="admin-report-relationship-tree.html" class="block py-2 text-sm text-gray-400 hover:text-white transition-colors">关系树统计</a>`;

            if (content.includes(depositActivePattern) && !content.includes('关系树统计')) {
                content = content.replace(depositActivePattern, depositActivePattern + newItemInactive);
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Updated ${filePath}`);
            } else if (content.includes(depositInactivePattern) && !content.includes('关系树统计')) {
                content = content.replace(depositInactivePattern, depositInactivePattern + newItemInactive);
                fs.writeFileSync(filePath, content, 'utf8');
                console.log(`Updated ${filePath}`);
            }
        }
    }
}

processDir('./CRM-HK-1.2.0');
processDir('./Crm-Group-1.2.0');