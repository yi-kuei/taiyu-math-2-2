# -*- coding: utf-8 -*-
"""
cards_part1.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
圖解學習卡資料集 Part 1 (CASE 01 ~ CASE 30)
遵循 SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版：
- 堅持「一題一卡、一小題獨立成卡」
- 課本例題與隨堂 100% 忠實原文
- 全欄位 100% KaTeX 標準數學式（全域 145% 渲染）
- 正面無水平捲軸，適度 <br> 換行
- 2~4 步結構化思維導引（名偵探推理筆記 ‧ 線索推理鏈）
- 高解析標準 SVG 向量幾何圖解
"""

CARDS_PART1 = [
    # ==========================================
    # 階段一：銳角三角函數定義篇 (CASE 01 ~ 11)
    # ==========================================
    {
        "id": 1,
        "tag": "CASE 01",
        "page": "課本 P.107 前言",
        "category": "三角比概念",
        "title": "正三角形對折與三角比的由來",
        "front_content": "將邊長為 $2$ 的正三角形對折，利用畢氏定理，<br>可以得到正三角形的高為 $\\sqrt{3}$。<br>由國中所學相似三角形對應邊成比例可知：<br>在直角 $\\triangle$ 中，只要一銳角固定，<br>其「邊長之比值」即為定值，此即<b>三角比</b>的起點。",
        "front_tip": "🕵️ 柯南破案導引：直角三角形放大或縮小，角度不變，邊長比例就不變！這就是三角函數的根本特徵！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：幾何對折與高長推導",
                "content": "邊長為 $2$ 的正三角形沿高對折，底邊平分為 $1$。由畢氏定理得高為 $\\sqrt{2^2 - 1^2} = \\sqrt{3}$，形成 $30^\\circ-60^\\circ-90^\\circ$ 直角三角形。"
            },
            {
                "num": 2,
                "title": "線索 2：三角形相似與邊長比值",
                "content": "若兩直角三角形滿足 $\\angle A = \\angle P$，則 $\\triangle ABC \\sim \\triangle PQR$。對應邊成比例：$\\frac{BC}{AB} = \\frac{QR}{PQ} = \\frac{1}{2}$、$\\frac{AC}{AB} = \\frac{PR}{PQ} = \\frac{\\sqrt{3}}{2}$。"
            },
            {
                "num": 3,
                "title": "線索 3：從比例常數到三角函數",
                "content": "比值只隨角度改變，不隨三角形大小改變！將「角度」對應到「邊長比值」的對應法則，就是銳角三角函數。"
            }
        ],
        "conclusion": "【CASE CLOSED 真香永遠只有一個！】銳角固定時，直角三角形邊長比值為定值，稱為該銳角的三角比！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <defs>
    <marker id="arr1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#dc2626"/></marker>
  </defs>
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#78350f">正三角形對折與邊長比例定值</text>
  <polygon points="90,170 190,40 190,170" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <polygon points="190,170 190,40 290,170" fill="#fed7aa" stroke="#c2410c" stroke-width="2" stroke-dasharray="4"/>
  <rect x="175" y="155" width="15" height="15" fill="none" stroke="#b45309" stroke-width="1.5"/>
  <text x="130" y="95" font-size="13" font-weight="bold" fill="#dc2626">斜邊 = 2</text>
  <text x="140" y="184" font-size="13" font-weight="bold" fill="#1e40af">底 = 1</text>
  <text x="198" y="110" font-size="13" font-weight="bold" fill="#15803d">高 = √3</text>
  <text x="110" y="162" font-size="12" fill="#78350f">60°</text>
  <text x="172" y="65" font-size="12" fill="#78350f">30°</text>
</svg>"""
    },
    {
        "id": 2,
        "tag": "CASE 02",
        "page": "課本 P.108 定義",
        "category": "六大函數定義",
        "title": "銳角三角函數的六大嚴格定義",
        "front_content": "在直角 $\\triangle$ 中，角 $\\theta$ 的斜邊為 $r$、對邊為 $y$、鄰邊為 $x$：<br>$\\sin\\theta = \\frac{y}{r} = \\frac{\\text{對邊}}{\\text{斜邊}}$（正弦） ； $\\csc\\theta = \\frac{r}{y} = \\frac{\\text{斜邊}}{\\text{對邊}}$（餘割）<br>$\\cos\\theta = \\frac{x}{r} = \\frac{\\text{鄰邊}}{\\text{斜邊}}$（餘弦） ； $\\sec\\theta = \\frac{r}{x} = \\frac{\\text{斜邊}}{\\text{鄰邊}}$（正割）<br>$\\tan\\theta = \\frac{y}{x} = \\frac{\\text{對邊}}{\\text{鄰邊}}$（正切） ； $\\cot\\theta = \\frac{x}{y} = \\frac{\\text{鄰邊}}{\\text{對邊}}$（餘切）",
        "front_tip": "🕵️ 柯南破案導引：牢記三原形（sin、cos、tan），再取倒數就是另外三個（csc、sec、cot）！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：直角三角形三邊角色定位",
                "content": "面對目標角 $\\theta$：斜對著直角的最長邊稱為「斜邊 $r$」；目標角對面的邊稱為「對邊 $y$」；與目標角相鄰且構成直角的邊稱為「鄰邊 $x$」。"
            },
            {
                "num": 2,
                "title": "線索 2：三大主幹函數對照",
                "content": "正弦 $\\sin\\theta = \\frac{\\text{對}}{\\text{斜}}$；餘弦 $\\cos\\theta = \\frac{\\text{鄰}}{\\text{斜}}$；正切 $\\tan\\theta = \\frac{\\text{對}}{\\text{鄰}}$。"
            },
            {
                "num": 3,
                "title": "線索 3：三大伴隨倒數函數",
                "content": "餘割 $\\csc\\theta = \\frac{1}{\\sin\\theta} = \\frac{\\text{斜}}{\\text{對}}$；正割 $\\sec\\theta = \\frac{1}{\\cos\\theta} = \\frac{\\text{斜}}{\\text{鄰}}$；餘切 $\\cot\\theta = \\frac{1}{\\tan\\theta} = \\frac{\\text{鄰}}{\\text{對}}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】三正三餘共六位，分母分子對應準確即破案！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 300,165 300,45" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <rect x="282" y="147" width="18" height="18" fill="none" stroke="#1d4ed8" stroke-width="1.5"/>
  <text x="85" y="158" font-size="14" font-weight="bold" fill="#b45309">θ</text>
  <text x="170" y="185" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 x</text>
  <text x="312" y="110" font-size="13" font-weight="bold" fill="#dc2626">對邊 y</text>
  <text x="160" y="95" font-size="13" font-weight="bold" fill="#15803d">斜邊 r</text>
</svg>"""
    },
    {
        "id": 3,
        "tag": "CASE 03",
        "page": "課本 P.108 概念",
        "category": "倒數關係記憶",
        "title": "倒數關係與英文字母字首記憶法",
        "front_content": "銳角三角函數中，存在三對天生倒數伴侶：<br>1. $\\sin\\theta \\cdot \\csc\\theta = 1 \\iff \\csc\\theta = \\frac{1}{\\sin\\theta}$<br>2. $\\cos\\theta \\cdot \\sec\\theta = 1 \\iff \\sec\\theta = \\frac{1}{\\cos\\theta}$<br>3. $\\tan\\theta \\cdot \\cot\\theta = 1 \\iff \\cot\\theta = \\frac{1}{\\tan\\theta}$<br>記憶訣竅：以「S 配 C，T 配 T」辨認對應組合！",
        "front_tip": "🕵️ 柯南破案導引：正弦 (sin, s開頭) 倒數是 cosecant (csc, c開頭)；餘弦 (cos, c開頭) 倒數是 secant (sec, s開頭)；首字必互換！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：倒數定義乘積檢驗",
                "content": "$\\sin\\theta \\times \\csc\\theta = \\frac{y}{r} \\times \\frac{r}{y} = 1$；同理 $\\cos\\theta \\sec\\theta = 1$、$\\tan\\theta \\cot\\theta = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：字母首碼防錯辨識",
                "content": "初學者常誤將 $\\sin$ 與 $\\sec$ 湊在一起。記住名偵探防錯口訣：『正配餘、餘配正』，s 配 c，不可同字首相配！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】牢記前三原形，後三者只需一鍵倒數！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#78350f">三對倒數伴侶（S 配 C ‧ T 配 T）</text>
  <rect x="30" y="55" width="95" height="110" rx="10" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
  <text x="77" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">sin θ</text>
  <text x="77" y="115" text-anchor="middle" font-size="16" fill="#dc2626">↕ 倒數</text>
  <text x="77" y="145" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">csc θ</text>
  
  <rect x="142" y="55" width="95" height="110" rx="10" fill="#e0e7ff" stroke="#6366f1" stroke-width="2"/>
  <text x="189" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#3730a3">cos θ</text>
  <text x="189" y="115" text-anchor="middle" font-size="16" fill="#4f46e5">↕ 倒數</text>
  <text x="189" y="145" text-anchor="middle" font-size="14" font-weight="bold" fill="#3730a3">sec θ</text>

  <rect x="255" y="55" width="95" height="110" rx="10" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
  <text x="302" y="85" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">tan θ</text>
  <text x="302" y="115" text-anchor="middle" font-size="16" fill="#d97706">↕ 倒數</text>
  <text x="302" y="145" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">cot θ</text>
</svg>"""
    },
    {
        "id": 4,
        "tag": "CASE 04",
        "page": "課本 P.109 例題 1(1)",
        "category": "邊長比求值",
        "title": "例題 1(1)：8-15-17 直角三角形求 ∠A 之六個函數值",
        "front_content": "在直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$。<br>已知 $AC = 8$、$BC = 15$、$AB = 17$。<br>試求出 $\\angle A$ 的六個三角函數值。",
        "front_tip": "🕵️ 柯南破案導引：站在 $\\angle A$ 視角審視三邊：對邊 $BC = 15$、鄰邊 $AC = 8$、斜邊 $AB = 17$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：鎖定 ∠A 視角之三邊長",
                "content": "斜邊 $r = 17$，對邊 $y = 15$，鄰邊 $x = 8$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算前三大三角函數值",
                "content": "$\\sin A = \\frac{15}{17}$ ； $\\cos A = \\frac{8}{17}$ ； $\\tan A = \\frac{15}{8}$。"
            },
            {
                "num": 3,
                "title": "線索 3：利用倒數直接求得後三者",
                "content": "$\\csc A = \\frac{17}{15}$ ； $\\sec A = \\frac{17}{8}$ ； $\\cot A = \\frac{8}{15}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin A = \\frac{15}{17}, \\cos A = \\frac{8}{17}, \\tan A = \\frac{15}{8}, \\csc A = \\frac{17}{15}, \\sec A = \\frac{17}{8}, \\cot A = \\frac{8}{15}$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="50,165 290,165 290,50" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>
  <rect x="272" y="147" width="18" height="18" fill="none" stroke="#15803d" stroke-width="1.5"/>
  <text x="35" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="298" y="172" font-size="14" font-weight="bold" fill="#1e3a8a">C</text>
  <text x="298" y="45" font-size="14" font-weight="bold" fill="#b91c1c">B</text>
  <text x="160" y="184" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 AC = 8</text>
  <text x="305" y="112" font-size="13" font-weight="bold" fill="#dc2626">對邊 BC = 15</text>
  <text x="150" y="98" font-size="13" font-weight="bold" fill="#15803d">斜邊 AB = 17</text>
</svg>"""
    },
    {
        "id": 5,
        "tag": "CASE 05",
        "page": "課本 P.110 例題 1(2)",
        "category": "邊長比求值",
        "title": "例題 1(2)：5-12-13 直角三角形求 ∠A 之六個函數值",
        "front_content": "在直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$。<br>已知 $AC = 5$、$BC = 12$、$AB = 13$。<br>試求出 $\\angle A$ 的六個三角函數值。",
        "front_tip": "🕵️ 柯南破案導引：確認邊長角色：$\\angle A$ 的對邊為 $12$，鄰邊為 $5$，斜邊為 $13$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：確認各邊對應角色",
                "content": "斜邊 $r = 13$，對邊 $BC = 12$，鄰邊 $AC = 5$。"
            },
            {
                "num": 2,
                "title": "線索 2：求 sin A、cos A、tan A",
                "content": "$\\sin A = \\frac{12}{13}$ ； $\\cos A = \\frac{5}{13}$ ； $\\tan A = \\frac{12}{5}$。"
            },
            {
                "num": 3,
                "title": "線索 3：倒數求 csc A、sec A、cot A",
                "content": "$\\csc A = \\frac{13}{12}$ ； $\\sec A = \\frac{13}{5}$ ； $\\cot A = \\frac{5}{12}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin A = \\frac{12}{13}, \\cos A = \\frac{5}{13}, \\tan A = \\frac{12}{5}, \\csc A = \\frac{13}{12}, \\sec A = \\frac{13}{5}, \\cot A = \\frac{5}{12}$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 240,165 240,40" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <rect x="222" y="147" width="18" height="18" fill="none" stroke="#2563eb" stroke-width="1.5"/>
  <text x="45" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="248" y="172" font-size="14" font-weight="bold" fill="#1e3a8a">C</text>
  <text x="248" y="38" font-size="14" font-weight="bold" fill="#b91c1c">B</text>
  <text x="135" y="184" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 AC = 5</text>
  <text x="255" y="105" font-size="13" font-weight="bold" fill="#dc2626">對邊 BC = 12</text>
  <text x="120" y="95" font-size="13" font-weight="bold" fill="#15803d">斜邊 AB = 13</text>
</svg>"""
    },
    {
        "id": 6,
        "tag": "CASE 06",
        "page": "課本 P.110 隨堂 1(1)",
        "category": "視角切換實戰",
        "title": "隨堂練習 1(1)：8-15-17 直角三角形求 ∠B 之六個函數值",
        "front_content": "在直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$。<br>$AC = 8$、$BC = 15$、$AB = 17$。<br>試求出 <b>$\\angle B$</b> 的六個三角函數值。",
        "front_tip": "🕵️ 柯南破案導引：警惕盲點！視角轉移到 $\\angle B$：現在對邊是 $AC = 8$，鄰邊變成 $BC = 15$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：以 ∠B 為基準重定三邊",
                "content": "斜邊仍為 $AB = 17$；但 $\\angle B$ 的對邊變為 $AC = 8$，鄰邊變為 $BC = 15$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算 sin B、cos B、tan B",
                "content": "$\\sin B = \\frac{\\text{對}}{\\text{斜}} = \\frac{8}{17}$ ； $\\cos B = \\frac{\\text{鄰}}{\\text{斜}} = \\frac{15}{17}$ ； $\\tan B = \\frac{\\text{對}}{\\text{鄰}} = \\frac{8}{15}$。"
            },
            {
                "num": 3,
                "title": "線索 3：計算倒數 csc B、sec B、cot B",
                "content": "$\\csc B = \\frac{17}{8}$ ； $\\sec B = \\frac{17}{15}$ ； $\\cot B = \\frac{15}{8}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin B = \\frac{8}{17}, \\cos B = \\frac{15}{17}, \\tan B = \\frac{8}{15}, \\csc B = \\frac{17}{8}, \\sec B = \\frac{17}{15}, \\cot B = \\frac{15}{8}$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="50,165 290,165 290,50" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
  <text x="270" y="70" font-size="14" font-weight="bold" fill="#dc2626">∠B 視角</text>
  <text x="160" y="184" font-size="13" font-weight="bold" fill="#dc2626">對邊 AC = 8 (下變對邊)</text>
  <text x="305" y="112" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 BC = 15</text>
  <text x="150" y="98" font-size="13" font-weight="bold" fill="#15803d">斜邊 AB = 17</text>
</svg>"""
    },
    {
        "id": 7,
        "tag": "CASE 07",
        "page": "課本 P.110 隨堂 1(2)",
        "category": "視角切換實戰",
        "title": "隨堂練習 1(2)：5-12-13 直角三角形求 ∠B 之六個函數值",
        "front_content": "在直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$。<br>$AC = 5$、$BC = 12$、$AB = 13$。<br>試求出 <b>$\\angle B$</b> 的六個三角函數值。",
        "front_tip": "🕵️ 柯南破案導引：站在 $\\angle B$ 前看：對邊是 $5$，鄰邊是 $12$，斜邊為 $13$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：重新確認 ∠B 之三邊位置",
                "content": "斜邊 $r = 13$，$\\angle B$ 的對邊 $y = AC = 5$，鄰邊 $x = BC = 12$。"
            },
            {
                "num": 2,
                "title": "線索 2：求 sin B、cos B、tan B",
                "content": "$\\sin B = \\frac{5}{13}$ ； $\\cos B = \\frac{12}{13}$ ； $\\tan B = \\frac{5}{12}$。"
            },
            {
                "num": 3,
                "title": "線索 3：求 csc B、sec B、cot B",
                "content": "$\\csc B = \\frac{13}{5}$ ； $\\sec B = \\frac{13}{12}$ ； $\\cot B = \\frac{12}{5}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin B = \\frac{5}{13}, \\cos B = \\frac{12}{13}, \\tan B = \\frac{5}{12}, \\csc B = \\frac{13}{5}, \\sec B = \\frac{13}{12}, \\cot B = \\frac{12}{5}$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 240,165 240,40" fill="#fdf4ff" stroke="#a855f7" stroke-width="2"/>
  <text x="215" y="60" font-size="14" font-weight="bold" fill="#9333ea">∠B</text>
  <text x="135" y="184" font-size="13" font-weight="bold" fill="#9333ea">對邊 AC = 5</text>
  <text x="255" y="105" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 BC = 12</text>
  <text x="120" y="95" font-size="13" font-weight="bold" fill="#15803d">斜邊 AB = 13</text>
</svg>"""
    },
    {
        "id": 8,
        "tag": "CASE 08",
        "page": "課本 P.111 例題 2",
        "category": "知一求其餘",
        "title": "例題 2：已知 cos A = 5/13，求其餘各三角函數值",
        "front_content": "已知直角三角形 $ABC$ 中，$\\angle C$ 為直角，<br>且 $\\cos A = \\frac{5}{13}$。<br>試求 $\\angle A$ 其餘各三角函數值。",
        "front_tip": "🕵️ 柯南破案導引：畫出輔助直角三角形！設鄰邊 $5k$、斜邊 $13k$，用畢氏定理緝拿對邊！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：設邊長比值參數 k",
                "content": "已知 $\\cos A = \\frac{\\text{鄰邊}}{\\text{斜邊}} = \\frac{5}{13}$，設鄰邊 $AC = 5k$、斜邊 $AB = 13k$（$k > 0$）。"
            },
            {
                "num": 2,
                "title": "線索 2：利用畢氏定理求對邊",
                "content": "對邊 $BC = \\sqrt{(13k)^2 - (5k)^2} = \\sqrt{169k^2 - 25k^2} = \\sqrt{144k^2} = 12k$。"
            },
            {
                "num": 3,
                "title": "線索 3：計算其餘五大三角函數值",
                "content": "$\\sin A = \\frac{12}{13}$ ； $\\tan A = \\frac{12}{5}$ ； $\\csc A = \\frac{13}{12}$ ； $\\sec A = \\frac{13}{5}$ ； $\\cot A = \\frac{5}{12}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin A = \\frac{12}{13}, \\tan A = \\frac{12}{5}, \\csc A = \\frac{13}{12}, \\sec A = \\frac{13}{5}, \\cot A = \\frac{5}{12}$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="70,165 250,165 250,55" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
  <text x="55" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="258" y="172" font-size="14" font-weight="bold" fill="#1e3a8a">C</text>
  <text x="258" y="50" font-size="14" font-weight="bold" fill="#b91c1c">B</text>
  <text x="145" y="184" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 AC = 5k</text>
  <text x="265" y="115" font-size="13" font-weight="bold" fill="#dc2626">對邊 BC = 12k</text>
  <text x="135" y="100" font-size="13" font-weight="bold" fill="#15803d">斜邊 AB = 13k</text>
</svg>"""
    },
    {
        "id": 9,
        "tag": "CASE 09",
        "page": "課本 P.111 隨堂 2",
        "category": "知一求其餘",
        "title": "隨堂練習 2：已知 tan A = 24/7，求其餘各三角函數值",
        "front_content": "已知直角三角形 $ABC$ 中，$\\angle C = 90^\\circ$，<br>且 $\\tan A = \\frac{24}{7}$。<br>試求 $\\angle A$ 其餘各三角函數值。",
        "front_tip": "🕵️ 柯南破案導引：$\\tan A = \\frac{\\text{對}}{\\text{鄰}}$！設對邊 $24k$、鄰邊 $7k$，用畢氏定理算出斜邊！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：依正切比設對邊與鄰邊",
                "content": "$\\tan A = \\frac{24}{7}$，設對邊 $BC = 24k$、鄰邊 $AC = 7k$（$k > 0$）。"
            },
            {
                "num": 2,
                "title": "線索 2：畢氏定理推求斜邊",
                "content": "斜邊 $AB = \\sqrt{(24k)^2 + (7k)^2} = \\sqrt{576k^2 + 49k^2} = \\sqrt{625k^2} = 25k$。"
            },
            {
                "num": 3,
                "title": "線索 3：依定義寫出其餘五個函數值",
                "content": "$\\sin A = \\frac{24}{25}$ ； $\\cos A = \\frac{7}{25}$ ； $\\csc A = \\frac{25}{24}$ ； $\\sec A = \\frac{25}{7}$ ； $\\cot A = \\frac{7}{24}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin A = \\frac{24}{25}, \\cos A = \\frac{7}{25}, \\csc A = \\frac{25}{24}, \\sec A = \\frac{25}{7}, \\cot A = \\frac{7}{24}$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 180,165 180,30" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
  <text x="45" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="110" y="184" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 AC = 7k</text>
  <text x="195" y="100" font-size="13" font-weight="bold" fill="#dc2626">對邊 BC = 24k</text>
  <text x="90" y="90" font-size="13" font-weight="bold" fill="#15803d">斜邊 AB = 25k</text>
</svg>"""
    },
    {
        "id": 10,
        "tag": "CASE 10",
        "page": "課本 P.112 例題 3",
        "category": "比例放大解邊長",
        "title": "例題 3：已知 sin A = 4/5 且 AB = 15，求邊長與各函數值",
        "front_content": "直角三角形 $ABC$ 中，$\\angle C$ 為直角，且 $\\sin A = \\frac{4}{5}$。<br>若 $AB = 15$，<br>試求 $\\cos A$、$\\tan A$、$BC$ 與 $AC$ 之長。",
        "front_tip": "🕵️ 柯南破案導引：比例放大！斜邊原本是 $5k$，已知實際長度 $15$，立即可解出放大倍率 $k = 3$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：由比例比值求 cos A 與 tan A",
                "content": "$\\sin A = \\frac{4}{5}$，形成經典 (3, 4, 5) 比例。得 $\\cos A = \\frac{3}{5}$、$\\tan A = \\frac{4}{3}$。"
            },
            {
                "num": 2,
                "title": "線索 2：由斜邊長度求放大倍數",
                "content": "已知斜邊 $AB = 15 = 5k \\implies k = 3$。"
            },
            {
                "num": 3,
                "title": "線索 3：計算實際邊長 BC 與 AC",
                "content": "對邊 $BC = 4k = 4 \\times 3 = 12$ ； 鄰邊 $AC = 3k = 3 \\times 3 = 9$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\cos A = \\frac{3}{5}, \\tan A = \\frac{4}{3}, BC = 12, AC = 9$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 240,165 240,40" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
  <text x="45" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="135" y="184" font-size="13" font-weight="bold" fill="#1e40af">AC = 3×3 = 9</text>
  <text x="255" y="105" font-size="13" font-weight="bold" fill="#dc2626">BC = 4×3 = 12</text>
  <text x="120" y="95" font-size="13" font-weight="bold" fill="#15803d">AB = 5×3 = 15</text>
</svg>"""
    },
    {
        "id": 11,
        "tag": "CASE 11",
        "page": "課本 P.112 隨堂 3",
        "category": "比例放大解邊長",
        "title": "隨堂練習 3：已知 csc A = 17/15 且 AC = 40，求邊長與各值",
        "front_content": "直角三角形 $ABC$ 中，$\\angle C = 90^\\circ$，且 $\\csc A = \\frac{17}{15}$。<br>若 $AC = 40$，<br>試求 $\\tan A$、$\\sec A$、$AB$ 與 $BC$ 之長。",
        "front_tip": "🕵️ 柯南破案導引：$\\csc A = \\frac{\\text{斜}}{\\text{對}} = \\frac{17}{15}$，鄰邊即為 $8k$！已知 $AC = 40$，求出 $k = 5$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：三邊比例鎖定",
                "content": "$\\csc A = \\frac{17}{15} \\implies \\sin A = \\frac{15}{17}$。斜邊 $17k$、對邊 $15k$、鄰邊 $\\sqrt{17^2 - 15^2}k = 8k$。"
            },
            {
                "num": 2,
                "title": "線索 2：利用鄰邊 AC = 40 解出 k",
                "content": "$AC = 8k = 40 \\implies k = 5$。"
            },
            {
                "num": 3,
                "title": "線索 3：計算實際邊長與函數值",
                "content": "$AB = 17 \\times 5 = 85$ ； $BC = 15 \\times 5 = 75$ ； $\\tan A = \\frac{15}{8}$ ； $\\sec A = \\frac{17}{8}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\tan A = \\frac{15}{8}, \\sec A = \\frac{17}{8}, AB = 85, BC = 75$。",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="50,165 290,165 290,50" fill="#fdf2f8" stroke="#db2777" stroke-width="2"/>
  <text x="35" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="150" y="184" font-size="13" font-weight="bold" fill="#1e40af">AC = 8×5 = 40</text>
  <text x="305" y="112" font-size="13" font-weight="bold" fill="#dc2626">BC = 15×5 = 75</text>
  <text x="140" y="98" font-size="13" font-weight="bold" fill="#15803d">AB = 17×5 = 85</text>
</svg>"""
    },

    # ==========================================
    # 階段二：特別角與生活科技篇 (CASE 12 ~ 20)
    # ==========================================
    {
        "id": 12,
        "tag": "CASE 12",
        "page": "課本 P.113 概念 1",
        "category": "特別角推導",
        "title": "30° 與 60° 特別角的六大三角函數值推導",
        "front_content": "由正三角形對折所得 $30^\\circ-60^\\circ-90^\\circ$ 直角三角形，<br>三邊長比為 $1 : \\sqrt{3} : 2$。<br>$\\sin 30^\\circ = \\frac{1}{2}$ ； $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$ ； $\\tan 30^\\circ = \\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}$<br>$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$ ； $\\cos 60^\\circ = \\frac{1}{2}$ ； $\\tan 60^\\circ = \\sqrt{3}$",
        "front_tip": "🕵️ 柯南破案導引：記住口訣：『$30^\\circ$ 對 $1$、$60^\\circ$ 對 $\\sqrt{3}$、$90^\\circ$ 對 $2$』！斜邊恆為 $2$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：30° 視角推導",
                "content": "面對 $30^\\circ$：對邊 $1$、鄰邊 $\\sqrt{3}$、斜邊 $2$。$\\sin 30^\\circ = \\frac{1}{2}, \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}, \\tan 30^\\circ = \\frac{\\sqrt{3}}{3}$。"
            },
            {
                "num": 2,
                "title": "線索 2：60° 視角推導",
                "content": "面對 $60^\\circ$：對邊 $\\sqrt{3}$、鄰邊 $1$、斜邊 $2$。$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}, \\cos 60^\\circ = \\frac{1}{2}, \\tan 60^\\circ = \\sqrt{3}$。"
            },
            {
                "num": 3,
                "title": "線索 3：餘角交叉互換特徵",
                "content": "$\\sin 30^\\circ = \\cos 60^\\circ = \\frac{1}{2}$ ； $\\cos 30^\\circ = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$；兩者互為餘角！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$30^\\circ$ 與 $60^\\circ$ 各值均來自 $1 : \\sqrt{3} : 2$ 標準幾何比例！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 260,165 260,50" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <text x="80" y="158" font-size="14" font-weight="bold" fill="#78350f">30°</text>
  <text x="235" y="75" font-size="14" font-weight="bold" fill="#78350f">60°</text>
  <text x="150" y="184" font-size="13" font-weight="bold" fill="#1e40af">鄰邊 = √3</text>
  <text x="275" y="115" font-size="13" font-weight="bold" fill="#dc2626">對邊 = 1</text>
  <text x="140" y="95" font-size="13" font-weight="bold" fill="#15803d">斜邊 = 2</text>
</svg>"""
    },
    {
        "id": 13,
        "tag": "CASE 13",
        "page": "課本 P.113 概念 2",
        "category": "特別角推導",
        "title": "45° 特別角的六大三角函數值推導",
        "front_content": "在兩股長均為 $1$ 的等腰直角三角形中，<br>由畢氏定理可得斜邊長為 $\\sqrt{1^2 + 1^2} = \\sqrt{2}$。<br>此時三邊比例為 $1 : 1 : \\sqrt{2}$：<br>$\\sin 45^\\circ = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$ ； $\\cos 45^\\circ = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$<br>$\\tan 45^\\circ = 1$ ； $\\cot 45^\\circ = 1$ ； $\\sec 45^\\circ = \\csc 45^\\circ = \\sqrt{2}$",
        "front_tip": "🕵️ 柯南破案導引：等腰直角三角形兩股相等，因此 $\\sin 45^\\circ = \\cos 45^\\circ$，且正切值剛好為 $1$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：等腰直角幾何特徵",
                "content": "兩股長皆為 $1$，夾直角 $90^\\circ$，兩銳角均為 $45^\\circ$。由畢氏定理知斜邊為 $\\sqrt{2}$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算 45° 各三角函數值",
                "content": "$\\sin 45^\\circ = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$；$\\cos 45^\\circ = \\frac{\\sqrt{2}}{2}$；$\\tan 45^\\circ = \\frac{1}{1} = 1$。"
            },
            {
                "num": 3,
                "title": "線索 3：倒數求得伴隨函數",
                "content": "$\\csc 45^\\circ = \\sqrt{2}$ ； $\\sec 45^\\circ = \\sqrt{2}$ ； $\\cot 45^\\circ = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$45^\\circ$ 函數值對稱極高，$\\sin = \\cos = \\frac{\\sqrt{2}}{2}, \\tan = \\cot = 1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="90,165 230,165 230,25" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
  <text x="115" y="158" font-size="14" font-weight="bold" fill="#15803d">45°</text>
  <text x="205" y="55" font-size="14" font-weight="bold" fill="#15803d">45°</text>
  <text x="150" y="184" font-size="13" font-weight="bold" fill="#1e40af">底股 = 1</text>
  <text x="245" y="100" font-size="13" font-weight="bold" fill="#dc2626">高股 = 1</text>
  <text x="135" y="90" font-size="13" font-weight="bold" fill="#15803d">斜邊 = √2</text>
</svg>"""
    },
    {
        "id": 14,
        "tag": "CASE 14",
        "page": "課本 P.114 表 2-1",
        "category": "特別角彙整",
        "title": "表 2-1 特別角三角函數精確值全覽表",
        "front_content": "全套必背特別角神技速查：<br>• $30^\\circ = \\frac{\\pi}{6}$：$\\sin=\\frac{1}{2}, \\cos=\\frac{\\sqrt{3}}{2}, \\tan=\\frac{\\sqrt{3}}{3}, \\cot=\\sqrt{3}, \\sec=\\frac{2\\sqrt{3}}{3}, \\csc=2$<br>• $45^\\circ = \\frac{\\pi}{4}$：$\\sin=\\frac{\\sqrt{2}}{2}, \\cos=\\frac{\\sqrt{2}}{2}, \\tan=1, \\cot=1, \\sec=\\sqrt{2}, \\csc=\\sqrt{2}$<br>• $60^\\circ = \\frac{\\pi}{3}$：$\\sin=\\frac{\\sqrt{3}}{2}, \\cos=\\frac{1}{2}, \\tan=\\sqrt{3}, \\cot=\\frac{\\sqrt{3}}{3}, \\sec=2, \\csc=\\frac{2\\sqrt{3}}{3}$",
        "front_tip": "🕵️ 柯南破案導引：正弦隨角度遞增（$\\frac{1}{2} < \\frac{\\sqrt{2}}{2} < \\frac{\\sqrt{3}}{2}$），餘弦隨角度遞減！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分子規律記憶法",
                "content": "$\\sin 30^\\circ = \\frac{\\sqrt{1}}{2}$、$\\sin 45^\\circ = \\frac{\\sqrt{2}}{2}$、$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$；分子為根號 1, 2, 3，優雅規律！"
            },
            {
                "num": 2,
                "title": "線索 2：餘弦逆序規律",
                "content": "$\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$、$\\cos 45^\\circ = \\frac{\\sqrt{2}}{2}$、$\\cos 60^\\circ = \\frac{\\sqrt{1}}{2}$；分子為根號 3, 2, 1 逆序！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】熟記根號 1, 2, 3 規律，考試分秒搶分！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full" style="max-width:100%; height:auto;">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="#78350f">特別角分子階梯定律 (分母恆為 2)</text>
  <rect x="20" y="48" width="340" height="36" rx="6" fill="#fee2e2"/>
  <text x="45" y="71" font-size="12" font-weight="bold" fill="#991b1b">sin θ</text>
  <text x="125" y="71" font-size="11.5" font-weight="bold" fill="#991b1b">√1/2 (30°)</text>
  <text x="215" y="71" font-size="11.5" font-weight="bold" fill="#991b1b">√2/2 (45°)</text>
  <text x="300" y="71" font-size="11.5" font-weight="bold" fill="#991b1b">√3/2 (60°)</text>
  
  <rect x="20" y="96" width="340" height="36" rx="6" fill="#e0e7ff"/>
  <text x="45" y="119" font-size="12" font-weight="bold" fill="#3730a3">cos θ</text>
  <text x="125" y="119" font-size="11.5" font-weight="bold" fill="#3730a3">√3/2 (30°)</text>
  <text x="215" y="119" font-size="11.5" font-weight="bold" fill="#3730a3">√2/2 (45°)</text>
  <text x="300" y="119" font-size="11.5" font-weight="bold" fill="#3730a3">√1/2 (60°)</text>

  <rect x="20" y="144" width="340" height="36" rx="6" fill="#fef3c7"/>
  <text x="45" y="167" font-size="12" font-weight="bold" fill="#92400e">tan θ</text>
  <text x="135" y="167" font-size="12" font-weight="bold" fill="#92400e">√3 / 3</text>
  <text x="225" y="167" font-size="12" font-weight="bold" fill="#92400e">1</text>
  <text x="305" y="167" font-size="12" font-weight="bold" fill="#92400e">√3</text>
</svg>"""
    },
    {
        "id": 15,
        "tag": "CASE 15",
        "page": "課本 P.114 例題 4(1)",
        "category": "特別角運算",
        "title": "例題 4(1)：特別角四則運算求值",
        "front_content": "試求下列各式之值：<br>$$\\sin 30^\\circ - \\cos 60^\\circ + \\tan 45^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：將各特別角的數值一一替換入算式：$\\sin 30^\\circ = \\frac{1}{2}$，$\\cos 60^\\circ = \\frac{1}{2}$，$\\tan 45^\\circ = 1$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用特別角數值證物",
                "content": "$\\sin 30^\\circ = \\frac{1}{2}$ ； $\\cos 60^\\circ = \\frac{1}{2}$ ； $\\tan 45^\\circ = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入原式運算",
                "content": "原式 $= \\frac{1}{2} - \\frac{1}{2} + 1 = 0 + 1 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">sin 30° - cos 60° + tan 45°</text>
  <text x="100" y="105" text-anchor="middle" font-size="18" fill="#dc2626">1/2</text>
  <text x="150" y="105" text-anchor="middle" font-size="18" fill="#475569">-</text>
  <text x="190" y="105" text-anchor="middle" font-size="18" fill="#dc2626">1/2</text>
  <text x="235" y="105" text-anchor="middle" font-size="18" fill="#475569">+</text>
  <text x="275" y="105" text-anchor="middle" font-size="18" fill="#16a34a">1</text>
  <line x1="80" y1="130" x2="300" y2="130" stroke="#b45309" stroke-width="2"/>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 1</text>
</svg>"""
    },
    {
        "id": 16,
        "tag": "CASE 16",
        "page": "課本 P.114 例題 4(2)",
        "category": "特別角運算",
        "title": "例題 4(2)：特別角平方與乘積運算求值",
        "front_content": "試求下列各式之值：<br>$$2 \\sin^2 45^\\circ + \\cot 30^\\circ \\csc 60^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：注意記號！$\\sin^2 45^\\circ$ 即 $(\\sin 45^\\circ)^2$！$\\cot 30^\\circ = \\sqrt{3}$，$\\csc 60^\\circ = \\frac{2}{\\sqrt{3}}$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：個別函數值提取",
                "content": "$\\sin 45^\\circ = \\frac{\\sqrt{2}}{2} = \\frac{1}{\\sqrt{2}}$ ； $\\cot 30^\\circ = \\sqrt{3}$ ； $\\csc 60^\\circ = \\frac{2}{\\sqrt{3}}$。"
            },
            {
                "num": 2,
                "title": "線索 2：展開平方項與乘積項",
                "content": "$2 \\sin^2 45^\\circ = 2 \\times \\left(\\frac{1}{\\sqrt{2}}\\right)^2 = 2 \\times \\frac{1}{2} = 1$。"
            },
            {
                "num": 3,
                "title": "線索 3：乘積約分並相加",
                "content": "$\\cot 30^\\circ \\csc 60^\\circ = \\sqrt{3} \\times \\frac{2}{\\sqrt{3}} = 2$。原式 $= 1 + 2 = 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $3$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">2 sin²45° + cot 30° · csc 60°</text>
  <rect x="50" y="70" width="120" height="50" rx="8" fill="#e0e7ff"/>
  <text x="110" y="100" text-anchor="middle" font-size="15" fill="#3730a3">2 · (1/2) = 1</text>
  <text x="190" y="100" text-anchor="middle" font-size="20" fill="#475569">+</text>
  <rect x="210" y="70" width="120" height="50" rx="8" fill="#fef3c7"/>
  <text x="270" y="100" text-anchor="middle" font-size="15" fill="#92400e">√3 · (2/√3) = 2</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 1 + 2 = 3</text>
</svg>"""
    },
    {
        "id": 17,
        "tag": "CASE 17",
        "page": "課本 P.114 隨堂 4(1)",
        "category": "特別角運算",
        "title": "隨堂練習 4(1)：含根號特別角四則運算求值",
        "front_content": "試求下列各式之值：<br>$$2 \\sin 60^\\circ - \\sqrt{2} \\cos 45^\\circ + \\tan 60^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2}$，$\\cos 45^\\circ = \\frac{\\sqrt{2}}{2}$，$\\tan 60^\\circ = \\sqrt{3}$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：帶入各項特別角精確值",
                "content": "$2 \\sin 60^\\circ = 2 \\times \\frac{\\sqrt{3}}{2} = \\sqrt{3}$ ； $\\sqrt{2} \\cos 45^\\circ = \\sqrt{2} \\times \\frac{\\sqrt{2}}{2} = \\frac{2}{2} = 1$ ； $\\tan 60^\\circ = \\sqrt{3}$。"
            },
            {
                "num": 2,
                "title": "線索 2：同類項合併化簡",
                "content": "原式 $= \\sqrt{3} - 1 + \\sqrt{3} = 2\\sqrt{3} - 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $2\\sqrt{3} - 1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">2 sin 60° - √2 cos 45° + tan 60°</text>
  <text x="100" y="105" text-anchor="middle" font-size="18" fill="#dc2626">√3</text>
  <text x="150" y="105" text-anchor="middle" font-size="18" fill="#475569">-</text>
  <text x="190" y="105" text-anchor="middle" font-size="18" fill="#16a34a">1</text>
  <text x="235" y="105" text-anchor="middle" font-size="18" fill="#475569">+</text>
  <text x="275" y="105" text-anchor="middle" font-size="18" fill="#dc2626">√3</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 2√3 - 1</text>
</svg>"""
    },
    {
        "id": 18,
        "tag": "CASE 18",
        "page": "課本 P.114 隨堂 4(2)",
        "category": "弳度特別角運算",
        "title": "隨堂練習 4(2)：弳度量特別角平方運算求值",
        "front_content": "試求下列各式之值：<br>$$\\sin^2 \\frac{\\pi}{4} + \\cos^2 \\frac{\\pi}{6} - \\cot^2 \\frac{\\pi}{3}$$",
        "front_tip": "🕵️ 柯南破案導引：$\\pi = 180^\\circ$！$\\frac{\\pi}{4} = 45^\\circ$、$\\frac{\\pi}{6} = 30^\\circ$、$\\frac{\\pi}{3} = 60^\\circ$！先換角度再代入！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：弳度與度數對應轉化",
                "content": "$\\frac{\\pi}{4} = 45^\\circ$ ； $\\frac{\\pi}{6} = 30^\\circ$ ； $\\frac{\\pi}{3} = 60^\\circ$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算各平方項數值",
                "content": "$\\sin^2 45^\\circ = \\left(\\frac{\\sqrt{2}}{2}\\right)^2 = \\frac{2}{4} = \\frac{1}{2}$ ； $\\cos^2 30^\\circ = \\left(\\frac{\\sqrt{3}}{2}\\right)^2 = \\frac{3}{4}$ ； $\\cot^2 60^\\circ = \\left(\\frac{\\sqrt{3}}{3}\\right)^2 = \\frac{3}{9} = \\frac{1}{3}$。"
            },
            {
                "num": 3,
                "title": "線索 3：通分並完成計算",
                "content": "原式 $= \\frac{1}{2} + \\frac{3}{4} - \\frac{1}{3} = \\frac{6}{12} + \\frac{9}{12} - \\frac{4}{12} = \\frac{11}{12}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $\\frac{11}{12}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">sin²(π/4) + cos²(π/6) - cot²(π/3)</text>
  <text x="90" y="105" text-anchor="middle" font-size="17" fill="#dc2626">1/2</text>
  <text x="140" y="105" text-anchor="middle" font-size="17" fill="#475569">+</text>
  <text x="190" y="105" text-anchor="middle" font-size="17" fill="#2563eb">3/4</text>
  <text x="240" y="105" text-anchor="middle" font-size="17" fill="#475569">-</text>
  <text x="290" y="105" text-anchor="middle" font-size="17" fill="#b45309">1/3</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 6/12 + 9/12 - 4/12 = 11/12</text>
</svg>"""
    },
    {
        "id": 19,
        "tag": "CASE 19",
        "page": "課本 P.115 例題 5",
        "category": "生活科技反推角",
        "title": "例題 5：內政部無障礙坡道坡度夾角反推",
        "front_content": "根據內政部營建署對於無障礙坡道的規定，<br>室內坡道坡度應小於八分之一（即 $\\tan\\theta = \\frac{1}{8}$）。<br>換句話說，室內坡道與地面的夾角大約要小於多少度？<br>（四捨五入至小數點後第 3 位）",
        "front_tip": "🕵️ 柯南破案導引：坡度即正切值！利用手機或計算機反三角函數按鍵 $\\tan^{-1}(1 \\div 8)$ 反推角度！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：坡度定義即正切函數",
                "content": "坡度 $=\\frac{\\text{垂直上升高度}}{\\text{水平前進距離}} = \\frac{\\text{對邊}}{\\text{鄰邊}} = \\tan\\theta = \\frac{1}{8} = 0.125$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算機或手機 2nd 鍵反推",
                "content": "按鍵操作：切換為角度制 (DEG) ➔ 按 `2nd` / `SHIFT` ➔ 按 `tan⁻¹` ➔ 輸入 `1 ÷ 8 =`。"
            },
            {
                "num": 3,
                "title": "線索 3：四捨五入結案",
                "content": "計算機顯示 $\\theta \\approx 7.125016^\\circ$，四捨五入至小數點後第 3 位得 $\\theta \\approx 7.125^\\circ$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】室內坡道與地面夾角大約要小於 $7.125^\\circ$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="50,160 320,160 320,126" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <line x1="50" y1="160" x2="320" y2="126" stroke="#dc2626" stroke-width="3"/>
  <text x="80" y="153" font-size="13" font-weight="bold" fill="#b91c1c">θ ≈ 7.125°</text>
  <text x="180" y="180" font-size="13" font-weight="bold" fill="#1e40af">水平距離 8</text>
  <text x="328" y="145" font-size="13" font-weight="bold" fill="#15803d">垂直高度 1</text>
</svg>"""
    },
    {
        "id": 20,
        "tag": "CASE 20",
        "page": "課本 P.116 隨堂 5",
        "category": "生活科技反推角",
        "title": "隨堂練習 5：自行車 20% 險升坡夾角反推",
        "front_content": "在自行車討論區出現坡度 20% 的險升坡標誌。<br>請計算這個險升坡與地面的夾角約是多少度？<br>（四捨五入至整數位）<br>其中 20% 是指每前進 100 公尺會上升 20 公尺。",
        "front_tip": "🕵️ 柯南破案導引：每前進 100 公尺上升 20 公尺，代表 $\\tan\\theta = \\frac{20}{100} = 0.2$！按 $\\tan^{-1}(0.2)$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：百分比坡度化為正切比值",
                "content": "坡度 $20\\% = \\frac{20}{100} = 0.2$。因此 $\\tan\\theta = 0.2$。"
            },
            {
                "num": 2,
                "title": "線索 2：反三角函數操作求角度",
                "content": "$\\theta = \\tan^{-1}(0.2) \\approx 11.3099^\\circ$。"
            },
            {
                "num": 3,
                "title": "線索 3：四捨五入至整數位",
                "content": "$11.3099^\\circ$ 四捨五入至整數位約為 $11^\\circ$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】該險升坡與地面夾角約為 $11^\\circ$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="50,160 300,160 300,110" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="75" y="153" font-size="13" font-weight="bold" fill="#dc2626">θ ≈ 11°</text>
  <text x="160" y="180" font-size="13" font-weight="bold" fill="#1e40af">前進 100 m</text>
  <text x="308" y="138" font-size="13" font-weight="bold" fill="#15803d">上升 20 m</text>
</svg>"""
    },

    # ==========================================
    # 階段三：魔法六角星與恆等關係篇 (CASE 21 ~ 30)
    # ==========================================
    {
        "id": 21,
        "tag": "CASE 21",
        "page": "課本 P.117 概念",
        "category": "恆等關係全覽",
        "title": "神奇魔法六角形四大破案星陣全覽",
        "front_content": "六角形頂點排列順序：左上 $\\sin$、右上 $\\cos$；<br>左中 $\\tan$、右中 $\\cot$；左下 $\\sec$、右下 $\\csc$；中央放數字 $1$。<br>具備四大神奇性質：<br>1. 對角線互為倒數 ； 2. 倒三角形平方和等於下方頂點<br>3. 每個頂點等於相鄰兩頂點之積（商數） ； 4. 每條橫線端點互為餘角",
        "front_tip": "🕵️ 柯南破案導引：記住左側無『co』(sin, tan, sec)，右側全帶『co』(cos, cot, csc)！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：六角星陣標準排位",
                "content": "左半邊全為無 co 的函數（$\\sin, \\tan, \\sec$）；右半邊全為對應的 co 函數（$\\cos, \\cot, \\csc$）。"
            },
            {
                "num": 2,
                "title": "線索 2：四大關係一圖網羅",
                "content": "對角相乘為 1；倒三角平方和；相鄰頂點相乘；橫向餘角互換。四大關係永不忘！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】六角星陣在手，所有恆等關係一覽無遺！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <circle cx="190" cy="100" r="16" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
  <text x="190" y="106" text-anchor="middle" font-size="16" font-weight="bold" fill="#854d0e">1</text>
  <line x1="120" y1="50" x2="260" y2="150" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="260" y1="50" x2="120" y2="150" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="90" y1="100" x2="290" y2="100" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="110" y="45" font-size="14" font-weight="bold" fill="#dc2626">sin</text>
  <text x="250" y="45" font-size="14" font-weight="bold" fill="#2563eb">cos</text>
  <text x="65" y="105" font-size="14" font-weight="bold" fill="#dc2626">tan</text>
  <text x="295" y="105" font-size="14" font-weight="bold" fill="#2563eb">cot</text>
  <text x="110" y="165" font-size="14" font-weight="bold" fill="#dc2626">sec</text>
  <text x="250" y="165" font-size="14" font-weight="bold" fill="#2563eb">csc</text>
</svg>"""
    },
    {
        "id": 22,
        "tag": "CASE 22",
        "page": "課本 P.117 關係 1",
        "category": "倒數關係",
        "title": "恆等關係一：倒數關係（對角互倒）",
        "front_content": "六角形中，每條對角線兩端點的三角函數，互為倒數：<br>(1) $\\sin\\theta \\cdot \\csc\\theta = 1$<br>(2) $\\cos\\theta \\cdot \\sec\\theta = 1$<br>(3) $\\tan\\theta \\cdot \\cot\\theta = 1$",
        "front_tip": "🕵️ 柯南破案導引：穿越中央數字 1 的對角線，兩端乘積必為 1！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：定義幾何推導",
                "content": "$\\sin\\theta \\csc\\theta = \\frac{y}{r} \\times \\frac{r}{y} = 1$；$\\cos\\theta \\sec\\theta = \\frac{x}{r} \\times \\frac{r}{x} = 1$；$\\tan\\theta \\cot\\theta = \\frac{y}{x} \\times \\frac{x}{y} = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：常見求值與化簡應用",
                "content": "遇到同角 $\\sin 50^\\circ \\csc 50^\\circ$ 或 $\\tan 40^\\circ \\cot 40^\\circ$，直接秒殺寫 $1$！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】同角對角線函數相乘，恆等於 1！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">對角線乘積恆為 1</text>
  <text x="190" y="80" text-anchor="middle" font-size="15" fill="#dc2626">sin θ · csc θ = 1</text>
  <text x="190" y="115" text-anchor="middle" font-size="15" fill="#2563eb">cos θ · sec θ = 1</text>
  <text x="190" y="150" text-anchor="middle" font-size="15" fill="#16a34a">tan θ · cot θ = 1</text>
</svg>"""
    },
    {
        "id": 23,
        "tag": "CASE 23",
        "page": "課本 P.117 關係 2",
        "category": "商數關係",
        "title": "恆等關係二：商數關係（相鄰相除）",
        "front_content": "六角形中，每個頂點為相鄰兩頂點之乘積：<br>(1) $\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}$（即 $\\sin\\theta = \\tan\\theta \\cdot \\cos\\theta$）<br>(2) $\\cot\\theta = \\frac{\\cos\\theta}{\\sin\\theta}$（即 $\\cos\\theta = \\cot\\theta \\cdot \\sin\\theta$）",
        "front_tip": "🕵️ 柯南破案導引：正切是正弦除以餘弦，餘切是餘弦除以正弦！一個頂點等於順時針或逆時針相鄰兩頂點之商！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：定義分式代入驗證",
                "content": "$\\frac{\\sin\\theta}{\\cos\\theta} = \\frac{y/r}{x/r} = \\frac{y}{x} = \\tan\\theta$。"
            },
            {
                "num": 2,
                "title": "線索 2：倒數推導餘切商數",
                "content": "$\\cot\\theta = \\frac{1}{\\tan\\theta} = \\frac{\\cos\\theta}{\\sin\\theta}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}, \\cot\\theta = \\frac{\\cos\\theta}{\\sin\\theta}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">商數關係結構圖</text>
  <rect x="70" y="65" width="240" height="50" rx="8" fill="#fef3c7"/>
  <text x="190" y="96" text-anchor="middle" font-size="16" font-weight="bold" fill="#b45309">tan θ = sin θ / cos θ</text>
  <rect x="70" y="125" width="240" height="50" rx="8" fill="#e0e7ff"/>
  <text x="190" y="156" text-anchor="middle" font-size="16" font-weight="bold" fill="#3730a3">cot θ = cos θ / sin θ</text>
</svg>"""
    },
    {
        "id": 24,
        "tag": "CASE 24",
        "page": "課本 P.117 關係 3",
        "category": "平方關係",
        "title": "恆等關係三：平方關係（倒三角平方和）",
        "front_content": "六角形中，每個倒三角形上方兩頂點之平方和，等於下方頂點之平方：<br>(1) $\\sin^2\\theta + \\cos^2\\theta = 1$<br>(2) $1 + \\tan^2\\theta = \\sec^2\\theta$<br>(3) $1 + \\cot^2\\theta = \\csc^2\\theta$",
        "front_tip": "🕵️ 柯南破案導引：倒三角形『左上平方 + 右上平方 = 下面平方』！畢氏定理在三角函數的完美化身！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：畢氏定理證明 sin² + cos² = 1",
                "content": "$\\sin^2\\theta + \\cos^2\\theta = \\left(\\frac{y}{r}\\right)^2 + \\left(\\frac{x}{r}\\right)^2 = \\frac{y^2 + x^2}{r^2} = \\frac{r^2}{r^2} = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：同除推廣出另外兩式",
                "content": "兩邊同除以 $\\cos^2\\theta$ 得 $\\tan^2\\theta + 1 = \\sec^2\\theta$；同除以 $\\sin^2\\theta$ 得 $1 + \\cot^2\\theta = \\csc^2\\theta$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin^2\\theta+\\cos^2\\theta=1$ 為核心樞紐，派生全部平方關係！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">三大倒三角平方關係</text>
  <polygon points="190,105 150,60 230,60" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="190" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#991b1b">sin² + cos² = 1</text>
  <text x="110" y="155" text-anchor="middle" font-size="14" font-weight="bold" fill="#b45309">1 + tan² = sec²</text>
  <text x="270" y="155" text-anchor="middle" font-size="14" font-weight="bold" fill="#4338ca">1 + cot² = csc²</text>
</svg>"""
    },
    {
        "id": 25,
        "tag": "CASE 25",
        "page": "課本 P.117 關係 4",
        "category": "餘角關係",
        "title": "恆等關係四：餘角關係（橫向端點互換）",
        "front_content": "六角形中，每條橫線兩端點的三角函數互為餘角關係：<br>$\\sin(90^\\circ - \\theta) = \\cos\\theta$ ； $\\cos(90^\\circ - \\theta) = \\sin\\theta$<br>$\\tan(90^\\circ - \\theta) = \\cot\\theta$ ； $\\cot(90^\\circ - \\theta) = \\tan\\theta$<br>$\\sec(90^\\circ - \\theta) = \\csc\\theta$ ； $\\csc(90^\\circ - \\theta) = \\sec\\theta$",
        "front_tip": "🕵️ 柯南破案導引：角度相加為 $90^\\circ$ 時，『正弦換餘弦、正切換餘切、正割換餘割』！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：直角三角形另一銳角視角",
                "content": "直角三角形兩銳角和為 $90^\\circ$，另一銳角必為 $90^\\circ - \\theta$。其對邊與鄰邊剛好對調！"
            },
            {
                "num": 2,
                "title": "線索 2：函數換裝法則",
                "content": "只要角度相加為 $90^\\circ$（如 $30^\\circ$ 與 $60^\\circ$、$20^\\circ$ 與 $70^\\circ$），函數直接換成對應的 co-函數！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】橫向端點同高度，角度互餘即互換！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">餘角橫向端點互換 (和為 90°)</text>
  <line x1="80" y1="70" x2="300" y2="70" stroke="#dc2626" stroke-width="2"/>
  <text x="100" y="65" font-size="14" font-weight="bold" fill="#dc2626">sin(90°-θ)</text>
  <text x="280" y="65" font-size="14" font-weight="bold" fill="#2563eb">cos θ</text>
  
  <line x1="80" y1="115" x2="300" y2="115" stroke="#16a34a" stroke-width="2"/>
  <text x="100" y="110" font-size="14" font-weight="bold" fill="#16a34a">tan(90°-θ)</text>
  <text x="280" y="110" font-size="14" font-weight="bold" fill="#b45309">cot θ</text>

  <line x1="80" y1="160" x2="300" y2="160" stroke="#7c3aed" stroke-width="2"/>
  <text x="100" y="155" font-size="14" font-weight="bold" fill="#7c3aed">sec(90°-θ)</text>
  <text x="280" y="155" font-size="14" font-weight="bold" fill="#4338ca">csc θ</text>
</svg>"""
    },
    {
        "id": 26,
        "tag": "CASE 26",
        "page": "課本 P.119 例題 6(1)",
        "category": "恆等關係求值",
        "title": "例題 6(1)：倒數關係求值",
        "front_content": "試求下列各式之值：<br>$$\\sin 50^\\circ \\times \\csc 50^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：同角 $50^\\circ$！正弦與餘割為對角線互倒伴侶！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：辨識函數與角度關係",
                "content": "角度皆為 $50^\\circ$。由倒數關係知 $\\sin\\theta \\times \\csc\\theta = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：直接得出乘積",
                "content": "$\\sin 50^\\circ \\times \\csc 50^\\circ = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="60" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e40af">sin 50° · csc 50°</text>
  <text x="190" y="110" text-anchor="middle" font-size="16" fill="#dc2626">利用倒數關係：sin θ · csc θ = 1</text>
  <text x="190" y="160" text-anchor="middle" font-size="26" font-weight="bold" fill="#b91c1c">= 1</text>
</svg>"""
    },
    {
        "id": 27,
        "tag": "CASE 27",
        "page": "課本 P.119 例題 6(2)",
        "category": "恆等關係求值",
        "title": "例題 6(2)：平方關係求值",
        "front_content": "試求下列各式之值：<br>$$\\sin^2 40^\\circ + \\cos^2 40^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：同角 $40^\\circ$！正弦平方加餘弦平方，畢氏恆等必得 1！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：辨認同角平方和特徵",
                "content": "角度皆為 $40^\\circ$。利用平方關係：$\\sin^2\\theta + \\cos^2\\theta = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：得出化簡結果",
                "content": "$\\sin^2 40^\\circ + \\cos^2 40^\\circ = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="60" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e40af">sin² 40° + cos² 40°</text>
  <text x="190" y="110" text-anchor="middle" font-size="16" fill="#dc2626">利用平方關係：sin²θ + cos²θ = 1</text>
  <text x="190" y="160" text-anchor="middle" font-size="26" font-weight="bold" fill="#b91c1c">= 1</text>
</svg>"""
    },
    {
        "id": 28,
        "tag": "CASE 28",
        "page": "課本 P.119 例題 6(3)",
        "category": "恆等關係求值",
        "title": "例題 6(3)：正割與正切平方差變形求值",
        "front_content": "試求下列各式之值：<br>$$\\sec^2 70^\\circ - \\tan^2 70^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：六角星陣倒三角：$1 + \\tan^2\\theta = \\sec^2\\theta$！移項即破案！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用正切正割平方公式",
                "content": "利用平方關係：$1 + \\tan^2 70^\\circ = \\sec^2 70^\\circ$。"
            },
            {
                "num": 2,
                "title": "線索 2：移項化簡",
                "content": "將 $\\tan^2 70^\\circ$ 移至等號右邊，得 $\\sec^2 70^\\circ - \\tan^2 70^\\circ = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="55" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e40af">sec² 70° - tan² 70°</text>
  <text x="190" y="105" text-anchor="middle" font-size="16" fill="#dc2626">因為 1 + tan²θ = sec²θ  ⇒  sec²θ - tan²θ = 1</text>
  <text x="190" y="160" text-anchor="middle" font-size="26" font-weight="bold" fill="#b91c1c">= 1</text>
</svg>"""
    },
    {
        "id": 29,
        "tag": "CASE 29",
        "page": "課本 P.120 隨堂 6(1)",
        "category": "恆等關係求值",
        "title": "隨堂練習 6(1)：餘弦與正割倒數求值",
        "front_content": "試求下列各式之值：<br>$$\\cos 35^\\circ \\times \\sec 35^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：同角 $35^\\circ$！餘弦 $\\cos$ 與正割 $\\sec$ 互為倒數！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：辨識倒數關係伴侶",
                "content": "$\\cos\\theta \\times \\sec\\theta = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：直接得出答案",
                "content": "$\\cos 35^\\circ \\times \\sec 35^\\circ = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="60" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e40af">cos 35° · sec 35°</text>
  <text x="190" y="110" text-anchor="middle" font-size="16" fill="#dc2626">利用倒數關係：cos θ · sec θ = 1</text>
  <text x="190" y="160" text-anchor="middle" font-size="26" font-weight="bold" fill="#b91c1c">= 1</text>
</svg>"""
    },
    {
        "id": 30,
        "tag": "CASE 30",
        "page": "課本 P.120 隨堂 6(2)",
        "category": "恆等關係求值",
        "title": "隨堂練習 6(2)：同角正餘弦平方和求值",
        "front_content": "試求下列各式之值：<br>$$\\sin^2 80^\\circ + \\cos^2 80^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：無論角度是多少度，只要角度相同，正餘弦平方相加永遠是 1！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：辨識同角平方關係",
                "content": "角度皆為 $80^\\circ$。由 $\\sin^2\\theta + \\cos^2\\theta = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：直接得出答案",
                "content": "$\\sin^2 80^\\circ + \\cos^2 80^\\circ = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="60" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e40af">sin² 80° + cos² 80°</text>
  <text x="190" y="110" text-anchor="middle" font-size="16" fill="#dc2626">利用平方關係：sin²θ + cos²θ = 1</text>
  <text x="190" y="160" text-anchor="middle" font-size="26" font-weight="bold" fill="#b91c1c">= 1</text>
</svg>"""
    }
]
