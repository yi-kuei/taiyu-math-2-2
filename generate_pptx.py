# -*- coding: utf-8 -*-
"""
generate_pptx.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
課堂旗艦 16:9 全螢幕教學簡報生成器 (HTML + Edge Headless + PyMuPDF + python-pptx)

嚴格遵守使用者指示與教室投影教學核心原則：
1. 【版面防斷裂與滿版呈現】：
   - 全面調校字體級距、行距與間距，完美契合 16:9 頁面，絕對無內容溢出、斷裂或跨頁現象。
   - 大題單頁呈現，排版開闊大氣，後排學生視野清晰。
2. 【教學引導導向（不列出解答）】：
   - 例題、隨堂練習與習題：重點在於提供教學者上課引導學生思考與說明解題方式！
   - 列出【解題核心方向】與【輔助思考線索】，嚴格隱藏計算數值解答與最終答案，保留課堂互動啟發空間。
3. 【全 SVG 圖形輔助說明】：
   - 100% 配置直角三角形、坐標系、六角星陣、特別角等幾何圖形，強化幾何直觀與代數聯想。
4. 【規範統一】：
   - 全面採用「第一冊」標準標註。
   - 象牙米杏暖白護眼底色 (#fbf9f4 ~ #f7f3ea)，教室投影高對比不反光。
   - 47 頁全螢幕 16:9 滿版（13.333" x 7.5"），每頁皆含專屬講者備忘稿 (Speaker Notes)。
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
        "badge": "課堂教學專用 ‧ 啟發式引導 16:9 簡報",
        "desc": "掌握銳角三角比、六大函數定義、特別角精確值、神奇魔法六角形四大關係與常用三角恆等式",
        "notes": "【單元破案引言】\n各位小小偵探大家好！今天我們要深入直角三角形的幾何世界，解鎖高中數學最重要的符號——三角函數。讓我們用名偵探的敏銳目光，一步一步找出每個函數背後的密碼！"
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
        "notes": "【例題 1 講解指引】\n引導重點：\n1. 請學生先找出直角 C，確認斜邊是哪一條。\n2. 鎖定角 A 視角，辨識誰是「對邊」（對面）、誰是「鄰邊」（相鄰）。\n3. 先求主幹 sin, cos, tan，再引導倒數求出 csc, sec, cot。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 1",
        "title": "隨堂練習 1：視角切換至 ∠B 之六個三角函數值",
        "cards": [ALL_CARDS[6], ALL_CARDS[7]],
        "notes": "【隨堂 1 演練指引】\n引導重點：\n1. 視角由角 A 切換至角 B，提醒學生「斜邊不變，對邊與鄰邊的角色對調」！\n2. 讓學生比較與例題 1 的數值關聯，為後續餘角關係埋下伏筆。"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 2",
        "title": "例題 2：已知 cos A = 5/13，求其餘各三角函數值",
        "cards": [ALL_CARDS[8]],
        "notes": "【知一求其餘指引】\n引導重點：\n1. 知一三角比即可設直角三角形邊長參數：鄰邊 5k、斜邊 13k。\n2. 透過畢氏定理 √(13^2 - 5^2) 求出對邊 12k。\n3. 三邊比例確定後，其餘五個比值即可逐一寫出。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 2",
        "title": "隨堂練習 2：已知 tan A = 24/7，求其餘各三角函數值",
        "cards": [ALL_CARDS[9]],
        "notes": "【隨堂 2 演練指引】\n引導重點：\n1. 正切 tan = 對邊 / 鄰邊 = 24/7。\n2. 畢氏定理算出斜邊為 25k (7-24-25 畢氏數)。\n3. 依定義直接寫出其餘五大函數值。"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 3",
        "title": "例題 3：已知 sin A = 4/5 且 AB = 15，求邊長與各函數值",
        "cards": [ALL_CARDS[10]],
        "notes": "【比例與長度指引】\n引導重點：\n1. 區分「比值」與「實際長度」：sin A = 4/5 確立 3:4:5 幾何模型。\n2. 比值不隨縮放改變，故 cos A 與 tan A 直接可得。\n3. 斜邊 5k = 15 決定放大倍率 k = 3，進而求出實際邊長。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 3",
        "title": "隨堂練習 3：已知 csc A = 17/15 且 AC = 40，求邊長與各值",
        "cards": [ALL_CARDS[11]],
        "notes": "【隨堂 3 演練指引】\n引導重點：\n1. 餘割 csc = 斜邊 / 對邊 = 17/15，鄰邊即為 8。\n2. 鄰邊 8k = 40 導出縮放係數 k = 5。\n3. 依比例倍數求出實際長度與其他函數值。"
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
        "notes": "【特別角運算指引】\n引導重點：\n1. 第 (1) 小題直接調用 30°, 60°, 45° 函數值進行加減。\n2. 第 (2) 小題提醒：sin^2 45° 是平方函數值，不是平方角度！乘積項善用根號相消。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 4",
        "title": "隨堂練習 4：含根號與弳度特別角求值",
        "cards": [ALL_CARDS[17], ALL_CARDS[18]],
        "notes": "【隨堂 4 演練指引】\n引導重點：\n1. 第 (1) 小題代入根號係數運算，同類項合併。\n2. 第 (2) 小題提醒：遇到弳度量先轉換為度數 (π/4=45°, π/6=30°, π/3=60°)，再通分計算。"
    },
    {
        "kind": "big_problem",
        "tag": "生活科技例題 5",
        "title": "例題 5：內政部營建署無障礙坡道坡度夾角反推",
        "cards": [ALL_CARDS[19]],
        "notes": "【工程素養引導】\n引導重點：\n1. 坡度定義為 tan θ = 垂直上升 / 水平前進 = 1/8 = 0.125。\n2. 指導學生在工程計算機上切換 DEG 模式，按 2nd 鍵啟用 tan^(-1) 反三角函數。"
    },
    {
        "kind": "big_problem",
        "tag": "生活科技隨堂 5",
        "title": "隨堂練習 5：自行車道 20% 險升坡夾角反推",
        "cards": [ALL_CARDS[20]],
        "notes": "【生活應用引導】\n引導重點：\n1. 20% 百分比坡度代表水平前進 100 公尺、垂直上升 20 公尺。\n2. tan θ = 20/100 = 0.2，由計算機反推地面夾角。"
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
        "notes": "【秒殺題型引導】\n引導重點：\n1. (1) 辨識同角正弦與餘割之對角線倒數關係。\n2. (2) 辨識同角正弦平方與餘弦平方之平方和關係。\n3. (3) 由 1 + tan^2 = sec^2 進行移項變形。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 6",
        "title": "隨堂練習 6：倒數與平方綜合求值",
        "cards": [ALL_CARDS[29], ALL_CARDS[30], ALL_CARDS[31]],
        "notes": "【隨堂 6 演練引導】\n引導重點：\n1. (1) 餘弦與正割之倒數乘積。\n2. (2) 同角 80° 正餘弦平方和。\n3. (3) 警惕符號陷阱：1 + cot^2 = csc^2 移項為 cot^2 - csc^2 = -1！"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 7",
        "title": "例題 7：餘角轉化與恆等混合求值",
        "cards": [ALL_CARDS[32]],
        "notes": "【非特別角化簡引導】\n引導重點：\n1. 尋找相加 90° 的互餘角配對：40° 與 50°、72° 與 18°。\n2. 餘角互換將 tan 50° 化為 cot 40°，csc 18° 化為 sec 72°。\n3. 套用倒數與平方變形關係快速化簡。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 7",
        "title": "隨堂練習 7：餘角平方和與平方差混合求值",
        "cards": [ALL_CARDS[33]],
        "notes": "【隨堂 7 演練引導】\n引導重點：\n1. 第一組：35° 與 55° 互餘，cos 55° = sin 35° 構成同角平方和。\n2. 第二組：47° 與 43° 互餘，tan 43° = cot 47° 構成 csc^2 - cot^2 平方差。"
    },
    {
        "kind": "big_problem",
        "tag": "課本例題 8",
        "title": "例題 8：已知 tan θ = 2，求一次齊次分式之值",
        "cards": [ALL_CARDS[34]],
        "notes": "【齊次同除神技引導】\n引導重點：\n1. 觀察分子分母均為 sin, cos 的一次齊次式。\n2. 分子分母同除以 cos θ，利用商數關係將 sin/cos 全化為 tan θ。\n3. 強調此法完全無需計算斜邊長度，極為迅速！"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 8",
        "title": "隨堂練習 8：已知 cot θ = 2/3，求一次齊次分式之值",
        "cards": [ALL_CARDS[35]],
        "notes": "【隨堂 8 演練引導】\n引導重點：\n1. 已知條件為 cot θ，導引學生思考「同除以 sin θ」化為 cot θ。\n2. 代入分式進行通分運算。"
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
        "notes": "【連環解題架構引導】\n引導重點：\n1. (1)「見和必平方」：等式兩邊平方，利用 (sin+cos)^2 = 1 + 2sin cos 解出乘積。\n2. (2) 將切和 tan+cot 通分為 1/(sin cos)，由上一小題結果直接倒數求解。"
    },
    {
        "kind": "big_problem",
        "tag": "隨堂實戰 9",
        "title": "隨堂練習 9：差平方連環扣求乘積與切和",
        "cards": [ALL_CARDS[39], ALL_CARDS[40]],
        "notes": "【差平方實戰引導】\n引導重點：\n1. (1) 差平方展開：(sin-cos)^2 = 1 - 2sin cos，移項求乘積。\n2. (2) 同樣透過 tan+cot = 1/(sin cos) 倒數求切和。"
    },

    # =========================================================
    # 第五階段：章末課後習題篇 (觀念是非、基礎題、進階題)
    # =========================================================
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (1)",
        "title": "習題 觀念 (1)：已知銳角正弦是否可求其餘五個函數值？",
        "cards": [ALL_CARDS[41]],
        "notes": "【觀念思辨 1】\n引導學生回想知一求其餘模型：sin θ 確定對邊與斜邊比例，畢氏定理確定鄰邊比例，因此其餘五值皆可解。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (2)",
        "title": "習題 觀念 (2)：已知 sin A = 3/5 是否可求出三邊長度？",
        "cards": [ALL_CARDS[42]],
        "notes": "【觀念思辨 2】\n引導學生分辨「比值」與「長度」之差異，若無給定任何邊長實際數值，三角形可任意縮放，長度無法確定。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (3)",
        "title": "習題 觀念 (3)：不同銳角平方和是否必等於 1？",
        "cards": [ALL_CARDS[43]],
        "notes": "【觀念思辨 3】\n引導學生注意平方關係公式前題：必須是「同角」！舉出 α=30°, β=60° 之反例檢驗。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (4)",
        "title": "習題 觀念 (4)：銳角 sin θ × cos θ 是否必等於 1？",
        "cards": [ALL_CARDS[44]],
        "notes": "【觀念思辨 4】\n引導學生澄清倒數伴侶概念：與 sin 乘積為 1 的是 csc，而非 cos。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 觀念 (5)",
        "title": "習題 觀念 (5)：和平方展開是否可省略交叉項？",
        "cards": [ALL_CARDS[45]],
        "notes": "【觀念思辨 5】\n引導乘法公式嚴密展開：(a+b)^2 = a^2 + 2ab + b^2，不可漏掉 2sin cos 交叉項。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 1",
        "title": "基礎題 1：已知直角三角形 sin A = 3/5，求 tan A + sec A",
        "cards": [ALL_CARDS[46]],
        "notes": "【基礎 1 解題指引】\n引導重點：\n1. 由 sin A = 3/5 建立 3-4-5 直角三角形比例。\n2. 分別寫出 tan A 與 sec A 之分式後相加化簡。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 2",
        "title": "基礎題 2：tan A = 12/5 且 AB = 26，求 sin A 與 AC",
        "cards": [ALL_CARDS[47], ALL_CARDS[48]],
        "notes": "【基礎 2 解題指引】\n引導重點：\n1. (1) tan A = 12/5 確定 5-12-13 比例，sin A 只看比例，與長度無關。\n2. (2) 由斜邊 13k = 26 算出比例放大倍率 k = 2，進而求出鄰邊 AC。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 3",
        "title": "基礎題 3：特別角四則與弳度乘積求值",
        "cards": [ALL_CARDS[49], ALL_CARDS[50]],
        "notes": "【基礎 3 解題指引】\n引導重點：\n1. (1) 分別提取 30°, 45°, 60° 特別角代入運算。\n2. (2) 將弳度化為角度，觀察兩括號結構利用平方差公式 (a+b)(a-b) 快速求值。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 4",
        "title": "基礎題 4：餘角與平方關係綜合求值",
        "cards": [ALL_CARDS[51]],
        "notes": "【基礎 4 解題指引】\n引導重點：\n1. 尋找餘角配對：將 70° 全部化為 20°。\n2. 分成 cos^2+sin^2 與 tan^2-sec^2 兩組平方關係化簡。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 5",
        "title": "基礎題 5：和平方加差平方之化簡",
        "cards": [ALL_CARDS[52]],
        "notes": "【基礎 5 解題指引】\n引導重點：\n1. 令角度為 θ，展開 (sin+cos)^2 與 (sin-cos)^2。\n2. 觀察交叉項 +2sincos 與 -2sincos 相互抵消，與具體角度無關！"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 6",
        "title": "基礎題 6：已知 cot θ = 5/12，求齊次分式之值",
        "cards": [ALL_CARDS[53]],
        "notes": "【基礎 6 解題指引】\n引導重點：\n1. 一次齊次分式同除神法：分子分母同除以 sin θ。\n2. 整體化為 cot θ 代入計算。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 基礎 7",
        "title": "基礎題 7：已知 sin θ - cos θ = 1/2，求乘積與切和",
        "cards": [ALL_CARDS[54], ALL_CARDS[55]],
        "notes": "【基礎 7 解題指引】\n引導重點：\n1. (1) 差平方展開求乘積 sin cos。\n2. (2) 切和 tan+cot 直接為乘積之倒數。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 進階 8",
        "title": "進階題 8：通分平方差求分式和",
        "cards": [ALL_CARDS[56]],
        "notes": "【進階 8 解題指引】\n引導重點：\n1. 兩分式通分相加：分母為 (1+sin)(1-sin) = 1 - sin^2 = cos^2。\n2. 分子交叉項相消得 2，原式簡化為 2 / cos^2 θ 後代入計算。"
    },
    {
        "kind": "big_problem",
        "tag": "課本習題 進階 9",
        "title": "進階題 9：切和求乘積、和與立方和",
        "cards": [ALL_CARDS[57], ALL_CARDS[58], ALL_CARDS[59]],
        "notes": "【進階 9 解題指引】\n引導重點：\n1. (1) 切和倒數求乘積 sin cos。\n2. (2) 利用 (sin+cos)^2 = 1 + 2sin cos 開根號求和。\n3. (3) 利用立方和因式分解 a^3 + b^3 = (a+b)(1 - ab) 直接代入求值。"
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

def clean_guidance_text(text):
    """清理多餘字眼，保留乾淨的引導方向"""
    text = re.sub(r'^🕵️\s*柯南破案導引[：:]\s*', '', text)
    text = re.sub(r'^線索\s*\d+[：:]\s*', '', text)
    return text.strip()

def render_concept_slide(slide_cfg, idx, total_slides):
    card = slide_cfg["card"]
    badge = slide_cfg.get("badge", "核心概念")
    title = slide_cfg.get("title", card["title"])
    front = card["front_content"]
    svg_html = card.get("svg", "")

    steps_html = "".join([f"""
      <div class="p-2.5 rounded-xl bg-white border border-amber-200 shadow-2xs">
        <div class="text-base font-black text-amber-900 mb-0.5">【{s['title']}】</div>
        <div class="text-base text-slate-800 leading-normal font-medium">{s['content']}</div>
      </div>
    """ for s in card.get("steps", [])])

    return f"""
  <div class="slide-page">
    <!-- 頂部標題區 -->
    <div class="flex items-center justify-between mb-2 border-b-2 border-amber-300 pb-1.5">
      <div class="flex items-center gap-3">
        <span class="px-3 py-1 rounded-lg text-sm font-black bg-amber-600 text-white shadow-xs">{badge}</span>
        <h2 class="text-2xl font-black text-amber-950 tracking-tight">{title}</h2>
      </div>
      <div class="text-sm font-bold text-amber-800 bg-amber-100/80 px-2.5 py-0.5 rounded-md">{card.get('page', '課本概念')}</div>
    </div>

    <!-- 雙欄主體內容：左欄 60% 概念與重點 / 右欄 40% 精密集幾何圖解 -->
    <div class="grid grid-cols-12 gap-4 flex-1 items-stretch my-1 overflow-hidden">
      <!-- 左欄 -->
      <div class="col-span-7 flex flex-col justify-between space-y-2">
        <div class="p-3.5 rounded-xl bg-amber-50/90 border-2 border-amber-300 text-lg font-bold text-slate-900 leading-snug shadow-2xs">
          {front}
        </div>
        <div class="space-y-2 flex-1">
          {steps_html}
        </div>
        <div class="p-2.5 rounded-lg bg-emerald-50 border border-emerald-400 text-base font-black text-emerald-900 text-center">
          {card.get('conclusion', '【核心歸納】掌握幾何比例與恆等定義即破案！')}
        </div>
      </div>

      <!-- 右欄：滿版清晰幾何 SVG 輔助說明 -->
      <div class="col-span-5 flex flex-col justify-center items-center p-3 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
        <div class="w-full h-full max-h-[140mm] flex items-center justify-center">
          {svg_html}
        </div>
        <div class="mt-1.5 text-xs font-bold text-slate-500 text-center">▲ 幾何模型輔助視覺解析</div>
      </div>
    </div>

    <!-- 頁尾 -->
    <div class="flex items-center justify-between pt-1.5 border-t border-amber-200 text-xs text-slate-500 font-medium">
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

    # 根據小題數量切分版面，嚴格不列出數值解答，列出解題重要方向與圖形
    if num_cards == 1:
        # 單題（單小題）：大題幹 + 雙欄 (左: 題目與教學解題方向 / 右: SVG圖形輔助)
        c = cards[0]
        tip_text = clean_guidance_text(c.get("front_tip", ""))

        guidance_items = []
        if tip_text:
            guidance_items.append(f"""
              <div class="p-2.5 rounded-xl bg-amber-50/90 border border-amber-300 text-base text-amber-950 leading-relaxed shadow-2xs font-bold">
                <span class="text-amber-700 font-black">💡 思考核心：</span>{tip_text}
              </div>
            """)

        for s in c.get("steps", []):
            stitle = clean_guidance_text(s['title'])
            guidance_items.append(f"""
              <div class="p-2.5 rounded-xl bg-white border border-slate-200 text-base text-slate-800 leading-relaxed shadow-2xs">
                <span class="font-bold text-blue-900">▸ 解題步驟：</span>{stitle}
              </div>
            """)

        guidance_html = "".join(guidance_items)

        body_html = f"""
        <div class="grid grid-cols-12 gap-4 flex-1 items-stretch my-1 overflow-hidden">
          <div class="col-span-7 flex flex-col justify-between space-y-2.5">
            <div>
              <div class="text-xs font-bold text-slate-400 mb-1">【題目描述】</div>
              <div class="p-3.5 rounded-xl bg-amber-50/70 border-2 border-amber-200 text-xl font-bold text-slate-900 leading-snug shadow-2xs">
                {c['front_content']}
              </div>
            </div>
            <div class="space-y-2 flex-1">
              <div class="text-xs font-black text-amber-800 uppercase tracking-wider">【解題方向與思考策略 ‧ 課堂討論】</div>
              {guidance_html}
            </div>
            <div class="p-2.5 rounded-xl bg-blue-50 border border-blue-400 text-base font-black text-blue-900 text-center shadow-xs">
              🎯 教學引導提示：引導學生依線索方向思考，動筆推導出最終解答！
            </div>
          </div>
          <div class="col-span-5 flex flex-col justify-center items-center p-3 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
            <div class="w-full h-full max-h-[140mm] flex items-center justify-center">
              {c.get('svg', '')}
            </div>
            <div class="mt-1.5 text-xs font-bold text-slate-500 text-center">▲ 幾何輔助解題模型</div>
          </div>
        </div>
        """
    elif num_cards == 2:
        # 兩小題：兩欄並列（左邊第 1 小題、右邊第 2 小題，各自包含題幹、重要解題方向與圖形）
        cols_html = []
        for i, c in enumerate(cards):
            tip_text = clean_guidance_text(c.get("front_tip", ""))
            step_dirs = [clean_guidance_text(s['title']) for s in c.get("steps", [])]

            dir_list_html = "".join([f"""
              <li class="text-sm text-slate-700 leading-relaxed font-medium">▸ {sd}</li>
            """ for sd in step_dirs])

            cols_html.append(f"""
            <div class="col-span-6 flex flex-col justify-between p-3.5 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
              <div>
                <div class="flex items-center justify-between mb-1.5 pb-1 border-b border-amber-200">
                  <span class="px-2.5 py-0.5 rounded text-xs font-black bg-amber-700 text-white">第 ({i+1}) 小題</span>
                  <span class="text-xs font-bold text-slate-400">{c.get('page', '')}</span>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 text-lg font-bold text-slate-900 mb-2 leading-snug">
                  {c['front_content']}
                </div>
                <div class="p-2 rounded-lg bg-amber-50/70 border border-amber-200 text-sm text-amber-950 font-bold mb-1.5">
                  💡 關鍵方向：{tip_text}
                </div>
                <ul class="space-y-1 my-1 px-1">
                  {dir_list_html}
                </ul>
              </div>
              <div>
                <div class="h-32 w-full flex items-center justify-center my-1 bg-amber-50/30 rounded-lg p-1 border border-amber-100">
                  {c.get('svg', '')}
                </div>
                <div class="p-1.5 rounded-lg bg-blue-50 border border-blue-300 text-xs font-black text-blue-900 text-center">
                  🎯 教師引導學生由圖形三邊比推算答案
                </div>
              </div>
            </div>
            """)
        body_html = f"""
        <div class="grid grid-cols-12 gap-3.5 flex-1 items-stretch my-1 overflow-hidden">
          {''.join(cols_html)}
        </div>
        """
    else:
        # 三小題：三欄並列（第 1, 2, 3 小題並列，例如例題 6、隨堂 6、進階 9）
        cols_html = []
        for i, c in enumerate(cards):
            tip_text = clean_guidance_text(c.get("front_tip", ""))
            step_dirs = [clean_guidance_text(s['title']) for s in c.get("steps", [])]

            dir_list_html = "".join([f"""
              <li class="text-xs text-slate-700 leading-tight font-medium">▸ {sd}</li>
            """ for sd in step_dirs])

            cols_html.append(f"""
            <div class="col-span-4 flex flex-col justify-between p-3 rounded-2xl bg-white border-2 border-amber-200 shadow-sm">
              <div>
                <div class="flex items-center justify-between mb-1 pb-1 border-b border-amber-200">
                  <span class="px-2 py-0.5 rounded text-xs font-black bg-amber-700 text-white">第 ({i+1}) 小題</span>
                  <span class="text-2xs font-bold text-slate-400">{c.get('page', '')}</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-50 border border-slate-200 text-base font-bold text-slate-900 mb-1.5 leading-snug">
                  {c['front_content']}
                </div>
                <div class="p-1.5 rounded-md bg-amber-50/70 border border-amber-200 text-xs text-amber-950 font-bold mb-1">
                  💡 核心：{tip_text}
                </div>
                <ul class="space-y-0.5 my-1 px-1">
                  {dir_list_html}
                </ul>
              </div>
              <div>
                <div class="h-28 w-full flex items-center justify-center my-1 bg-amber-50/30 rounded-lg p-1 border border-amber-100">
                  {c.get('svg', '')}
                </div>
                <div class="p-1 rounded bg-blue-50 border border-blue-300 text-2xs font-black text-blue-900 text-center">
                  🎯 啟發學生套用星陣化簡求值
                </div>
              </div>
            </div>
            """)
        body_html = f"""
        <div class="grid grid-cols-12 gap-3 flex-1 items-stretch my-1 overflow-hidden">
          {''.join(cols_html)}
        </div>
        """

    return f"""
  <div class="slide-page">
    <!-- 頂部標題區 -->
    <div class="flex items-center justify-between mb-2 border-b-2 border-amber-300 pb-1.5">
      <div class="flex items-center gap-3">
        <span class="px-3 py-1 rounded-lg text-sm font-black bg-red-600 text-white shadow-xs">{tag}</span>
        <h2 class="text-2xl font-black text-amber-950 tracking-tight">{title}</h2>
      </div>
      <div class="text-xs font-bold text-slate-500 bg-amber-100/70 px-2.5 py-0.5 rounded-md">課堂教學 ‧ 解題思考方向引導</div>
    </div>

    <!-- 主體內容 -->
    {body_html}

    <!-- 頁尾 -->
    <div class="flex items-center justify-between pt-1.5 border-t border-amber-200 text-xs text-slate-500 font-medium">
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
      padding: 12mm 18mm 8mm 18mm;
      background: #fbf9f4; /* 象牙米杏暖白護眼底色 */
    }
    .katex, .katex-html, .katex-display {
      white-space: nowrap !important;
      font-size: 1.25em !important;
      font-weight: 700 !important;
    }
    .katex-display {
      margin: 0.1em 0 !important;
      display: inline-block !important;
    }
    /* 避免任何捲軸或文字溢出斷裂 */
    * {
      box-sizing: border-box;
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
              <span class="px-6 py-2 rounded-full text-base font-black bg-amber-600 text-white shadow-md mb-6 tracking-wide">
                {cfg['badge']}
              </span>
              <h1 class="text-5xl font-black text-amber-950 mb-5 tracking-tight leading-tight">
                {cfg['title']}
              </h1>
              <p class="text-2xl font-bold text-amber-800 mb-6">
                {cfg['subtitle']}
              </p>
              <div class="max-w-4xl p-5 rounded-2xl bg-amber-50 border-2 border-amber-300 text-slate-800 text-xl font-medium shadow-sm leading-relaxed">
                {cfg['desc']}
              </div>
            </div>
            """
            html += f"""
            <div class="slide-page">
              {content_html}
              <div class="flex items-center justify-between pt-1.5 border-t border-amber-200 text-xs text-slate-500 font-medium">
                <div>泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質</div>
                <div>投影片 {idx+1} / {total}</div>
                <div>PLVS 數學科  教育學習用</div>
              </div>
            </div>
            """
        elif kind == "roadmap":
            mods_html = "".join([f"""
              <div class="p-5 rounded-2xl bg-white border-2 border-amber-200 shadow-sm flex flex-col justify-between">
                <div>
                  <span class="px-2.5 py-0.5 rounded text-xs font-black bg-amber-600 text-white">{m['num']}</span>
                  <h3 class="text-xl font-black text-amber-950 mt-2 mb-1.5">{m['title']}</h3>
                  <p class="text-base text-slate-700 leading-relaxed">{m['desc']}</p>
                </div>
              </div>
            """ for m in cfg['modules']])
            content_html = f"""
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <span class="text-xs font-black text-amber-700 tracking-wider">ROADMAP</span>
                <h2 class="text-3xl font-black text-amber-950 mb-1">{cfg['title']}</h2>
                <p class="text-base text-slate-600 mb-3">{cfg['subtitle']}</p>
              </div>
              <div class="grid grid-cols-4 gap-4 flex-1 items-stretch my-2">
                {mods_html}
              </div>
            </div>
            """
            html += f"""
            <div class="slide-page">
              {content_html}
              <div class="flex items-center justify-between pt-1.5 border-t border-amber-200 text-xs text-slate-500 font-medium">
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
