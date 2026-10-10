# -*- coding: utf-8 -*-
"""
cards_part2.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
圖解學習卡資料集 Part 2 (CASE 31 ~ CASE 60)
遵循 SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版：
- 堅持「一題一卡、一小題獨立成卡」
- 課本例題、隨堂與全套習題（是非、基礎、進階）100% 忠實原文
- 全欄位 100% KaTeX 標準數學式（全域 145% 渲染）
- 正面無水平捲軸，適度 <br> 換行
- 2~4 步結構化思維導引（名偵探推理筆記 ‧ 線索推理鏈）
- 高解析標準 SVG 向量幾何圖解
"""

CARDS_PART2 = [
    # ==========================================
    # 延續階段三：恆等關係深入篇 (CASE 31 ~ 35)
    # ==========================================
    {
        "id": 31,
        "tag": "CASE 31",
        "page": "課本 P.120 隨堂 6(3)",
        "category": "恆等關係求值",
        "title": "隨堂練習 6(3)：餘切與餘割平方差求值",
        "front_content": "試求下列各式之值：<br>$$\\cot^2 12^\\circ - \\csc^2 12^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：小心符號陷阱！平方關係是 $1 + \\cot^2\\theta = \\csc^2\\theta$，移項時是 $\\cot^2\\theta - \\csc^2\\theta = -1$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用餘切餘割平方公式",
                "content": "利用平方關係：$1 + \\cot^2 12^\\circ = \\csc^2 12^\\circ$。"
            },
            {
                "num": 2,
                "title": "線索 2：精確移項注意正負號",
                "content": "將 $\\csc^2 12^\\circ$ 移至左邊，常數 $1$ 移至右邊，得 $\\cot^2 12^\\circ - \\csc^2 12^\\circ = -1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $-1$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="55" text-anchor="middle" font-size="20" font-weight="bold" fill="#1e40af">cot² 12° - csc² 12°</text>
  <text x="190" y="105" text-anchor="middle" font-size="16" fill="#dc2626">因為 1 + cot²θ = csc²θ  ⇒  cot²θ - csc²θ = -1</text>
  <text x="190" y="160" text-anchor="middle" font-size="26" font-weight="bold" fill="#b91c1c">= -1</text>
</svg>"""
    },
    {
        "id": 32,
        "tag": "CASE 32",
        "page": "課本 P.120 例題 7",
        "category": "餘角綜合化簡",
        "title": "例題 7：餘角轉化與恆等混合求值",
        "front_content": "試求下列各式之值：<br>$$\\tan 40^\\circ \\tan 50^\\circ + \\tan^2 72^\\circ - \\csc^2 18^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：雙重餘角偵查！$40^\\circ+50^\\circ=90^\\circ \\implies \\tan 50^\\circ = \\cot 40^\\circ$！$18^\\circ+72^\\circ=90^\\circ \\implies \\csc 18^\\circ = \\sec 72^\\circ$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：餘角關係換裝",
                "content": "$\\tan 50^\\circ = \\cot 40^\\circ$ ； $\\csc 18^\\circ = \\sec 72^\\circ \\implies \\csc^2 18^\\circ = \\sec^2 72^\\circ$。"
            },
            {
                "num": 2,
                "title": "線索 2：分段代換原式",
                "content": "第一部分：$\\tan 40^\\circ \\cot 40^\\circ = 1$。<br>第二部分：$\\tan^2 72^\\circ - \\sec^2 72^\\circ = -1$（由 $1 + \\tan^2 = \\sec^2$ 移項）。"
            },
            {
                "num": 3,
                "title": "線索 3：兩段相加真相大白",
                "content": "原式 $= 1 + (-1) = 0$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $0$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">tan 40° tan 50° + tan² 72° - csc² 18°</text>
  <rect x="50" y="70" width="120" height="50" rx="8" fill="#e0e7ff"/>
  <text x="110" y="100" text-anchor="middle" font-size="14" fill="#3730a3">tan 40° cot 40° = 1</text>
  <text x="190" y="100" text-anchor="middle" font-size="20" fill="#475569">+</text>
  <rect x="210" y="70" width="120" height="50" rx="8" fill="#fee2e2"/>
  <text x="270" y="100" text-anchor="middle" font-size="14" fill="#991b1b">tan² 72° - sec² 72° = -1</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 1 + (-1) = 0</text>
</svg>"""
    },
    {
        "id": 33,
        "tag": "CASE 33",
        "page": "課本 P.120 隨堂 7",
        "category": "餘角綜合化簡",
        "title": "隨堂練習 7：餘角平方和與平方差混合求值",
        "front_content": "試求下列各式之值：<br>$$\\cos^2 35^\\circ + \\cos^2 55^\\circ + \\csc^2 47^\\circ - \\tan^2 43^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：鎖定餘角配對：$35^\\circ+55^\\circ=90^\\circ \\implies \\cos 55^\\circ = \\sin 35^\\circ$；$47^\\circ+43^\\circ=90^\\circ \\implies \\tan 43^\\circ = \\cot 47^\\circ$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：第一組餘角平方和",
                "content": "$\\cos 55^\\circ = \\sin 35^\\circ \\implies \\cos^2 35^\\circ + \\cos^2 55^\\circ = \\cos^2 35^\\circ + \\sin^2 35^\\circ = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：第二組餘角平方差",
                "content": "$\\tan 43^\\circ = \\cot 47^\\circ \\implies \\csc^2 47^\\circ - \\tan^2 43^\\circ = \\csc^2 47^\\circ - \\cot^2 47^\\circ = 1$（由 $1 + \\cot^2 = \\csc^2$）。"
            },
            {
                "num": 3,
                "title": "線索 3：合併兩部分",
                "content": "原式 $= 1 + 1 = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $2$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="15" font-weight="bold" fill="#1e40af">cos² 35° + cos² 55° + csc² 47° - tan² 43°</text>
  <rect x="50" y="70" width="120" height="50" rx="8" fill="#e0e7ff"/>
  <text x="110" y="100" text-anchor="middle" font-size="14" fill="#3730a3">cos² 35° + sin² 35° = 1</text>
  <text x="190" y="100" text-anchor="middle" font-size="20" fill="#475569">+</text>
  <rect x="210" y="70" width="120" height="50" rx="8" fill="#fef3c7"/>
  <text x="270" y="100" text-anchor="middle" font-size="14" fill="#92400e">csc² 47° - cot² 47° = 1</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 1 + 1 = 2</text>
</svg>"""
    },
    {
        "id": 34,
        "tag": "CASE 34",
        "page": "課本 P.121 例題 8",
        "category": "齊次商數轉化",
        "title": "例題 8：已知 tan θ = 2，求一次齊次分式之值",
        "front_content": "已知 $\\theta$ 為銳角，且 $\\tan\\theta = 2$。<br>試求下列分式之值：<br>$$\\frac{\\sin\\theta + 2\\cos\\theta}{3\\sin\\theta - \\cos\\theta}$$",
        "front_tip": "🕵️ 柯南破案導引：齊次式神技！分子分母同除以 $\\cos\\theta$，立刻將全部 $\\sin\\theta$ 轉化為 $\\tan\\theta$！完全不必求斜邊！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分子分母同除以 cos θ",
                "content": "原式 $= \\frac{\\frac{\\sin\\theta}{\\cos\\theta} + 2}{\\frac{3\\sin\\theta}{\\cos\\theta} - 1} = \\frac{\\tan\\theta + 2}{3\\tan\\theta - 1}$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入 tan θ = 2 計算",
                "content": "原式 $= \\frac{2 + 2}{3(2) - 1} = \\frac{4}{6 - 1} = \\frac{4}{5}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】分式之值為 $\\frac{4}{5}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">齊次式同除 cos θ 神技</text>
  <rect x="50" y="60" width="280" height="50" rx="8" fill="#fef3c7"/>
  <text x="190" y="90" text-anchor="middle" font-size="15" font-weight="bold" fill="#b45309">分子分母 ÷ cos θ  ⇒  (tan θ + 2) / (3 tan θ - 1)</text>
  <text x="190" y="155" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= (2 + 2) / (6 - 1) = 4/5</text>
</svg>"""
    },
    {
        "id": 35,
        "tag": "CASE 35",
        "page": "課本 P.121 隨堂 8",
        "category": "齊次商數轉化",
        "title": "隨堂練習 8：已知 cot θ = 2/3，求一次齊次分式之值",
        "front_content": "已知 $\\theta$ 為銳角，且 $\\cot\\theta = \\frac{2}{3}$。<br>試求下列分式之值：<br>$$\\frac{\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 6\\cos\\theta}$$",
        "front_tip": "🕵️ 柯南破案導引：法一：分子分母同除以 $\\sin\\theta$ 轉化為 $\\cot\\theta$！法二：由 $\\cot\\theta = \\frac{2}{3} \\implies \\tan\\theta = \\frac{3}{2}$，同除 $\\cos\\theta$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分子分母同除以 sin θ",
                "content": "原式 $= \\frac{1 - 3\\left(\\frac{\\cos\\theta}{\\sin\\theta}\\right)}{5 + 6\\left(\\frac{\\cos\\theta}{\\sin\\theta}\\right)} = \\frac{1 - 3\\cot\\theta}{5 + 6\\cot\\theta}$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入 cot θ = 2/3 計算",
                "content": "分子 $= 1 - 3\\left(\\frac{2}{3}\\right) = 1 - 2 = -1$。<br>分母 $= 5 + 6\\left(\\frac{2}{3}\\right) = 5 + 4 = 9$。"
            },
            {
                "num": 3,
                "title": "線索 3：求得分式之值",
                "content": "原式 $= \\frac{-1}{9} = -\\frac{1}{9}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】分式之值為 $-\\frac{1}{9}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">同除 sin θ 化為 cot θ 破案</text>
  <rect x="60" y="60" width="260" height="50" rx="8" fill="#e0e7ff"/>
  <text x="190" y="90" text-anchor="middle" font-size="15" font-weight="bold" fill="#3730a3">(1 - 3 cot θ) / (5 + 6 cot θ)</text>
  <text x="190" y="155" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= (1 - 2) / (5 + 4) = -1/9</text>
</svg>"""
    },

    # ==========================================
    # 階段四：三角恆等式核心篇 (CASE 36 ~ 40)
    # ==========================================
    {
        "id": 36,
        "tag": "CASE 36",
        "page": "課本 P.121 概念",
        "category": "三角恆等式推導",
        "title": "常用三角恆等式三大核心架構推導",
        "front_content": "三大必備三角恆等式：<br>(1) $(\\sin\\theta + \\cos\\theta)^2 = 1 + 2\\sin\\theta\\cos\\theta$<br>(2) $(\\sin\\theta - \\cos\\theta)^2 = 1 - 2\\sin\\theta\\cos\\theta$<br>(3) $\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$",
        "front_tip": "🕵️ 柯南破案導引：展開和差平方：$\\sin^2 + \\cos^2 = 1$，交叉項為 $\\pm 2\\sin\\cos$！正切加餘切通分後分子也是 $1$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：和差平方展開證明",
                "content": "$(\\sin\\theta \\pm \\cos\\theta)^2 = \\sin^2\\theta \\pm 2\\sin\\theta\\cos\\theta + \\cos^2\\theta = (\\sin^2\\theta + \\cos^2\\theta) \\pm 2\\sin\\theta\\cos\\theta = 1 \\pm 2\\sin\\theta\\cos\\theta$。"
            },
            {
                "num": 2,
                "title": "線索 2：tan + cot 通分證明",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{\\sin\\theta}{\\cos\\theta} + \\frac{\\cos\\theta}{\\sin\\theta} = \\frac{\\sin^2\\theta + \\cos^2\\theta}{\\sin\\theta\\cos\\theta} = \\frac{1}{\\sin\\theta\\cos\\theta}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】見和差必平方、見 tan+cot 必通分倒數！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="35" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">三大核心三角恆等式架構</text>
  <rect x="40" y="55" width="300" height="38" rx="6" fill="#fee2e2"/>
  <text x="190" y="80" text-anchor="middle" font-size="14" font-weight="bold" fill="#991b1b">(sin θ ± cos θ)² = 1 ± 2 sin θ cos θ</text>
  <rect x="40" y="105" width="300" height="38" rx="6" fill="#fef3c7"/>
  <text x="190" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#92400e">tan θ + cot θ = 1 / (sin θ cos θ)</text>
</svg>"""
    },
    {
        "id": 37,
        "tag": "CASE 37",
        "page": "課本 P.122 例題 9(1)",
        "category": "恆等式求乘積",
        "title": "例題 9(1)：已知 sin θ + cos θ = 4/3，求 sin θ cos θ",
        "front_content": "已知 $\\theta$ 為銳角，若 $\\sin\\theta + \\cos\\theta = \\frac{4}{3}$。<br>試求：<br>$$\\sin\\theta \\cos\\theta$$",
        "front_tip": "🕵️ 柯南破案導引：見和必平方！等式兩邊同時平方，利用 $(\\sin\\theta+\\cos\\theta)^2 = 1 + 2\\sin\\theta\\cos\\theta$ 破案！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：兩邊同時平方",
                "content": "$(\\sin\\theta + \\cos\\theta)^2 = \\left(\\frac{4}{3}\\right)^2 = \\frac{16}{9}$。"
            },
            {
                "num": 2,
                "title": "線索 2：展開恆等式求 2sin cos",
                "content": "$1 + 2\\sin\\theta\\cos\\theta = \\frac{16}{9} \\implies 2\\sin\\theta\\cos\\theta = \\frac{16}{9} - 1 = \\frac{7}{9}$。"
            },
            {
                "num": 3,
                "title": "線索 3：兩邊同除以 2",
                "content": "$\\sin\\theta\\cos\\theta = \\frac{7}{9} \\div 2 = \\frac{7}{18}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin\\theta\\cos\\theta = \\frac{7}{18}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">和平方導出乘積</text>
  <text x="190" y="80" text-anchor="middle" font-size="15" fill="#475569">(sin θ + cos θ)² = 1 + 2 sin θ cos θ = 16/9</text>
  <text x="190" y="115" text-anchor="middle" font-size="15" fill="#dc2626">2 sin θ cos θ = 16/9 - 1 = 7/9</text>
  <text x="190" y="160" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">sin θ cos θ = 7/18</text>
</svg>"""
    },
    {
        "id": 38,
        "tag": "CASE 38",
        "page": "課本 P.122 例題 9(2)",
        "category": "恆等式求切和",
        "title": "例題 9(2)：已知 sin θ + cos θ = 4/3，求 tan θ + cot θ",
        "front_content": "已知 $\\theta$ 為銳角，若 $\\sin\\theta + \\cos\\theta = \\frac{4}{3}$。<br>承上題（已求得 $\\sin\\theta\\cos\\theta = \\frac{7}{18}$），<br>試求：<br>$$\\tan\\theta + \\cot\\theta$$",
        "front_tip": "🕵️ 柯南破案導引：調用恆等式 $\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$，直接取上一題答案的倒數！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用切和恆等轉化式",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入已求得乘積值",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{1}{\\frac{7}{18}} = \\frac{18}{7}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\tan\\theta + \\cot\\theta = \\frac{18}{7}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="50" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">tan θ + cot θ 倒數秒解</text>
  <rect x="70" y="75" width="240" height="50" rx="8" fill="#fef3c7"/>
  <text x="190" y="106" text-anchor="middle" font-size="16" font-weight="bold" fill="#b45309">1 / (sin θ cos θ) = 1 / (7/18)</text>
  <text x="190" y="165" text-anchor="middle" font-size="24" font-weight="bold" fill="#b91c1c">= 18/7</text>
</svg>"""
    },
    {
        "id": 39,
        "tag": "CASE 39",
        "page": "課本 P.122 隨堂 9(1)",
        "category": "恆等式求差平方",
        "title": "隨堂練習 9(1)：已知 sin θ - cos θ = 3/5，求 sin θ cos θ",
        "front_content": "已知 $\\theta$ 為銳角，若 $\\sin\\theta - \\cos\\theta = \\frac{3}{5}$。<br>試求：<br>$$\\sin\\theta \\cos\\theta$$",
        "front_tip": "🕵️ 柯南破案導引：見差亦平方！$(\\sin\\theta - \\cos\\theta)^2 = 1 - 2\\sin\\theta\\cos\\theta$！注意負號移項！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：兩邊同時平方",
                "content": "$(\\sin\\theta - \\cos\\theta)^2 = \\left(\\frac{3}{5}\\right)^2 = \\frac{9}{25}$。"
            },
            {
                "num": 2,
                "title": "線索 2：利用差平方公式展開",
                "content": "$1 - 2\\sin\\theta\\cos\\theta = \\frac{9}{25} \\implies 2\\sin\\theta\\cos\\theta = 1 - \\frac{9}{25} = \\frac{16}{25}$。"
            },
            {
                "num": 3,
                "title": "線索 3：同除以 2 結案",
                "content": "$\\sin\\theta\\cos\\theta = \\frac{16}{25} \\div 2 = \\frac{8}{25}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin\\theta\\cos\\theta = \\frac{8}{25}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">差平方導出乘積</text>
  <text x="190" y="80" text-anchor="middle" font-size="15" fill="#475569">(sin θ - cos θ)² = 1 - 2 sin θ cos θ = 9/25</text>
  <text x="190" y="115" text-anchor="middle" font-size="15" fill="#dc2626">2 sin θ cos θ = 1 - 9/25 = 16/25</text>
  <text x="190" y="160" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">sin θ cos θ = 8/25</text>
</svg>"""
    },
    {
        "id": 40,
        "tag": "CASE 40",
        "page": "課本 P.122 隨堂 9(2)",
        "category": "恆等式求切和",
        "title": "隨堂練習 9(2)：已知 sin θ - cos θ = 3/5，求 tan θ + cot θ",
        "front_content": "已知 $\\theta$ 為銳角，若 $\\sin\\theta - \\cos\\theta = \\frac{3}{5}$。<br>承上題（已求得 $\\sin\\theta\\cos\\theta = \\frac{8}{25}$），<br>試求：<br>$$\\tan\\theta + \\cot\\theta$$",
        "front_tip": "🕵️ 柯南破案導引：恆等式 $\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$，取 $\\frac{8}{25}$ 的倒數即答案！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用切和恆等關係",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入乘積倒數求值",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{1}{\\frac{8}{25}} = \\frac{25}{8}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\tan\\theta + \\cot\\theta = \\frac{25}{8}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="50" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">tan θ + cot θ 秒殺倒數</text>
  <rect x="70" y="75" width="240" height="50" rx="8" fill="#e0e7ff"/>
  <text x="190" y="106" text-anchor="middle" font-size="16" font-weight="bold" fill="#3730a3">1 / (sin θ cos θ) = 1 / (8/25)</text>
  <text x="190" y="165" text-anchor="middle" font-size="24" font-weight="bold" fill="#b91c1c">= 25/8</text>
</svg>"""
    },

    # ==========================================
    # 階段五：課後習題 ‧ 觀念釐清是非篇 (CASE 41 ~ 45)
    # ==========================================
    {
        "id": 41,
        "tag": "CASE 41",
        "page": "課本 P.123 觀念 (1)",
        "category": "觀念是非判定",
        "title": "習題 觀念 (1)：已知銳角正弦是否可求其餘五個函數值？",
        "front_content": "試判斷下列敘述之對錯（正確畫「○」，錯誤畫「×」）：<br>「已知 $\\theta$ 為銳角，若已知 $\\sin\\theta$，<br>則可求出剩餘的五個三角函數值。」",
        "front_tip": "🕵️ 柯南破案導引：銳角三角函數只要已知其中一個（如 $\\sin\\theta = \\frac{y}{r}$），利用畢氏定理即可確定三邊比例！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：幾何直角三角形驗證",
                "content": "已知 $\\sin\\theta = \\frac{y}{r}$，可設對邊為 $y$、斜邊為 $r$。由畢氏定理鄰邊 $x = \\sqrt{r^2 - y^2}$ 唯一確定。"
            },
            {
                "num": 2,
                "title": "線索 2：五大函數值均可確定",
                "content": "因此 $\\cos\\theta = \\frac{x}{r}, \\tan\\theta = \\frac{y}{x}, \\cot\\theta = \\frac{x}{y}, \\sec\\theta = \\frac{r}{x}, \\csc\\theta = \\frac{r}{y}$ 均可求出。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確（○）！知一銳角三角比，其餘五個皆能求出！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <circle cx="190" cy="80" r="36" fill="#dcfce7" stroke="#16a34a" stroke-width="3"/>
  <text x="190" y="93" text-anchor="middle" font-size="40" font-weight="bold" fill="#15803d">○</text>
  <text x="190" y="145" text-anchor="middle" font-size="16" font-weight="bold" fill="#166534">已知 sin θ，藉由畢氏定理可推知其餘五個值</text>
</svg>"""
    },
    {
        "id": 42,
        "tag": "CASE 42",
        "page": "課本 P.123 觀念 (2)",
        "category": "觀念是非判定",
        "title": "習題 觀念 (2)：已知 sin A = 3/5 是否可求出三邊長度？",
        "front_content": "試判斷下列敘述之對錯（正確畫「○」，錯誤畫「×」）：<br>「直角三角形 $ABC$ 中，$\\angle C = 90^\\circ$。<br>若 $\\sin A = \\frac{3}{5}$，則可求出 $AB$、$BC$、$CA$ 的長度。」",
        "front_tip": "🕵️ 柯南破案導引：名偵探破案焦點：比例 $\\ne$ 實際長度！三角形可以放大縮小，沒有任何實際邊長條件，無法得知絕對長度！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：三角函數是『比值』而非『長度』",
                "content": "$\\sin A = \\frac{3}{5}$ 只代表邊長比 $BC : AB = 3 : 5$，三邊比為 $3k : 4k : 5k$。"
            },
            {
                "num": 2,
                "title": "線索 2：反例舉證",
                "content": "若 $k = 1$，三邊為 $3, 4, 5$；若 $k = 2$，三邊為 $6, 8, 10$。兩者 $\\sin A$ 皆為 $\\frac{3}{5}$，但實際邊長完全不同！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】錯誤（×）！未給予任何邊長條件，無法求得實際長度！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <circle cx="190" cy="80" r="36" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
  <text x="190" y="93" text-anchor="middle" font-size="40" font-weight="bold" fill="#b91c1c">×</text>
  <text x="190" y="145" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">比值 ≠ 實際長度！只能得知比例 3k : 4k : 5k</text>
</svg>"""
    },
    {
        "id": 43,
        "tag": "CASE 43",
        "page": "課本 P.123 觀念 (3)",
        "category": "觀念是非判定",
        "title": "習題 觀念 (3)：不同銳角平方和是否必等於 1？",
        "front_content": "試判斷下列敘述之對錯（正確畫「○」，錯誤畫「×」）：<br>「若 $\\alpha$、$\\beta$ 為銳角，<br>由平方關係可得 $\\sin^2\\alpha + \\cos^2\\beta = 1$。」",
        "front_tip": "🕵️ 柯南破案導引：防錯避雷針！平方關係 $\\sin^2\\theta + \\cos^2\\theta = 1$ 嚴格限定『角度必須完全相同』！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：平方關係的前提是同角",
                "content": "公式為 $\\sin^2\\theta + \\cos^2\\theta = 1$，角度必須同為 $\\theta$。"
            },
            {
                "num": 2,
                "title": "線索 2：反例擊破",
                "content": "令 $\\alpha = 30^\\circ, \\beta = 60^\\circ$。$\\sin^2 30^\\circ = \\frac{1}{4}$，$\\cos^2 60^\\circ = \\frac{1}{4}$。$\\frac{1}{4} + \\frac{1}{4} = \\frac{1}{2} \\ne 1$！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】錯誤（×）！角 $\\alpha \\ne \\beta$ 時，平方和不保證等於 1！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <circle cx="190" cy="80" r="36" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
  <text x="190" y="93" text-anchor="middle" font-size="40" font-weight="bold" fill="#b91c1c">×</text>
  <text x="190" y="145" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">平方關係限定同角！α 與 β 不同角不成立！</text>
</svg>"""
    },
    {
        "id": 44,
        "tag": "CASE 44",
        "page": "課本 P.123 觀念 (4)",
        "category": "觀念是非判定",
        "title": "習題 觀念 (4)：銳角 sin θ × cos θ 是否必等於 1？",
        "front_content": "試判斷下列敘述之對錯（正確畫「○」，錯誤畫「×」）：<br>「若 $\\theta$ 為銳角，<br>則 $\\sin\\theta \\times \\cos\\theta = 1$。」",
        "front_tip": "🕵️ 柯南破案導引：混淆倒數伴侶！倒數為 1 的是 $\\sin\\theta \\times \\csc\\theta = 1$；$\\sin$ 與 $\\cos$ 乘積絕不等於 1！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：辨識倒數關係的正確認知",
                "content": "倒數關係是 $\\sin\\theta \\times \\csc\\theta = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：反例檢驗",
                "content": "若 $\\theta = 30^\\circ$，$\\sin 30^\\circ \\times \\cos 30^\\circ = \\frac{1}{2} \\times \\frac{\\sqrt{3}}{2} = \\frac{\\sqrt{3}}{4} \\ne 1$！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】錯誤（×）！正弦與餘弦乘積不等於 1！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <circle cx="190" cy="80" r="36" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
  <text x="190" y="93" text-anchor="middle" font-size="40" font-weight="bold" fill="#b91c1c">×</text>
  <text x="190" y="145" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">倒數關係是 sin · csc = 1，不是 sin · cos = 1！</text>
</svg>"""
    },
    {
        "id": 45,
        "tag": "CASE 45",
        "page": "課本 P.123 觀念 (5)",
        "category": "觀念是非判定",
        "title": "習題 觀念 (5)：和平方展開是否可省略交叉項？",
        "front_content": "試判斷下列敘述之對錯（正確畫「○」，錯誤畫「×」）：<br>「若 $\\theta$ 為銳角，<br>則 $(\\sin\\theta + \\cos\\theta)^2 = \\sin^2\\theta + \\cos^2\\theta = 1$。」",
        "front_tip": "🕵️ 柯南破案導引：經典致命漏洞！$(a+b)^2 = a^2 + 2ab + b^2$！遺漏了關鍵的交叉項 $2\\sin\\theta\\cos\\theta$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：乘法公式嚴密展開",
                "content": "$(\\sin\\theta + \\cos\\theta)^2 = \\sin^2\\theta + 2\\sin\\theta\\cos\\theta + \\cos^2\\theta = 1 + 2\\sin\\theta\\cos\\theta$。"
            },
            {
                "num": 2,
                "title": "線索 2：銳角乘積必大於 0",
                "content": "當 $\\theta$ 為銳角時，$\\sin\\theta > 0, \\cos\\theta > 0$，故 $2\\sin\\theta\\cos\\theta > 0$。因此原式必大於 1，不可能等於 1！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】錯誤（×）！和平方展開必須包含交叉項 $2\\sin\\theta\\cos\\theta$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <circle cx="190" cy="80" r="36" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
  <text x="190" y="93" text-anchor="middle" font-size="40" font-weight="bold" fill="#b91c1c">×</text>
  <text x="190" y="145" text-anchor="middle" font-size="16" font-weight="bold" fill="#991b1b">遺漏交叉項！(sin+cos)² = 1 + 2sin·cos ≠ 1</text>
</svg>"""
    },

    # ==========================================
    # 階段六：課後習題 ‧ 基礎與進階篇 (CASE 46 ~ 60)
    # ==========================================
    {
        "id": 46,
        "tag": "CASE 46",
        "page": "課本 P.123 基礎 1",
        "category": "基礎實戰求值",
        "title": "基礎題 1：已知直角三角形 sin A = 3/5，求 tan A + sec A",
        "front_content": "已知直角三角形 $ABC$ 中，$\\angle C$ 為直角，<br>$\\sin A = \\frac{3}{5}$。<br>試求：<br>$$\\tan A + \\sec A$$",
        "front_tip": "🕵️ 柯南破案導引：由 $\\sin A = \\frac{3}{5}$，知直角三角形三邊為 3-4-5！對邊 3、鄰邊 4、斜邊 5！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：畢氏定理求鄰邊",
                "content": "斜邊 $r = 5$，對邊 $y = 3$，鄰邊 $x = \\sqrt{5^2 - 3^2} = 4$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算 tan A 與 sec A",
                "content": "$\\tan A = \\frac{\\text{對}}{\\text{鄰}} = \\frac{3}{4}$ ； $\\sec A = \\frac{\\text{斜}}{\\text{鄰}} = \\frac{5}{4}$。"
            },
            {
                "num": 3,
                "title": "線索 3：兩者相加結案",
                "content": "$\\tan A + \\sec A = \\frac{3}{4} + \\frac{5}{4} = \\frac{8}{4} = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\tan A + \\sec A = 2$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">tan A + sec A 求值</text>
  <text x="190" y="90" text-anchor="middle" font-size="16" fill="#475569">tan A = 3/4   ,   sec A = 5/4</text>
  <text x="190" y="125" text-anchor="middle" font-size="18" fill="#dc2626">3/4 + 5/4 = 8/4 = 2</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 2</text>
</svg>"""
    },
    {
        "id": 47,
        "tag": "CASE 47",
        "page": "課本 P.123 基礎 2(1)",
        "category": "基礎實戰求值",
        "title": "基礎題 2(1)：tan A = 12/5 且 AB = 26，求 sin A",
        "front_content": "直角三角形 $ABC$ 中，$\\angle C$ 為直角，且 $\\tan A = \\frac{12}{5}$。<br>若 $AB = 26$，<br>試求：<br>$$\\sin A$$",
        "front_tip": "🕵️ 柯南破案導引：$\\tan A = \\frac{12}{5}$，形成 5-12-13 比例！求 $\\sin A$ 只看比例，與實際長度無關！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：由正切比確定三邊比例",
                "content": "對邊 $BC = 12k$，鄰邊 $AC = 5k$。斜邊 $AB = \\sqrt{(12k)^2 + (5k)^2} = 13k$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算正弦值",
                "content": "$\\sin A = \\frac{\\text{對邊}}{\\text{斜邊}} = \\frac{12k}{13k} = \\frac{12}{13}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin A = \\frac{12}{13}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <polygon points="60,165 240,165 240,40" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="45" y="172" font-size="14" font-weight="bold" fill="#b45309">A</text>
  <text x="140" y="184" font-size="13" font-weight="bold" fill="#1e40af">鄰 = 5k</text>
  <text x="255" y="105" font-size="13" font-weight="bold" fill="#dc2626">對 = 12k</text>
  <text x="120" y="95" font-size="13" font-weight="bold" fill="#15803d">斜 = 13k = 26</text>
  <text x="190" y="25" text-anchor="middle" font-size="14" font-weight="bold" fill="#b91c1c">sin A = 12k / 13k = 12/13</text>
</svg>"""
    },
    {
        "id": 48,
        "tag": "CASE 48",
        "page": "課本 P.123 基礎 2(2)",
        "category": "基礎實戰求長",
        "title": "基礎題 2(2)：tan A = 12/5 且 AB = 26，求邊長 AC",
        "front_content": "直角三角形 $ABC$ 中，$\\angle C$ 為直角，且 $\\tan A = \\frac{12}{5}$。<br>若 $AB = 26$，<br>試求邊長：<br>$$AC$$",
        "front_tip": "🕵️ 柯南破案導引：比例斜邊為 $13k$，實際長度 $AB = 26$，立即可解出放大倍率 $k = 2$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：由斜邊求放大參數 k",
                "content": "斜邊 $AB = 13k = 26 \\implies k = 2$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算實際邊長 AC",
                "content": "鄰邊 $AC = 5k = 5 \\times 2 = 10$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】邊長 $AC = 10$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">邊長 AC 比例放大推算</text>
  <text x="190" y="90" text-anchor="middle" font-size="16" fill="#475569">斜邊 AB = 13k = 26  ⇒  k = 2</text>
  <text x="190" y="125" text-anchor="middle" font-size="18" fill="#dc2626">AC = 5k = 5 × 2 = 10</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 10</text>
</svg>"""
    },
    {
        "id": 49,
        "tag": "CASE 49",
        "page": "課本 P.123 基礎 3(1)",
        "category": "特別角運算",
        "title": "基礎題 3(1)：特別角四則運算求值",
        "front_content": "試求下列各式之值：<br>$$4 \\sin^2 30^\\circ + 2 \\tan 45^\\circ + \\frac{1}{3} \\cot^2 30^\\circ \\times \\sec^2 60^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：逐步提取：$\\sin 30^\\circ = \\frac{1}{2}$，$\\tan 45^\\circ = 1$，$\\cot 30^\\circ = \\sqrt{3}$，$\\sec 60^\\circ = 2$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：第一部分 4 sin² 30°",
                "content": "$4 \\times \\left(\\frac{1}{2}\\right)^2 = 4 \\times \\frac{1}{4} = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：第二部分 2 tan 45°",
                "content": "$2 \\times 1 = 2$。"
            },
            {
                "num": 3,
                "title": "線索 3：第三部分 1/3 cot² 30° · sec² 60°",
                "content": "$\\frac{1}{3} \\times (\\sqrt{3})^2 \\times 2^2 = \\frac{1}{3} \\times 3 \\times 4 = 4$。"
            },
            {
                "num": 4,
                "title": "線索 4：三項相加結案",
                "content": "原式 $= 1 + 2 + 4 = 7$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $7$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="15" font-weight="bold" fill="#1e40af">4 sin² 30° + 2 tan 45° + (1/3) cot² 30° · sec² 60°</text>
  <text x="100" y="95" text-anchor="middle" font-size="18" fill="#dc2626">1</text>
  <text x="150" y="95" text-anchor="middle" font-size="18" fill="#475569">+</text>
  <text x="190" y="95" text-anchor="middle" font-size="18" fill="#2563eb">2</text>
  <text x="230" y="95" text-anchor="middle" font-size="18" fill="#475569">+</text>
  <text x="270" y="95" text-anchor="middle" font-size="18" fill="#16a34a">4</text>
  <text x="190" y="155" text-anchor="middle" font-size="24" font-weight="bold" fill="#b91c1c">= 1 + 2 + 4 = 7</text>
</svg>"""
    },
    {
        "id": 50,
        "tag": "CASE 50",
        "page": "課本 P.123 基礎 3(2)",
        "category": "特別角運算",
        "title": "基礎題 3(2)：弳度特別角乘積求值",
        "front_content": "試求下列各式之值：<br>$$\\left(1 + 2\\sin\\frac{\\pi}{6} + \\cos\\frac{\\pi}{4}\\right)\\left(1 - \\sin\\frac{\\pi}{4} + 2\\cos\\frac{\\pi}{3}\\right)$$",
        "front_tip": "🕵️ 柯南破案導引：$\\frac{\\pi}{6} = 30^\\circ$、$\\frac{\\pi}{4} = 45^\\circ$、$\\frac{\\pi}{3} = 60^\\circ$！化簡兩括號後再相乘！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：第一括號化簡",
                "content": "$1 + 2\\sin 30^\\circ + \\cos 45^\\circ = 1 + 2\\left(\\frac{1}{2}\\right) + \\frac{\\sqrt{2}}{2} = 1 + 1 + \\frac{\\sqrt{2}}{2} = 2 + \\frac{\\sqrt{2}}{2}$。"
            },
            {
                "num": 2,
                "title": "線索 2：第二括號化簡",
                "content": "$1 - \\sin 45^\\circ + 2\\cos 60^\\circ = 1 - \\frac{\\sqrt{2}}{2} + 2\\left(\\frac{1}{2}\\right) = 1 - \\frac{\\sqrt{2}}{2} + 1 = 2 - \\frac{\\sqrt{2}}{2}$。"
            },
            {
                "num": 3,
                "title": "線索 3：平方差公式展開",
                "content": "原式 $= \\left(2 + \\frac{\\sqrt{2}}{2}\\right)\\left(2 - \\frac{\\sqrt{2}}{2}\\right) = 2^2 - \\left(\\frac{\\sqrt{2}}{2}\\right)^2 = 4 - \\frac{2}{4} = 4 - \\frac{1}{2} = \\frac{7}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $\\frac{7}{2}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="15" font-weight="bold" fill="#1e40af">利用平方差 (a + b)(a - b) = a² - b²</text>
  <text x="190" y="85" text-anchor="middle" font-size="16" fill="#475569">[ 2 + (√2/2) ] · [ 2 - (√2/2) ]</text>
  <text x="190" y="125" text-anchor="middle" font-size="17" fill="#dc2626">= 2² - (√2/2)² = 4 - 1/2</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 7/2</text>
</svg>"""
    },
    {
        "id": 51,
        "tag": "CASE 51",
        "page": "課本 P.124 基礎 4",
        "category": "餘角平方混合",
        "title": "基礎題 4：餘角與平方關係綜合求值",
        "front_content": "試求下列各式之值：<br>$$\\cos^2 20^\\circ + \\cos^2 70^\\circ + \\tan^2 20^\\circ - \\csc^2 70^\\circ$$",
        "front_tip": "🕵️ 柯南破案導引：餘角配對：$\\cos 70^\\circ = \\sin 20^\\circ$；$\\csc 70^\\circ = \\sec 20^\\circ$！全部化為 $20^\\circ$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：全數轉化為 20°",
                "content": "$\\cos 70^\\circ = \\sin 20^\\circ \\implies \\cos^2 70^\\circ = \\sin^2 20^\\circ$。<br>$\\csc 70^\\circ = \\sec 20^\\circ \\implies \\csc^2 70^\\circ = \\sec^2 20^\\circ$。"
            },
            {
                "num": 2,
                "title": "線索 2：分組利用平方關係",
                "content": "第一組：$\\cos^2 20^\\circ + \\sin^2 20^\\circ = 1$。<br>第二組：$\\tan^2 20^\\circ - \\sec^2 20^\\circ = -1$（由 $1 + \\tan^2 = \\sec^2$）。"
            },
            {
                "num": 3,
                "title": "線索 3：兩組合併結案",
                "content": "原式 $= 1 + (-1) = 0$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $0$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="15" font-weight="bold" fill="#1e40af">cos² 20° + cos² 70° + tan² 20° - csc² 70°</text>
  <rect x="50" y="65" width="120" height="50" rx="8" fill="#e0e7ff"/>
  <text x="110" y="95" text-anchor="middle" font-size="14" fill="#3730a3">cos² 20° + sin² 20° = 1</text>
  <text x="190" y="95" text-anchor="middle" font-size="20" fill="#475569">+</text>
  <rect x="210" y="65" width="120" height="50" rx="8" fill="#fee2e2"/>
  <text x="270" y="95" text-anchor="middle" font-size="14" fill="#991b1b">tan² 20° - sec² 20° = -1</text>
  <text x="190" y="155" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 1 + (-1) = 0</text>
</svg>"""
    },
    {
        "id": 52,
        "tag": "CASE 52",
        "page": "課本 P.124 基礎 5",
        "category": "恆等式求值",
        "title": "基礎題 5：和平方加差平方之化簡",
        "front_content": "試求下列各式之值：<br>$$\\left(\\sin\\frac{\\pi}{5} + \\cos\\frac{\\pi}{5}\\right)^2 + \\left(\\sin\\frac{\\pi}{5} - \\cos\\frac{\\pi}{5}\\right)^2$$",
        "front_tip": "🕵️ 柯南破案導引：令 $\\theta = \\frac{\\pi}{5}$！展開後 $(1 + 2\\sin\\cos) + (1 - 2\\sin\\cos)$，交叉項完美抵消！根本無需知道 $\\frac{\\pi}{5}$ 是幾度！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：展開兩平方括號",
                "content": "$(\\sin\\theta + \\cos\\theta)^2 = 1 + 2\\sin\\theta\\cos\\theta$ ； $(\\sin\\theta - \\cos\\theta)^2 = 1 - 2\\sin\\theta\\cos\\theta$。"
            },
            {
                "num": 2,
                "title": "線索 2：交叉項相互抵消",
                "content": "原式 $= (1 + 2\\sin\\theta\\cos\\theta) + (1 - 2\\sin\\theta\\cos\\theta) = 1 + 1 = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $2$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">(sin θ + cos θ)² + (sin θ - cos θ)²</text>
  <text x="190" y="90" text-anchor="middle" font-size="15" fill="#475569">= (1 + 2 sin θ cos θ) + (1 - 2 sin θ cos θ)</text>
  <text x="190" y="125" text-anchor="middle" font-size="16" fill="#dc2626">交叉項相互抵消：+2sin·cos 與 -2sin·cos</text>
  <text x="190" y="165" text-anchor="middle" font-size="24" font-weight="bold" fill="#b91c1c">= 1 + 1 = 2</text>
</svg>"""
    },
    {
        "id": 53,
        "tag": "CASE 53",
        "page": "課本 P.124 基礎 6",
        "category": "齊次商數轉化",
        "title": "基礎題 6：已知 cot θ = 5/12，求齊次分式之值",
        "front_content": "若 $\\theta$ 為銳角，且 $\\cot\\theta = \\frac{5}{12}$。<br>試求：<br>$$\\frac{5\\sin\\theta - 4\\cos\\theta}{5\\sin\\theta + 3\\cos\\theta}$$",
        "front_tip": "🕵️ 柯南破案導引：齊次式同除神法！分子分母同除以 $\\sin\\theta$，立即化為 $\\cot\\theta$ 代入！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分子分母同除以 sin θ",
                "content": "原式 $= \\frac{5 - 4\\left(\\frac{\\cos\\theta}{\\sin\\theta}\\right)}{5 + 3\\left(\\frac{\\cos\\theta}{\\sin\\theta}\\right)} = \\frac{5 - 4\\cot\\theta}{5 + 3\\cot\\theta}$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入 cot θ = 5/12 計算",
                "content": "分子 $= 5 - 4\\left(\\frac{5}{12}\\right) = 5 - \\frac{5}{3} = \\frac{10}{3}$。<br>分母 $= 5 + 3\\left(\\frac{5}{12}\\right) = 5 + \\frac{5}{4} = \\frac{25}{4}$。"
            },
            {
                "num": 3,
                "title": "線索 3：分式相除化簡",
                "content": "原式 $= \\frac{10/3}{25/4} = \\frac{10}{3} \\times \\frac{4}{25} = \\frac{2 \\times 4}{3 \\times 5} = \\frac{8}{15}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】分式之值為 $\\frac{8}{15}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">同除 sin θ 化為 cot θ</text>
  <text x="190" y="80" text-anchor="middle" font-size="15" fill="#475569">[ 5 - 4(5/12) ] / [ 5 + 3(5/12) ]</text>
  <text x="190" y="115" text-anchor="middle" font-size="16" fill="#dc2626">= (10/3) / (25/4) = (10/3) · (4/25)</text>
  <text x="190" y="160" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 8/15</text>
</svg>"""
    },
    {
        "id": 54,
        "tag": "CASE 54",
        "page": "課本 P.124 基礎 7(1)",
        "category": "恆等式求乘積",
        "title": "基礎題 7(1)：已知 sin θ - cos θ = 1/2，求 sin θ cos θ",
        "front_content": "已知 $\\sin\\theta - \\cos\\theta = \\frac{1}{2}$。<br>試求：<br>$$\\sin\\theta \\cdot \\cos\\theta$$",
        "front_tip": "🕵️ 柯南破案導引：見差必平方！$(\\sin\\theta - \\cos\\theta)^2 = 1 - 2\\sin\\theta\\cos\\theta = \\left(\\frac{1}{2}\\right)^2 = \\frac{1}{4}$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：兩邊平方展開",
                "content": "$(\\sin\\theta - \\cos\\theta)^2 = \\left(\\frac{1}{2}\\right)^2 = \\frac{1}{4}$。"
            },
            {
                "num": 2,
                "title": "線索 2：移項求 2sin cos",
                "content": "$1 - 2\\sin\\theta\\cos\\theta = \\frac{1}{4} \\implies 2\\sin\\theta\\cos\\theta = 1 - \\frac{1}{4} = \\frac{3}{4}$。"
            },
            {
                "num": 3,
                "title": "線索 3：同除以 2 結案",
                "content": "$\\sin\\theta\\cos\\theta = \\frac{3}{4} \\div 2 = \\frac{3}{8}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin\\theta\\cos\\theta = \\frac{3}{8}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">差平方求乘積</text>
  <text x="190" y="80" text-anchor="middle" font-size="15" fill="#475569">(sin θ - cos θ)² = 1 - 2 sin θ cos θ = 1/4</text>
  <text x="190" y="115" text-anchor="middle" font-size="15" fill="#dc2626">2 sin θ cos θ = 1 - 1/4 = 3/4</text>
  <text x="190" y="160" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">sin θ cos θ = 3/8</text>
</svg>"""
    },
    {
        "id": 55,
        "tag": "CASE 55",
        "page": "課本 P.124 基礎 7(2)",
        "category": "恆等式求切和",
        "title": "基礎題 7(2)：已知 sin θ - cos θ = 1/2，求 tan θ + cot θ",
        "front_content": "已知 $\\sin\\theta - \\cos\\theta = \\frac{1}{2}$。<br>承上題（已求得 $\\sin\\theta\\cos\\theta = \\frac{3}{8}$），<br>試求：<br>$$\\tan\\theta + \\cot\\theta$$",
        "front_tip": "🕵️ 柯南破案導引：利用 $\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$，取 $\\frac{3}{8}$ 的倒數秒殺！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用切和恆等倒數公式",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta}$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入已求得之乘積",
                "content": "$\\tan\\theta + \\cot\\theta = \\frac{1}{3/8} = \\frac{8}{3}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\tan\\theta + \\cot\\theta = \\frac{8}{3}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="50" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">tan θ + cot θ 倒數秒解</text>
  <rect x="70" y="75" width="240" height="50" rx="8" fill="#fef3c7"/>
  <text x="190" y="106" text-anchor="middle" font-size="16" font-weight="bold" fill="#b45309">1 / (sin θ cos θ) = 1 / (3/8)</text>
  <text x="190" y="165" text-anchor="middle" font-size="24" font-weight="bold" fill="#b91c1c">= 8/3</text>
</svg>"""
    },
    {
        "id": 56,
        "tag": "CASE 56",
        "page": "課本 P.124 進階 8",
        "category": "進階通分化簡",
        "title": "進階題 8：通分平方差求分式和",
        "front_content": "已知 $\\theta$ 為銳角，且 $\\cos\\theta = \\frac{1}{5}$。<br>試求下列各式之值：<br>$$\\frac{1}{1 + \\sin\\theta} + \\frac{1}{1 - \\sin\\theta}$$",
        "front_tip": "🕵️ 柯南破案導引：通分出奇蹟！分母相乘 $(1+\\sin)(1-\\sin) = 1 - \\sin^2\\theta = \\cos^2\\theta$！分子相加交叉項消去得 $2$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：通分合併兩分式",
                "content": "原式 $= \\frac{(1 - \\sin\\theta) + (1 + \\sin\\theta)}{(1 + \\sin\\theta)(1 - \\sin\\theta)} = \\frac{2}{1 - \\sin^2\\theta}$。"
            },
            {
                "num": 2,
                "title": "線索 2：分母由平方關係轉為 cos²",
                "content": "因為 $1 - \\sin^2\\theta = \\cos^2\\theta$，故原式 $= \\frac{2}{\\cos^2\\theta}$。"
            },
            {
                "num": 3,
                "title": "線索 3：代入 cos θ = 1/5 計算",
                "content": "原式 $= \\frac{2}{(1/5)^2} = \\frac{2}{1/25} = 2 \\times 25 = 50$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式之值為 $50$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">通分化簡 1/(1+sin) + 1/(1-sin)</text>
  <text x="190" y="80" text-anchor="middle" font-size="16" fill="#475569">= 2 / (1 - sin²θ) = 2 / cos²θ</text>
  <text x="190" y="115" text-anchor="middle" font-size="16" fill="#dc2626">= 2 / (1/5)² = 2 / (1/25)</text>
  <text x="190" y="160" text-anchor="middle" font-size="24" font-weight="bold" fill="#b91c1c">= 2 × 25 = 50</text>
</svg>"""
    },
    {
        "id": 57,
        "tag": "CASE 57",
        "page": "課本 P.124 進階 9(1)",
        "category": "進階對稱式",
        "title": "進階題 9(1)：已知 tan x + cot x = 25/12，求 sin x cos x",
        "front_content": "已知 $x$ 為銳角，$\\tan x + \\cot x = \\frac{25}{12}$。<br>試求：<br>$$\\sin x \\cdot \\cos x$$",
        "front_tip": "🕵️ 柯南破案導引：逆向倒數思維！$\\tan x + \\cot x = \\frac{1}{\\sin x \\cos x}$，故乘積就是它的倒數！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：調用切和恆等關係",
                "content": "$\\tan x + \\cot x = \\frac{\\sin x}{\\cos x} + \\frac{\\cos x}{\\sin x} = \\frac{\\sin^2 x + \\cos^2 x}{\\sin x \\cos x} = \\frac{1}{\\sin x \\cos x}$。"
            },
            {
                "num": 2,
                "title": "線索 2：取倒數求得乘積",
                "content": "$\\frac{1}{\\sin x \\cos x} = \\frac{25}{12} \\implies \\sin x \\cos x = \\frac{12}{25}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin x \\cos x = \\frac{12}{25}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">切和逆推乘積</text>
  <rect x="70" y="70" width="240" height="50" rx="8" fill="#e0e7ff"/>
  <text x="190" y="100" text-anchor="middle" font-size="15" font-weight="bold" fill="#3730a3">tan x + cot x = 1 / (sin x cos x) = 25/12</text>
  <text x="190" y="160" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">sin x cos x = 12/25</text>
</svg>"""
    },
    {
        "id": 58,
        "tag": "CASE 58",
        "page": "課本 P.124 進階 9(2)",
        "category": "進階對稱式",
        "title": "進階題 9(2)：已知 tan x + cot x = 25/12，求 sin x + cos x",
        "front_content": "已知 $x$ 為銳角，$\\tan x + \\cot x = \\frac{25}{12}$。<br>承上題（已求得 $\\sin x \\cos x = \\frac{12}{25}$），<br>試求：<br>$$\\sin x + \\cos x$$",
        "front_tip": "🕵️ 柯南破案導引：和平方開根號！$(\\sin x + \\cos x)^2 = 1 + 2\\sin x \\cos x$！銳角開根號取正值！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：計算和的平方",
                "content": "$(\\sin x + \\cos x)^2 = 1 + 2\\sin x \\cos x = 1 + 2\\left(\\frac{12}{25}\\right) = 1 + \\frac{24}{25} = \\frac{49}{25}$。"
            },
            {
                "num": 2,
                "title": "線索 2：開根號取正值",
                "content": "因為 $x$ 為銳角，$\\sin x > 0, \\cos x > 0 \\implies \\sin x + \\cos x > 0$。<br>$\\sin x + \\cos x = \\sqrt{\\frac{49}{25}} = \\frac{7}{5}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin x + \\cos x = \\frac{7}{5}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="45" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">乘積開根推求和</text>
  <text x="190" y="85" text-anchor="middle" font-size="15" fill="#475569">(sin x + cos x)² = 1 + 2(12/25) = 49/25</text>
  <text x="190" y="125" text-anchor="middle" font-size="16" fill="#dc2626">因為 x 為銳角，取正根號 √(49/25)</text>
  <text x="190" y="165" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">sin x + cos x = 7/5</text>
</svg>"""
    },
    {
        "id": 59,
        "tag": "CASE 59",
        "page": "課本 P.124 進階 9(3)",
        "category": "進階立方和",
        "title": "進階題 9(3)：已知 tan x + cot x = 25/12，求 sin³ x + cos³ x",
        "front_content": "已知 $x$ 為銳角，$\\tan x + \\cot x = \\frac{25}{12}$。<br>承前兩小題：$\\sin x \\cos x = \\frac{12}{25}$ 且 $\\sin x + \\cos x = \\frac{7}{5}$。<br>試求：<br>$$\\sin^3 x + \\cos^3 x$$<br>（提示：$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$）",
        "front_tip": "🕵️ 柯南破案導引：立方和公式：$a^3 + b^3 = (a + b)(1 - ab)$！和乘積均已破案，直接代入！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：展開立方和因式分解公式",
                "content": "$\\sin^3 x + \\cos^3 x = (\\sin x + \\cos x)(\\sin^2 x - \\sin x \\cos x + \\cos^2 x) = (\\sin x + \\cos x)(1 - \\sin x \\cos x)$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入已求得之和與乘積",
                "content": "$\\sin x + \\cos x = \\frac{7}{5}$ ； $1 - \\sin x \\cos x = 1 - \\frac{12}{25} = \\frac{13}{25}$。"
            },
            {
                "num": 3,
                "title": "線索 3：兩式相乘結案",
                "content": "原式 $= \\frac{7}{5} \\times \\frac{13}{25} = \\frac{91}{125}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\sin^3 x + \\cos^3 x = \\frac{91}{125}$！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <text x="190" y="40" text-anchor="middle" font-size="16" font-weight="bold" fill="#1e40af">立方和公式因式分解</text>
  <text x="190" y="80" text-anchor="middle" font-size="15" fill="#475569">sin³ x + cos³ x = (sin x + cos x)(1 - sin x cos x)</text>
  <text x="190" y="115" text-anchor="middle" font-size="16" fill="#dc2626">= (7/5) × [ 1 - 12/25 ] = (7/5) × (13/25)</text>
  <text x="190" y="160" text-anchor="middle" font-size="22" font-weight="bold" fill="#b91c1c">= 91/125</text>
</svg>"""
    },
    {
        "id": 60,
        "tag": "CASE 60",
        "page": "全單元總結錦囊",
        "category": "總結神技錦囊",
        "title": "【名偵探破案密碼 ‧ 終極神技卷】全單元破案公式總覽",
        "front_content": "名偵探柯南數理探案特訓 ‧ 終極通關密碼：<br>1. 銳角三角比：$\\sin = \\frac{\\text{對}}{\\text{斜}}, \\cos = \\frac{\\text{鄰}}{\\text{斜}}, \\tan = \\frac{\\text{對}}{\\text{鄰}}$<br>2. 倒數伴侶：$\\sin\\csc=1, \\cos\\sec=1, \\tan\\cot=1$<br>3. 六角平方：$\\sin^2+\\cos^2=1, 1+\\tan^2=\\sec^2, 1+\\cot^2=\\csc^2$<br>4. 餘角互換：$\\sin(90^\\circ-\\theta)=\\cos\\theta, \\tan\\leftrightarrow\\cot, \\sec\\leftrightarrow\\csc$<br>5. 齊次同除：正餘弦分式同除 $\\cos$ 秒化 $\\tan$！<br>6. 和差連環扣：$(\\sin\\pm\\cos)^2 = 1\\pm 2\\sin\\cos$ ； $\\tan+\\cot = \\frac{1}{\\sin\\cos}$",
        "front_tip": "🕵️ 柯南破案導引：掌握這六大通關密碼，技術高中數學 2-2 案件真相永遠逃不出你的法眼！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：定義是根基",
                "content": "面對任意直角三角形，標明對邊、鄰邊、斜邊，三比一定即得前三，倒數即得後三。"
            },
            {
                "num": 2,
                "title": "線索 2：恆等關係是武器",
                "content": "平方關係、倒數關係、商數關係與餘角關係，四大陣法靈活切換化繁為簡。"
            },
            {
                "num": 3,
                "title": "線索 3：和差立方是終結者",
                "content": "遇到和差求乘積，平方破之；遇到切和求對稱式，倒數破之；遇到立方和，因式分解破之！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】全單元 60 案全部偵破！恭喜特派員晉升名偵探！",
        "svg": r"""<svg viewBox="0 0 380 200" class="w-full h-full">
  <rect x="8" y="6" width="364" height="188" rx="12" fill="#fbf9f4" stroke="#d97706" stroke-width="2"/>
  <rect x="30" y="25" width="320" height="150" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <text x="190" y="55" text-anchor="middle" font-size="16" font-weight="bold" fill="#78350f">【CASE CLOSED 真相永遠只有一個！】</text>
  <text x="190" y="85" text-anchor="middle" font-size="14" fill="#92400e">sin²θ + cos²θ = 1   ·   tan θ + cot θ = 1/(sin θ cos θ)</text>
  <text x="190" y="115" text-anchor="middle" font-size="14" fill="#92400e">(sin θ ± cos θ)² = 1 ± 2 sin θ cos θ</text>
  <text x="190" y="150" text-anchor="middle" font-size="18" font-weight="bold" fill="#b91c1c">★ 泰宇高中數學 2-2 案件圓滿結案 ★</text>
</svg>"""
    }
]
