# -*- coding: utf-8 -*-
"""
generate_full_flipcard_page.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
數位翻牌圖解互動平台主頁 index.html 生成器
遵循 SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版：
- 卡片網格強制雙欄 (grid-cols-1 md:grid-cols-2)
- 全欄位 100% KaTeX 標準數學式，正面無水平捲軸適度折行
- 頁尾第一列三色膠囊訪客計數器 (總搜查/特派員/破案互動由 0 起算)
- 雙向同步逐步導引 showStep，課堂聚焦與半透明模糊遮蔽
- 劇院全螢幕滿版 (100% 滿版劇院投影) 內嵌多功能電子白板
- 內嵌 Base64 學生學習單、教師解答版 (密碼 88888888) 與 16:9 PPTX 簡報
"""

import json
import cards_part1
import cards_part2
import interactive_cards_data
import interactive_js_module
import docx_b64

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質 ‧ 名偵探柯南數理探案特訓平台</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- QRCode.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>

  <style>
    .perspective {
      perspective: 1200px;
    }
    .transform-style-3d {
      transform-style: preserve-3d;
      -webkit-transform-style: preserve-3d;
    }
    .backface-hidden {
      backface-visibility: hidden !important;
      -webkit-backface-visibility: hidden !important;
    }
    .rotate-y-180 {
      transform: rotateY(180deg) !important;
      -webkit-transform: rotateY(180deg) !important;
    }

    .katex, .katex-html, .katex-display {
      white-space: nowrap !important;
    }
    .katex-display {
      margin: 0.2em 0 !important;
      display: inline-block !important;
      max-width: 100% !important;
    }
    .katex svg,
    #fullscreen-modal .katex svg {
      display: block !important;
      position: absolute !important;
      width: 100% !important;
      height: inherit !important;
      fill: currentColor !important;
      stroke: currentColor !important;
      max-height: none !important;
      margin: 0 !important;
    }

    #fullscreen-modal:fullscreen,
    #fullscreen-modal:-webkit-full-screen {
      width: 100vw !important;
      height: 100vh !important;
      max-width: 100vw !important;
      max-height: 100vh !important;
      padding: 0 !important;
      margin: 0 !important;
      border-radius: 0 !important;
    }

    #mindmap-modal-dialog:fullscreen,
    #mindmap-modal-dialog:-webkit-full-screen {
      max-width: 100vw !important;
      width: 100vw !important;
      height: 100vh !important;
      max-height: 100vh !important;
      border-radius: 0 !important;
    }

    /* =================================================== */
    /* 全站題幹與公式上下行距優化 (利於公式與分數舒適閱讀) */
    /* =================================================== */
    .card-front-content,
    #modal-front-content {
      line-height: 2.35 !important;
    }
    .card-front-content br,
    #modal-front-content br {
      display: block !important;
      content: "" !important;
      margin-top: 0.75rem !important;
    }
    .card-step-content,
    #modal-steps-container .text-slate-800 {
      line-height: 2.05 !important;
    }
    .card-step-content br,
    #modal-steps-container br {
      display: block !important;
      content: "" !important;
      margin-top: 0.5rem !important;
    }
    .katex {
      font-size: 1.08em !important;
      line-height: 1.25 !important;
    }
  </style>
</head>
<body class="bg-slate-100 text-slate-800 min-h-screen flex flex-col font-sans">

  <!-- 頂部導覽列 -->
  <header class="sticky top-0 z-40 bg-[#0a192f] text-white shadow-md border-b border-amber-500/40">
    <div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-amber-600 flex items-center justify-center text-white shadow-inner font-black text-lg">
          <i class="fa-solid fa-glasses"></i>
        </div>
        <div>
          <h1 class="text-base sm:text-lg font-black tracking-wide text-amber-300">
            名偵探柯南數理探案特訓
          </h1>
          <p class="text-[11px] text-slate-300 font-medium">
            泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
          </p>
        </div>
      </div>

      <!-- 功能按鈕群 -->
      <div class="flex items-center gap-2">
        <button onclick="openCheatsheetModal()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 transition-colors shadow-xs flex items-center gap-1.5">
          <i class="fa-solid fa-scroll text-red-700"></i>
          <span>解密口訣錦囊</span>
        </button>

        <button onclick="openLabModal()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 hover:bg-indigo-500 text-white transition-colors shadow-xs flex items-center gap-1.5">
          <i class="fa-solid fa-flask text-amber-300"></i>
          <span>阿笠博士實驗室</span>
        </button>

        <button onclick="openChallengeModal()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition-colors shadow-xs flex items-center gap-1.5">
          <i class="fa-solid fa-crosshairs text-amber-300"></i>
          <span>少年偵探團考核</span>
        </button>

        <button onclick="openMindmapModal()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-400/40 transition-colors shadow-xs flex items-center gap-1.5">
          <i class="fa-solid fa-sitemap"></i>
          <span>破案心智圖</span>
        </button>

        <button onclick="togglePageFullscreen()" id="fullscreen-toggle-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition-all shadow-xs flex items-center gap-1.5" title="首頁全螢幕投影 (快捷鍵 F)">
          <i id="fullscreen-toggle-icon" class="fa-solid fa-expand"></i>
          <span id="fullscreen-toggle-text">全螢幕投影</span>
        </button>

        <button onclick="openQrcodeModal()" class="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors text-sm" title="手機掃碼連線">
          <i class="fa-solid fa-qrcode"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- 主視覺首頁橫幅 -->
  <section class="bg-gradient-to-b from-[#0a192f] via-[#10243e] to-slate-100 text-white pt-8 pb-10 px-4">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
      
      <!-- 左側專案簡介 -->
      <div class="max-w-2xl">
        <div class="flex items-center gap-2 mb-3">
          <span class="px-3 py-1 rounded-full text-xs font-black bg-amber-500 text-slate-950 shadow-sm">
            <i class="fa-solid fa-shield-halved mr-1"></i>旗艦全功能標準版
          </span>
          <span class="text-xs text-amber-200 font-medium">全套 60 張圖解卡 ‧ 100% 忠實泰宇課本</span>
        </div>

        <h2 class="text-3xl sm:text-4xl font-black text-amber-300 mb-3 tracking-tight">
          泰宇技術高中數學 2-2 數位互動學習包
        </h2>
        <p class="text-sm sm:text-base text-slate-200 leading-relaxed mb-5 font-normal">
          將銳角三角比、特別角運算、神奇六角星四大恆等關係與生活工程坡度模型，全面轉化為名偵探柯南沉浸式探案情境。
          配備雙向逐步引導、多功能電子白板、動態幾何形變實驗室與六階段升級特訓考核。
        </p>

        <!-- 下載工具列 -->
        <div class="flex flex-wrap items-center gap-2.5">
          <button onclick="downloadStudentDocx()" class="px-4 py-2 rounded-xl text-xs font-bold bg-amber-500 hover:bg-amber-400 text-slate-950 transition-all shadow-md flex items-center gap-2">
            <i class="fa-solid fa-file-word text-blue-900"></i>
            <span>偵探搜查實作單 (B4)</span>
          </button>

          <button onclick="openTeacherPwdModal('lesson_plan')" class="px-4 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition-all shadow-md flex items-center gap-2">
            <i class="fa-solid fa-lock"></i>
            <span>四節課教學計畫與教案 (B4)</span>
          </button>

          <button onclick="openTeacherPwdModal('teacher')" class="px-4 py-2 rounded-xl text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition-all shadow-md flex items-center gap-2">
            <i class="fa-solid fa-lock"></i>
            <span>警視廳機密解答卷宗</span>
          </button>

          <a href="2-2_三角函數的定義與性質_全套60張圖解學習卡.pdf" download class="px-4 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-amber-300 border border-amber-400/50 transition-all shadow-md flex items-center gap-2">
            <i class="fa-solid fa-file-pdf text-red-400"></i>
            <span>全套圖解卡 PDF</span>
          </a>
        </div>
      </div>

      <!-- 右側情報儀表板 -->
      <div class="w-full md:w-80 bg-white/10 backdrop-blur-md border border-white/20 p-5 rounded-2xl shadow-xl text-white">
        <h3 class="text-sm font-black text-amber-300 mb-3 flex items-center justify-between">
          <span><i class="fa-solid fa-chart-line mr-1.5"></i>即時偵查情報儀表板</span>
          <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-400/30">即時連線</span>
        </h3>

        <div class="grid grid-cols-3 gap-2 mb-4 text-center">
          <div class="p-2.5 rounded-xl bg-white/10 border border-white/10">
            <div class="text-[10px] text-slate-300">總搜查人次</div>
            <div id="stat-pageviews" class="text-lg font-black text-amber-300 mt-0.5">0</div>
          </div>
          <div class="p-2.5 rounded-xl bg-white/10 border border-white/10">
            <div class="text-[10px] text-slate-300">到訪特派員</div>
            <div id="stat-visitors" class="text-lg font-black text-sky-300 mt-0.5">0</div>
          </div>
          <div class="p-2.5 rounded-xl bg-white/10 border border-white/10">
            <div class="text-[10px] text-slate-300">破案互動數</div>
            <div id="stat-interactions" class="text-lg font-black text-emerald-300 mt-0.5">0</div>
          </div>
        </div>

        <div>
          <div class="flex justify-between text-xs font-bold mb-1">
            <span class="text-slate-300">案件結案進度</span>
            <span id="case-progress-text" class="text-amber-300">0 / 60 (0%)</span>
          </div>
          <div class="w-full bg-white/20 h-2.5 rounded-full overflow-hidden">
            <div id="case-progress-bar" class="bg-gradient-to-r from-amber-400 to-emerald-400 h-full w-0 transition-all duration-500"></div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 內容主體區 -->
  <main class="max-w-7xl mx-auto px-4 py-8 flex-1 w-full">
    
    <!-- 篩選與工具列 -->
    <div class="bg-white border border-slate-200 rounded-2xl p-4 shadow-xs mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4">
      
      <!-- 分類標籤 -->
      <div class="flex flex-wrap items-center gap-1.5">
        <button onclick="filterCategory('all')" data-category="all" class="cat-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-600 text-white transition-all shadow-2xs">
          全單元案件
        </button>
        <button onclick="filterCategory('六大函數定義')" data-category="六大函數定義" class="cat-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-100 transition-all border border-slate-200">
          六大定義
        </button>
        <button onclick="filterCategory('特別角運算')" data-category="特別角運算" class="cat-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-100 transition-all border border-slate-200">
          特別角運算
        </button>
        <button onclick="filterCategory('恆等關係求值')" data-category="恆等關係求值" class="cat-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-100 transition-all border border-slate-200">
          六角星恆等式
        </button>
        <button onclick="filterCategory('恆等式求乘積')" data-category="恆等式求乘積" class="cat-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-100 transition-all border border-slate-200">
          和差連環扣
        </button>
        <button onclick="filterCategory('基礎實戰求值')" data-category="基礎實戰求值" class="cat-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-100 transition-all border border-slate-200">
          課後習題實戰
        </button>
      </div>

      <!-- 視圖切換與翻轉操作 -->
      <div class="flex items-center gap-2">
        <div class="flex items-center bg-slate-100 p-1 rounded-xl text-xs font-bold">
          <button onclick="filterCardView('all')" data-view="all" class="view-btn px-2.5 py-1 rounded-lg bg-amber-600 text-white">
            全部
          </button>
          <button onclick="filterCardView('mastered')" data-view="mastered" class="view-btn px-2.5 py-1 rounded-lg text-amber-800">
            已結案
          </button>
          <button onclick="filterCardView('review')" data-view="review" class="view-btn px-2.5 py-1 rounded-lg text-amber-800">
            待複習
          </button>
        </div>

        <button onclick="flipAll()" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-100 hover:bg-amber-200 text-amber-900 border border-amber-300 transition-colors" title="一鍵翻開全部解答">
          <i class="fa-solid fa-arrows-rotate mr-1"></i>全翻開
        </button>
        <button onclick="resetFlip()" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300 transition-colors" title="一鍵翻回正面題目">
          <i class="fa-solid fa-rotate-left mr-1"></i>全翻回
        </button>

        <span id="card-count-badge" class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-600 text-xs font-bold border border-slate-200">
          共 60 個案件
        </span>
      </div>

    </div>

    <!-- 學習卡網格 (雙欄響應式佈局) -->
    <div id="cards-grid" class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- 由 JS 動態注入 60 張卡片 -->
    </div>

  </main>

  <!-- 頁尾 (Core Rule 5 第一列三色膠囊計數器) -->
  <footer class="bg-[#0a192f] text-white pt-8 pb-10 border-t-2 border-amber-500/50 mt-12">
    <div class="max-w-7xl mx-auto px-4 flex flex-col items-center text-center">
      
      <!-- 第一列：三色圖示圓角膠囊計數器 -->
      <div class="flex flex-wrap items-center justify-center gap-3 mb-6">
        <div class="flex items-center gap-2 px-4 py-1.5 rounded-full bg-rose-950/80 border border-rose-500/50 text-rose-300 text-xs font-bold shadow-xs">
          <i class="fa-solid fa-eye text-rose-400"></i>
          <span>總搜查人次：</span>
          <span id="footer-pageviews" class="font-black text-rose-200 text-sm">0</span>
        </div>

        <div class="flex items-center gap-2 px-4 py-1.5 rounded-full bg-sky-950/80 border border-sky-500/50 text-sky-300 text-xs font-bold shadow-xs">
          <i class="fa-solid fa-user-secret text-sky-400"></i>
          <span>到訪特派員：</span>
          <span id="footer-visitors" class="font-black text-sky-200 text-sm">0</span>
        </div>

        <div class="flex items-center gap-2 px-4 py-1.5 rounded-full bg-amber-950/80 border border-amber-500/50 text-amber-300 text-xs font-bold shadow-xs">
          <i class="fa-solid fa-bolt text-amber-400"></i>
          <span>破案互動數：</span>
          <span id="footer-interactions" class="font-black text-amber-200 text-sm">0</span>
        </div>
      </div>

      <!-- 第二列：課程名稱與版權署名 -->
      <div class="text-sm font-bold text-amber-300 mb-1">
        泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
      </div>
      <div class="text-xs text-slate-400 mb-2">
        PLVS 數學科  教育學習用
      </div>
      <div class="text-[11px] text-slate-500">
        名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版 v3.0 ｜ 遵循 15 大核心製作鐵律
      </div>

    </div>
  </footer>

  <!-- ======================================================= -->
  <!-- 彈窗集合 (Modals) -->
  <!-- ======================================================= -->

  <!-- 1. 全螢幕劇院模式視窗 (含電子白板) -->
  <div id="fullscreen-modal" class="fixed inset-0 z-50 bg-[#0a192f]/95 backdrop-blur-md hidden flex flex-col justify-between p-4 sm:p-6 overflow-hidden">
    
    <!-- 頂部標頭與白板工具列 -->
    <div class="flex flex-wrap items-center justify-between pb-3 border-b border-amber-500/30 gap-2">
      <div class="flex items-center gap-2">
        <span id="modal-case-tag" class="px-3 py-1 rounded-md text-xs font-black bg-amber-600 text-white">CASE 01</span>
        <h2 id="modal-case-title" class="text-lg font-black text-amber-300">案件標題</h2>
        <span id="modal-case-page" class="text-xs text-slate-400">課本 P.107</span>
      </div>

      <!-- 電子白板工具箱 -->
      <div class="flex items-center gap-1.5 bg-slate-800/90 p-1.5 rounded-xl border border-slate-700">
        <button onclick="setWhiteboardMode('mouse')" data-mode="mouse" class="wb-tool-btn px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white" title="現場調查 (穿透操作)">
          <i class="fa-solid fa-arrow-pointer mr-1"></i>調查 (V)
        </button>
        <button onclick="setWhiteboardMode('pen')" data-mode="pen" class="wb-tool-btn px-2 py-1 rounded text-xs font-bold bg-white text-slate-700" title="偵探筆記 (繪圖)">
          <i class="fa-solid fa-pen mr-1"></i>筆記 (B)
        </button>
        <button onclick="setWhiteboardMode('highlighter')" data-mode="highlighter" class="wb-tool-btn px-2 py-1 rounded text-xs font-bold bg-white text-slate-700" title="螢光標註">
          <i class="fa-solid fa-highlighter mr-1"></i>螢光 (H)
        </button>
        <button onclick="setWhiteboardMode('eraser')" data-mode="eraser" class="wb-tool-btn px-2 py-1 rounded text-xs font-bold bg-white text-slate-700" title="消除證物 (橡皮擦)">
          <i class="fa-solid fa-eraser mr-1"></i>橡皮擦 (E)
        </button>

        <div class="h-4 w-px bg-slate-600 mx-1"></div>

        <!-- 調色盤 -->
        <button onclick="setPenColor('#dc2626')" data-color="#dc2626" class="wb-color-btn w-5 h-5 rounded-full bg-red-600 ring-2 ring-amber-500 scale-110" title="領結紅"></button>
        <button onclick="setPenColor('#1e40af')" data-color="#1e40af" class="wb-color-btn w-5 h-5 rounded-full bg-blue-700" title="西裝藍"></button>
        <button onclick="setPenColor('#facc15')" data-color="#facc15" class="wb-color-btn w-5 h-5 rounded-full bg-amber-400" title="眼鏡金"></button>
        <button onclick="setPenColor('#16a34a')" data-color="#16a34a" class="wb-color-btn w-5 h-5 rounded-full bg-emerald-600" title="翠綠"></button>

        <!-- 輔助按鈕 -->
        <button onclick="undoWhiteboard()" class="p-1 text-slate-300 hover:text-white text-xs ml-1" title="復原上一筆">
          <i class="fa-solid fa-rotate-left"></i>
        </button>
        <button onclick="clearWhiteboard()" class="p-1 text-slate-300 hover:text-red-400 text-xs" title="清屏">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </div>

      <!-- 控制按鈕 -->
      <div class="flex items-center gap-2">
        <button id="modal-back-mindmap-btn" onclick="closeFullscreenModal()" class="hidden px-3 py-1 rounded-lg text-xs font-bold bg-indigo-600 text-white hover:bg-indigo-500">
          <i class="fa-solid fa-arrow-left mr-1"></i>返回心智圖
        </button>
        <button onclick="toggleModalFullscreen()" class="p-1.5 text-slate-300 hover:text-white rounded-lg hover:bg-slate-800 text-sm" title="全螢幕切換 (F)">
          <i class="fa-solid fa-expand"></i>
        </button>
        <button onclick="closeFullscreenModal()" class="px-3 py-1 rounded-lg text-xs font-bold bg-red-600 hover:bg-red-700 text-white">
          <i class="fa-solid fa-xmark mr-1"></i>離開劇院 (ESC)
        </button>
      </div>
    </div>

    <!-- 劇院中央內容區 (左右雙欄大版面) -->
    <div class="relative flex-1 grid grid-cols-1 lg:grid-cols-2 gap-6 my-4 overflow-hidden items-stretch">
      
      <!-- 畫布圖層 (覆蓋在中央全區) -->
      <canvas id="whiteboard-canvas" class="absolute inset-0 z-30 pointer-events-none w-full h-full"></canvas>

      <!-- 左欄：題幹與審題導引 (米杏暖白底色) -->
      <div class="p-6 rounded-2xl bg-[#fbf9f4] border-2 border-amber-300/80 flex flex-col justify-between overflow-y-auto shadow-md">
        <div>
          <span class="px-3 py-1 rounded-full text-xs font-black bg-red-600 text-white mb-3 inline-block">
            案情卷宗題幹
          </span>
          <div id="modal-front-content" class="card-front-content text-xl sm:text-2xl text-slate-900 leading-[2.35] font-bold mb-6">
            <!-- 題幹 -->
          </div>
        </div>

        <div id="modal-front-tip" class="p-4 rounded-xl bg-red-50 border border-red-200 text-base text-red-900 font-bold">
          <!-- 導引 -->
        </div>
      </div>

      <!-- 右欄：逐步推理鏈與 SVG 幾何 -->
      <div class="p-6 rounded-2xl bg-white border-2 border-slate-200 flex flex-col justify-between overflow-y-auto shadow-md">
        <div>
          <div class="flex items-center justify-between pb-3 border-b border-slate-200 mb-4">
            <span class="text-sm font-black text-amber-950 flex items-center gap-1.5">
              <i class="fa-solid fa-magnifying-glass text-amber-600"></i>👓 名偵探推理筆記 ‧ 線索推理鏈
            </span>
            <div id="modal-step-controls" class="flex items-center gap-1.5">
              <!-- 步驟按鈕 -->
            </div>
          </div>

          <div id="modal-steps-container" class="space-y-2.5">
            <!-- 步驟清單 -->
          </div>
        </div>

        <div class="mt-4">
          <div id="modal-svg-container" class="min-h-[180px] h-52 bg-slate-50 rounded-xl p-2.5 border border-slate-200 flex items-center justify-center mb-3 overflow-hidden">
            <!-- SVG -->
          </div>

          <div id="modal-conclusion" class="p-3.5 rounded-xl bg-emerald-50 border-2 border-emerald-500 text-lg font-black text-emerald-950 text-center">
            <!-- 結論 -->
          </div>
        </div>
      </div>

    </div>

    <!-- 底部導航狀態列 -->
    <div class="flex items-center justify-between pt-2 border-t border-amber-500/30 text-xs text-slate-400">
      <div class="flex items-center gap-2">
        <button onclick="prevModalCard()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold">
          <i class="fa-solid fa-chevron-left mr-1"></i>上一案 (←)
        </button>
        <button onclick="nextModalCard()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold">
          下一案 (→)<i class="fa-solid fa-chevron-right ml-1"></i>
        </button>
      </div>

      <div id="modal-nav-info" class="font-bold text-amber-300 text-sm">
        1 / 60
      </div>

      <div class="text-[11px] text-slate-400">
        支援快捷鍵：[←][→] 切換卡片 ｜ [F] 全螢幕 ｜ [ESC] 退出
      </div>
    </div>

  </div>

  <!-- 2. 解密口訣錦囊彈窗 -->
  <div id="cheatsheet-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-xs hidden flex items-center justify-center p-4">
    <div class="bg-[#fbf9f4] border-2 border-amber-500 rounded-3xl max-w-3xl w-full p-6 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-3 border-b border-amber-300 mb-4">
        <h3 class="text-xl font-black text-amber-950 flex items-center gap-2">
          <i class="fa-solid fa-scroll text-red-600"></i>【名偵探破案密碼 ‧ 解密口訣錦囊】
        </h3>
        <button onclick="closeCheatsheetModal()" class="p-1.5 text-slate-500 hover:text-slate-800 text-lg">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="space-y-4 text-sm leading-relaxed text-slate-800">
        <div class="p-4 rounded-2xl bg-amber-100/70 border border-amber-300">
          <h4 class="font-black text-amber-950 text-base mb-1">【正三角對折神算】30°-60°-90° 比例</h4>
          <p>邊長為 2 的正三角形沿高對折，三邊長比為 <b>$1 : \\sqrt{3} : 2$</b>。對角對短邊（$30^\\circ$ 對 $1$），直角對斜邊（$90^\\circ$ 對 $2$），餘角對中邊（$60^\\circ$ 對 $\\sqrt{3}$）。</p>
        </div>

        <div class="p-4 rounded-2xl bg-sky-50 border border-sky-300">
          <h4 class="font-black text-sky-950 text-base mb-1">【等腰直角神盾】45°-45°-90° 比例</h4>
          <p>兩股長為 1 時，斜邊為 $\\sqrt{2}$，三邊長比為 <b>$1 : 1 : \\sqrt{2}$</b>。正弦餘弦相等：$\\sin 45^\\circ = \\cos 45^\\circ = \\frac{\\sqrt{2}}{2}$，正切剛好為 $1$！</p>
        </div>

        <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-300">
          <h4 class="font-black text-emerald-950 text-base mb-1">【神奇六角星陣四大破案秘技】</h4>
          <ul class="list-disc list-inside space-y-1">
            <li><b>對角互倒</b>：$\\sin\\csc=1, \\cos\\sec=1, \\tan\\cot=1$（穿過中央 1 乘積必為 1）。</li>
            <li><b>倒三角平方和</b>：上面兩個平方和等於下面頂點（$\\sin^2+\\cos^2=1, 1+\\tan^2=\\sec^2, 1+\\cot^2=\\csc^2$）。</li>
            <li><b>橫向餘角換裝</b>：同高度左右兩端角度和為 $90^\\circ$ 函數直接互換。</li>
            <li><b>相鄰商數相除</b>：每個頂點等於相鄰兩頂點之商（$\\tan = \\sin / \\cos, \\cot = \\cos / \\sin$）。</li>
          </ul>
        </div>

        <div class="p-4 rounded-2xl bg-rose-50 border border-rose-300">
          <h4 class="font-black text-rose-950 text-base mb-1">【和差連環扣 ＆ 齊次同除神法】</h4>
          <p>• <b>和差連環扣</b>：$(\\sin\\theta \\pm \\cos\\theta)^2 = 1 \\pm 2\\sin\\theta\\cos\\theta$ ； 見和差必平方、見平方求乘積！<br>
          • <b>切和倒數</b>：$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$；<br>
          • <b>齊次同除神法</b>：一次正餘弦分式同除 $\\cos\\theta$ 秒變 $\\tan\\theta$，免求斜邊秒殺破案！</p>
        </div>
      </div>

      <div class="mt-6 text-center">
        <button onclick="closeCheatsheetModal()" class="px-6 py-2.5 rounded-xl font-bold text-sm bg-amber-600 text-white hover:bg-amber-700">
          關閉錦囊 (ESC)
        </button>
      </div>
    </div>
  </div>

  <!-- 3. 阿笠博士名偵探互動探案實驗室 (3 大旗艦互動學習模組) -->
  <div id="lab-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-xs hidden flex items-center justify-center p-3 sm:p-4">
    <div class="bg-white border-2 border-indigo-500 rounded-3xl max-w-4xl w-full p-5 sm:p-6 shadow-2xl max-h-[92vh] overflow-y-auto flex flex-col">
      <!-- 實驗室頂部標題與關閉按鈕 -->
      <div class="flex items-center justify-between pb-3 border-b border-indigo-200 mb-4 shrink-0">
        <h3 class="text-lg sm:text-xl font-black text-indigo-950 flex items-center gap-2">
          <i class="fa-solid fa-flask text-amber-500"></i>【阿笠博士動態探案實驗室】高中三角函數互動特訓中心
        </h3>
        <button onclick="closeLabModal()" class="p-1.5 text-slate-500 hover:text-slate-800 text-lg rounded-lg hover:bg-slate-100 transition-colors">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- 頂部 3 大功能切換頁籤 -->
      <div class="flex items-center gap-2 mb-4 p-1 bg-slate-100 rounded-xl shrink-0">
        <button onclick="switchLabTab('triangle')" id="lab-tab-btn-triangle" class="flex-1 py-2 px-3 rounded-lg text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-1.5 bg-indigo-600 text-white shadow-xs">
          <i class="fa-solid fa-draw-polygon"></i>
          <span>📐 直角光學測距儀</span>
        </button>
        <button onclick="switchLabTab('hexagon')" id="lab-tab-btn-hexagon" class="flex-1 py-2 px-3 rounded-lg text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-1.5 text-slate-600 hover:text-indigo-600">
          <i class="fa-solid fa-shapes"></i>
          <span>🧩 魔法六角密碼盤</span>
        </button>
        <button onclick="switchLabTab('speeddrill')" id="lab-tab-btn-speeddrill" class="flex-1 py-2 px-3 rounded-lg text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-1.5 text-slate-600 hover:text-indigo-600">
          <i class="fa-solid fa-stopwatch-20"></i>
          <span>⏱️ 60秒特別角速算挑戰</span>
        </button>
      </div>

      <!-- TAB 1: 動態直角三角形光學測距儀 -->
      <div id="lab-tab-pane-triangle" class="space-y-4">
        <!-- 角度快速切換器與滑桿 -->
        <div class="p-4 bg-indigo-50/70 border border-indigo-200 rounded-2xl flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div class="flex items-center gap-2 flex-wrap">
            <span class="text-xs font-bold text-slate-700">特別角一鍵聚焦：</span>
            <button onclick="setLabAngle(15)" class="px-2.5 py-1 bg-white hover:bg-indigo-600 hover:text-white rounded-lg text-xs font-bold border border-indigo-200 transition-colors">15°</button>
            <button onclick="setLabAngle(30)" class="px-2.5 py-1 bg-white hover:bg-indigo-600 hover:text-white rounded-lg text-xs font-bold border border-indigo-200 transition-colors">30°</button>
            <button onclick="setLabAngle(45)" class="px-2.5 py-1 bg-white hover:bg-indigo-600 hover:text-white rounded-lg text-xs font-bold border border-indigo-200 transition-colors">45°</button>
            <button onclick="setLabAngle(60)" class="px-2.5 py-1 bg-white hover:bg-indigo-600 hover:text-white rounded-lg text-xs font-bold border border-indigo-200 transition-colors">60°</button>
            <button onclick="setLabAngle(75)" class="px-2.5 py-1 bg-white hover:bg-indigo-600 hover:text-white rounded-lg text-xs font-bold border border-indigo-200 transition-colors">75°</button>
          </div>
          <div class="flex items-center gap-3 min-w-[200px]">
            <span class="text-xs font-bold text-slate-700 whitespace-nowrap">連續微調 θ：</span>
            <input id="lab-angle-slider" type="range" min="1" max="89" step="0.5" value="30" class="w-full accent-indigo-600 cursor-pointer">
            <span id="lab-deg-display" class="text-indigo-600 text-lg font-black min-w-[55px] text-right">30.0°</span>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
          <!-- 左側動態 SVG 直角三角形 -->
          <div id="lab-svg-stage" class="h-64 sm:h-72 bg-slate-50 rounded-2xl border-2 border-indigo-200/80 p-2 flex items-center justify-center overflow-hidden shadow-inner">
            <!-- JS 動態繪製直角三角形 -->
          </div>

          <!-- 右側六大三角函數實時數值面板 -->
          <div class="space-y-3">
            <div class="grid grid-cols-3 gap-2 text-center">
              <div class="p-2.5 bg-red-50 rounded-xl border border-red-200">
                <div class="text-[11px] font-bold text-red-700">正弦 sin θ (對/斜)</div>
                <div id="lab-sin-val" class="text-base font-black text-red-900 mt-0.5">0.5000</div>
              </div>
              <div class="p-2.5 bg-blue-50 rounded-xl border border-blue-200">
                <div class="text-[11px] font-bold text-blue-700">餘弦 cos θ (鄰/斜)</div>
                <div id="lab-cos-val" class="text-base font-black text-blue-900 mt-0.5">0.8660</div>
              </div>
              <div class="p-2.5 bg-amber-50 rounded-xl border border-amber-200">
                <div class="text-[11px] font-bold text-amber-700">正切 tan θ (對/鄰)</div>
                <div id="lab-tan-val" class="text-base font-black text-amber-900 mt-0.5">0.5774</div>
              </div>
            </div>

            <div class="grid grid-cols-3 gap-2 text-center">
              <div class="p-2.5 bg-purple-50 rounded-xl border border-purple-200">
                <div class="text-[11px] font-bold text-purple-700">餘割 csc θ (斜/對)</div>
                <div id="lab-csc-val" class="text-base font-black text-purple-900 mt-0.5">2.0000</div>
              </div>
              <div class="p-2.5 bg-teal-50 rounded-xl border border-teal-200">
                <div class="text-[11px] font-bold text-teal-700">正割 sec θ (斜/鄰)</div>
                <div id="lab-sec-val" class="text-base font-black text-teal-900 mt-0.5">1.1547</div>
              </div>
              <div class="p-2.5 bg-orange-50 rounded-xl border border-orange-200">
                <div class="text-[11px] font-bold text-orange-700">餘切 cot θ (鄰/對)</div>
                <div id="lab-cot-val" class="text-base font-black text-orange-900 mt-0.5">1.7321</div>
              </div>
            </div>

            <!-- 兩大核心恆等式即時驗證 -->
            <div class="p-3 bg-emerald-50 rounded-xl border-2 border-emerald-400 grid grid-cols-2 gap-2 text-center">
              <div>
                <div class="text-[11px] font-bold text-emerald-800">平方關係 sin²θ + cos²θ</div>
                <div id="lab-pythagoras-val" class="text-base font-black text-emerald-950 mt-0.5">1.000000</div>
              </div>
              <div>
                <div class="text-[11px] font-bold text-emerald-800">商數關係 sinθ / cosθ</div>
                <div id="lab-quotient-val" class="text-base font-black text-emerald-950 mt-0.5">0.5774 (＝ tan θ)</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 2: 神級魔法六角密碼盤 (Magic Super Hexagon) -->
      <div id="lab-tab-pane-hexagon" class="hidden space-y-4">
        <!-- 模式切換按鈕列 -->
        <div class="flex items-center justify-center gap-2 flex-wrap">
          <button onclick="setHexagonMode('reciprocal')" id="hex-mode-reciprocal-btn" class="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-amber-500 text-slate-950 shadow-xs border border-amber-600 transition-all">
            <i class="fa-solid fa-arrows-rotate mr-1"></i>對角互倒關係 (乘積 = 1)
          </button>
          <button onclick="setHexagonMode('quotient')" id="hex-mode-quotient-btn" class="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-slate-200 text-slate-700 hover:bg-slate-300 transition-all">
            <i class="fa-solid fa-divide mr-1"></i>相鄰商數關係 (頂點 = 商)
          </button>
          <button onclick="setHexagonMode('pythagorean')" id="hex-mode-pythagorean-btn" class="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-slate-200 text-slate-700 hover:bg-slate-300 transition-all">
            <i class="fa-solid fa-square-root-variable mr-1"></i>倒三角平方關係 (平方和)
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
          <!-- 互動 SVG 魔法六角星圖 -->
          <div id="hexagon-svg-container" class="h-68 bg-slate-900 rounded-2xl border-2 border-amber-500/50 p-2 flex items-center justify-center shadow-lg relative">
            <!-- JS 動態生成互動 SVG 六角形 -->
          </div>

          <!-- 右側解密破案筆記動態面板 -->
          <div class="p-5 rounded-2xl bg-[#fbf9f4] border-2 border-amber-300 flex flex-col justify-between h-full shadow-sm">
            <div>
              <span id="hex-badge-title" class="px-3 py-1 rounded-full text-xs font-black bg-amber-600 text-white inline-block mb-3">
                【對角互倒關係】穿透中心的倒數伴侶
              </span>
              <div id="hex-formula-display" class="text-base sm:text-lg font-black text-amber-950 mb-3 leading-relaxed overflow-x-auto max-w-full text-center py-1">
                sin θ · csc θ = 1
              </div>
              <p id="hex-explanation-text" class="text-xs sm:text-sm text-slate-700 leading-relaxed font-medium">
                點擊六角形對角頂點：穿過中央的「1」，對角線兩端的三角函數相乘恆等於 1！<br>
                例如正弦 sin 與餘割 csc 互為倒數，餘弦 cos 與正割 sec 互為倒數，正切 tan 與餘切 cot 互為倒數。
              </p>
            </div>

            <div class="mt-4 p-3 bg-amber-100/80 rounded-xl border border-amber-300 text-xs font-bold text-amber-900 flex items-center gap-2">
              <i class="fa-solid fa-lightbulb text-amber-600 text-base"></i>
              <span>偵探秘訣：點擊六角形任一頂點可立即切換聚焦點！</span>
            </div>
          </div>
        </div>
      </div>

      <!-- TAB 3: 60秒特別角速算破案挑戰 -->
      <div id="lab-tab-pane-speeddrill" class="hidden space-y-4">
        <!-- 挑戰進行前：規則介紹與開始按鈕 -->
        <div id="speeddrill-start-view" class="p-8 rounded-2xl bg-gradient-to-br from-indigo-900 to-slate-900 text-white text-center space-y-5">
          <div class="w-16 h-16 mx-auto rounded-2xl bg-amber-500/20 border-2 border-amber-400 flex items-center justify-center text-amber-400 text-2xl font-black shadow-lg">
            <i class="fa-solid fa-bolt"></i>
          </div>
          <div>
            <h4 class="text-xl sm:text-2xl font-black text-amber-300">60秒特別角極速破案特訓</h4>
            <p class="text-xs sm:text-sm text-slate-300 mt-1.5 max-w-md mx-auto">
              隨機抽取 30°、45°、60° 之六大三角函數特別角數值！考驗名偵探的直覺反射與肌肉記憶！
            </p>
          </div>
          <div class="flex justify-center gap-6 text-xs text-amber-200">
            <div>⏱️ 限時：60 秒</div>
            <div>🔥 連擊 Combo 加倍</div>
            <div>🏆 依戰績獲頒偵探勳章</div>
          </div>
          <button onclick="startSpeedDrill()" class="px-8 py-3 rounded-2xl text-base font-black bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-lg hover:scale-105 active:scale-95 transition-all">
            <i class="fa-solid fa-play mr-2"></i>啟動極速特訓
          </button>
        </div>

        <!-- 挑戰進行中畫面 -->
        <div id="speeddrill-game-view" class="hidden space-y-4">
          <!-- 頂部資訊列：計時器、Combo、積分 -->
          <div class="flex items-center justify-between p-3 bg-slate-900 text-white rounded-2xl">
            <div class="flex items-center gap-2 font-black text-amber-400 text-lg">
              <i class="fa-solid fa-stopwatch"></i>
              <span id="drill-timer-text">60s</span>
            </div>
            <div class="flex items-center gap-3">
              <span id="drill-combo-badge" class="px-2.5 py-1 rounded-lg text-xs font-black bg-amber-500 text-slate-950">Combo x0</span>
              <span id="drill-score-badge" class="px-2.5 py-1 rounded-lg text-xs font-black bg-indigo-600 text-white">Score: 0</span>
            </div>
          </div>

          <!-- 核心題目大字板 -->
          <div class="p-6 rounded-2xl bg-indigo-50 border-2 border-indigo-300 text-center relative overflow-hidden">
            <div id="drill-question-card" class="text-3xl sm:text-4xl font-black text-indigo-950 tracking-wide">
              sin 30° = ?
            </div>
            <div id="drill-feedback-overlay" class="absolute inset-0 flex items-center justify-center font-black text-3xl pointer-events-none opacity-0 transition-opacity">
              <!-- 正確/錯誤動畫 -->
            </div>
          </div>

          <!-- 8 大候選答案快速點選按鈕網格 (標準直式分式與高對比排版) -->
          <div id="drill-options-grid" class="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <button onclick="handleDrillAnswer('1/2')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $\frac{1}{2}$
            </button>
            <button onclick="handleDrillAnswer('√2/2')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $\frac{\sqrt{2}}{2}$
            </button>
            <button onclick="handleDrillAnswer('√3/2')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $\frac{\sqrt{3}}{2}$
            </button>
            <button onclick="handleDrillAnswer('1')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $1$
            </button>
            <button onclick="handleDrillAnswer('√3/3')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $\frac{\sqrt{3}}{3}$
            </button>
            <button onclick="handleDrillAnswer('√3')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $\sqrt{3}$
            </button>
            <button onclick="handleDrillAnswer('√2')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $\sqrt{2}$
            </button>
            <button onclick="handleDrillAnswer('2')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
              $2$
            </button>
          </div>
        </div>

        <!-- 挑戰結算報告畫面 -->
        <div id="speeddrill-result-view" class="hidden p-6 rounded-2xl bg-white border-2 border-amber-400 text-center space-y-4">
          <div class="text-4xl">🏆</div>
          <h4 class="text-2xl font-black text-amber-950">特訓圓滿達成！</h4>
          <div id="drill-rank-badge" class="px-4 py-1.5 rounded-full text-sm font-black bg-amber-500 text-slate-950 inline-block shadow-xs">
            名偵探級別：高中生名偵探
          </div>
          <div class="grid grid-cols-3 gap-3 max-w-sm mx-auto text-center">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <div class="text-xs text-slate-500">答對題數</div>
              <div id="drill-result-correct" class="text-xl font-black text-indigo-950 mt-1">0</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <div class="text-xs text-slate-500">最高連擊</div>
              <div id="drill-result-combo" class="text-xl font-black text-amber-600 mt-1">0</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <div class="text-xs text-slate-500">總破案分</div>
              <div id="drill-result-score" class="text-xl font-black text-emerald-600 mt-1">0</div>
            </div>
          </div>
          <div class="pt-2">
            <button onclick="startSpeedDrill()" class="px-6 py-2.5 rounded-xl font-black bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition-all">
              <i class="fa-solid fa-rotate-right mr-1"></i>再挑戰一次
            </button>
          </div>
        </div>
      </div>

      <!-- 底部關閉按鈕 -->
      <div class="mt-5 pt-3 border-t border-slate-200 flex justify-end shrink-0">
        <button onclick="closeLabModal()" class="px-5 py-2 rounded-xl font-bold text-xs sm:text-sm bg-slate-800 text-white hover:bg-slate-700 transition-colors">
          關閉實驗室 (ESC)
        </button>
      </div>
    </div>
  </div>

  <!-- 4. 少年偵探團升級特訓考核彈窗 -->
  <div id="challenge-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-xs hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-rose-500 rounded-3xl max-w-2xl w-full p-6 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between pb-3 border-b border-rose-200 mb-4">
        <h3 class="text-xl font-black text-rose-950 flex items-center gap-2">
          <i class="fa-solid fa-crosshairs text-rose-600"></i>【少年偵探團 ‧ 數理升級特訓考核】
        </h3>
        <button onclick="closeChallengeModal()" class="p-1.5 text-slate-500 hover:text-slate-800 text-lg">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- 關卡清單視圖 -->
      <div id="challenge-stages-view">
        <!-- JS 動態填入 STAGE 01~06 -->
      </div>

      <!-- 答題進行視圖 -->
      <div id="challenge-quiz-view" class="hidden">
        <div class="flex items-center justify-between pb-2 border-b border-slate-200 mb-3">
          <div>
            <span id="quiz-stage-title" class="text-xs font-bold text-slate-500 block">STAGE 01</span>
            <span id="quiz-progress-text" class="text-sm font-black text-rose-900">問題 1 / 6</span>
          </div>
          <div class="flex items-center gap-3">
            <span id="quiz-combo-badge" class="px-2 py-0.5 rounded text-xs font-bold bg-amber-100 text-amber-800">連擊：0</span>
            <span id="quiz-score-badge" class="px-2 py-0.5 rounded text-xs font-bold bg-indigo-100 text-indigo-800">積分：0</span>
            <div id="quiz-lives-container" class="flex items-center">
              <!-- 3 個生命值 -->
            </div>
          </div>
        </div>

        <div id="quiz-question-text" class="text-base font-bold text-slate-900 my-4 leading-relaxed bg-amber-50/50 p-4 rounded-xl border border-amber-200">
          <!-- 題目文字 -->
        </div>

        <div id="quiz-options-container" class="space-y-2 mb-4">
          <!-- 選項按鈕 -->
        </div>

        <div id="quiz-feedback-box" class="hidden">
          <!-- 答題回饋 -->
        </div>
      </div>

      <!-- 結算成績視圖 -->
      <div id="challenge-result-view" class="hidden">
        <!-- 結算內容 -->
      </div>

    </div>
  </div>

  <!-- 5. 破案心智圖全螢幕彈窗 -->
  <div id="mindmap-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden flex items-center justify-center p-4 sm:p-6">
    <div id="mindmap-modal-dialog" class="bg-white border-2 border-amber-500 rounded-3xl max-w-5xl w-full h-[85vh] p-6 shadow-2xl flex flex-col justify-between overflow-hidden">
      
      <div class="flex items-center justify-between pb-3 border-b border-amber-300 mb-4">
        <div class="flex items-center gap-2">
          <span class="w-8 h-8 rounded-lg bg-amber-600 text-white flex items-center justify-center font-bold text-sm">
            <i class="fa-solid fa-sitemap"></i>
          </span>
          <h3 class="text-xl font-black text-amber-950">
            泰宇高中數學 2-2 破案知識網絡心智圖
          </h3>
        </div>

        <div class="flex items-center gap-2">
          <button onclick="toggleMindmapFullscreen()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">
            <i class="fa-solid fa-expand mr-1"></i>全螢幕 (F)
          </button>
          <button onclick="closeMindmapModal()" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 text-white hover:bg-amber-700">
            返回案件總覽 (ESC)
          </button>
        </div>
      </div>

      <div id="mindmap-tree-container" class="flex-1 overflow-y-auto pr-2">
        <!-- 心智圖節點結構 -->
      </div>

      <div class="pt-3 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500 font-medium">
        <div>點擊任意案件標題，可直接跳轉劇院投影模式</div>
        <div>按 ESC 隨時返回總覽</div>
      </div>
    </div>
  </div>

  <!-- 6. 教師解答密碼驗證彈窗 -->
  <div id="teacher-pwd-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-xs hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-rose-500 rounded-3xl max-w-sm w-full p-6 shadow-2xl text-center">
      <div class="w-12 h-12 rounded-full bg-rose-100 text-rose-600 flex items-center justify-center mx-auto mb-3 text-xl">
        <i class="fa-solid fa-lock"></i>
      </div>
      <h3 id="teacher-pwd-modal-title" class="text-lg font-black text-slate-900 mb-1">警視廳機密解答卷宗驗證</h3>
      <p id="teacher-pwd-modal-desc" class="text-xs text-slate-500 mb-4">本卷宗包含教師專用紅字 OMML 步驟解答，請輸入專業授權密碼：</p>

      <input id="teacher-pwd-input" type="password" onkeydown="if(event.key==='Enter')verifyTeacherPassword()" placeholder="請輸入授權密碼" class="w-full text-center px-4 py-2.5 rounded-xl border-2 border-slate-300 focus:border-rose-500 focus:outline-hidden text-base tracking-widest font-bold mb-2">
      <div id="teacher-pwd-error" class="text-xs font-bold text-red-600 mb-3 hidden">密碼錯誤，請重新輸入！</div>

      <div class="flex gap-2">
        <button onclick="closeTeacherPwdModal()" class="flex-1 py-2.5 rounded-xl font-bold text-xs bg-slate-200 text-slate-700 hover:bg-slate-300">
          取消
        </button>
        <button onclick="verifyTeacherPassword()" class="flex-1 py-2.5 rounded-xl font-bold text-xs bg-rose-600 text-white hover:bg-rose-700">
          解鎖下載
        </button>
      </div>
    </div>
  </div>

  <!-- 7. 正面單卡自檢抽屜彈窗 -->
  <div id="card-quiz-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-xs hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-amber-500 rounded-3xl max-w-md w-full p-6 shadow-2xl">
      <div class="flex items-center justify-between pb-2 border-b border-slate-200 mb-3">
        <h4 id="card-quiz-title" class="text-base font-black text-amber-950">自我檢核</h4>
        <button onclick="closeCardQuizModal()" class="p-1 text-slate-500 hover:text-slate-800">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div id="card-quiz-question" class="text-sm font-bold text-slate-900 mb-3 leading-relaxed"></div>
      <div id="card-quiz-options" class="space-y-1.5 mb-3"></div>
      <div id="card-quiz-feedback" class="hidden"></div>
      <div class="text-center mt-4">
        <button onclick="closeCardQuizModal()" class="px-5 py-2 rounded-xl text-xs font-bold bg-slate-200 text-slate-700 hover:bg-slate-300">
          完成
        </button>
      </div>
    </div>
  </div>

  <!-- 8. 手機掃碼投影彈窗 -->
  <div id="qrcode-modal" class="fixed inset-0 z-50 bg-black/70 backdrop-blur-xs hidden flex items-center justify-center p-4">
    <div class="bg-white border-2 border-blue-600 rounded-3xl max-w-sm w-full p-6 shadow-2xl text-center">
      <div class="flex items-center justify-between pb-2 border-b border-slate-200 mb-4">
        <h3 class="text-base font-black text-blue-950">手機掃碼連線伺服器</h3>
        <button onclick="closeQrcodeModal()" class="p-1 text-slate-500 hover:text-slate-800">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div id="qrcode-display" class="w-56 h-56 mx-auto bg-slate-50 p-2 rounded-xl border border-slate-200 flex items-center justify-center mb-4"></div>
      <input id="qrcode-url-input" type="text" readonly class="w-full text-xs text-slate-600 bg-slate-100 p-2 rounded-lg border border-slate-200 text-center mb-3">
      <button onclick="copyQrcodeUrl()" class="w-full py-2.5 rounded-xl font-bold text-xs bg-blue-600 text-white hover:bg-blue-700 shadow-sm">
        <i class="fa-solid fa-copy mr-1"></i>複製連線網址
      </button>
    </div>
  </div>

  <!-- 數據與邏輯注入 -->
  <script>
    window.CARDS_DATA = __CARDS_JSON__;
    window.QUIZ_DATA = __QUIZ_JSON__;
    window.CHALLENGE_STAGES = __STAGES_JSON__;
    window.STUDENT_DOCX_B64 = "__STUDENT_DOCX_B64__";
    window.TEACHER_DOCX_B64 = "__TEACHER_DOCX_B64__";
    window.LESSON_PLAN_DOCX_B64 = "__LESSON_PLAN_DOCX_B64__";
  </script>

  <!-- 前端主邏輯 JS -->
  <script>
    __INTERACTIVE_JS_CODE__
  </script>
</body>
</html>
"""

def generate_index_html():
    cards = cards_part1.CARDS_PART1 + cards_part2.CARDS_PART2
    cards_json = json.dumps(cards, ensure_ascii=False)
    quiz_json = json.dumps(interactive_cards_data.QUIZ_DATA, ensure_ascii=False)
    stages_json = json.dumps(interactive_cards_data.CHALLENGE_STAGES, ensure_ascii=False)

    html = HTML_TEMPLATE.replace('__CARDS_JSON__', cards_json)
    html = html.replace('__QUIZ_JSON__', quiz_json)
    html = html.replace('__STAGES_JSON__', stages_json)
    html = html.replace('__STUDENT_DOCX_B64__', docx_b64.STUDENT_DOCX_B64)
    html = html.replace('__TEACHER_DOCX_B64__', docx_b64.TEACHER_DOCX_B64)
    html = html.replace('__LESSON_PLAN_DOCX_B64__', getattr(docx_b64, 'LESSON_PLAN_DOCX_B64', ''))
    html = html.replace('__INTERACTIVE_JS_CODE__', interactive_js_module.INTERACTIVE_JS_CODE)
    return html

def main():
    print("正在編譯泰宇 2-2 數位互動全功能平台 index.html...")
    html_content = generate_index_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("成功產出 index.html！檔案大小：", len(html_content), "字元")

if __name__ == "__main__":
    main()
