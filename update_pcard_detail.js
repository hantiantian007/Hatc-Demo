const fs = require('fs');
const file = '/Users/joker/Desktop/Ai/AI/1.2.0/Crm-Group/admin-activity-pcard-detail.html';
let content = fs.readFileSync(file, 'utf8');

// 1. 取消编辑活动、结束活动按钮
content = content.replace(/<div class="flex items-center gap-2">\s*<button class="h-8 px-4 rounded-md border border-gray-200 bg-white text-gray-600 hover:bg-gray-50 transition-colors text-xs font-medium">\s*<i class="fa-solid fa-pen mr-1.5"><\/i> 编辑活动\s*<\/button>\s*<button class="h-8 px-4 rounded-md bg-red-50 text-red-600 border border-red-200 hover:bg-red-100 transition-colors text-xs font-medium">\s*<i class="fa-solid fa-stop mr-1.5"><\/i> 结束活动\s*<\/button>\s*<\/div>/g, '');

// 2. 取消图片内的状态tab (用户列表上面的Tab切换)
const tabRegex = /<!-- Tab 切换 -->\s*<div class="px-5 pt-3 border-b border-gray-100 bg-gray-50\/60">\s*<div class="flex items-center gap-2 text-xs overconst fs = require('fs');
const file = '/Users/coconst file = '/Users/joker/D, let content = fs.readFileSync(file, 'utf8');

// 1. 取消编辑活动、结束活动按钡?// 1. 取消编辑活动、结束活动按钮
contex content = content.replace(/<div class="flex ow
// 2. 取消图片内的状态tab (用户列表上面的Tab切换)
const tabRegex = /<!-- Tab 切换 -->\s*<div class="px-5 pt-3 border-b border-gray-100 bg-gray-50\/60">\s*<div class="flex items-center gap-2 text-xs overconst fs = require('fs');
const file = '/Users/coconst file = '/Users/joker/D, let content = fs.readFileSync(file, 'utf8');

// 1. 取消编辑活动、结束活动按钡?// 1. 取消编辑活动、结束活动按钮
contex content = content.replace(/<div clid const tabRegex = /<!-- Tab 切换 -->\s*<div class="px-5 pt-3 bor?"const file = '/Users/coconst file = '/Users/joker/D, let content = fs.readFileSync(file, 'utf8');

// 1. 取消编辑活动、结束活动按钡?// 1. 取消编辑活动"