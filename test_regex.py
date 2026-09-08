import re
import glob

pattern = r'(<nav class="[^"]*py-4 px-3 space-y-2">).*?(</nav>)'

count = 0
for file in glob.glob('Crm-Group/admin-*.html'):
    if 'prd' in file: continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if re.search(pattern, content, re.DOTALL):
        count += 1
print(f"Matched {count} files.")
