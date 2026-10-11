# -*- coding: utf-8 -*-
import os
import shutil
import zipfile

def package_project():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    download_dir = os.path.join(base_dir, "download")
    os.makedirs(download_dir, exist_ok=True)
    
    files_to_download = [
        "2-2_三角函數的定義與性質_學生學習單.docx",
        "2-2_三角函數的定義與性質_教師解答版.docx",
        "2-2_三角函數的定義與性質_全套60張圖解學習卡.pdf",
        "2-2_三角函數的定義與性質_四節課教學計畫與教案.docx"
    ]
    
    print("=== 正在複製檔案至 download/ ===")
    for fname in files_to_download:
        src = os.path.join(base_dir, fname)
        dst = os.path.join(download_dir, fname)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  [OK] 複製 {fname} -> download/")
        else:
            print(f"  [警告] 找不到來源檔案: {fname}")
            
    # 建立網站上傳包目錄
    pkg_name = "網站上傳包_2-2_三角函數的定義與性質"
    pkg_dir = os.path.join(base_dir, pkg_name)
    if os.path.exists(pkg_dir):
        shutil.rmtree(pkg_dir)
    os.makedirs(pkg_dir, exist_ok=True)
    
    print(f"\n=== 正在建立 {pkg_name}/ ===")
    idx_src = os.path.join(base_dir, "index.html")
    if os.path.exists(idx_src):
        shutil.copy2(idx_src, os.path.join(pkg_dir, "index.html"))
        print("  [OK] 複製 index.html")
        
    cp_src = os.path.join(base_dir, "cards_printable.html")
    if os.path.exists(cp_src):
        shutil.copy2(cp_src, os.path.join(pkg_dir, "cards_printable.html"))
        print("  [OK] 複製 cards_printable.html")
        
    shutil.copytree(download_dir, os.path.join(pkg_dir, "download"))
    print("  [OK] 複製 download/ 目錄")
    
    zip_path = os.path.join(base_dir, "2-2_三角函數的定義與性質_網站上傳包.zip")
    print(f"\n=== 正在壓縮打包為 {os.path.basename(zip_path)} ===")
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(pkg_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, pkg_dir)
                zf.write(full_path, rel_path)
    print(f"  [OK] 打包完成！ZIP 大小: {os.path.getsize(zip_path) / (1024*1024):.2f} MB")

if __name__ == "__main__":
    package_project()
