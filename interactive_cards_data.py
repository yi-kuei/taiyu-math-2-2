# -*- coding: utf-8 -*-
"""
interactive_cards_data.py - 泰宇版 技術高中數學（第二冊）2-2 三角函數的定義與性質
正面互動檢核題庫 (QUIZ_DATA)、動態模型參數 (MODEL_DATA) 與六大闖關關卡 (CHALLENGE_STAGES)
遵循 SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版：
- 全套 60 張圖卡每張均配置正面檢核抽屜題
- 100% KaTeX 標準數學式
- 六階段少年偵探團闖關考核系統
"""

QUIZ_DATA = {
    # 階段一：銳角三角函數定義 (1 ~ 11)
    1: {
        "question": "將邊長為 2 的正三角形沿高對折，所得直角三角形三邊長比為何？",
        "options": ["$1 : 1 : \\sqrt{2}$", "$1 : \\sqrt{3} : 2$", "$3 : 4 : 5$", "$5 : 12 : 13$"],
        "answer": 1,
        "explanation": "由畢氏定理，底為 1、高為 $\\sqrt{2^2 - 1^2} = \\sqrt{3}$、斜邊為 2，邊長比為 $1 : \\sqrt{3} : 2$。"
    },
    2: {
        "question": "直角三角形中，角 $\\theta$ 的「正切函數」$\\tan\\theta$ 定義為下列何者？",
        "options": ["$\\frac{\\text{對邊}}{\\text{斜邊}}$", "$\\frac{\\text{鄰邊}}{\\text{斜邊}}$", "$\\frac{\\text{對邊}}{\\text{鄰邊}}$", "$\\frac{\\text{斜邊}}{\\text{對邊}}$"],
        "answer": 2,
        "explanation": "正弦為 $\\frac{\\text{對}}{\\text{斜}}$、餘弦為 $\\frac{\\text{鄰}}{\\text{斜}}$、正切為 $\\frac{\\text{對}}{\\text{鄰}}$。"
    },
    3: {
        "question": "關於三角函數的倒數伴侶，下列配對何者正確？",
        "options": ["$\\sin\\theta$ 與 $\\sec\\theta$", "$\\cos\\theta$ 與 $\\csc\\theta$", "$\\sin\\theta$ 與 $\\csc\\theta$", "$\\tan\\theta$ 與 $\\sec\\theta$"],
        "answer": 2,
        "explanation": "正弦 $\\sin$ 的倒數為餘割 $\\csc$；餘弦 $\\cos$ 的倒數為正割 $\\sec$；正切 $\\tan$ 的倒數為餘切 $\\cot$。"
    },
    4: {
        "question": "直角三角形三邊長為 8、15、17，若斜邊為 17、$\\angle A$ 的對邊為 15，則 $\\cos A$ 為何？",
        "options": ["$\\frac{15}{17}$", "$\\frac{8}{17}$", "$\\frac{15}{8}$", "$\\frac{17}{8}$"],
        "answer": 1,
        "explanation": "$\\angle A$ 的鄰邊為 8，故 $\\cos A = \\frac{\\text{鄰邊}}{\\text{斜邊}} = \\frac{8}{17}$。"
    },
    5: {
        "question": "直角三角形三邊長為 5、12、13，若 $\\angle A$ 的對邊為 12，則 $\\csc A$ 為何？",
        "options": ["$\\frac{12}{13}$", "$\\frac{5}{13}$", "$\\frac{13}{12}$", "$\\frac{13}{5}$"],
        "answer": 2,
        "explanation": "$\\sin A = \\frac{12}{13}$，取倒數得 $\\csc A = \\frac{13}{12}$。"
    },
    6: {
        "question": "直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ, AC=8, BC=15, AB=17$，則 $\\sin B$ 為何？",
        "options": ["$\\frac{15}{17}$", "$\\frac{8}{17}$", "$\\frac{8}{15}$", "$\\frac{17}{8}$"],
        "answer": 1,
        "explanation": "$\\angle B$ 的對邊是 $AC = 8$，斜邊為 17，故 $\\sin B = \\frac{8}{17}$。"
    },
    7: {
        "question": "直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ, AC=5, BC=12, AB=13$，則 $\\tan B$ 為何？",
        "options": ["$\\frac{12}{5}$", "$\\frac{5}{12}$", "$\\frac{5}{13}$", "$\\frac{12}{13}$"],
        "answer": 1,
        "explanation": "$\\angle B$ 的對邊為 $AC = 5$，鄰邊為 $BC = 12$，故 $\\tan B = \\frac{5}{12}$。"
    },
    8: {
        "question": "已知直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$ 且 $\\cos A = \\frac{5}{13}$，則 $\\tan A$ 為何？",
        "options": ["$\\frac{12}{13}$", "$\\frac{12}{5}$", "$\\frac{5}{12}$", "$\\frac{13}{12}$"],
        "answer": 1,
        "explanation": "設鄰邊 5、斜邊 13，則對邊為 12，$\\tan A = \\frac{12}{5}$。"
    },
    9: {
        "question": "已知直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ$ 且 $\\tan A = \\frac{24}{7}$，則 $\\sin A$ 為何？",
        "options": ["$\\frac{7}{25}$", "$\\frac{24}{25}$", "$\\frac{25}{24}$", "$\\frac{25}{7}$"],
        "answer": 1,
        "explanation": "對邊 24、鄰邊 7，斜邊 $\\sqrt{24^2 + 7^2} = 25$，故 $\\sin A = \\frac{24}{25}$。"
    },
    10: {
        "question": "直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ, \\sin A = \\frac{4}{5}$，若斜邊 $AB = 15$，則對邊 $BC$ 長度為何？",
        "options": ["$9$", "$12$", "$15$", "$20$"],
        "answer": 1,
        "explanation": "$\\sin A = \\frac{BC}{AB} = \\frac{4}{5} \\implies BC = 15 \\times \\frac{4}{5} = 12$。"
    },
    11: {
        "question": "直角 $\\triangle ABC$ 中，$\\angle C = 90^\\circ, \\csc A = \\frac{17}{15}$，若鄰邊 $AC = 40$，則斜邊 $AB$ 長度為何？",
        "options": ["$75$", "$80$", "$85$", "$90$"],
        "answer": 2,
        "explanation": "$\\sin A = \\frac{15}{17}$，三邊比為 $8 : 15 : 17$。鄰邊 $8k = 40 \\implies k = 5$，斜邊 $AB = 17 \\times 5 = 85$。"
    },

    # 階段二：特別角與生活科技 (12 ~ 20)
    12: {
        "question": "特別角 $30^\\circ$ 的正切函數值 $\\tan 30^\\circ$ 為何？",
        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{3}$", "$1$", "$\\sqrt{3}$"],
        "answer": 1,
        "explanation": "$\\tan 30^\\circ = \\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}$。"
    },
    13: {
        "question": "特別角 $45^\\circ$ 的餘弦函數值 $\\cos 45^\\circ$ 為何？",
        "options": ["$\\frac{1}{2}$", "$\\frac{\\sqrt{2}}{2}$", "$\\frac{\\sqrt{3}}{2}$", "$1$"],
        "answer": 1,
        "explanation": "等腰直角三角形三邊比 $1:1:\\sqrt{2}$，$\\cos 45^\\circ = \\frac{1}{\\sqrt{2}} = \\frac{\\sqrt{2}}{2}$。"
    },
    14: {
        "question": "下列哪一個三角函數值「最大」？",
        "options": ["$\\sin 30^\\circ$", "$\\sin 45^\\circ$", "$\\sin 60^\\circ$", "$\\cos 60^\\circ$"],
        "answer": 2,
        "explanation": "$\\sin 30^\\circ = 0.5$、$\\sin 45^\\circ \\approx 0.707$、$\\sin 60^\\circ = \\frac{\\sqrt{3}}{2} \\approx 0.866$、$\\cos 60^\\circ = 0.5$。最大者為 $\\sin 60^\\circ$。"
    },
    15: {
        "question": "求 $\\sin 30^\\circ - \\cos 60^\\circ + \\tan 45^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$2$", "$\\frac{1}{2}$"],
        "answer": 1,
        "explanation": "$\\frac{1}{2} - \\frac{1}{2} + 1 = 1$。"
    },
    16: {
        "question": "求 $2 \\sin^2 45^\\circ + \\cot 30^\\circ \\csc 60^\\circ$ 之值為何？",
        "options": ["$2$", "$3$", "$4$", "$5$"],
        "answer": 1,
        "explanation": "$2(\\frac{1}{2}) + \\sqrt{3}(\\frac{2}{\\sqrt{3}}) = 1 + 2 = 3$。"
    },
    17: {
        "question": "求 $2\\sin 60^\\circ - \\sqrt{2}\\cos 45^\\circ + \\tan 60^\\circ$ 之值為何？",
        "options": ["$2\\sqrt{3} - 1$", "$\\sqrt{3} - 1$", "$2\\sqrt{3}$", "$1$"],
        "answer": 0,
        "explanation": "$2(\\frac{\\sqrt{3}}{2}) - \\sqrt{2}(\\frac{\\sqrt{2}}{2}) + \\sqrt{3} = \\sqrt{3} - 1 + \\sqrt{3} = 2\\sqrt{3} - 1$。"
    },
    18: {
        "question": "求 $\\sin^2 \\frac{\\pi}{4} + \\cos^2 \\frac{\\pi}{6} - \\cot^2 \\frac{\\pi}{3}$ 之值為何？",
        "options": ["$\\frac{5}{12}$", "$\\frac{7}{12}$", "$\\frac{11}{12}$", "$1$"],
        "answer": 2,
        "explanation": "$\\frac{1}{2} + \\frac{3}{4} - \\frac{1}{3} = \\frac{6 + 9 - 4}{12} = \\frac{11}{12}$。"
    },
    19: {
        "question": "若無障礙坡道坡度為 $\\frac{1}{8}$，求夾角應按計算機何種功能鍵？",
        "options": ["$\\sin(1/8)$", "$\\tan(1/8)$", "$\\tan^{-1}(1/8)$", "$\\cos^{-1}(1/8)$"],
        "answer": 2,
        "explanation": "已知正切比值反推求角度，需按反正切鍵 $\\tan^{-1}$。"
    },
    20: {
        "question": "自行車 20% 險升坡（前進 100m 上升 20m），其夾角 $\\tan\\theta$ 為何？",
        "options": ["$0.02$", "$0.2$", "$2$", "$5$"],
        "answer": 1,
        "explanation": "$\\tan\\theta = \\frac{20}{100} = 0.2$。"
    },

    # 階段三：魔法六角形與恆等關係 (21 ~ 30)
    21: {
        "question": "魔法六角星陣中，位於中央的數字為何？",
        "options": ["$0$", "$1$", "$\\pi$", "$e$"],
        "answer": 1,
        "explanation": "中央核心數字為 1，代表對角線兩端乘積為 1。"
    },
    22: {
        "question": "同角三角函數中，$\\tan\\theta \\cdot \\cot\\theta$ 恆等於何值？",
        "options": ["$0$", "$1$", "$-1$", "$\\sin\\theta$"],
        "answer": 1,
        "explanation": "正切與餘切互為倒數，乘積恆為 1。"
    },
    23: {
        "question": "商數關係中，$\\frac{\\cos\\theta}{\\sin\\theta}$ 等於下列何者？",
        "options": ["$\\tan\\theta$", "$\\cot\\theta$", "$\\sec\\theta$", "$\\csc\\theta$"],
        "answer": 1,
        "explanation": "$\\frac{\\cos\\theta}{\\sin\\theta} = \\cot\\theta$。"
    },
    24: {
        "question": "平方關係中，與 $1 + \\tan^2\\theta$ 相等的是下列何者？",
        "options": ["$\\sin^2\\theta$", "$\\cot^2\\theta$", "$\\sec^2\\theta$", "$\\csc^2\\theta$"],
        "answer": 2,
        "explanation": "$1 + \\tan^2\\theta = \\sec^2\\theta$。"
    },
    25: {
        "question": "餘角關係中，$\\sin(90^\\circ - \\theta)$ 等於下列何者？",
        "options": ["$\\cos\\theta$", "$\\tan\\theta$", "$\\csc\\theta$", "$-\\sin\\theta$"],
        "answer": 0,
        "explanation": "橫向端點互餘互換：$\\sin(90^\\circ - \\theta) = \\cos\\theta$。"
    },
    26: {
        "question": "求 $\\sin 50^\\circ \\times \\csc 50^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$\\frac{1}{2}$", "無法確定"],
        "answer": 1,
        "explanation": "同角正弦與餘割為倒數伴侶，乘積為 1。"
    },
    27: {
        "question": "求 $\\sin^2 40^\\circ + \\cos^2 40^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$2$", "$\\frac{1}{2}$"],
        "answer": 1,
        "explanation": "同角平方和 $\\sin^2\\theta + \\cos^2\\theta = 1$。"
    },
    28: {
        "question": "求 $\\sec^2 70^\\circ - \\tan^2 70^\\circ$ 之值為何？",
        "options": ["$-1$", "$0$", "$1$", "$2$"],
        "answer": 2,
        "explanation": "由 $1 + \\tan^2\\theta = \\sec^2\\theta \\implies \\sec^2\\theta - \\tan^2\\theta = 1$。"
    },
    29: {
        "question": "求 $\\cos 35^\\circ \\times \\sec 35^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$\\frac{\\sqrt{2}}{2}$", "$-1$"],
        "answer": 1,
        "explanation": "餘弦與正割互為倒數，乘積為 1。"
    },
    30: {
        "question": "求 $\\sin^2 80^\\circ + \\cos^2 80^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$1.6$", "$-1$"],
        "answer": 1,
        "explanation": "無論角度幾度，只要同角，平方和必為 1。"
    },

    # 延續階段三與階段四：恆等式進階 (31 ~ 40)
    31: {
        "question": "求 $\\cot^2 12^\\circ - \\csc^2 12^\\circ$ 之值為何？",
        "options": ["$1$", "$-1$", "$0$", "$2$"],
        "answer": 1,
        "explanation": "由 $1 + \\cot^2\\theta = \\csc^2\\theta \\implies \\cot^2\\theta - \\csc^2\\theta = -1$。"
    },
    32: {
        "question": "求 $\\tan 40^\\circ \\tan 50^\\circ + \\tan^2 72^\\circ - \\csc^2 18^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$-1$", "$2$"],
        "answer": 0,
        "explanation": "$\\tan 50^\\circ = \\cot 40^\\circ \\implies 1$；$\\csc 18^\\circ = \\sec 72^\\circ \\implies \\tan^2 72^\\circ - \\sec^2 72^\\circ = -1$。$1 + (-1) = 0$。"
    },
    33: {
        "question": "求 $\\cos^2 35^\\circ + \\cos^2 55^\\circ + \\csc^2 47^\\circ - \\tan^2 43^\\circ$ 之值為何？",
        "options": ["$1$", "$2$", "$0$", "$-1$"],
        "answer": 1,
        "explanation": "第一組為 1，第二組為 1，合計 $1 + 1 = 2$。"
    },
    34: {
        "question": "已知 $\\tan\\theta = 2$，求 $\\frac{\\sin\\theta + 2\\cos\\theta}{3\\sin\\theta - \\cos\\theta}$ 之值為何？",
        "options": ["$\\frac{3}{5}$", "$\\frac{4}{5}$", "$1$", "$\\frac{5}{4}$"],
        "answer": 1,
        "explanation": "同除 $\\cos\\theta$ 得 $\\frac{2 + 2}{3(2) - 1} = \\frac{4}{5}$。"
    },
    35: {
        "question": "已知 $\\cot\\theta = \\frac{2}{3}$，求 $\\frac{\\sin\\theta - 3\\cos\\theta}{5\\sin\\theta + 6\\cos\\theta}$ 之值為何？",
        "options": ["$-\\frac{1}{9}$", "$\\frac{1}{9}$", "$-\\frac{1}{3}$", "$\\frac{2}{5}$"],
        "answer": 0,
        "explanation": "同除 $\\sin\\theta$ 得 $\\frac{1 - 3(2/3)}{5 + 6(2/3)} = \\frac{1 - 2}{5 + 4} = -\\frac{1}{9}$。"
    },
    36: {
        "question": "三角恆等式中，$\\tan\\theta + \\cot\\theta$ 經通分後可化簡為下列何者？",
        "options": ["$\\frac{1}{\\sin\\theta + \\cos\\theta}$", "$\\frac{1}{\\sin\\theta\\cos\\theta}$", "$\\sin\\theta\\cos\\theta$", "$1$"],
        "answer": 1,
        "explanation": "$\\frac{\\sin}{\\cos} + \\frac{\\cos}{\\sin} = \\frac{\\sin^2 + \\cos^2}{\\sin\\cos} = \\frac{1}{\\sin\\cos}$。"
    },
    37: {
        "question": "若 $\\sin\\theta + \\cos\\theta = \\frac{4}{3}$，則 $\\sin\\theta\\cos\\theta$ 為何？",
        "options": ["$\\frac{7}{9}$", "$\\frac{7}{18}$", "$\\frac{1}{2}$", "$\\frac{16}{9}$"],
        "answer": 1,
        "explanation": "平方得 $1 + 2\\sin\\cos = \\frac{16}{9} \\implies 2\\sin\\cos = \\frac{7}{9} \\implies \\sin\\cos = \\frac{7}{18}$。"
    },
    38: {
        "question": "已知 $\\sin\\theta\\cos\\theta = \\frac{7}{18}$，則 $\\tan\\theta + \\cot\\theta$ 為何？",
        "options": ["$\\frac{7}{18}$", "$\\frac{18}{7}$", "$\\frac{9}{7}$", "$\\frac{14}{9}$"],
        "answer": 1,
        "explanation": "$\\tan\\theta + \\cot\\theta = \\frac{1}{\\sin\\theta\\cos\\theta} = \\frac{18}{7}$。"
    },
    39: {
        "question": "若 $\\sin\\theta - \\cos\\theta = \\frac{3}{5}$，則 $\\sin\\theta\\cos\\theta$ 為何？",
        "options": ["$\\frac{16}{25}$", "$\\frac{8}{25}$", "$\\frac{9}{25}$", "$\\frac{4}{5}$"],
        "answer": 1,
        "explanation": "平方得 $1 - 2\\sin\\cos = \\frac{9}{25} \\implies 2\\sin\\cos = \\frac{16}{25} \\implies \\sin\\cos = \\frac{8}{25}$。"
    },
    40: {
        "question": "承上題已知 $\\sin\\theta\\cos\\theta = \\frac{8}{25}$，則 $\\tan\\theta + \\cot\\theta$ 為何？",
        "options": ["$\\frac{8}{25}$", "$\\frac{25}{8}$", "$\\frac{25}{16}$", "$\\frac{16}{25}$"],
        "answer": 1,
        "explanation": "取倒數得 $\\frac{25}{8}$。"
    },

    # 階段五：課後習題是非 (41 ~ 45)
    41: {
        "question": "已知銳角 $\\theta$ 的 $\\sin\\theta$，必能求出其餘五個三角函數值？",
        "options": ["○ 正確", "× 錯誤"],
        "answer": 0,
        "explanation": "正確！由畢氏定理可唯一確定三邊比例，故其餘五個值均可求出。"
    },
    42: {
        "question": "直角 $\\triangle$ 中若 $\\sin A = \\frac{3}{5}$，則可求出三邊的實際長度？",
        "options": ["○ 正確", "× 錯誤"],
        "answer": 1,
        "explanation": "錯誤！三角函數是比值，無其他條件無法得知實際邊長。"
    },
    43: {
        "question": "若 $\\alpha, \\beta$ 為任意銳角，則 $\\sin^2\\alpha + \\cos^2\\beta = 1$ 恆成立？",
        "options": ["○ 正確", "× 錯誤"],
        "answer": 1,
        "explanation": "錯誤！平方關係嚴格限定同角，角度不同不一定等於 1。"
    },
    44: {
        "question": "若 $\\theta$ 為銳角，則 $\\sin\\theta \\times \\cos\\theta = 1$？",
        "options": ["○ 正確", "× 錯誤"],
        "answer": 1,
        "explanation": "錯誤！倒數關係為 $\\sin\\theta \\times \\csc\\theta = 1$。"
    },
    45: {
        "question": "若 $\\theta$ 為銳角，則 $(\\sin\\theta + \\cos\\theta)^2 = 1$？",
        "options": ["○ 正確", "× 錯誤"],
        "answer": 1,
        "explanation": "錯誤！遺漏交叉項：$(\\sin+\\cos)^2 = 1 + 2\\sin\\cos > 1$。"
    },

    # 階段六：課後習題實戰與進階 (46 ~ 60)
    46: {
        "question": "直角 $\\triangle$ 中，$\\sin A = \\frac{3}{5}$，求 $\\tan A + \\sec A$ 之值為何？",
        "options": ["$1$", "$2$", "$\\frac{3}{2}$", "$\\frac{8}{5}$"],
        "answer": 1,
        "explanation": "三邊為 3-4-5，$\\tan A = \\frac{3}{4}, \\sec A = \\frac{5}{4} \\implies \\frac{8}{4} = 2$。"
    },
    47: {
        "question": "直角 $\\triangle$ 中，$\\tan A = \\frac{12}{5}, AB = 26$，求 $\\sin A$ 為何？",
        "options": ["$\\frac{5}{13}$", "$\\frac{12}{13}$", "$\\frac{13}{12}$", "$\\frac{12}{26}$"],
        "answer": 1,
        "explanation": "三邊比為 5:12:13，$\\sin A = \\frac{12}{13}$。"
    },
    48: {
        "question": "直角 $\\triangle$ 中，$\\tan A = \\frac{12}{5}, AB = 26$，求邊長 $AC$ 為何？",
        "options": ["$5$", "$10$", "$12$", "$24$"],
        "answer": 1,
        "explanation": "斜邊 $13k = 26 \\implies k = 2$。鄰邊 $AC = 5k = 10$。"
    },
    49: {
        "question": "求 $4\\sin^2 30^\\circ + 2\\tan 45^\\circ + \\frac{1}{3}\\cot^2 30^\\circ\\sec^2 60^\\circ$ 之值為何？",
        "options": ["$5$", "$6$", "$7$", "$8$"],
        "answer": 2,
        "explanation": "$4(1/4) + 2(1) + (1/3)(3)(4) = 1 + 2 + 4 = 7$。"
    },
    50: {
        "question": "求 $(1 + 2\\sin\\frac{\\pi}{6} + \\cos\\frac{\\pi}{4})(1 - \\sin\\frac{\\pi}{4} + 2\\cos\\frac{\\pi}{3})$ 之值為何？",
        "options": ["$3$", "$\\frac{7}{2}$", "$4$", "$\\frac{9}{2}$"],
        "answer": 1,
        "explanation": "$(2 + \\frac{\\sqrt{2}}{2})(2 - \\frac{\\sqrt{2}}{2}) = 4 - \\frac{1}{2} = \\frac{7}{2}$。"
    },
    51: {
        "question": "求 $\\cos^2 20^\\circ + \\cos^2 70^\\circ + \\tan^2 20^\\circ - \\csc^2 70^\\circ$ 之值為何？",
        "options": ["$0$", "$1$", "$-1$", "$2$"],
        "answer": 0,
        "explanation": "$1 + (-1) = 0$。"
    },
    52: {
        "question": "求 $(\\sin\\frac{\\pi}{5} + \\cos\\frac{\\pi}{5})^2 + (\\sin\\frac{\\pi}{5} - \\cos\\frac{\\pi}{5})^2$ 之值為何？",
        "options": ["$1$", "$2$", "$0$", "$4$"],
        "answer": 1,
        "explanation": "交叉項相消，得 $1 + 1 = 2$。"
    },
    53: {
        "question": "若 $\\cot\\theta = \\frac{5}{12}$，求 $\\frac{5\\sin\\theta - 4\\cos\\theta}{5\\sin\\theta + 3\\cos\\theta}$ 之值為何？",
        "options": ["$\\frac{8}{15}$", "$\\frac{7}{15}$", "$\\frac{2}{3}$", "$\\frac{3}{5}$"],
        "answer": 0,
        "explanation": "同除 $\\sin\\theta$ 得 $\\frac{5 - 4(5/12)}{5 + 3(5/12)} = \\frac{10/3}{25/4} = \\frac{8}{15}$。"
    },
    54: {
        "question": "已知 $\\sin\\theta - \\cos\\theta = \\frac{1}{2}$，求 $\\sin\\theta\\cos\\theta$ 之值為何？",
        "options": ["$\\frac{1}{4}$", "$\\frac{3}{8}$", "$\\frac{3}{4}$", "$\\frac{1}{2}$"],
        "answer": 1,
        "explanation": "$1 - 2\\sin\\cos = \\frac{1}{4} \\implies 2\\sin\\cos = \\frac{3}{4} \\implies \\sin\\cos = \\frac{3}{8}$。"
    },
    55: {
        "question": "承上題若 $\\sin\\theta\\cos\\theta = \\frac{3}{8}$，求 $\\tan\\theta + \\cot\\theta$ 之值為何？",
        "options": ["$\\frac{3}{8}$", "$\\frac{8}{3}$", "$\\frac{4}{3}$", "$\\frac{5}{3}$"],
        "answer": 1,
        "explanation": "取倒數得 $\\frac{8}{3}$。"
    },
    56: {
        "question": "已知 $\\cos\\theta = \\frac{1}{5}$，求 $\\frac{1}{1 + \\sin\\theta} + \\frac{1}{1 - \\sin\\theta}$ 之值為何？",
        "options": ["$25$", "$50$", "$10$", "$5$"],
        "answer": 1,
        "explanation": "通分得 $\\frac{2}{1 - \\sin^2\\theta} = \\frac{2}{\\cos^2\\theta} = \\frac{2}{1/25} = 50$。"
    },
    57: {
        "question": "已知 $\\tan x + \\cot x = \\frac{25}{12}$，求 $\\sin x\\cos x$ 之值為何？",
        "options": ["$\\frac{25}{12}$", "$\\frac{12}{25}$", "$\\frac{1}{2}$", "$\\frac{7}{25}$"],
        "answer": 1,
        "explanation": "倒數得 $\\frac{12}{25}$。"
    },
    58: {
        "question": "承上題已知 $\\sin x\\cos x = \\frac{12}{25}$，且 $x$ 為銳角，求 $\\sin x + \\cos x$ 之值為何？",
        "options": ["$\\frac{7}{5}$", "$\\frac{49}{25}$", "$\\frac{5}{7}$", "$1$"],
        "answer": 0,
        "explanation": "$(\\sin + \\cos)^2 = 1 + 2(12/25) = \\frac{49}{25}$，開根號得 $\\frac{7}{5}$。"
    },
    59: {
        "question": "已知 $\\sin x + \\cos x = \\frac{7}{5}$ 且 $\\sin x\\cos x = \\frac{12}{25}$，求 $\\sin^3 x + \\cos^3 x$ 之值為何？",
        "options": ["$\\frac{91}{125}$", "$\\frac{84}{125}$", "$\\frac{7}{5}$", "$\\frac{13}{25}$"],
        "answer": 0,
        "explanation": "因式分解 $(\\frac{7}{5})(1 - \\frac{12}{25}) = \\frac{7}{5} \\times \\frac{13}{25} = \\frac{91}{125}$。"
    },
    60: {
        "question": "【終極神技卷】關於直角三角形與三角函數的恆等關係，下列何者「恆成立」？",
        "options": ["$\\sin\\theta \\cdot \\cos\\theta = 1$", "$\\sin^2\\theta + \\cos^2\\theta = 1$", "$\\tan^2\\theta + \\sec^2\\theta = 1$", "$\\cot\\theta = \\frac{\\sin\\theta}{\\cos\\theta}$"],
        "answer": 1,
        "explanation": "畢氏平方恆等式 $\\sin^2\\theta + \\cos^2\\theta = 1$ 恆成立！"
    }
}

# 動態幾何模型參數切換資料 (一題多變)
MODEL_DATA = {
    # CASE 04 (8-15-17 三角形切換)
    4: [
        {"name": "標準比例 (8-15-17)", "desc": "AC=8, BC=15, AB=17", "vals": {"sin": "15/17", "cos": "8/17", "tan": "15/8"}},
        {"name": "擴大 2 倍 (16-30-34)", "desc": "AC=16, BC=30, AB=34", "vals": {"sin": "15/17", "cos": "8/17", "tan": "15/8"}},
        {"name": "互換角視角 (∠B)", "desc": "對邊變 8, 鄰邊變 15", "vals": {"sin": "8/17", "cos": "15/17", "tan": "8/15"}}
    ],
    # CASE 08 (5-12-13 三角形切換)
    8: [
        {"name": "基準參數 k=1", "desc": "鄰=5, 對=12, 斜=13", "vals": {"sin": "12/13", "cos": "5/13", "tan": "12/5"}},
        {"name": "放大倍率 k=3", "desc": "鄰=15, 對=36, 斜=39", "vals": {"sin": "12/13", "cos": "5/13", "tan": "12/5"}}
    ],
    # CASE 14 (特別角切換)
    14: [
        {"name": "30° (π/6)", "desc": "對邊=1, 鄰邊=√3, 斜邊=2", "vals": {"sin": "1/2", "cos": "√3/2", "tan": "√3/3"}},
        {"name": "45° (π/4)", "desc": "對邊=1, 鄰邊=1, 斜邊=√2", "vals": {"sin": "√2/2", "cos": "√2/2", "tan": "1"}},
        {"name": "60° (π/3)", "desc": "對邊=√3, 鄰邊=1, 斜邊=2", "vals": {"sin": "√3/2", "cos": "1/2", "tan": "√3"}}
    ]
}

# 少年偵探團六大升級考核關卡設定
CHALLENGE_STAGES = [
    {
        "stage": 1,
        "title": "STAGE 01：基礎偵查關（銳角三角比入門）",
        "desc": "考核直角三角形三邊定位、六大函數定義與知一求其餘",
        "card_ids": [1, 2, 3, 4, 8, 10]
    },
    {
        "stage": 2,
        "title": "STAGE 02：特別角速算特訓關",
        "desc": "考核 30°、45°、60° 精確值與四則運算速算",
        "card_ids": [12, 13, 14, 15, 16, 18]
    },
    {
        "stage": 3,
        "title": "STAGE 03：現場搜查素養關（生活工程反推）",
        "desc": "考核無障礙坡道與險升坡反三角函數計算機操作",
        "card_ids": [19, 20]
    },
    {
        "stage": 4,
        "title": "STAGE 04：六角星陣推理關（恆等關係）",
        "desc": "考核倒數、商數、平方與餘角四大關係靈活化簡",
        "card_ids": [21, 24, 25, 28, 32, 34]
    },
    {
        "stage": 5,
        "title": "STAGE 05：警視廳實戰考核關（章末習作是非與實戰）",
        "desc": "考核課本章末習題觀念是非與核心基礎題型",
        "card_ids": [41, 42, 43, 45, 46, 51]
    },
    {
        "stage": 6,
        "title": "STAGE 06：劇場版終極魔王破解案",
        "desc": "考核三角恆等式對稱式、通分化簡與立方和終極破案",
        "card_ids": [36, 37, 54, 56, 58, 59]
    }
]
