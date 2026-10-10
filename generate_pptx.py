# -*- coding: utf-8 -*-
"""
generate_pptx.py - 泰宇版 技術高中數學（第二冊）2-2 三角函數的定義與性質
教學專案 16:9 簡報生成器 (HTML + Edge Headless + PyMuPDF + python-pptx)
遵循《SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版》規範：
1. 16:9 滿版渲染 (338.67mm x 190.5mm / 13.333" x 7.5")，0 邊距滿版貼合無黑邊
2. 象牙米杏暖白護眼底色 (#fbf9f4 ~ #f7f3ea)，教室投影高對比不反光
3. 教室投影特大字型：標題 36~44pt、題幹 26~30pt、推理鏈 22~24pt、結論 28~32pt
4. 一張投影片一個重點，課本核心隨堂練習與例題成對呼應放入簡報
5. 全面 KaTeX 渲染（全域放大 145%，嚴禁純文字 ASCII）
6. 每頁配置專屬教學備忘 Speaker Notes
7. 自動將 PPTX 轉為 Base64 寫入 docx_b64.py
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

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE_EXE = next((p for p in EDGE_PATHS if os.path.exists(p)), None)

LESSON_SLIDES = [
    # 1. 封面
    {
        "type": "cover",
        "title": "2-2 三角函數的定義與性質",
        "subtitle": "泰宇版 ‧ 技術型高級中等學校數學 第二冊 ‧ 第二章 三角函數",
        "badge": "名偵探柯南數理特訓簡報",
        "desc": "掌握銳角三角比、六角星四大恆等關係、特別角精確值與生活坡度工程模型",
        "notes": "【單元破案引言】\n各位小小偵探大家好！今天我們要深入直角三角形的幾何世界，解鎖高中數學最重要的符號——三角函數。真相永遠只有一個，讓我們用名偵探的敏銳目光，一步一步找出每個函數背後的密碼！"
    },
    # 2. 地圖
    {
        "type": "roadmap",
        "title": "單元探案學習地圖",
        "subtitle": "循序漸進 ‧ 四大階段破案路線圖",
        "modules": [
            {"num": "階段一", "title": "銳角三角函數定義", "desc": "正三角形對折、六大函數邊長比、知一求其餘"},
            {"num": "階段二", "title": "特別角與生活工程", "desc": "30°-45°-60° 精確值、弳度換算、坡度反三角函數"},
            {"num": "階段三", "title": "六角星四大恆等關係", "desc": "倒數、商數、平方、餘角四大星陣化簡神技"},
            {"num": "階段四", "title": "三角恆等式與章末實戰", "desc": "和差平方連環扣、切和倒數、齊次同除、是非與進階"}
        ],
        "notes": "【地圖導讀】\n全班請看路線圖：我們先從直角三角形三邊比建立六大函數定義；接著熟背 30°、45°、60° 特別角；然後掌握神奇魔法六角形四大關係；最後攻克和差平方連環扣與章末實戰！"
    },
    # 3. 模組一章頭
    {
        "type": "section",
        "section_num": "STAGE 01",
        "title": "銳角三角函數的定義與邊長比",
        "desc": "直角三角形三邊如何角色定位？為什麼邊長放大縮小比值卻不變？",
        "notes": "進入第一階段：強調三角比是「比值」而非「長度」，與三角形相似密切相關。"
    },
    # 4. 定義觀念
    {
        "type": "concept",
        "tag": "核心定義",
        "title": "銳角三角函數的六大邊長比定義",
        "highlight": "直角三角形中，角 θ 的斜邊為 r、對邊為 y、鄰邊為 x",
        "points": [
            "正弦：$\\sin\\theta = \\frac{y}{r} = \\frac{\\text{對邊}}{\\text{斜邊}}$ ； 餘割：$\\csc\\theta = \\frac{r}{y} = \\frac{\\text{斜邊}}{\\text{對邊}}$（倒數）",
            "餘弦：$\\cos\\theta = \\frac{x}{r} = \\frac{\\text{鄰邊}}{\\text{斜邊}}$ ； 正割：$\\sec\\theta = \\frac{r}{x} = \\frac{\\text{斜邊}}{\\text{鄰邊}}$（倒數）",
            "正切：$\\tan\\theta = \\frac{y}{x} = \\frac{\\text{對邊}}{\\text{鄰邊}}$ ； 餘切：$\\cot\\theta = \\frac{x}{y} = \\frac{\\text{鄰邊}}{\\text{對邊}}$（倒數）"
        ],
        "tip": "★ 記憶密碼：牢記 sin、cos、tan 三原形，倒數即得 csc、sec、cot！",
        "notes": "【板書重點】\n帶領學生用手指比劃：sin 是從斜邊滑向對邊、cos 是從斜邊繞過角度滑向鄰邊、tan 是從鄰邊走向對邊。"
    },
    # 5. 例題 1 講解
    {
        "type": "problem",
        "tag": "課本例題 1",
        "title": "例題 1：直角三角形三邊已知求 ∠A 之六個函數值",
        "question": "在直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$。已知 $AC = 8$、$BC = 15$、$AB = 17$。<br>試求出 $\\angle A$ 的六個三角函數值。",
        "steps": [
            "線索 1：鎖定 $\\angle A$ 視角：斜邊 $r = 17$、對邊 $y = 15$、鄰邊 $x = 8$。",
            "線索 2：求前三主幹函數：$\\sin A = \\frac{15}{17}$，$\\cos A = \\frac{8}{17}$，$\\tan A = \\frac{15}{8}$。",
            "線索 3：倒數求伴隨函數：$\\csc A = \\frac{17}{15}$，$\\sec A = \\frac{17}{8}$，$\\cot A = \\frac{8}{15}$。"
        ],
        "conclusion": "CASE CLOSED：$\\sin A=\\frac{15}{17}, \\cos A=\\frac{8}{17}, \\tan A=\\frac{15}{8}, \\csc A=\\frac{17}{15}, \\sec A=\\frac{17}{8}, \\cot A=\\frac{8}{15}$",
        "notes": "【解題引導】\n提醒學生務必先確認「對邊」是哪一條（角 A 正對面的 BC），「鄰邊」是哪一條（與角 A 相鄰且構成直角的 AC）。"
    },
    # 6. 隨堂 1 呼應
    {
        "type": "problem",
        "tag": "隨堂實戰 1",
        "title": "隨堂練習 1：視角切換至 ∠B 之六個三角函數值",
        "question": "承例題 1，直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$，$AC = 8, BC = 15, AB = 17$。<br>試求出 <b>$\\angle B$</b> 的六個三角函數值。",
        "steps": [
            "線索 1：視角切換至 $\\angle B$！對邊轉變為 $AC = 8$，鄰邊轉變為 $BC = 15$，斜邊仍為 $17$。",
            "線索 2：前三大函數：$\\sin B = \\frac{8}{17}$，$\\cos B = \\frac{15}{17}$，$\\tan B = \\frac{8}{15}$。",
            "線索 3：倒數三大函數：$\\csc B = \\frac{17}{8}$，$\\sec B = \\frac{17}{15}$，$\\cot B = \\frac{15}{8}$。"
        ],
        "conclusion": "CASE CLOSED：$\\sin B=\\frac{8}{17}, \\cos B=\\frac{15}{17}, \\tan B=\\frac{8}{15}, \\csc B=\\frac{17}{8}, \\sec B=\\frac{17}{15}, \\cot B=\\frac{15}{8}$",
        "notes": "【觀察引導】\n請同學對照例題 1 與隨堂 1：$\\sin A = \\cos B$、$\\cos A = \\sin B$、$\\tan A = \\cot B$！這就是之後要學的餘角關係！"
    },
    # 7. 例題 2 講解
    {
        "type": "problem",
        "tag": "課本例題 2",
        "title": "例題 2：已知 cos A = 5/13，求 ∠A 其餘各函數值",
        "question": "已知直角三角形 $ABC$ 中，$\\angle C$ 為直角，且 $\\cos A = \\frac{5}{13}$。<br>求 $\\angle A$ 其餘各三角函數值。",
        "steps": [
            "線索 1：設比值參數：鄰邊 $AC = 5k$、斜邊 $AB = 13k$（$k > 0$）。",
            "線索 2：利用畢氏定理求對邊：$BC = \\sqrt{(13k)^2 - (5k)^2} = \\sqrt{144k^2} = 12k$。",
            "線索 3：計算其餘五值：$\\sin A = \\frac{12}{13}$，$\\tan A = \\frac{12}{5}$，$\\csc A = \\frac{13}{12}$，$\\sec A = \\frac{13}{5}$，$\\cot A = \\frac{5}{12}$。"
        ],
        "conclusion": "CASE CLOSED：$\\sin A=\\frac{12}{13}, \\tan A=\\frac{12}{5}, \\csc A=\\frac{13}{12}, \\sec A=\\frac{13}{5}, \\cot A=\\frac{5}{12}$",
        "notes": "【破案技巧】\n知一求其餘，永遠先畫一個直角三角形，標上邊長比例，畢氏定理一算，其餘五個馬上現形！"
    },
    # 8. 隨堂 2 呼應
    {
        "type": "problem",
        "tag": "隨堂實戰 2",
        "title": "隨堂練習 2：已知 tan A = 24/7，求 ∠A 其餘各函數值",
        "question": "已知直角三角形 $ABC$ 中，$\\angle C = 90^\\circ$，且 $\\tan A = \\frac{24}{7}$。<br>求 $\\angle A$ 其餘各三角函數值。",
        "steps": [
            "線索 1：設對邊 $BC = 24k$、鄰邊 $AC = 7k$。",
            "線索 2：畢氏定理求斜邊：$AB = \\sqrt{(24k)^2 + (7k)^2} = \\sqrt{625k^2} = 25k$。",
            "線索 3：寫出其餘五值：$\\sin A = \\frac{24}{25}$，$\\cos A = \\frac{7}{25}$，$\\csc A = \\frac{25}{24}$，$\\sec A = \\frac{25}{7}$，$\\cot A = \\frac{7}{24}$。"
        ],
        "conclusion": "CASE CLOSED：$\\sin A=\\frac{24}{25}, \\cos A=\\frac{7}{25}, \\csc A=\\frac{25}{24}, \\sec A=\\frac{25}{7}, \\cot A=\\frac{7}{24}$",
        "notes": "【學生演練】\n讓學生自行計算 (7, 24, 25) 勾股數，提醒斜邊為 25。"
    },
    # 9. 例題 3 講解
    {
        "type": "problem",
        "tag": "課本例題 3",
        "title": "例題 3：已知比例與一邊長，求實際邊長與各函數值",
        "question": "直角三角形 $ABC$ 中，$\\angle C = 90^\\circ$，且 $\\sin A = \\frac{4}{5}$。<br>若斜邊 $AB = 15$，求 $\\cos A$、$\\tan A$、$BC$ 與 $AC$ 之長。",
        "steps": [
            "線索 1：由 $\\sin A = \\frac{4}{5}$，得邊長比 $3k : 4k : 5k$。$\\cos A = \\frac{3}{5}, \\tan A = \\frac{4}{3}$。",
            "線索 2：斜邊實際長度 $AB = 15 = 5k \\implies k = 3$（放大 3 倍）。",
            "線索 3：計算實際邊長：對邊 $BC = 4(3) = 12$，鄰邊 $AC = 3(3) = 9$。"
        ],
        "conclusion": "CASE CLOSED：$\\cos A = \\frac{3}{5}, \\tan A = \\frac{4}{3}, BC = 12, AC = 9$",
        "notes": "【概念釐清】\n再次強化：函數值是「比值」（不隨放大改變），邊長是「實際長度」（依比例 k 縮放）。"
    },
    # 10. 隨堂 3 呼應
    {
        "type": "problem",
        "tag": "隨堂實戰 3",
        "title": "隨堂練習 3：已知 csc A = 17/15 且 AC = 40，求邊長與函數值",
        "question": "直角三角形 $ABC$ 中，$\\angle C = 90^\\circ$，且 $\\csc A = \\frac{17}{15}$。<br>若 $AC = 40$，求 $\\tan A$、$\\sec A$、$AB$ 與 $BC$ 之長。",
        "steps": [
            "線索 1：$\\csc A = \\frac{17}{15} \\implies \\sin A = \\frac{15}{17}$，三邊比為 $8k : 15k : 17k$。",
            "線索 2：已知鄰邊 $AC = 8k = 40 \\implies k = 5$（放大 5 倍）。",
            "線索 3：實際邊長：$AB = 17(5) = 85$，$BC = 15(5) = 75$；$\\tan A = \\frac{15}{8}$，$\\sec A = \\frac{17}{8}$。"
        ],
        "conclusion": "CASE CLOSED：$\\tan A = \\frac{15}{8}, \\sec A = \\frac{17}{8}, AB = 85, BC = 75$",
        "notes": "【計算提示】\n$\\csc A$ 即斜邊除以對邊，鄰邊為 8k，由 $8k = 40$ 得 $k = 5$。"
    },
    # 11. 模組二章頭
    {
        "type": "section",
        "section_num": "STAGE 02",
        "title": "特別角精確值與生活科技反推",
        "desc": "30°、45°、60° 必背幾何模型，以及計算機反推工程坡度",
        "notes": "進入第二階段：特別角是高中數學最常出題的基石，必須達到反射神經級別的熟練度。"
    },
    # 12. 特別角彙整
    {
        "type": "concept",
        "tag": "速記秘技",
        "title": "特別角 30°、45°、60° 精確值神技速記",
        "highlight": "正弦分子遞增：√1 / 2 ➔ √2 / 2 ➔ √3 / 2 ； 餘弦分子逆序遞減",
        "points": [
            "$30^\\circ = \\frac{\\pi}{6}$：$\\sin=\\frac{1}{2}, \\cos=\\frac{\\sqrt{3}}{2}, \\tan=\\frac{\\sqrt{3}}{3}, \\cot=\\sqrt{3}, \\sec=\\frac{2\\sqrt{3}}{3}, \\csc=2$",
            "$45^\\circ = \\frac{\\pi}{4}$：$\\sin=\\frac{\\sqrt{2}}{2}, \\cos=\\frac{\\sqrt{2}}{2}, \\tan=1, \\cot=1, \\sec=\\sqrt{2}, \\csc=\\sqrt{2}$",
            "$60^\\circ = \\frac{\\pi}{3}$：$\\sin=\\frac{\\sqrt{3}}{2}, \\cos=\\frac{1}{2}, \\tan=\\sqrt{3}, \\cot=\\frac{\\sqrt{3}}{3}, \\sec=2, \\csc=\\frac{2\\sqrt{3}}{3}$"
        ],
        "tip": "★ 口訣：sin 分子 1, 2, 3 根號開，分母恆為 2；cos 剛好倒過來！",
        "notes": "【課堂互動】\n請全班背誦正弦三兄弟：二分之一、二分之根號二、二分之根號三。"
    },
    # 13. 例題 4 講解
    {
        "type": "problem",
        "tag": "課本例題 4",
        "title": "例題 4：特別角四則運算求值",
        "question": "試求下列各式之值：<br>(1) $\\sin 30^\\circ - \\cos 60^\\circ + \\tan 45^\\circ$<br>(2) $2\\sin^2 45^\\circ + \\cot 30^\\circ \\csc 60^\\circ$",
        "steps": [
            "線索 1：第 (1) 小題代入：$\\frac{1}{2} - \\frac{1}{2} + 1 = 1$。",
            "線索 2：第 (2) 小題平方項：$2\\left(\\frac{1}{\\sqrt{2}}\\right)^2 = 2 \\times \\frac{1}{2} = 1$。",
            "線索 3：第 (2) 小題乘積項：$\\sqrt{3} \\times \\frac{2}{\\sqrt{3}} = 2$。合計 $1 + 2 = 3$。"
        ],
        "conclusion": "CASE CLOSED：(1) 原式 = 1  ；  (2) 原式 = 3",
        "notes": "【常犯錯誤】\n提醒：$\\sin^2 45^\\circ$ 是 $(\\sin 45^\\circ)^2$，平方的是函數值，不是角度！"
    },
    # 14. 隨堂 4 呼應
    {
        "type": "problem",
        "tag": "隨堂實戰 4",
        "title": "隨堂練習 4：根號與弳度量混合求值",
        "question": "試求下列各式之值：<br>(1) $2\\sin 60^\\circ - \\sqrt{2}\\cos 45^\\circ + \\tan 60^\\circ$<br>(2) $\\sin^2 \\frac{\\pi}{4} + \\cos^2 \\frac{\\pi}{6} - \\cot^2 \\frac{\\pi}{3}$",
        "steps": [
            "線索 1：第 (1) 小題代入：$2\\left(\\frac{\\sqrt{3}}{2}\\right) - \\sqrt{2}\\left(\\frac{\\sqrt{2}}{2}\\right) + \\sqrt{3} = \\sqrt{3} - 1 + \\sqrt{3} = 2\\sqrt{3} - 1$。",
            "線索 2：第 (2) 小題弳度換度數：$\\frac{\\pi}{4}=45^\\circ, \\frac{\\pi}{6}=30^\\circ, \\frac{\\pi}{3}=60^\\circ$。",
            "線索 3：第 (2) 小題通分計算：$\\frac{1}{2} + \\frac{3}{4} - \\frac{1}{3} = \\frac{6 + 9 - 4}{12} = \\frac{11}{12}$。"
        ],
        "conclusion": "CASE CLOSED：(1) 原式 = 2√3 - 1  ；  (2) 原式 = 11/12",
        "notes": "【運算提醒】\n$\\pi$ 弳等於 180 度，遇到弳度量先轉為度數再代入數值。"
    },
    # 15. 例題 5 & 隨堂 5 生活素養
    {
        "type": "problem",
        "tag": "生活科技素養",
        "title": "例題 5 & 隨堂 5：無障礙坡道與險升坡夾角反推",
        "question": "(1) [例題 5] 室內無障礙坡道坡度應小於 $\\frac{1}{8}$，求坡道與地面夾角約小於幾度？<br>(2) [隨堂 5] 自行車險升坡 20%（前進 100m 上升 20m），求與地面夾角約多少度？",
        "steps": [
            "線索 1：坡度定義即正切值 $\\tan\\theta = \\frac{\\text{垂直上升}}{\\text{水平前進}}$。",
            "線索 2：無障礙坡道：$\\tan\\theta = \\frac{1}{8} = 0.125 \\implies \\theta = \\tan^{-1}(0.125) \\approx 7.125^\\circ$。",
            "線索 3：自行車險升坡：$\\tan\\theta = \\frac{20}{100} = 0.2 \\implies \\theta = \\tan^{-1}(0.2) \\approx 11.3^\\circ \\approx 11^\\circ$。"
        ],
        "conclusion": "CASE CLOSED：(1) 夾角約小於 7.125°  ；  (2) 夾角約為 11°",
        "notes": "【計算機教學】\n指導學生在手機或工程計算機上切換 DEG 模式，按 2nd/SHIFT 啟用 tan⁻¹ 反三角函數。"
    },
    # 16. 模組三章頭
    {
        "type": "section",
        "section_num": "STAGE 03",
        "title": "神奇魔法六角星四大恆等關係",
        "desc": "倒數、商數、平方、餘角四大星陣，一圖掌握全部恆等式！",
        "notes": "進入第三階段：六角星陣是技術高中學生最強大的視覺記憶武器。"
    },
    # 17. 六角星陣觀念
    {
        "type": "concept",
        "tag": "終極武器",
        "title": "神奇六角星陣四大破案法則",
        "highlight": "頂點：左側無 co (sin, tan, sec)，右側帶 co (cos, cot, csc)，中央為 1",
        "points": [
            "1. 倒數關係：對角線兩端乘積為 1（$\\sin\\csc=1, \\cos\\sec=1, \\tan\\cot=1$）",
            "2. 商數關係：一個頂點等於相鄰兩頂點之商（$\\tan = \\frac{\\sin}{\\cos}, \\cot = \\frac{\\cos}{\\sin}$）",
            "3. 平方關係：倒三角上方平方和等於下方（$\\sin^2+\\cos^2=1, 1+\\tan^2=\\sec^2, 1+\\cot^2=\\csc^2$）",
            "4. 餘角關係：同高度橫線兩端角度和為 90° 函數互換（$\\sin\\leftrightarrow\\cos, \\tan\\leftrightarrow\\cot, \\sec\\leftrightarrow\\csc$）"
        ],
        "tip": "★ 口訣：對角互倒、倒三角平方和、橫向餘角換裝！",
        "notes": "【黑板繪製】\n在黑板上畫出六角形，中央寫 1，塗出三個倒三角形（上面兩個加起來等於下面）。"
    },
    # 18. 例題 6 & 隨堂 6
    {
        "type": "problem",
        "tag": "課本例題 6 & 隨堂 6",
        "title": "例題 6 & 隨堂 6：倒數與平方關係秒殺求值",
        "question": "試求下列各式之值：<br>(1) $\\sin 50^\\circ \\csc 50^\\circ$<br>(2) $\\sec^2 70^\\circ - \\tan^2 70^\\circ$<br>(3) $\\cot^2 12^\\circ - \\csc^2 12^\\circ$",
        "steps": [
            "線索 1：第 (1) 題：同角正弦與餘割為倒數伴侶，乘積恆為 $1$。",
            "線索 2：第 (2) 題：由 $1 + \\tan^2 70^\\circ = \\sec^2 70^\\circ \\implies \\sec^2 70^\\circ - \\tan^2 70^\\circ = 1$。",
            "線索 3：第 (3) 題：由 $1 + \\cot^2 12^\\circ = \\csc^2 12^\\circ \\implies \\cot^2 12^\\circ - \\csc^2 12^\\circ = -1$（注意移項負號！）。"
        ],
        "conclusion": "CASE CLOSED：(1) 原式 = 1  ；  (2) 原式 = 1  ；  (3) 原式 = -1",
        "notes": "【避雷針】\n特別強調第 (3) 小題，學生最常把 $\\cot^2 - \\csc^2$ 誤寫為 +1，正確是 -1。"
    },
    # 19. 例題 7 & 隨堂 7
    {
        "type": "problem",
        "tag": "課本例題 7 & 隨堂 7",
        "title": "例題 7 & 隨堂 7：餘角轉化與平方綜合求值",
        "question": "(1) [例題 7] 試求 $\\tan 40^\\circ \\tan 50^\\circ + \\tan^2 72^\\circ - \\csc^2 18^\\circ$ 之值。<br>(2) [隨堂 7] 試求 $\\cos^2 35^\\circ + \\cos^2 55^\\circ + \\csc^2 47^\\circ - \\tan^2 43^\\circ$ 之值。",
        "steps": [
            "線索 1：第 (1) 題：$\\tan 50^\\circ = \\cot 40^\\circ \\implies \\tan 40^\\circ\\cot 40^\\circ = 1$ ； $\\csc 18^\\circ = \\sec 72^\\circ \\implies \\tan^2 72^\\circ - \\sec^2 72^\\circ = -1$。合計 $1 + (-1) = 0$。",
            "線索 2：第 (2) 題：$\\cos 55^\\circ = \\sin 35^\\circ \\implies \\cos^2 35^\\circ + \\sin^2 35^\\circ = 1$。",
            "線索 3：第 (2) 題：$\\tan 43^\\circ = \\cot 47^\\circ \\implies \\csc^2 47^\\circ - \\cot^2 47^\\circ = 1$。合計 $1 + 1 = 2$。"
        ],
        "conclusion": "CASE CLOSED：(1) 原式 = 0  ；  (2) 原式 = 2",
        "notes": "【破案關鍵】\n看到非特別角（40°、50°、72°、18°），第一步找互餘配對（相加等於 90°），化為同角後套用平方關係！"
    },
    # 20. 例題 8 & 隨堂 8
    {
        "type": "problem",
        "tag": "課本例題 8 & 隨堂 8",
        "title": "例題 8 & 隨堂 8：一次齊次分式商數同除神技",
        "question": "(1) [例題 8] 已知 $\\tan\\theta = 2$，求 $\\frac{\\sin\\theta + 2\\cos\\theta}{3\\sin\\theta - \\cos\\theta}$ 之值。<br>(2) [隨堂 8] 已知 $\\cot\\theta = \\frac{2}{3}$，求 $\\frac{\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 6\\cos\\theta}$ 之值。",
        "steps": [
            "線索 1：第 (1) 題：分子分母同除以 $\\cos\\theta$ 轉為正切：$\\frac{\\tan\\theta + 2}{3\\tan\\theta - 1} = \\frac{2 + 2}{3(2) - 1} = \\frac{4}{5}$。",
            "線索 2：第 (2) 題：分子分母同除以 $\\sin\\theta$ 轉為餘切：$\\frac{1 - 3\\cot\\theta}{5 + 6\\cot\\theta} = \\frac{1 - 3(2/3)}{5 + 6(2/3)} = \\frac{1 - 2}{5 + 4} = -\\frac{1}{9}$。"
        ],
        "conclusion": "CASE CLOSED：(1) 分式之值 = 4/5  ；  (2) 分式之值 = -1/9",
        "notes": "【技巧傳授】\n齊次分式同除法可以完全避開求斜邊的麻煩，是技高段考極高頻率出現的必得分題型！"
    },
    # 21. 模組四章頭
    {
        "type": "section",
        "section_num": "STAGE 04",
        "title": "三角恆等式核心與課後實戰",
        "desc": "和差平方連環扣、切和通分倒數，以及章末是非進階題全破案！",
        "notes": "進入第四階段：對稱式、平方與乘積的互換是三角函數的高階思維。"
    },
    # 22. 例題 9 講解
    {
        "type": "problem",
        "tag": "課本例題 9",
        "title": "例題 9：和差連環扣求乘積與切和",
        "question": "已知銳角 $\\theta$ 滿足 $\\sin\\theta + \\cos\\theta = \\frac{4}{3}$。<br>試求：(1) $\\sin\\theta\\cos\\theta$　(2) $\\tan\\theta + \\cot\\theta$ 之值。",
        "steps": [
            "線索 1：見和必平方！$(\\sin\\theta+\\cos\\theta)^2 = 1 + 2\\sin\\theta\\cos\\theta = \\left(\\frac{4}{3}\\right)^2 = \\frac{16}{9}$。",
            "線索 2：移項求乘積：$2\\sin\\theta\\cos\\theta = \\frac{16}{9} - 1 = \\frac{7}{9} \\implies \\sin\\theta\\cos\\theta = \\frac{7}{18}$。",
            "線索 3：求切和：$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta} = \\frac{1}{7/18} = \\frac{18}{7}$。"
        ],
        "conclusion": "CASE CLOSED：(1) sin θ cos θ = 7/18  ；  (2) tan θ + cot θ = 18/7",
        "notes": "【連環口訣】\n和平方得乘積，乘積倒數得切和！這是一套標準組合拳！"
    },
    # 23. 隨堂 9 呼應
    {
        "type": "problem",
        "tag": "隨堂實戰 9",
        "title": "隨堂練習 9：差平方求乘積與切和",
        "question": "已知銳角 $\\theta$ 滿足 $\\sin\\theta - \\cos\\theta = \\frac{3}{5}$。<br>試求：(1) $\\sin\\theta\\cos\\theta$　(2) $\\tan\\theta + \\cot\\theta$ 之值。",
        "steps": [
            "線索 1：差平方展開：$(\\sin\\theta-\\cos\\theta)^2 = 1 - 2\\sin\\theta\\cos\\theta = \\left(\\frac{3}{5}\\right)^2 = \\frac{9}{25}$。",
            "線索 2：移項求乘積：$2\\sin\\theta\\cos\\theta = 1 - \\frac{9}{25} = \\frac{16}{25} \\implies \\sin\\theta\\cos\\theta = \\frac{8}{25}$。",
            "線索 3：求切和：$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta} = \\frac{1}{8/25} = \\frac{25}{8}$。"
        ],
        "conclusion": "CASE CLOSED：(1) sin θ cos θ = 8/25  ；  (2) tan θ + cot θ = 25/8",
        "notes": "【正負號注意】\n差平方中間是減號：$1 - 2\\sin\\cos$，移項時小心正負號不要搞反。"
    },
    # 24. 習題觀念是非
    {
        "type": "concept",
        "tag": "課本習題是非",
        "title": "課後習題 觀念釐清區五大迷思診斷",
        "highlight": "審查案卷細節，揪出常見錯誤觀念！",
        "points": [
            "(○) 1. 已知銳角 $\\sin\\theta$，必可由畢氏定理確定三邊比例求其餘五值。",
            "(×) 2. $\\sin A = \\frac{3}{5}$ 只是邊長比，無具體數據無法得知實際邊長！",
            "(×) 3. $\\sin^2\\alpha + \\cos^2\\beta = 1$ 錯誤！平方關係嚴格限定同角！",
            "(×) 4. $\\sin\\theta \\times \\cos\\theta = 1$ 錯誤！倒數關係為 $\\sin\\theta \\times \\csc\\theta = 1$！",
            "(×) 5. $(\\sin\\theta+\\cos\\theta)^2 = 1$ 錯誤！遺漏交叉項 $2\\sin\\theta\\cos\\theta$！"
        ],
        "tip": "★ 迷思破案：比值不等於長度；平方限定同角；和平方必有交叉項！",
        "notes": "【全班快問快答】\n逐條提問學生為什麼對、為什麼錯，讓學生口頭說出反例。"
    },
    # 25. 習題進階題
    {
        "type": "problem",
        "tag": "課本進階題",
        "title": "進階題 8 & 9：通分化簡與立方和終極大案",
        "question": "(1) [進階 8] $\\cos\\theta = \\frac{1}{5}$，求 $\\frac{1}{1+\\sin\\theta} + \\frac{1}{1-\\sin\\theta}$ 之值。<br>(2) [進階 9] $\\tan x + \\cot x = \\frac{25}{12}$，求 $\\sin^3 x + \\cos^3 x$ 之值。",
        "steps": [
            "線索 1：第 (1) 題通分：$\\frac{2}{1-\\sin^2\\theta} = \\frac{2}{\\cos^2\\theta} = \\frac{2}{(1/5)^2} = 2 \\times 25 = 50$。",
            "線索 2：第 (2) 題乘積與和：$\\sin x\\cos x = \\frac{12}{25}$ ； $(\\sin+\\cos)^2 = 1 + \\frac{24}{25} = \\frac{49}{25} \\implies \\sin+\\cos = \\frac{7}{5}$。",
            "線索 3：第 (2) 題立方和因式分解：$(\\sin+\\cos)(1-\\sin\\cos) = \\left(\\frac{7}{5}\\right)\\left(1 - \\frac{12}{25}\\right) = \\frac{7}{5} \\times \\frac{13}{25} = \\frac{91}{125}$。"
        ],
        "conclusion": "CASE CLOSED：(1) 原式 = 50  ；  (2) sin³ x + cos³ x = 91/125",
        "notes": "【高階挑戰】\n這是本單元難度最高的劇場版魔王題，引導學生利用因式分解公式結合對稱式求解。"
    },
    # 26. 總結
    {
        "type": "summary",
        "title": "名偵探柯南數理探案特訓 ‧ 終極結案錦囊",
        "subtitle": "泰宇高中數學 2-2 三角函數的定義與性質 ‧ 真相大白！",
        "points": [
            "1. 銳角三角比：$\\sin = \\frac{\\text{對}}{\\text{斜}}, \\cos = \\frac{\\text{鄰}}{\\text{斜}}, \\tan = \\frac{\\text{對}}{\\text{鄰}}$；倒數伴侶為 $\\csc, \\sec, \\cot$",
            "2. 特別角分子律：正弦分子階梯 $\\sqrt{1}, \\sqrt{2}, \\sqrt{3}$，餘弦逆序，正切 $1$ 在 $45^\\circ$",
            "3. 六角星四大陣法：對角互倒、倒三角平方和、橫向餘角互換、頂點商數相鄰積",
            "4. 齊次同除神法：一次正餘弦分式同除 $\\cos$ 秒化 $\\tan$",
            "5. 和差連環扣：$(\\sin\\pm\\cos)^2 = 1\\pm 2\\sin\\cos$ ； $\\tan+\\cot = \\frac{1}{\\sin\\cos}$"
        ],
        "stamp": "CASE CLOSED 真相永遠只有一個！",
        "notes": "【結案鼓舞】\n恭喜全班完成泰宇數學 2-2 探案特訓！掌握這五大神技，所有三角函數題目都能迎刃而解！下課！"
    }
]

def generate_slides_html(slides):
    html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>泰宇版 2-2 三角函數的定義與性質 教學簡報</title>
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
      padding: 16mm 22mm 12mm 22mm;
      background: #fbf9f4; /* 象牙米杏暖白護眼底色 */
    }
    .katex, .katex-html, .katex-display {
      white-space: nowrap !important;
      font-size: 1.45em !important;
      font-weight: 700 !important;
    }
    .katex-display {
      margin: 0.25em 0 !important;
      display: inline-block !important;
    }
  </style>
</head>
<body>
"""

    for idx, slide in enumerate(slides):
        stype = slide["type"]

        if stype == "cover":
            content_html = f"""
            <div class="flex-1 flex flex-col justify-center items-center text-center">
              <span class="px-5 py-2 rounded-full text-base font-black bg-amber-600 text-white shadow-md mb-6 tracking-wide">
                {slide['badge']}
              </span>
              <h1 class="text-5xl font-black text-amber-950 mb-6 tracking-tight leading-tight">
                {slide['title']}
              </h1>
              <p class="text-2xl font-bold text-amber-800 mb-6">
                {slide['subtitle']}
              </p>
              <div class="max-w-4xl p-5 rounded-2xl bg-amber-50 border-2 border-amber-300 text-slate-800 text-xl font-medium shadow-sm">
                {slide['desc']}
              </div>
            </div>
            """
        elif stype == "roadmap":
            mods_html = "".join([f"""
              <div class="p-6 rounded-2xl bg-white border-2 border-amber-200 shadow-sm flex flex-col justify-between">
                <div>
                  <span class="px-3 py-1 rounded-md text-sm font-black bg-amber-600 text-white">{m['num']}</span>
                  <h3 class="text-2xl font-black text-amber-950 mt-3 mb-2">{m['title']}</h3>
                  <p class="text-base text-slate-700 leading-relaxed">{m['desc']}</p>
                </div>
              </div>
            """ for m in slide['modules']])
            content_html = f"""
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <span class="text-sm font-black text-amber-700 tracking-wider">ROADMAP</span>
                <h2 class="text-4xl font-black text-amber-950 mb-1">{slide['title']}</h2>
                <p class="text-lg text-slate-600 mb-6">{slide['subtitle']}</p>
              </div>
              <div class="grid grid-cols-4 gap-6 flex-1 items-stretch my-2">
                {mods_html}
              </div>
            </div>
            """
        elif stype == "section":
            content_html = f"""
            <div class="flex-1 flex flex-col justify-center items-center text-center">
              <span class="px-5 py-2 rounded-full text-lg font-black bg-amber-600 text-white mb-6">
                {slide['section_num']}
              </span>
              <h2 class="text-5xl font-black text-amber-950 mb-6">{slide['title']}</h2>
              <p class="text-2xl text-slate-700 max-w-3xl leading-relaxed">{slide['desc']}</p>
            </div>
            """
        elif stype == "concept":
            pts_html = "".join([f"""
              <li class="text-2xl text-slate-800 leading-relaxed font-medium mb-3">{p}</li>
            """ for p in slide['points']])
            content_html = f"""
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center gap-3 mb-2">
                  <span class="px-3 py-1 rounded-md text-sm font-black bg-amber-600 text-white">{slide['tag']}</span>
                  <h2 class="text-4xl font-black text-amber-950">{slide['title']}</h2>
                </div>
                <div class="p-4 rounded-xl bg-amber-100/70 border-l-8 border-amber-600 text-xl font-bold text-amber-950 mb-6">
                  {slide['highlight']}
                </div>
              </div>
              <ul class="list-disc list-inside space-y-2 px-4 flex-1">
                {pts_html}
              </ul>
              <div class="p-4 rounded-xl bg-white border border-amber-300 text-lg font-bold text-amber-800">
                {slide['tip']}
              </div>
            </div>
            """
        elif stype == "problem":
            steps_html = "".join([f"""
              <div class="p-4 rounded-xl bg-white border border-slate-200 text-xl leading-relaxed text-slate-800 shadow-2xs">
                {st}
              </div>
            """ for st in slide['steps']])
            content_html = f"""
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-2">
                  <div class="flex items-center gap-3">
                    <span class="px-3 py-1 rounded-md text-sm font-black bg-red-600 text-white">{slide['tag']}</span>
                    <h2 class="text-3xl font-black text-amber-950">{slide['title']}</h2>
                  </div>
                </div>
                <div class="p-4 rounded-xl bg-amber-50/80 border border-amber-200 text-2xl font-bold text-slate-900 mb-4 leading-relaxed">
                  {slide['question']}
                </div>
              </div>
              <div class="space-y-3 flex-1 my-1">
                {steps_html}
              </div>
              <div class="p-4 rounded-xl bg-emerald-50 border-2 border-emerald-500 text-2xl font-black text-emerald-900 text-center mt-3">
                【{slide['conclusion']}】
              </div>
            </div>
            """
        elif stype == "summary":
            pts_html = "".join([f"""
              <div class="p-4 rounded-xl bg-white border border-amber-200 text-xl font-bold text-slate-800 leading-relaxed shadow-2xs">
                {p}
              </div>
            """ for p in slide['points']])
            content_html = f"""
            <div class="flex-1 flex flex-col justify-between">
              <div>
                <h2 class="text-4xl font-black text-amber-950 mb-1">{slide['title']}</h2>
                <p class="text-lg text-slate-600 mb-4">{slide['subtitle']}</p>
              </div>
              <div class="space-y-3 flex-1">
                {pts_html}
              </div>
              <div class="p-4 rounded-xl bg-red-600 text-white text-2xl font-black text-center tracking-wide mt-3 shadow-md">
                ★ {slide['stamp']} ★
              </div>
            </div>
            """

        html += f"""
  <div class="slide-page">
    {content_html}
    <!-- 頁尾 -->
    <div class="flex items-center justify-between pt-3 border-t border-amber-200/80 text-sm text-slate-500 font-medium">
      <div>泰宇版 技術高中數學（第二冊）2-2 三角函數的定義與性質</div>
      <div>投影片 {idx+1} / {len(slides)}</div>
      <div>PLVS 數學科  教育學習用</div>
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
    print(f"投影片總數：{len(LESSON_SLIDES)} 頁 (16:9 全螢幕滿版)")

    html_file = "slides_16_9.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(generate_slides_html(LESSON_SLIDES))
    print(f"成功產出簡報 HTML：{html_file}")

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
        "--virtual-time-budget=12000",
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

        if page_idx < len(LESSON_SLIDES):
            s_data = LESSON_SLIDES[page_idx]
            tf.text = s_data.get("notes", "PLVS 數學科  教育學習用")

    prs.save(pptx_file)
    print(f"成功產出教學簡報：{pptx_file} (檔案大小：{os.path.getsize(pptx_file):,} 位元組)")

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
