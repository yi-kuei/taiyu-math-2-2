# -*- coding: utf-8 -*-
"""
generate_cards_pdf.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
A4 橫向滿版圖解學習卡產生器 (HTML + Edge Headless 高解析向量 PDF)
遵循 SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版：
- A4 橫向 (297mm x 210mm) 一頁一張雙欄卡片
- 左側正面題目與破案提示，右側背面線索推理鏈與標準 SVG 向量幾何圖解
- 全欄位 100% KaTeX 標準數學式渲染
- 產出 2-2_三角函數的定義與性質_全套60張圖解學習卡.pdf
"""

import os
import subprocess
import time
import cards_part1
import cards_part2

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE_EXE = next((p for p in EDGE_PATHS if os.path.exists(p)), None)

def generate_printable_html(cards):
    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質 ‧ 全套 {len(cards)} 張圖解學習卡</title>
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @page {{
      size: 297mm 210mm landscape;
      margin: 0;
    }}
    body {{
      margin: 0;
      padding: 0;
      background-color: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    .page-container {{
      width: 297mm;
      height: 210mm;
      padding: 10mm 14mm 8mm 14mm;
      box-sizing: border-box;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #ffffff;
      position: relative;
    }}
    .katex, .katex-html, .katex-display {{
      white-space: nowrap !important;
    }}
    .katex-display {{
      margin: 0.2em 0 !important;
      display: inline-block !important;
    }}
    .katex svg {{
      display: block !important;
      position: absolute !important;
      width: 100% !important;
      height: inherit !important;
      fill: currentColor !important;
      stroke: currentColor !important;
      max-height: none !important;
      margin: 0 !important;
    }}
  </style>
</head>
<body>
"""

    for idx, card in enumerate(cards):
        steps_html = "".join([f"""
          <div class="mb-2 p-2.5 rounded-lg bg-amber-50/60 border border-amber-200/80 text-xs">
            <span class="font-bold text-amber-800 mr-1">{s['title']}：</span>
            <span class="text-slate-800">{s['content']}</span>
          </div>
        """ for s in card['steps']])

        html += f"""
  <div class="page-container">
    <!-- 頂部頁首 -->
    <div class="flex items-center justify-between pb-2 border-b border-amber-200">
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-0.5 rounded text-xs font-black bg-amber-600 text-white">{card['tag']}</span>
        <span class="text-sm font-bold text-slate-800">泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質</span>
        <span class="px-2 py-0.5 rounded text-xs font-semibold bg-amber-100 text-amber-800">{card['category']} ‧ {card['page']}</span>
      </div>
      <div class="text-xs font-bold text-amber-700">
        名偵探柯南數理探案特訓 ‧ 數位教學學習包
      </div>
    </div>

    <!-- 主體內容：左右雙欄自適應卡片 -->
    <div class="grid grid-cols-2 gap-4 flex-1 my-3 items-stretch">
      <!-- 左欄：正面案情題幹與審題導引 -->
      <div class="flex flex-col justify-between p-4 rounded-xl bg-[#fbf9f4] border-2 border-amber-300/80 shadow-xs">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-red-100 text-red-700">
              案情卷宗題幹
            </span>
            <span class="text-xs text-slate-500 font-medium">{card['page']}</span>
          </div>
          <h2 class="text-base font-black text-amber-950 mb-3">{card['title']}</h2>
          <div class="text-sm leading-relaxed text-slate-800 py-1">
            {card['front_content']}
          </div>
        </div>

        <div class="mt-3 p-3 rounded-lg bg-red-50/80 border border-red-200 text-xs">
          <div class="font-bold text-red-800 mb-1">{card['front_tip']}</div>
        </div>
      </div>

      <!-- 右欄：背面名偵探推理筆記與幾何圖解 -->
      <div class="flex flex-col justify-between p-4 rounded-xl bg-white border-2 border-slate-200 shadow-xs">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-700">
              👓 名偵探推理筆記 ‧ 線索推理鏈
            </span>
            <span class="text-xs text-slate-500 font-medium">結構化推演</span>
          </div>
          <div class="space-y-1">
            {steps_html}
          </div>
        </div>

        <div>
          <!-- 標準 SVG 向量圖解 (高度提升，移除裁切) -->
          <div class="h-40 my-2 flex items-center justify-center bg-slate-50 rounded-lg p-1 border border-slate-100">
            {card['svg']}
          </div>

          <!-- 結論印章 -->
          <div class="p-2.5 rounded-lg bg-emerald-50 border-2 border-emerald-500 text-xs font-bold text-emerald-900 text-center">
            {card['conclusion']}
          </div>
        </div>
      </div>
    </div>

    <!-- 底部頁尾 -->
    <div class="flex items-center justify-between pt-1 border-t border-slate-200 text-[11px] text-slate-500">
      <div>第 {idx+1} 頁 ｜ 全套 {len(cards)} 張圖解卡完整收錄</div>
      <div class="font-medium">PLVS 數學科  教育學習用</div>
      <div>授權密碼：88888888</div>
    </div>
  </div>
"""

    html += """
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      renderMathInElement(document.body, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ],
        throwOnError: false
      });
    });
  </script>
</body>
</html>
"""
    return html

def main():
    cards = cards_part1.CARDS_PART1 + cards_part2.CARDS_PART2
    print(f"載入圖解學習卡總數：{len(cards)} 張 (CASE 01 ~ CASE {len(cards):02d})")

    html_content = generate_printable_html(cards)
    html_file = "cards_printable.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"成功產出列印版網頁：{html_file}")

    if not EDGE_EXE:
        print("未偵測到 Edge 瀏覽器，無法自動產出 PDF！")
        return

    pdf_file = "2-2_三角函數的定義與性質_全套60張圖解學習卡.pdf"
    abs_html = os.path.abspath(html_file)
    abs_pdf = os.path.abspath(pdf_file)

    print(f"由 Edge Headless 編譯高解析 A4 橫向 PDF：{pdf_file}...")
    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=12000",
        f"--print-to-pdf={abs_pdf}",
        abs_html
    ]
    subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="ignore")

    if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 1000:
        print(f"成功產出全套學習卡 PDF：{pdf_file} (檔案大小：{os.path.getsize(abs_pdf):,} 位元組)")
    else:
        print("PDF 產出失敗或檔案異常！")

if __name__ == "__main__":
    main()
