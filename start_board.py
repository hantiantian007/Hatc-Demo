#!/usr/bin/env python3
import http.server
import socketserver
import json
import re
import os

PORT = 8080

class BoardHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/save_dates':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            try:
                with open('index.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for item in data:
                    task = item['task']
                    new_date = item['date']
                    
                    # Update display span
                    pattern1 = r'(<span class="date-text" data-task="' + re.escape(task) + r'">)(.*?)(</span>)'
                    content = re.sub(pattern1, r'\g<1>' + new_date + r'\g<3>', content)
                    
                    # Update input value
                    pattern2 = r'(<input type="text" class="[^"]*date-input[^"]*" data-task="' + re.escape(task) + r'" value=")([^"]*)(")'
                    content = re.sub(pattern2, r'\g<1>' + new_date + r'\g<3>', content)

                with open('index.html', 'w', encoding='utf-8') as f:
                    f.write(content)
                    
                # 自动提交到 Git
                os.system('git add index.html && git commit -m "chore: 需求看板更新计划上线时间" --quiet')

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_error(404)

socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("", PORT), BoardHandler) as httpd:
        print("\n" + "="*60)
        print(" 🚀 看板管理服务已成功启动！")
        print(f" 👉 请在浏览器中打开: http://localhost:{PORT}")
        print(" 📝 在页面中修改日期并保存后，系统将自动提交到 Git")
        print(" 🛑 按 Ctrl+C 停止服务")
        print("="*60 + "\n")
        httpd.serve_forever()
except OSError as e:
    if e.errno == 48:
        print(f"端口 {PORT} 已被占用，请更换端口或关闭其他服务。")
    else:
        print(e)
