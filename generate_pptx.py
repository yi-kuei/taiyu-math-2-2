# -*- coding: utf-8 -*-
"""
generate_pptx.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
課堂旗艦 16:9 全螢幕教學簡報生成器 (HTML + Edge Headless + PyMuPDF + python-pptx)

嚴格遵守使用者指示與教室投影教學五大核心原則：
1. 依據課程內容與主題，每張簡報放一個重點概念解說 (包含正三角形對折、六大定義、倒數、特別角、六角星四大星陣、常用恆等式等)
2. 例題跟隨堂練習，每一大題一張頁面 (例題 1~9 與隨堂 1~9 各自獨立成頁，多小題並列左右或三欄清楚對照)
3. 習題也是一題一張頁面 (是非題 5 小題獨立頁面診斷、基礎題 1~7 與進階題 8~9 每一大題獨立一張頁面)
4. 字體全面放大：標題 36~40px、題幹 24~28px、算式與推理 20~24px、結論 22~26px，保證後排清晰可見
5. 能夠用圖形來解釋說明的，盡量放上圖形來輔助說明 (100% 配置精密 SVG 向量幾何圖形、六角星陣、直角三角形坐標)
6. 16:9 滿版渲染 (338.67mm x 190.5mm / 13.333" x 7.5")，0 邊距滿版貼合無黑邊
7. 象牙米杏暖白護眼底色 (#fbf9f4 ~ #f7f3ea)，教室投影高對比不反光
8. 每頁配置專屬教學備忘 Speaker Notes
9. 自動將 PPTX 轉為 Base64 寫入 docx_b64.py
"""

import os
import io
import re
import base64
import subprocess
import pymupdf
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

from cards_part1 import CARDS_PART1
from cards_part2 import CARDS_PART2

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE_EXE = next((p for p in EDGE_PATHS if os.path.exists(p)), None)

ALL_CARDS = {c['id']: c for c in (CARDS_PART1 + CARDS_PART2)}

# 建立 47 頁完整的教學簡報結構清單
SLIDES_CONFIG = [
    # 01. 封面
    {
        "kind": "cover",
        "title": "2-2 三角函數的定義與性質",
        "subtitle": "泰宇版 ‧ 技術型高級中等學校數學 第一冊 ‧ 第二章 三角函數",
        "badge": "課堂教學專用 ‧ 旗艦全螢幕 16:9 簡報",
        "desc": "掌握銳角三角比、六大函數邊長比、特別角精確值、神奇魔法六角形四大關係與常用三角恆等式",
        "notes": "【單元引言】\n全班同學好！今天我們要進入高中數學最關鍵的核心——三角函數。我們將從直角三角形邊長比例出發，一步步推導六大函數、熟記特別角、掌握神奇六角星陣，輕鬆攻克所有題型！"
    },
    # 02. 學習地圖
    {
        "kind": "roadmap",
        "title": "單元學習探案地圖",
        "subtitle": "循序漸進 ‧ 四大階段破案路線圖",
        "modules": [
            {"num": "第一階段", "title": "銳角三角函數定義", "desc": "正三角形對折幾何比值、六大函數邊長比定義、知一求其餘三邊"},
            {"num": "第二階段", "title": "特別角與生活工程", "desc": "30°-45°-60° 精確值速記、弳度換算、無障礙坡道與險升坡反推"},
            {"num": "第三階段", "title": "六角星四大恆等關係", "desc": "倒數、商數、平方、餘角四大星陣法則、齊次分式同除神技"},
            {"num": "第四階段", "title": "三角恆等式與課後習題", "desc": "和差平方連環扣、切和倒數、是非題診斷、基礎與進階實戰破案"}
        ],
        "notes": "【地圖導讀】\n全班請看路線圖：我們先從直角三角形三邊比建立六大函數定義；接著熟背 30°、45°、60° 特別角；然後掌握神奇魔法六角形四大關係；最後攻克和差平方連環扣與章末實戰！"
    },

    # =========================================================
    # 第一階段：銳角三角函數定義篇
    # =========================================================
    {
        "kind": "concept",
        "card": ALL_CARDS[1],
        "badge": "核心概念 1",
        "title": "正三角形對折與三角比的由來",
        "notes": "【觀念精講】\n邊長為 2 的正三角形對折後，高為根號 3。相似三角形對應邊成比例，因此角 A 固定時，邊長比值為定值，這就是三角比的由來！"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[2],
        "badge": "核心概念 2",
        "title": "銳角三角函數的六大嚴格定義",
        "notes": "【板書重點】\n斜邊為 r、對邊為 y、鄰邊為 x。正弦 sin=y/r、餘弦 cos=x/r、正切 tan=y/x。其倒數分別為餘割 csc、正割 sec、餘切 cot。"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[3],
        "badge": "核心概念 3",
        "title": "倒數關係與英文字母字首記憶法",
        "notes": "【記憶口訣】\n記住：S 配 C，T 配 T！正弦 sin 配餘割 csc；餘弦 cos 配正割 sec；正切 tan 配餘切 cot。正配餘、餘配正，切勿同字首相配！"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 1",
        "title": "例題 1：三邊已知求 ∠A 之六個三角函數值",
        "cards": [ALL_CARDS[4], ALL_CARDS[5]],
        "notes": "【例題 1 講解】\n本大題包含兩小題直角三角形：第 (1) 小題為 8-15-17，第 (2) 小題為 5-12-13。請同學先鎖定角 A 的對邊與鄰邊，先求 sin、cos、tan，再直接取倒數得 csc、sec、cot！"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 1",
        "title": "隨堂練習 1：視角切換至 ∠B 之六個三角函數值",
        "cards": [ALL_CARDS[6], ALL_CARDS[7]],
        "notes": "【隨堂 1 演練】\n注意視角切換到角 B！此時角 B 的對邊與鄰邊剛好跟角 A 互換，斜邊仍維持不變。請全班對照例題 1 與隨堂 1 的結果，體會餘角互換的關係！"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 2",
        "title": "例題 2：已知 cos A = 5/13，求其餘各三角函數值",
        "cards": [ALL_CARDS[8]],
        "notes": "【知一求其餘】\n已知 cos A = 5/13，設鄰邊為 5k、斜邊為 13k，利用畢氏定理求出對邊為 12k。三邊比例 5:12:13 一確定，其餘五個函數值直接寫出！"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 2",
        "title": "隨堂練習 2：已知 tan A = 24/7，求其餘各三角函數值",
        "cards": [ALL_CARDS[9]],
        "notes": "【學生實戰】\n設對邊為 24k、鄰邊為 7k，畢氏定理算斜邊：根號(24^2 + 7^2) = 25k。三邊比 7:24:25，迅速寫出其餘五個函數值！"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 3",
        "title": "例題 3：已知 sin A = 4/5 且 AB = 15，求邊長與各函數值",
        "cards": [ALL_CARDS[10]],
        "notes": "【比例與長度】\n強調函數值是比值（不隨放大改變），邊長是實際長度。由三邊比 3:4:5，斜邊 5k=15 得放大倍數 k=3，實際邊長為 9 與 12。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 3",
        "title": "隨堂練習 3：已知 csc A = 17/15 且 AC = 40，求邊長與各值",
        "cards": [ALL_CARDS[11]],
        "notes": "【倒數與邊長】\ncsc A = 17/15 代表斜邊與對邊比為 17:15，鄰邊即為 8。由鄰邊 8k=40 得 k=5，故斜邊 AB=85、對邊 BC=75。"
    },

    # =========================================================
    # 第二階段：特別角與生活科技篇
    # =========================================================
    {
        "kind": "concept",
        "card": ALL_CARDS[12],
        "badge": "核心概念 4",
        "title": "30° 與 60° 特別角的六大三角函數值推導",
        "notes": "【幾何推導】\n30°-60°-90° 直角三角形三邊比為 1:根號3:2。對角對短邊（30° 對 1，60° 對根號 3，90° 對 2），牢記三邊比即可推出所有值！"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[13],
        "badge": "核心概念 5",
        "title": "45° 特別角的六大三角函數值推導",
        "notes": "【等腰直角】\n45°-45°-90° 等腰直角三角形三邊比為 1:1:根號2。sin 45° = cos 45° = 根號2/2，tan 45° = cot 45° = 1。"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[14],
        "badge": "速記秘技",
        "title": "特別角 30°、45°、60° 精確值全覽表",
        "notes": "【階梯規律】\nsin 分子是根號1、根號2、根號3（分子遞增）；cos 分子是根號3、根號2、根號1（分子逆序遞減）；分母恆為 2！"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 4",
        "title": "例題 4：特別角四則運算求值",
        "cards": [ALL_CARDS[15], ALL_CARDS[16]],
        "notes": "【代值計算】\n第 (1) 小題代入 sin 30°=1/2、cos 60°=1/2、tan 45°=1 得 1。\n第 (2) 小題注意 sin^2 45° 是平方函數值：2*(1/根號2)^2 = 1，乘積項 cot 30°*csc 60° = 根號3*(2/根號3) = 2，合計 3。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 4",
        "title": "隨堂練習 4：含根號與弳度特別角求值",
        "cards": [ALL_CARDS[17], ALL_CARDS[18]],
        "notes": "【根號與弳度】\n第 (1) 小題計算化簡得 2*根號3 - 1。\n第 (2) 小題將弳度 pi/4, pi/6, pi/3 轉為 45°, 30°, 60°，通分計算得 11/12。"
    },
    {
        "kind": "big_problem",
        "tag": "生活科技例題 5",
        "title": "例題 5：內政部營建署無障礙坡道坡度夾角反推",
        "cards": [ALL_CARDS[19]],
        "notes": "【科技素養】\n坡度定義即正切值 tan θ = 垂直上升 / 水平前進。tan θ = 1/8 = 0.125，使用工程計算機按 tan^(-1)(0.125) 得夾角約 7.125°。"
    },
    {
        "kind": "big_problem",
        "tag": "生活科技隨堂 5",
        "title": "隨堂練習 5：自行車道 20% 險升坡夾角反推",
        "cards": [ALL_CARDS[20]],
        "notes": "【生活應用】\n20% 坡度代表水平前進 100 公尺、垂直上升 20 公尺。tan θ = 20/100 = 0.2，計算機按 tan^(-1)(0.2) 得約 11.3°，夾角約為 11°。"
    },

    # =========================================================
    # 第三階段：神奇魔法六角星四大恆等關係篇
    # =========================================================
    {
        "kind": "concept",
        "card": ALL_CARDS[21],
        "badge": "核心概念 6",
        "title": "神奇魔法六角形四大破案星陣全覽",
        "notes": "【六角星陣全覽】\n頂點順序：左側無 co (sin, tan, sec)，右側帶 co (cos, cot, csc)，中央放 1。涵蓋對角互倒、倒三角平方和、相鄰相除、橫向餘角互換！"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[22],
        "badge": "恆等關係 1",
        "title": "恆等關係一：倒數關係（對角互倒）",
        "notes": "【倒數律】\n每條對角線兩端乘積為 1：sin*csc=1, cos*sec=1, tan*cot=1。"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[23],
        "badge": "恆等關係 2",
        "title": "恆等關係二：商數關係（相鄰相除）",
        "notes": "【商數律】\n每個頂點等於相鄰兩頂點之商：tan = sin/cos、cot = cos/sin。"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[24],
        "badge": "恆等關係 3",
        "title": "恆等關係三：平方關係（倒三角平方和）",
        "notes": "【平方律】\n三個倒三角形：上方兩頂點平方和等於下方頂點！sin^2+cos^2=1、1+tan^2=sec^2、1+cot^2=csc^2。"
    },
    {
        "kind": "concept",
        "card": ALL_CARDS[25],
        "badge": "恆等關係 4",
        "title": "恆等關係四：餘角關係（橫向端點互換）",
        "notes": "【餘角律】\n同高度橫向端點角度相加 90° 函數互換：sin(90°-θ)=cos θ、tan(90°-θ)=cot θ、sec(90°-θ)=csc θ。"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 6",
        "title": "例題 6：基本恆等關係秒殺求值",
        "cards": [ALL_CARDS[26], ALL_CARDS[27], ALL_CARDS[28]],
        "notes": "【秒殺題型】\n(1) 同角倒數相乘：sin 50° * csc 50° = 1。\n(2) 同角平方和：sin^2 40° + cos^2 40° = 1。\n(3) 平方關係變形：sec^2 70° - tan^2 70° = 1。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 6",
        "title": "隨堂練習 6：倒數與平方綜合求值",
        "cards": [ALL_CARDS[29], ALL_CARDS[30], ALL_CARDS[31]],
        "notes": "【符號陷阱提醒】\n(1) cos 35° * sec 35° = 1。\n(2) sin^2 80° + cos^2 80° = 1。\n(3) cot^2 12° - csc^2 12° = -1（注意移項負號！）。"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 7",
        "title": "例題 7：餘角轉化與恆等混合求值",
        "cards": [ALL_CARDS[32]],
        "notes": "【非特別角破案】\n40°+50°=90° 得 tan 50°=cot 40°，故 tan 40°*cot 40°=1；72°+18°=90° 得 csc 18°=sec 72°，tan^2 72°-sec^2 72°=-1。合計 1 + (-1) = 0。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 7",
        "title": "隨堂練習 7：餘角平方和與平方差混合求值",
        "cards": [ALL_CARDS[33]],
        "notes": "【兩組餘角配對】\n第一組：cos^2 35° + cos^2 55° = cos^2 35° + sin^2 35° = 1。\n第二組：csc^2 47° - tan^2 43° = csc^2 47° - cot^2 47° = 1。合計 1 + 1 = 2。"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 8",
        "title": "例題 8：已知 tan θ = 2，求一次齊次分式之值",
        "cards": [ALL_CARDS[34]],
        "notes": "【齊次同除神技】\n分子分母同除以 cos θ，正弦全變正切：(tan θ + 2) / (3 tan θ - 1) = (2 + 2) / (6 - 1) = 4/5！完全不必算斜邊！"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 8",
        "title": "隨堂練習 8：已知 cot θ = 2/3，求一次齊次分式之值",
        "cards": [ALL_CARDS[35]],
        "notes": "【同除正弦】\n已知餘切，分子分母同除以 sin θ：(1 - 3 cot θ) / (5 + 6 cot θ) = (1 - 2) / (5 + 4) = -1/9。"
    },

    # =========================================================
    # 第四階段：三角恆等式核心篇
    # =========================================================
    {
        "kind": "concept",
        "card": ALL_CARDS[36],
        "badge": "核心概念 7",
        "title": "常用三角恆等式三大核心架構推導",
        "notes": "【三大核心式】\n(1) 和平方：(sin+cos)^2 = 1 + 2 sin cos。\n(2) 差平方：(sin-cos)^2 = 1 - 2 sin cos。\n(3) 切和倒數：tan + cot = 1 / (sin cos)。見和差必平方！"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 9",
        "title": "例題 9：和平方連環扣求乘積與切和",
        "cards": [ALL_CARDS[37], ALL_CARDS[38]],
        "notes": "【連環口訣】\n(1) 平方展開：1 + 2 sin cos = (4/3)^2 = 16/9 得 sin cos = 7/18。\n(2) 切和即乘積倒數：tan + cot = 1 / (7/18) = 18/7！"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 9",
        "title": "隨堂練習 9：差平方連環扣求乘積與切和",
        "cards": [ALL_CARDS[39], ALL_CARDS[40]],
        "notes": "【差平方實戰】\n(1) 差平方：1 - 2 sin cos = (3/5)^2 = 9/25 得 sin cos = 8/25。\n(2) 切和即倒數：tan + cot = 1 / (8/25) = 25/8！"
    },

    # =========================================================
    # 第五階段：章末課後習題篇 (觀念是非、基礎題、進階題)
    # =========================================================
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (1)",
        "title": "習題 觀念 (1)：已知銳角正弦是否可求其餘五個函數值？",
        "cards": [ALL_CARDS[41]],
        "notes": "【觀念診斷 1】\n正確（○）！已知 sin θ = y/r，由畢氏定理鄰邊 x = 根號(r^2 - y^2) 唯一確定，因此其餘五個三角函數值皆能完全求出！"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (2)",
        "title": "習題 觀念 (2)：已知 sin A = 3/5 是否可求出三邊長度？",
        "cards": [ALL_CARDS[42]],
        "notes": "【觀念診斷 2】\n錯誤（×）！函數值是邊長『比值』而非『長度』！三邊比為 3k:4k:5k，若未給予任何邊長條件，無法求得實際長度！"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (3)",
        "title": "習題 觀念 (3)：不同銳角平方和是否必等於 1？",
        "cards": [ALL_CARDS[43]],
        "notes": "【觀念診斷 3】\n錯誤（×）！平方關係的前提是『同角』！sin^2 α + cos^2 β 不保證等於 1。反例：α=30°, β=60° 時平方和為 1/2 ≠ 1。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (4)",
        "title": "習題 觀念 (4)：銳角 sin θ × cos θ 是否必等於 1？",
        "cards": [ALL_CARDS[44]],
        "notes": "【觀念診斷 4】\n錯誤（×）！倒數關係是 sin θ * csc θ = 1，並非 sin θ * cos θ = 1！反例：θ=30° 時乘積為 根號3/4 ≠ 1。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (5)",
        "title": "習題 觀念 (5)：和平方展開是否可省略交叉項？",
        "cards": [ALL_CARDS[45]],
        "notes": "【觀念診斷 5】\n錯誤（×）！(sin+cos)^2 展開必須包含交叉項 2 sin cos！因為 θ 為銳角，交叉項大於 0，故展開值大於 1，不可能等於 1。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 1",
        "title": "基礎題 1：已知直角三角形 sin A = 3/5，求 tan A + sec A",
        "cards": [ALL_CARDS[46]],
        "notes": "【基礎 1 詳解】\nsin A = 3/5 得三邊比 3:4:5。對邊 3、鄰邊 4、斜邊 5。tan A = 3/4、sec A = 5/4，相加 3/4 + 5/4 = 8/4 = 2。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 2",
        "title": "基礎題 2：tan A = 12/5 且 AB = 26，求 sin A 與 AC",
        "cards": [ALL_CARDS[47], ALL_CARDS[48]],
        "notes": "【基礎 2 詳解】\n三邊比 5:12:13。第 (1) 小題 sin A = 12/13。\n第 (2) 小題斜邊 13k = 26 得 k=2，鄰邊 AC = 5(2) = 10。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 3",
        "title": "基礎題 3：特別角四則與弳度乘積求值",
        "cards": [ALL_CARDS[49], ALL_CARDS[50]],
        "notes": "【基礎 3 詳解】\n第 (1) 小題代入特別角算得 1 + 2 + 4 = 7。\n第 (2) 小題利用平方差公式 (2 + 根號2/2)(2 - 根號2/2) = 4 - 1/2 = 7/2。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 4",
        "title": "基礎題 4：餘角與平方關係綜合求值",
        "cards": [ALL_CARDS[51]],
        "notes": "【基礎 4 詳解】\ncos 70° = sin 20° 得 cos^2 20° + sin^2 20° = 1；csc 70° = sec 20° 得 tan^2 20° - sec^2 20° = -1。原式 = 1 + (-1) = 0。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 5",
        "title": "基礎題 5：和平方加差平方之化簡",
        "cards": [ALL_CARDS[52]],
        "notes": "【基礎 5 詳解】\n(sin+cos)^2 + (sin-cos)^2 = (1 + 2sincos) + (1 - 2sincos) = 1 + 1 = 2！交叉項完美抵消！"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 6",
        "title": "基礎題 6：已知 cot θ = 5/12，求齊次分式之值",
        "cards": [ALL_CARDS[53]],
        "notes": "【基礎 6 詳解】\n分子分母同除以 sin θ：(5 - 4 cot θ) / (5 + 3 cot θ) = (5 - 5/3) / (5 + 5/4) = (10/3) / (25/4) = 8/15。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 7",
        "title": "基礎題 7：已知 sin θ - cos θ = 1/2，求乘積與切和",
        "cards": [ALL_CARDS[54], ALL_CARDS[55]],
        "notes": "【基礎 7 詳解】\n第 (1) 小題差平方 1 - 2sincos = 1/4 得 sincos = 3/8。\n第 (2) 小題切和為乘積倒數：tan + cot = 1 / (3/8) = 8/3。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 進階 8",
        "title": "進階題 8：通分平方差求分式和",
        "cards": [ALL_CARDS[56]],
        "notes": "【進階 8 詳解】\n通分分母 (1+sin)(1-sin) = 1 - sin^2 = cos^2 θ；分子為 (1-sin) + (1+sin) = 2。原式 = 2 / cos^2 θ = 2 / (1/25) = 50！"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 進階 9",
        "title": "進階題 9：切和求乘積、和與立方和",
        "cards": [ALL_CARDS[57], ALL_CARDS[58], ALL_CARDS[59]],
        "notes": "【進階 9 劇場版魔王題】\n(1) tan+cot = 1/sincos = 25/12 得 sincos = 12/25。\n(2) (sin+cos)^2 = 1 + 24/25 = 49/25 得 sin+cos = 7/5。\n(3) 立方和公式 (sin+cos)(1 - sincos) = (7/5) * (13/25) = 91/125！"
    },

    # 47. 終極結案錦囊
    {
        "kind": "concept",
        "card": ALL_CARDS[60],
        "badge": "結案錦囊",
        "title": "【名偵探破案密碼 ‧ 終極神技卷】全單元破案公式總覽",
        "notes": "【結案鼓舞】\n恭喜全班完成泰宇技術高中數學（第一冊）2-2 三角函數的定義與性質探案特訓！掌握這五大神技，所有三角函數題目都能迎刃而解！真相永遠只有一個！"
    }
]

def render_concept_slide(slide_cfg, idx, total_slides):
    card = slide_cfg["card"]
    badge = slide_cfg.get("badge", "核心概念")
    title = slide_cfg.get("title", card["title"])
    front = card["front_content"]
    svg_html = card.get("svg", "")

    steps_html = "".join([f"""
      <div class="p-3.5 rounded-xl bg-white border border-amber-200/80 shadow-2xs">
        <div class="text-base font-black text-amber-900 mb-1">【{s['title']}】</div>
        <div class="text-lg text-slate-800 leading-relaxed font-medium">{s['content']}</div>
      </div>
    """ for s in card.get("steps", [])])

    return f"""
  <div class="slide-page">
    <!-- 頂部標題區 -->
    <div class="flex items-center justify-between mb-3 border-b-2 border-amber-300 pb-2">
      <div class="flex items-center gap-3">
        <span class="px-4 py-1.5 rounded-lg text-base font-black bg-amber-600 text-white shadow-xs">{badge}</span>
        <h2 class="text-3xl font-black text-amber-950 tracking-tight">{title}</h2>
      </div>
      <div class="text-base font-bold text-amber-800 bg-amber-100/80 px-3 py-1 rounded-md">{card.get('page', '課本概念')}</div>
    </div>

    <!-- 雙欄主體內容：左欄 60% 概念與推理 / 右欄 40% 精密集幾何圖解 -->
    <div class="grid grid-cols-12 gap-5 flex-1 items-stretch my-1 overflow-hidden">
      <!-- 左欄 -->
      <div class="col-span-7 flex flex-col justify-between space-y-3">
        <div class="p-4 rounded-xl bg-amber-50/90 border-2 border-amber-300 text-xl font-bold text-slate-900 leading-relaxed shadow-2xs">
          {front}
        </div>
        <div class="space-y-2.5 flex-1">
          {steps_html}
        </div>
        <div class="p-3 rounded-lg bg-emerald-50 border border-emerald-400 text-lg font-black text-emerald-900 text-center">
          {card.get('conclusion', '【真相大白】掌握概念定義即破案！')}
        </div>
      </div>

      <!-- 右欄：滿版清晰幾何 SVG 輔助說明 -->
      <div class="col-span-5 flex flex-col justify-center items-center p-3 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
        <div class="w-full h-full max-h-[140mm] flex items-center justify-center">
          {svg_html}
        </div>
        <div class="mt-2 text-sm font-bold text-slate-500 text-center">▲ 幾何模型輔助視覺解析</div>
      </div>
    </div>

    <!-- 頁尾 -->
    <div class="flex items-center justify-between pt-2 border-t border-amber-200 text-sm text-slate-500 font-medium">
      <div>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質</div>
      <div>投影片 {idx+1} / {total_slides}</div>
      <div>PLVS 數學科  教育學習用</div>
    </div>
  </div>
"""

def render_big_problem_slide(slide_cfg, idx, total_slides):
    tag = slide_cfg["tag"]
    title = slide_cfg["title"]
    cards = slide_cfg["cards"]
    num_cards = len(cards)

    # 根據小題數量切分版面
    if num_cards == 1:
        # 單題（單小題）：大題幹 + 雙欄 (左: 題目與推理步驟 / 右: SVG圖形輔助)
        c = cards[0]
        steps_html = "".join([f"""
          <div class="p-3 rounded-xl bg-white border border-slate-200 text-lg text-slate-800 leading-relaxed shadow-2xs">
            <span class="font-bold text-amber-900">{s['title']}：</span>{s['content']}
          </div>
        """ for s in c.get("steps", [])])

        body_html = f"""
        <div class="grid grid-cols-12 gap-5 flex-1 items-stretch my-1 overflow-hidden">
          <div class="col-span-7 flex flex-col justify-between space-y-3">
            <div class="p-4 rounded-xl bg-amber-50/90 border-2 border-amber-300 text-2xl font-bold text-slate-900 leading-relaxed shadow-2xs">
              {c['front_content']}
            </div>
            <div class="space-y-2.5 flex-1">
              {steps_html}
            </div>
            <div class="p-3.5 rounded-xl bg-emerald-50 border-2 border-emerald-500 text-xl font-black text-emerald-900 text-center shadow-xs">
              {c.get('conclusion', '')}
            </div>
          </div>
          <div class="col-span-5 flex flex-col justify-center items-center p-3 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
            <div class="w-full h-full max-h-[140mm] flex items-center justify-center">
              {c.get('svg', '')}
            </div>
            <div class="mt-2 text-sm font-bold text-slate-500 text-center">▲ 題目幾何圖解與解題線索</div>
          </div>
        </div>
        """
    elif num_cards == 2:
        # 兩小題：兩欄並列（左邊第 1 小題、右邊第 2 小題，各自包含題幹、步驟、結論與圖形）
        cols_html = []
        for i, c in enumerate(cards):
            st_html = "".join([f"""
              <div class="p-2.5 rounded-lg bg-amber-50/60 border border-amber-200/80 text-base text-slate-800 leading-relaxed">
                <span class="font-bold text-amber-900">{s['title']}：</span>{s['content']}
              </div>
            """ for s in c.get("steps", [])])
            svg_mini = c.get("svg", "")

            cols_html.append(f"""
            <div class="col-span-6 flex flex-col justify-between p-4 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
              <div>
                <div class="flex items-center justify-between mb-2 pb-1 border-b border-amber-200">
                  <span class="px-2.5 py-0.5 rounded text-sm font-black bg-amber-700 text-white">第 ({i+1}) 小題</span>
                  <span class="text-xs font-bold text-slate-400">{c.get('page', '')}</span>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xl font-bold text-slate-900 mb-2 leading-relaxed">
                  {c['front_content']}
                </div>
                <div class="space-y-1.5 my-2">
                  {st_html}
                </div>
              </div>
              <div>
                <div class="h-32 w-full flex items-center justify-center my-1 bg-amber-50/30 rounded-lg p-1 border border-amber-100">
                  {svg_mini}
                </div>
                <div class="p-2 rounded-lg bg-emerald-50 border border-emerald-400 text-base font-black text-emerald-900 text-center">
                  {c.get('conclusion', '')}
                </div>
              </div>
            </div>
            """)
        body_html = f"""
        <div class="grid grid-cols-12 gap-4 flex-1 items-stretch my-1 overflow-hidden">
          {''.join(cols_html)}
        </div>
        """
    else:
        # 三小題：三欄並列（第 1, 2, 3 小題並列，例如例題 6、隨堂 6、進階 9）
        cols_html = []
        for i, c in enumerate(cards):
            st_html = "".join([f"""
              <div class="p-2 rounded bg-amber-50/50 border border-amber-200 text-sm text-slate-800 leading-relaxed">
                <span class="font-bold text-amber-900">{s['title']}：</span>{s['content']}
              </div>
            """ for s in c.get("steps", [])])
            svg_mini = c.get("svg", "")

            cols_html.append(f"""
            <div class="col-span-4 flex flex-col justify-between p-3.5 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
              <div>
                <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-amber-200">
                  <span class="px-2 py-0.5 rounded text-xs font-black bg-amber-700 text-white">第 ({i+1}) 小題</span>
                  <span class="text-xs font-bold text-slate-400">{c.get('page', '')}</span>
                </div>
                <div class="p-2.5 rounded-lg bg-slate-50 border border-slate-200 text-lg font-bold text-slate-900 mb-2 leading-relaxed">
                  {c['front_content']}
                </div>
                <div class="space-y-1.5 my-1.5">
                  {st_html}
                </div>
              </div>
              <div>
                <div class="h-28 w-full flex items-center justify-center my-1 bg-amber-50/30 rounded-lg p-1 border border-amber-100">
                  {svg_mini}
                </div>
                <div class="p-1.5 rounded-lg bg-emerald-50 border border-emerald-400 text-sm font-black text-emerald-900 text-center">
                  {c.get('conclusion', '')}
                </div>
              </div>
            </div>
            """)
        body_html = f"""
        <div class="grid grid-cols-12 gap-3.5 flex-1 items-stretch my-1 overflow-hidden">
          {''.join(cols_html)}
        </div>
        """

    return f"""
  <div class="slide-page">
    <!-- 頂部標題區 -->
    <div class="flex items-center justify-between mb-3 border-b-2 border-amber-300 pb-2">
      <div class="flex items-center gap-3">
        <span class="px-4 py-1.5 rounded-lg text-base font-black bg-red-600 text-white shadow-xs">{tag}</span>
        <h2 class="text-3xl font-black text-amber-950 tracking-tight">{title}</h2>
      </div>
      <div class="text-sm font-bold text-slate-500 bg-amber-100/70 px-3 py-1 rounded-md">泰宇課本 ‧ 大題完整獨立頁</div>
    </div>

    <!-- 主體內容 -->
    {body_html}

    <!-- 頁尾 -->
    <div class="flex items-center justify-between pt-2 border-t border-amber-200 text-sm text-slate-500 font-medium">
      <div>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質</div>
      <div>投影片 {idx+1} / {total_slides}</div>
      <div>PLVS 數學科  教育學習用</div>
    </div>
  </div>
"""

def generate_full_slides_html(slides_cfg):
    total = len(slides_cfg)
    html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質 課堂旗艦簡報</title>
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @page {
      size: 338.67mm 190.5mm;
      margin: 0;
    }
    body {
      margin: 0;
      padding: 0;
      background: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }
    .slide-page {
      width: 338.67mm;
      height: 190.5mm;
      box-sizing: border-box;
      page-break-after: always;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 14mm 20mm 10mm 20mm;
      background: #fbf9f4; /* 象牙米杏暖白護眼底色 */
    }
    .katex, .katex-html, .katex-display {
      white-space: nowrap !important;
      font-size: 1.35em !important;
      font-weight: 700 !important;
    }
    .katex-display {
      margin: 0.15em 0 !important;
      display: inline-block !important;
    }
  </style>
</head>
<body>
"""

    for idx, cfg in enumerate(slides_cfg):
        kind = cfg["kind"]
        if kind == "cover":
            content_html = f"""
            <div class="flex-1 flex flex-col justify-center items-center text-center">
              <span class="px-6 py-2.5 rounded-full text-lg font-black bg-amber-600 text-white shadow-md mb-6 tracking-wide">
                {cfg['badge']}
              </span>
              <h1 class="text-6xl font-black text-amber-950 mb-6 tracking-tight leading-tight">
                {cfg['title']}
              </h1>
              <p class="text-3xl font-bold text-amber-800 mb-8">
                {cfg['subtitle']}
              </p>
              <div class="max-w-4xl p-6 rounded-2xl bg-amber-50 border-2 border-amber-300 text-slate-800 text-2xl font-medium shadow-sm leading-relaxed">
                {cfg['desc']}
              </div>
            </div>
            """
            html += f"""
            <div class="slide-page">
              {content_html}
              <div class="flex items-center justify-between pt-2 border-t border-amber-200 text-sm text-slate-500 font-medium">
                <div>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質</div>
                <div>投影片 {idx+1} / {total}</div>
                <div>PLVS 數學科  教育學習用</div>
              </div>
            </div>
            """
        elif kind == "roadmap":
            mods_html = "".join([f"""
              <div class="p-6 rounded-2xl bg-white border-2 border-amber-200 shadow-sm flex flex-col justify-between">
                <div>
                  <span class="px-3 py-1 rounded-md text-sm font-black bg-amber-600 text-white">{m['num']}</span>
                  <h3 class="text-2xl font-black text-amber-950 mt-3 mb-2">{m['title']}</h3>
                  <p class="text-lg text-slate-700 leading-relaxed">{m['desc']}</p>
                </div>
              </div>
            """ for m in cfg['modules']])
            content_html = f"""
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <span class="text-sm font-black text-amber-700 tracking-wider">ROADMAP</span>
                <h2 class="text-4xl font-black text-amber-950 mb-1">{cfg['title']}</h2>
                <p class="text-lg text-slate-600 mb-4">{cfg['subtitle']}</p>
              </div>
              <div class="grid grid-cols-4 gap-6 flex-1 items-stretch my-2">
                {mods_html}
              </div>
            </div>
            """
            html += f"""
            <div class="slide-page">
              {content_html}
              <div class="flex items-center justify-between pt-2 border-t border-amber-200 text-sm text-slate-500 font-medium">
                <div>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質</div>
                <div>投影片 {idx+1} / {total}</div>
                <div>PLVS 數學科  教育學習用</div>
              </div>
            </div>
            """
        elif kind == "concept":
            html += render_concept_slide(cfg, idx, total)
        elif kind == "big_problem":
            html += render_big_problem_slide(cfg, idx, total)

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
    print(f"課堂教學專用簡報總頁數：{len(SLIDES_CONFIG)} 頁 (16:9 全螢幕滿版)")

    html_file = "slides_16_9.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(generate_full_slides_html(SLIDES_CONFIG))
    print(f"成功產出全新課堂簡報 HTML：{html_file}")

    if not EDGE_EXE:
        print("未偵測到 Edge 瀏覽器，無法產出 PPTX！")
        return

    temp_pdf_file = "temp_slides.pdf"
    pptx_file = "2-2_三角函數的定義與性質_教學簡報.pptx"

    abs_html = os.path.abspath(html_file)
    abs_pdf = os.path.abspath(temp_pdf_file)

    print("由 Edge Headless 滿版渲染暫存 PDF (1920x1080 滿版無邊框)...")
    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--window-size=1920,1080",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=15000",
        f"--print-to-pdf={abs_pdf}",
        abs_html
    ]
    subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="ignore")

    if not os.path.exists(abs_pdf) or os.path.getsize(abs_pdf) < 1000:
        print("暫存 PDF 渲染失敗！")
        return

    print(f"暫存 PDF 渲染成功：{os.path.getsize(abs_pdf):,} 位元組")

    # 讀取暫存 PDF 並建立 python-pptx 物件
    pdf_doc = pymupdf.open(abs_pdf)
    print(f"PyMuPDF 讀取 PDF 總頁數：{len(pdf_doc)} 頁")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    for page_idx in range(len(pdf_doc)):
        page = pdf_doc[page_idx]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        img_stream = io.BytesIO(img_bytes)

        slide = prs.slides.add_slide(blank_layout)
        slide.shapes.add_picture(img_stream, Inches(0), Inches(0), width=prs.slide_width, height=prs.slide_height)

        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = ""

        if page_idx < len(SLIDES_CONFIG):
            s_data = SLIDES_CONFIG[page_idx]
            tf.text = s_data.get("notes", "泰宇版 技術高中數學（第一冊）2-2 課堂教學用")

    prs.save(pptx_file)
    print(f"成功產出全新課堂教學簡報：{pptx_file} (檔案大小：{os.path.getsize(pptx_file):,} 位元組)")

    # 轉換為 Base64 並更新 docx_b64.py
    with open(pptx_file, "rb") as f:
        b64_pptx = base64.b64encode(f.read()).decode("utf-8")

    b64_student = ""
    b64_teacher = ""
    if os.path.exists("docx_b64.py"):
        with open("docx_b64.py", "r", encoding="utf-8") as f:
            content = f.read()
            m_s = re.search(r'(?:STUDENT_DOCX_B64|DOCX_STUDENT_B64|B64_STUDENT_DOCX)\s*=\s*"([^"]+)"', content)
            m_t = re.search(r'(?:TEACHER_DOCX_B64|DOCX_TEACHER_B64|B64_TEACHER_DOCX)\s*=\s*"([^"]+)"', content)
            if m_s: b64_student = m_s.group(1)
            if m_t: b64_teacher = m_t.group(1)

    with open("docx_b64.py", "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Base64 檔案內嵌模組 (自動由腳本生成)"""\n')
        f.write(f'STUDENT_DOCX_B64 = "{b64_student}"\n')
        f.write(f'TEACHER_DOCX_B64 = "{b64_teacher}"\n')
        f.write(f'B64_STUDENT_DOCX = "{b64_student}"\n')
        f.write(f'B64_TEACHER_DOCX = "{b64_teacher}"\n')
        f.write(f'PPTX_B64 = "{b64_pptx}"\n')
        f.write(f'B64_PPTX = "{b64_pptx}"\n')

    print("成功更新 docx_b64.py 中的 PPTX 簡報 Base64 資源！")

    # 清理暫存檔
    if os.path.exists(temp_pdf_file):
        try:
            pdf_doc.close()
            os.remove(temp_pdf_file)
            print(f"已清理暫存檔：{temp_pdf_file}")
        except Exception:
            pass

if __name__ == "__main__":
    main()
