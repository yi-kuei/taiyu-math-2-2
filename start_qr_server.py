# -*- coding: utf-8 -*-
import os
import socket
import http.server
import socketserver
import webbrowser

PORT = 8080

def get_ip_addresses():
    ip_list = []
    try:
        hostname = socket.gethostname()
        for ip in socket.gethostbyname_ex(hostname)[2]:
            if not ip.startswith("127."):
                ip_list.append(ip)
    except Exception:
        pass
    if not ip_list:
        ip_list.append("127.0.0.1")
    return ip_list

def run():
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    ips = get_ip_addresses()
    primary_ip = ips[0]
    local_url = f"http://localhost:{PORT}"
    lan_url = f"http://{primary_ip}:{PORT}"
    
    print("=" * 65)
    print("  ★ 泰宇技術高中數學 2-2「三角函數的定義與性質」教學平台伺服器 ★")
    print("=" * 65)
    print(f"\n  [電腦本機瀏覽]  : {local_url}")
    print(f"  [手機 / 平板連線] : {lan_url}")
    if len(ips) > 1:
        print("  [其他備用區域網路 IP]:")
        for ip in ips[1:]:
            print(f"    -> http://{ip}:{PORT}")
    print("\n  請確保手機/平板與此電腦連接至【同一個 Wi-Fi 區域網路】！")
    print("  提示：在手機瀏覽器直接輸入上方連線網址即可立即同步互動。\n")
    print("=" * 65)
    print("  伺服器運行中... 按 Ctrl+C 可隨時停止伺服器。\n")
    
    try:
        webbrowser.open(local_url)
    except Exception:
        pass
        
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  伺服器已正常停止。")

if __name__ == "__main__":
    run()
