# -*- coding: utf-8 -*-
"""
interactive_js_module.py - 泰宇版 技術高中數學（第一冊）2-2 三角函數的定義與性質
前端十大互動 JavaScript 核心邏輯模組
遵循 SOP v3.0 名偵探柯南數理探案特訓 ‧ 旗艦全功能標準版：
- 雙向同步逐步導引 showStep（防短路鐵律，課堂聚焦與半透明模糊遮蔽）
- 心智圖返回鍵、全螢幕投影 (F 鍵) 與返回心智圖跳轉
- 多功能電子白板（穿透現場 V、筆記 B、螢光 H、橡皮擦 E 4 段粗細、8 色 + 自訂取色、Undo、Clear）
- 頁尾第一列膠囊計數器（人氣/到訪/互動雙向同步，從 0 起算）
- 教師解答版密碼驗證 (88888888)
- 阿笠博士動態幾何實驗室 (直角三角形三角比動態形變與畢氏平方恆等檢驗儀)
- 六大關卡少年偵探團升級考核系統 (麻醉槍生命值、STAGE 05 習作實戰關與 STAGE 06 終極魔王關)
"""

INTERACTIVE_JS_CODE = r"""
// ==========================================
// 1. 全域狀態與初始化
// ==========================================
let allCards = [];
let currentCategory = 'all';
let currentCardView = 'all'; // all, mastered, review
let currentModalIndex = 0;
let fromMindmap = false;
let cardStepStates = {}; // 記錄每張卡片目前停留在哪一步 (預設 0=全部)

// 電子白板狀態
let isDrawing = false;
let whiteboardCanvas = null;
let whiteboardCtx = null;
let currentPenColor = '#dc2626';
let currentPenSize = 4;
let currentHighlighterAlpha = 0.4;
let currentEraserSize = 26;
let whiteboardMode = 'mouse'; // 'mouse', 'pen', 'highlighter', 'eraser'
let isEraserMode = false;
let strokeHistory = [];

// 闖關檢核狀態
let currentStageIndex = 0;
let currentQuizQuestionIndex = 0;
let stageQuizList = [];
let currentLives = 3;
let currentScore = 0;
let currentCombo = 0;
let maxCombo = 0;

// 動態實驗室狀態
let currentLabAngle = 30.0;

document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

function initApp() {
    allCards = window.CARDS_DATA || [];
    renderCards();
    initStats();
    initWhiteboard();
    initKeyboardShortcuts();
    renderMindmapTree();
    updateProgressBar();
    initLab();
}

// ==========================================
// 2. 頁面載入與統計計數器 (Core Rule 5)
// ==========================================
function initStats() {
    let pageviews = parseInt(localStorage.getItem('taiyu_2_2_pageviews') || '0', 10) + 1;
    let visitors = parseInt(localStorage.getItem('taiyu_2_2_visitors') || '0', 10);
    let interactions = parseInt(localStorage.getItem('taiyu_2_2_interactions') || '0', 10);

    if (!sessionStorage.getItem('taiyu_2_2_session_visited')) {
        visitors += 1;
        sessionStorage.setItem('taiyu_2_2_session_visited', 'true');
    }

    localStorage.setItem('taiyu_2_2_pageviews', pageviews.toString());
    localStorage.setItem('taiyu_2_2_visitors', visitors.toString());
    localStorage.setItem('taiyu_2_2_interactions', interactions.toString());

    updateStatsDisplay(pageviews, visitors, interactions);
}

function recordInteraction() {
    let interactions = parseInt(localStorage.getItem('taiyu_2_2_interactions') || '0', 10) + 1;
    localStorage.setItem('taiyu_2_2_interactions', interactions.toString());
    let pageviews = parseInt(localStorage.getItem('taiyu_2_2_pageviews') || '1', 10);
    let visitors = parseInt(localStorage.getItem('taiyu_2_2_visitors') || '1', 10);
    updateStatsDisplay(pageviews, visitors, interactions);
}

function updateStatsDisplay(pv, vis, act) {
    const sPv = document.getElementById('stat-pageviews');
    const sVis = document.getElementById('stat-visitors');
    const sAct = document.getElementById('stat-interactions');
    if (sPv) sPv.innerText = pv;
    if (sVis) sVis.innerText = vis;
    if (sAct) sAct.innerText = act;

    const fPv = document.getElementById('footer-pageviews');
    const fVis = document.getElementById('footer-visitors');
    const fAct = document.getElementById('footer-interactions');
    if (fPv) fPv.innerText = pv;
    if (fVis) fVis.innerText = vis;
    if (fAct) fAct.innerText = act;
}

// ==========================================
// 3. 卡片渲染與分類篩選
// ==========================================
function filterCategory(cat) {
    currentCategory = cat;
    recordInteraction();
    document.querySelectorAll('.cat-btn').forEach(btn => {
        if (btn.dataset.category === cat) {
            btn.classList.add('bg-amber-600', 'text-white');
            btn.classList.remove('bg-white', 'text-slate-700');
        } else {
            btn.classList.remove('bg-amber-600', 'text-white');
            btn.classList.add('bg-white', 'text-slate-700');
        }
    });
    renderCards();
}

function filterCardView(view) {
    currentCardView = view;
    recordInteraction();
    document.querySelectorAll('.view-btn').forEach(btn => {
        if (btn.dataset.view === view) {
            btn.classList.add('bg-amber-600', 'text-white');
            btn.classList.remove('bg-amber-50', 'text-amber-800');
        } else {
            btn.classList.remove('bg-amber-600', 'text-white');
            btn.classList.add('bg-amber-50', 'text-amber-800');
        }
    });
    renderCards();
}

function renderCards() {
    const grid = document.getElementById('cards-grid');
    if (!grid) return;

    let filtered = allCards.filter(card => {
        if (currentCategory !== 'all' && card.category !== currentCategory) return false;
        const isMastered = localStorage.getItem(`mastered_${card.id}`) === 'true';
        if (currentCardView === 'mastered' && !isMastered) return false;
        if (currentCardView === 'review' && isMastered) return false;
        return true;
    });

    document.getElementById('card-count-badge').innerText = `共 ${filtered.length} 個案件`;

    grid.innerHTML = filtered.map((card, idx) => {
        const isMastered = localStorage.getItem(`mastered_${card.id}`) === 'true';
        const cardRealIndex = allCards.findIndex(c => c.id === card.id);
        const curStep = cardStepStates[cardRealIndex] || 0;

        // 生成步驟導引按鈕 (動態匹配步驟數)
        let stepButtonsHtml = `<button onclick="showStep(${cardRealIndex}, 0, event)" class="step-btn px-2.5 py-1 text-xs sm:text-sm rounded-lg font-bold ${curStep===0?'bg-amber-600 text-white':'bg-slate-100 text-slate-600 hover:bg-slate-200'}">全部</button>`;
        card.steps.forEach(s => {
            stepButtonsHtml += `<button onclick="showStep(${cardRealIndex}, ${s.num}, event)" class="step-btn px-2.5 py-1 text-xs sm:text-sm rounded-lg font-bold ${curStep===s.num?'bg-amber-600 text-white':'bg-slate-100 text-slate-600 hover:bg-slate-200'}">線索${s.num}</button>`;
        });

        // 生成步驟內容 (含模糊遮蔽)
        let stepsHtml = card.steps.map(s => {
            const isBlur = (curStep > 0 && s.num > curStep);
            const isHighlight = (curStep > 0 && s.num === curStep);
            return `
            <div id="grid-card-${cardRealIndex}-step-${s.num}" class="p-3 rounded-xl border text-sm sm:text-base mb-2 transition-all duration-300 ${isHighlight ? 'bg-amber-50 border-amber-400 shadow-xs' : 'bg-slate-50 border-slate-200'} ${isBlur ? 'blur-[1.5px] opacity-20' : ''}">
                <div class="font-bold text-amber-900 mb-1 text-sm sm:text-base">${s.title}</div>
                <div class="text-slate-800 leading-relaxed text-sm sm:text-base">${s.content}</div>
            </div>`;
        }).join('');

        const isConclusionBlur = (curStep > 0 && curStep < card.steps.length);

        return `
        <div class="card-item perspective relative min-h-[710px] h-[755px]" data-card-index="${cardRealIndex}">
            <div id="flipper-${cardRealIndex}" class="flipper w-full h-full relative transition-transform duration-500 transform-style-3d">
                
                <!-- 卡片正面 (題幹、幾何模型與破案導引) -->
                <div onclick="if(!event.target.closest('button, a, input')) flipCard(${cardRealIndex}, event)" class="card-front cursor-pointer absolute inset-0 w-full h-full bg-[#fbf9f4] border-2 border-amber-300 rounded-2xl p-5 flex flex-col justify-between backface-hidden shadow-sm hover:shadow-md transition-shadow">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-3 py-1 text-xs sm:text-sm font-black rounded-full bg-amber-600 text-white shadow-2xs">${card.tag}</span>
                            <span class="text-xs sm:text-sm font-bold text-slate-500">${card.page}</span>
                            <button onclick="toggleMastered(${card.id}, event)" class="text-xs sm:text-sm px-2.5 py-1 rounded-full font-bold border transition-colors ${isMastered ? 'bg-emerald-500 text-white border-emerald-500' : 'bg-slate-100 text-slate-500 border-slate-200'}">
                                <i class="fa-solid ${isMastered ? 'fa-check' : 'fa-circle-question'} mr-1"></i>${isMastered ? '已結案' : '未結案'}
                            </button>
                        </div>
                        <h3 class="text-lg sm:text-xl font-black text-amber-950 mb-2 leading-snug tracking-tight">${card.title}</h3>
                        <div class="text-sm sm:text-base text-slate-800 leading-relaxed bg-white/90 p-3 rounded-xl border border-amber-200/80 max-h-40 overflow-y-auto font-medium mb-3">
                            ${card.front_content}
                        </div>

                        <!-- 正面幾何模型圖形展示 (黃色方框容器，高度充裕、溢出保護，圖表完全置入內部) -->
                        <div class="h-48 sm:h-52 bg-amber-50/70 rounded-xl p-2.5 border-2 border-amber-300/90 flex items-center justify-center mt-4 mb-3 shadow-2xs overflow-hidden">
                            ${card.svg}
                        </div>
                    </div>

                    <div>
                        <div class="bg-red-50/95 border border-red-200 p-3 rounded-xl text-xs sm:text-sm text-red-950 mb-3 font-semibold shadow-2xs">
                            ${card.front_tip}
                        </div>

                        <!-- 正面互動作答抽屜 -->
                        <div class="pt-2 border-t border-slate-200 flex items-center justify-between">
                            <button onclick="openCardQuiz(${card.id}, event)" class="px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-bold bg-amber-100 text-amber-900 hover:bg-amber-200 transition-colors shadow-2xs">
                                <i class="fa-solid fa-bullseye mr-1 text-red-600"></i>破案自檢抽屜
                            </button>
                            <div class="flex items-center gap-2">
                                <button onclick="openFullscreenModal(${cardRealIndex}, event)" class="p-2 text-slate-500 hover:text-amber-600 rounded-xl hover:bg-amber-50 text-base" title="全螢幕投影劇院">
                                    <i class="fa-solid fa-expand"></i>
                                </button>
                                <button onclick="flipCard(${cardRealIndex}, event)" class="px-3.5 py-1.5 rounded-xl text-xs sm:text-sm font-bold bg-amber-600 text-white hover:bg-amber-700 transition-colors shadow-2xs">
                                    <i class="fa-solid fa-rotate mr-1"></i>翻轉查線索
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 卡片背面 (推理筆記與 SVG 圖解) -->
                <div onclick="if(!event.target.closest('button, a, input')) flipCard(${cardRealIndex}, event)" class="card-back cursor-pointer absolute inset-0 w-full h-full bg-white border-2 border-amber-400 rounded-2xl p-4 flex flex-col justify-between rotate-y-180 backface-hidden shadow-md">
                    <div>
                        <div class="flex items-center justify-between pb-2 border-b border-slate-200 mb-2">
                            <div class="flex items-center gap-1.5">
                                <span class="px-2.5 py-0.5 text-xs sm:text-sm font-black rounded-lg bg-amber-600 text-white">${card.tag}</span>
                                <span class="text-sm sm:text-base font-black text-amber-900">👓 名偵探推理筆記</span>
                            </div>
                            <div class="flex items-center gap-1">
                                ${stepButtonsHtml}
                            </div>
                        </div>

                        <div class="max-h-44 overflow-y-auto pr-1">
                            ${stepsHtml}
                        </div>
                    </div>

                    <div>
                        <!-- 背面幾何圖解展示 (高度提升至 44~48) -->
                        <div class="h-44 sm:h-48 bg-slate-50 rounded-xl p-2 border border-slate-200 flex items-center justify-center my-1">
                            ${card.svg}
                        </div>

                        <div id="grid-card-${cardRealIndex}-conclusion" class="p-2.5 rounded-xl bg-emerald-50 border-2 border-emerald-500 text-xs sm:text-sm font-bold text-emerald-950 text-center transition-all duration-300 ${isConclusionBlur ? 'blur-[1.5px] opacity-20' : ''}">
                            ${card.conclusion}
                        </div>

                        <div class="flex justify-between items-center pt-2 mt-1 border-t border-slate-100">
                            <button onclick="openFullscreenModal(${cardRealIndex}, event)" class="text-xs sm:text-sm font-bold text-amber-700 hover:underline">
                                <i class="fa-solid fa-expand mr-1"></i>劇院投影模式
                            </button>
                            <button onclick="flipCard(${cardRealIndex}, event)" class="px-3.5 py-1.5 text-xs sm:text-sm font-bold rounded-xl bg-slate-200 text-slate-700 hover:bg-slate-300 transition-colors">
                                <i class="fa-solid fa-rotate-left mr-1"></i>返回案情
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
        `;
    }).join('');

    renderMath();
}

// 翻牌操作
function flipCard(idx, e) {
    if (e) e.stopPropagation();
    recordInteraction();
    const flipper = document.getElementById(`flipper-${idx}`);
    if (flipper) {
        flipper.classList.toggle('rotate-y-180');
    }
}

function flipAll() {
    recordInteraction();
    document.querySelectorAll('.flipper').forEach(f => f.classList.add('rotate-y-180'));
}

function resetFlip() {
    recordInteraction();
    document.querySelectorAll('.flipper').forEach(f => f.classList.remove('rotate-y-180'));
}

// 結案標記
function toggleMastered(cardId, e) {
    if (e) e.stopPropagation();
    recordInteraction();
    const key = `mastered_${cardId}`;
    const cur = localStorage.getItem(key) === 'true';
    localStorage.setItem(key, (!cur).toString());
    renderCards();
    updateProgressBar();
}

function updateProgressBar() {
    let masteredCount = 0;
    allCards.forEach(c => {
        if (localStorage.getItem(`mastered_${c.id}`) === 'true') masteredCount++;
    });
    const percent = allCards.length ? Math.round((masteredCount / allCards.length) * 100) : 0;
    const bar = document.getElementById('case-progress-bar');
    const txt = document.getElementById('case-progress-text');
    if (bar) bar.style.width = `${percent}%`;
    if (txt) txt.innerText = `${masteredCount} / ${allCards.length} (${percent}%)`;
}

// ==========================================
// 4. 逐步引導 showStep 雙向同步 (Core Rule 10)
// ==========================================
function showStep(cardIdx, stepNum, e) {
    if (e) e.stopPropagation();
    recordInteraction();
    cardStepStates[cardIdx] = stepNum;

    // 1. 同步更新主畫面網格
    const card = allCards[cardIdx];
    if (card) {
        // 更新網格按鈕高亮
        const gridCardEl = document.querySelector(`.card-item[data-card-index="${cardIdx}"]`);
        if (gridCardEl) {
            gridCardEl.querySelectorAll('.step-btn').forEach((btn, bIdx) => {
                if (bIdx === stepNum) {
                    btn.classList.add('bg-amber-600', 'text-white');
                    btn.classList.remove('bg-slate-100', 'text-slate-600');
                } else {
                    btn.classList.remove('bg-amber-600', 'text-white');
                    btn.classList.add('bg-slate-100', 'text-slate-600');
                }
            });
        }

        // 更新網格步驟遮蔽
        card.steps.forEach(s => {
            const stepEl = document.getElementById(`grid-card-${cardIdx}-step-${s.num}`);
            if (stepEl) {
                if (stepNum === 0) {
                    stepEl.classList.remove('blur-[1.5px]', 'opacity-20', 'bg-amber-50', 'border-amber-400');
                    stepEl.classList.add('bg-slate-50', 'border-slate-200');
                } else if (s.num === stepNum) {
                    stepEl.classList.remove('blur-[1.5px]', 'opacity-20', 'bg-slate-50', 'border-slate-200');
                    stepEl.classList.add('bg-amber-50', 'border-amber-400');
                } else if (s.num < stepNum) {
                    stepEl.classList.remove('blur-[1.5px]', 'opacity-20', 'bg-amber-50', 'border-amber-400');
                    stepEl.classList.add('bg-slate-50', 'border-slate-200');
                } else {
                    stepEl.classList.add('blur-[1.5px]', 'opacity-20');
                    stepEl.classList.remove('bg-amber-50', 'border-amber-400');
                }
            }
        });

        // 結論框遮蔽
        const conEl = document.getElementById(`grid-card-${cardIdx}-conclusion`);
        if (conEl) {
            if (stepNum > 0 && stepNum < card.steps.length) {
                conEl.classList.add('blur-[1.5px]', 'opacity-20');
            } else {
                conEl.classList.remove('blur-[1.5px]', 'opacity-20');
            }
        }
    }

    // 2. 同步更新全螢幕劇院視窗 (如果當前開啟)
    if (currentModalIndex === cardIdx) {
        updateModalStepUI(cardIdx, stepNum);
    }
}

function updateModalStepUI(cardIdx, stepNum) {
    const card = allCards[cardIdx];
    if (!card) return;

    // 按鈕高亮
    const modalControls = document.getElementById('modal-step-controls');
    if (modalControls) {
        modalControls.querySelectorAll('.modal-step-btn').forEach((btn, bIdx) => {
            if (bIdx === stepNum) {
                btn.classList.add('bg-amber-600', 'text-white');
                btn.classList.remove('bg-slate-200', 'text-slate-700');
            } else {
                btn.classList.remove('bg-amber-600', 'text-white');
                btn.classList.add('bg-slate-200', 'text-slate-700');
            }
        });
    }

    // 步驟遮蔽
    card.steps.forEach(s => {
        const stepEl = document.getElementById(`modal-step-${s.num}`);
        if (stepEl) {
            if (stepNum === 0) {
                stepEl.classList.remove('blur-[1.5px]', 'opacity-20', 'bg-amber-50', 'border-amber-400');
                stepEl.classList.add('bg-slate-50', 'border-slate-200');
            } else if (s.num === stepNum) {
                stepEl.classList.remove('blur-[1.5px]', 'opacity-20', 'bg-slate-50', 'border-slate-200');
                stepEl.classList.add('bg-amber-50', 'border-amber-400');
            } else if (s.num < stepNum) {
                stepEl.classList.remove('blur-[1.5px]', 'opacity-20', 'bg-amber-50', 'border-amber-400');
                stepEl.classList.add('bg-slate-50', 'border-slate-200');
            } else {
                stepEl.classList.add('blur-[1.5px]', 'opacity-20');
                stepEl.classList.remove('bg-amber-50', 'border-amber-400');
            }
        }
    });

    // 結論框遮蔽
    const conEl = document.getElementById('modal-conclusion');
    if (conEl) {
        if (stepNum > 0 && stepNum < card.steps.length) {
            conEl.classList.add('blur-[1.5px]', 'opacity-20');
        } else {
            conEl.classList.remove('blur-[1.5px]', 'opacity-20');
        }
    }
}

// ==========================================
// 5. 全螢幕劇院模式 (Core Rule 11 & 12)
// ==========================================
function openFullscreenModal(cardIdx, e) {
    if (e) e.stopPropagation();
    recordInteraction();
    currentModalIndex = cardIdx;
    const modal = document.getElementById('fullscreen-modal');
    if (!modal) return;

    modal.classList.remove('hidden');
    document.body.classList.add('overflow-hidden');
    renderModalContent(cardIdx);
}

function closeFullscreenModal() {
    recordInteraction();
    const modal = document.getElementById('fullscreen-modal');
    if (modal) modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
    clearWhiteboard();

    if (fromMindmap) {
        fromMindmap = false;
        openMindmapModal();
    }
}

function renderModalContent(cardIdx) {
    const card = allCards[cardIdx];
    if (!card) return;

    const curStep = cardStepStates[cardIdx] || 0;

    // 頂部標題
    document.getElementById('modal-case-tag').innerText = card.tag;
    document.getElementById('modal-case-title').innerText = card.title;
    document.getElementById('modal-case-page').innerText = card.page;

    // 左欄題幹與破案導引
    document.getElementById('modal-front-content').innerHTML = card.front_content;
    document.getElementById('modal-front-tip').innerHTML = card.front_tip;

    // 右欄步驟與按鈕
    let stepButtonsHtml = `<button onclick="showStep(${cardIdx}, 0, event)" class="modal-step-btn px-3 py-1 rounded text-xs font-bold ${curStep===0?'bg-amber-600 text-white':'bg-slate-200 text-slate-700 hover:bg-slate-300'}">全部</button>`;
    card.steps.forEach(s => {
        stepButtonsHtml += `<button onclick="showStep(${cardIdx}, ${s.num}, event)" class="modal-step-btn px-3 py-1 rounded text-xs font-bold ${curStep===s.num?'bg-amber-600 text-white':'bg-slate-200 text-slate-700 hover:bg-slate-300'}">線索${s.num}</button>`;
    });
    document.getElementById('modal-step-controls').innerHTML = stepButtonsHtml;

    let stepsHtml = card.steps.map(s => {
        const isBlur = (curStep > 0 && s.num > curStep);
        const isHighlight = (curStep > 0 && s.num === curStep);
        return `
        <div id="modal-step-${s.num}" class="p-3.5 rounded-xl border mb-2 text-sm transition-all duration-300 ${isHighlight ? 'bg-amber-50 border-amber-400 shadow-sm' : 'bg-slate-50 border-slate-200'} ${isBlur ? 'blur-[1.5px] opacity-20' : ''}">
            <div class="font-bold text-amber-950 mb-1">${s.title}</div>
            <div class="text-slate-800 leading-relaxed">${s.content}</div>
        </div>`;
    }).join('');
    document.getElementById('modal-steps-container').innerHTML = stepsHtml;

    // SVG 圖解與結論
    document.getElementById('modal-svg-container').innerHTML = card.svg;
    const conEl = document.getElementById('modal-conclusion');
    conEl.innerHTML = card.conclusion;
    if (curStep > 0 && curStep < card.steps.length) {
        conEl.classList.add('blur-[1.5px]', 'opacity-20');
    } else {
        conEl.classList.remove('blur-[1.5px]', 'opacity-20');
    }

    // 序號導航
    document.getElementById('modal-nav-info').innerText = `${cardIdx + 1} / ${allCards.length}`;

    // 返回心智圖按鈕顯示
    const backMmBtn = document.getElementById('modal-back-mindmap-btn');
    if (backMmBtn) {
        if (fromMindmap) backMmBtn.classList.remove('hidden');
        else backMmBtn.classList.add('hidden');
    }

    renderMath();
    resizeWhiteboard();
}

function prevModalCard() {
    if (currentModalIndex > 0) {
        currentModalIndex--;
        renderModalContent(currentModalIndex);
    }
}

function nextModalCard() {
    if (currentModalIndex < allCards.length - 1) {
        currentModalIndex++;
        renderModalContent(currentModalIndex);
    }
}

// ==========================================
// 6. 電子搜查白板 (Core Rule 7)
// ==========================================
function initWhiteboard() {
    whiteboardCanvas = document.getElementById('whiteboard-canvas');
    if (!whiteboardCanvas) return;
    whiteboardCtx = whiteboardCanvas.getContext('2d');

    window.addEventListener('resize', resizeWhiteboard);

    whiteboardCanvas.addEventListener('mousedown', startDrawing);
    whiteboardCanvas.addEventListener('mousemove', draw);
    whiteboardCanvas.addEventListener('mouseup', stopDrawing);
    whiteboardCanvas.addEventListener('mouseleave', stopDrawing);

    whiteboardCanvas.addEventListener('touchstart', handleTouchStart, { passive: false });
    whiteboardCanvas.addEventListener('touchmove', handleTouchMove, { passive: false });
    whiteboardCanvas.addEventListener('touchend', stopDrawing);
}

function resizeWhiteboard() {
    if (!whiteboardCanvas) return;
    const parent = whiteboardCanvas.parentElement;
    if (parent) {
        whiteboardCanvas.width = parent.clientWidth;
        whiteboardCanvas.height = parent.clientHeight;
        redrawHistory();
    }
}

function setWhiteboardMode(mode) {
    whiteboardMode = mode;
    recordInteraction();
    const canvas = document.getElementById('whiteboard-canvas');

    document.querySelectorAll('.wb-tool-btn').forEach(btn => {
        if (btn.dataset.mode === mode) {
            btn.classList.add('bg-amber-600', 'text-white');
            btn.classList.remove('bg-white', 'text-slate-700');
        } else {
            btn.classList.remove('bg-amber-600', 'text-white');
            btn.classList.add('bg-white', 'text-slate-700');
        }
    });

    if (mode === 'mouse') {
        canvas.style.pointerEvents = 'none';
        canvas.style.cursor = 'default';
    } else {
        canvas.style.pointerEvents = 'auto';
        if (mode === 'pen') canvas.style.cursor = 'crosshair';
        else if (mode === 'highlighter') canvas.style.cursor = 'cell';
        else if (mode === 'eraser') canvas.style.cursor = 'not-allowed';
    }
}

function setPenColor(color) {
    currentPenColor = color;
    recordInteraction();
    document.querySelectorAll('.wb-color-btn').forEach(btn => {
        if (btn.dataset.color === color) btn.classList.add('ring-2', 'ring-amber-500', 'scale-110');
        else btn.classList.remove('ring-2', 'ring-amber-500', 'scale-110');
    });
    if (whiteboardMode === 'mouse' || whiteboardMode === 'eraser') {
        setWhiteboardMode('pen');
    }
}

function setPenSize(size) {
    currentPenSize = size;
}

function setHighlighterAlpha(alpha) {
    currentHighlighterAlpha = parseFloat(alpha);
    recordInteraction();
}

function setEraserSize(size) {
    currentEraserSize = parseInt(size, 10);
    recordInteraction();
}

function startDrawing(e) {
    if (whiteboardMode === 'mouse') return;
    isDrawing = true;
    const rect = whiteboardCanvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    strokeHistory.push({
        mode: whiteboardMode,
        color: currentPenColor,
        size: whiteboardMode === 'eraser' ? currentEraserSize : currentPenSize,
        alpha: currentHighlighterAlpha,
        points: [{ x, y }]
    });

    draw(e);
}

function draw(e) {
    if (!isDrawing || whiteboardMode === 'mouse') return;
    const rect = whiteboardCanvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const currentStroke = strokeHistory[strokeHistory.length - 1];
    currentStroke.points.push({ x, y });

    renderCurrentStroke(currentStroke);
}

function stopDrawing() {
    isDrawing = false;
}

function handleTouchStart(e) {
    if (whiteboardMode === 'mouse') return;
    e.preventDefault();
    const touch = e.touches[0];
    startDrawing(touch);
}

function handleTouchMove(e) {
    if (whiteboardMode === 'mouse') return;
    e.preventDefault();
    const touch = e.touches[0];
    draw(touch);
}

function renderCurrentStroke(stroke) {
    if (!whiteboardCtx || stroke.points.length < 2) return;
    const p1 = stroke.points[stroke.points.length - 2];
    const p2 = stroke.points[stroke.points.length - 1];

    whiteboardCtx.beginPath();
    whiteboardCtx.moveTo(p1.x, p1.y);
    whiteboardCtx.lineTo(p2.x, p2.y);

    if (stroke.mode === 'eraser') {
        whiteboardCtx.globalCompositeOperation = 'destination-out';
        whiteboardCtx.lineWidth = stroke.size;
        whiteboardCtx.lineCap = 'round';
        whiteboardCtx.stroke();
        whiteboardCtx.globalCompositeOperation = 'source-over';
    } else if (stroke.mode === 'highlighter') {
        whiteboardCtx.globalCompositeOperation = 'source-over';
        whiteboardCtx.strokeStyle = hexToRgba(stroke.color, stroke.alpha);
        whiteboardCtx.lineWidth = stroke.size * 3.5;
        whiteboardCtx.lineCap = 'square';
        whiteboardCtx.stroke();
    } else {
        whiteboardCtx.globalCompositeOperation = 'source-over';
        whiteboardCtx.strokeStyle = stroke.color;
        whiteboardCtx.lineWidth = stroke.size;
        whiteboardCtx.lineCap = 'round';
        whiteboardCtx.stroke();
    }
}

function redrawHistory() {
    if (!whiteboardCtx) return;
    whiteboardCtx.clearRect(0, 0, whiteboardCanvas.width, whiteboardCanvas.height);
    strokeHistory.forEach(stroke => {
        if (stroke.points.length < 2) return;
        for (let i = 1; i < stroke.points.length; i++) {
            const p1 = stroke.points[i - 1];
            const p2 = stroke.points[i];
            whiteboardCtx.beginPath();
            whiteboardCtx.moveTo(p1.x, p1.y);
            whiteboardCtx.lineTo(p2.x, p2.y);
            if (stroke.mode === 'eraser') {
                whiteboardCtx.globalCompositeOperation = 'destination-out';
                whiteboardCtx.lineWidth = stroke.size;
                whiteboardCtx.lineCap = 'round';
                whiteboardCtx.stroke();
                whiteboardCtx.globalCompositeOperation = 'source-over';
            } else if (stroke.mode === 'highlighter') {
                whiteboardCtx.strokeStyle = hexToRgba(stroke.color, stroke.alpha);
                whiteboardCtx.lineWidth = stroke.size * 3.5;
                whiteboardCtx.lineCap = 'square';
                whiteboardCtx.stroke();
            } else {
                whiteboardCtx.strokeStyle = stroke.color;
                whiteboardCtx.lineWidth = stroke.size;
                whiteboardCtx.lineCap = 'round';
                whiteboardCtx.stroke();
            }
        }
    });
}

function undoWhiteboard() {
    recordInteraction();
    if (strokeHistory.length > 0) {
        strokeHistory.pop();
        redrawHistory();
    }
}

function clearWhiteboard() {
    recordInteraction();
    strokeHistory = [];
    if (whiteboardCtx) {
        whiteboardCtx.clearRect(0, 0, whiteboardCanvas.width, whiteboardCanvas.height);
    }
}

function hexToRgba(hex, alpha) {
    let c = hex.replace('#', '');
    if (c.length === 3) c = c.split('').map(x => x + x).join('');
    const r = parseInt(c.substring(0, 2), 16);
    const g = parseInt(c.substring(2, 4), 16);
    const b = parseInt(c.substring(4, 6), 16);
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

// ==========================================
// 7. 解密口訣錦囊彈窗 (Core Rule 6)
// ==========================================
function openCheatsheetModal() {
    recordInteraction();
    const modal = document.getElementById('cheatsheet-modal');
    if (modal) modal.classList.remove('hidden');
    renderMath();
}

function closeCheatsheetModal() {
    const modal = document.getElementById('cheatsheet-modal');
    if (modal) modal.classList.add('hidden');
}

// ==========================================
// 8. 阿笠博士動態探案實驗室 (3 大互動學習模組)
// ==========================================
let currentLabTab = 'triangle';
let currentHexagonMode = 'reciprocal';
let selectedHexVertex = 'sin';

// 60秒特別角速算挑戰狀態
let drillTimer = null;
let drillSecondsLeft = 60;
let drillScore = 0;
let drillCombo = 0;
let drillMaxCombo = 0;
let drillCorrectCount = 0;
let currentDrillQuestion = null;

const DRILL_QUESTION_POOL = [
    { q: 'sin 30°', latexQ: '\\sin 30^\\circ', a: '1/2', latex: '\\frac{1}{2}' },
    { q: 'cos 30°', latexQ: '\\cos 30^\\circ', a: '√3/2', latex: '\\frac{\\sqrt{3}}{2}' },
    { q: 'tan 30°', latexQ: '\\tan 30^\\circ', a: '√3/3', latex: '\\frac{\\sqrt{3}}{3}' },
    { q: 'cot 30°', latexQ: '\\cot 30^\\circ', a: '√3', latex: '\\sqrt{3}' },
    { q: 'sec 30°', latexQ: '\\sec 30^\\circ', a: '2√3/3', latex: '\\frac{2\\sqrt{3}}{3}' },
    { q: 'csc 30°', latexQ: '\\csc 30^\\circ', a: '2', latex: '2' },

    { q: 'sin 45°', latexQ: '\\sin 45^\\circ', a: '√2/2', latex: '\\frac{\\sqrt{2}}{2}' },
    { q: 'cos 45°', latexQ: '\\cos 45^\\circ', a: '√2/2', latex: '\\frac{\\sqrt{2}}{2}' },
    { q: 'tan 45°', latexQ: '\\tan 45^\\circ', a: '1', latex: '1' },
    { q: 'cot 45°', latexQ: '\\cot 45^\\circ', a: '1', latex: '1' },
    { q: 'sec 45°', latexQ: '\\sec 45^\\circ', a: '√2', latex: '\\sqrt{2}' },
    { q: 'csc 45°', latexQ: '\\csc 45^\\circ', a: '√2', latex: '\\sqrt{2}' },

    { q: 'sin 60°', latexQ: '\\sin 60^\\circ', a: '√3/2', latex: '\\frac{\\sqrt{3}}{2}' },
    { q: 'cos 60°', latexQ: '\\cos 60^\\circ', a: '1/2', latex: '\\frac{1}{2}' },
    { q: 'tan 60°', latexQ: '\\tan 60^\\circ', a: '√3', latex: '\\sqrt{3}' },
    { q: 'cot 60°', latexQ: '\\cot 60^\\circ', a: '√3/3', latex: '\\frac{\\sqrt{3}}{3}' },
    { q: 'sec 60°', latexQ: '\\sec 60^\\circ', a: '2', latex: '2' },
    { q: 'csc 60°', latexQ: '\\csc 60^\\circ', a: '2√3/3', latex: '\\frac{2\\sqrt{3}}{3}' }
];

const DRILL_OPTIONS = [
    { latex: '\\frac{1}{2}', val: '1/2' },
    { latex: '\\frac{\\sqrt{2}}{2}', val: '√2/2' },
    { latex: '\\frac{\\sqrt{3}}{2}', val: '√3/2' },
    { latex: '1', val: '1' },
    { latex: '\\frac{\\sqrt{3}}{3}', val: '√3/3' },
    { latex: '\\sqrt{3}', val: '√3' },
    { latex: '\\sqrt{2}', val: '√2' },
    { latex: '2', val: '2' }
];

function openLabModal() {
    recordInteraction();
    const modal = document.getElementById('lab-modal');
    if (modal) modal.classList.remove('hidden');
    switchLabTab(currentLabTab);
}

function closeLabModal() {
    const modal = document.getElementById('lab-modal');
    if (modal) modal.classList.add('hidden');
    if (drillTimer) {
        clearInterval(drillTimer);
        drillTimer = null;
    }
}

function switchLabTab(tabName) {
    currentLabTab = tabName;
    recordInteraction();

    const tabs = ['triangle', 'hexagon', 'speeddrill'];
    tabs.forEach(t => {
        const pane = document.getElementById(`lab-tab-pane-${t}`);
        const btn = document.getElementById(`lab-tab-btn-${t}`);
        if (pane) {
            if (t === tabName) pane.classList.remove('hidden');
            else pane.classList.add('hidden');
        }
        if (btn) {
            if (t === tabName) {
                btn.className = "flex-1 py-2 px-3 rounded-lg text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-1.5 bg-indigo-600 text-white shadow-xs";
            } else {
                btn.className = "flex-1 py-2 px-3 rounded-lg text-xs sm:text-sm font-black transition-all flex items-center justify-center gap-1.5 text-slate-600 hover:text-indigo-600";
            }
        }
    });

    if (tabName === 'triangle') {
        updateTrigLab(currentLabAngle);
    } else if (tabName === 'hexagon') {
        renderSuperHexagon();
    }
}

function initLab() {
    const slider = document.getElementById('lab-angle-slider');
    if (slider) {
        slider.addEventListener('input', (e) => {
            currentLabAngle = parseFloat(e.target.value);
            updateTrigLab(currentLabAngle);
        });
    }
}

function setLabAngle(deg) {
    currentLabAngle = deg;
    const slider = document.getElementById('lab-angle-slider');
    if (slider) slider.value = deg;
    updateTrigLab(deg);
}

function updateTrigLab(deg) {
    const rad = deg * (Math.PI / 180);
    const sinVal = Math.sin(rad);
    const cosVal = Math.cos(rad);
    const tanVal = Math.tan(rad);
    const secVal = 1 / cosVal;
    const cscVal = 1 / sinVal;
    const cotVal = 1 / tanVal;

    const degDisplay = document.getElementById('lab-deg-display');
    if (degDisplay) degDisplay.innerText = `${deg.toFixed(1)}°`;

    const setTxt = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.innerText = val;
    };

    setTxt('lab-sin-val', sinVal.toFixed(4));
    setTxt('lab-cos-val', cosVal.toFixed(4));
    setTxt('lab-tan-val', tanVal.toFixed(4));
    setTxt('lab-csc-val', cscVal.toFixed(4));
    setTxt('lab-sec-val', secVal.toFixed(4));
    setTxt('lab-cot-val', cotVal.toFixed(4));

    const pythagoras = (sinVal * sinVal + cosVal * cosVal).toFixed(6);
    setTxt('lab-pythagoras-val', `${pythagoras}`);
    setTxt('lab-quotient-val', `${(sinVal / cosVal).toFixed(4)} (＝ tan θ)`);

    // 動態繪製直角三角形 SVG
    const svgContainer = document.getElementById('lab-svg-stage');
    if (svgContainer) {
        const cx = 45;
        const cy = 220;
        const r = 210; // 斜邊放大比例
        const bx = cx + cosVal * r;
        const by = cy;
        const ax = bx;
        const ay = cy - sinVal * r;

        svgContainer.innerHTML = `
        <svg viewBox="0 0 340 250" class="w-full h-full">
            <rect width="340" height="250" fill="#f8fafc" rx="14"/>
            <!-- 直角三角形著色底色 -->
            <polygon points="${cx},${cy} ${bx},${by} ${ax},${ay}" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>
            
            <!-- 直角記號 -->
            <rect x="${bx - 14}" y="${by - 14}" width="14" height="14" fill="none" stroke="#2563eb" stroke-width="1.5"/>
            <circle cx="${bx - 7}" cy="${by - 7}" r="1.5" fill="#2563eb"/>

            <!-- 銳角 θ 弧線與標註 -->
            <path d="M ${cx + 34} ${cy} A 34 34 0 0 0 ${cx + 34 * cosVal} ${cy - 34 * sinVal}" fill="none" stroke="#dc2626" stroke-width="2.2"/>
            <text x="${cx + 42}" y="${cy - 9}" font-size="13" font-weight="bold" fill="#dc2626">θ = ${deg.toFixed(1)}°</text>
            
            <!-- 頂點標記 -->
            <circle cx="${cx}" cy="${cy}" r="3.5" fill="#1e40af"/>
            <text x="${cx - 15}" y="${cy + 5}" font-size="14" font-weight="bold" fill="#1e40af">A</text>

            <circle cx="${bx}" cy="${by}" r="3.5" fill="#2563eb"/>
            <text x="${bx + 8}" y="${by + 16}" font-size="14" font-weight="bold" fill="#2563eb">C(90°)</text>

            <circle cx="${ax}" cy="${ay}" r="3.5" fill="#dc2626"/>
            <text x="${ax + 8}" y="${ay - 6}" font-size="14" font-weight="bold" fill="#dc2626">B</text>

            <!-- 三邊長標記 -->
            <text x="${(cx + bx) / 2}" y="${cy + 18}" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">鄰邊 x = cos θ = ${cosVal.toFixed(3)}</text>
            <text x="${bx + 8}" y="${(by + ay) / 2}" font-size="12" font-weight="bold" fill="#dc2626">對邊 y = sin θ = ${sinVal.toFixed(3)}</text>
            <text x="${(cx + ax) / 2 - 14}" y="${(cy + ay) / 2 - 12}" font-size="12" font-weight="bold" fill="#16a34a">斜邊 r = 1.000</text>
        </svg>
        `;
    }
}

// ------------------------------------------
// 魔法六角密碼盤 (Magic Super Hexagon)
// ------------------------------------------
const HEX_VERTICES = {
    sin: { name: 'sin θ', latex: '\\sin\\theta', x: 100, y: 55, partner: 'csc', adjRight: 'cos', adjLeft: 'tan' },
    cos: { name: 'cos θ', latex: '\\cos\\theta', x: 240, y: 55, partner: 'sec', adjRight: 'cot', adjLeft: 'sin' },
    cot: { name: 'cot θ', latex: '\\cot\\theta', x: 285, y: 135, partner: 'tan', adjRight: 'csc', adjLeft: 'cos' },
    csc: { name: 'csc θ', latex: '\\csc\\theta', x: 240, y: 215, partner: 'sin', adjRight: 'sec', adjLeft: 'cot' },
    sec: { name: 'sec θ', latex: '\\sec\\theta', x: 100, y: 215, partner: 'cos', adjRight: 'tan', adjLeft: 'csc' },
    tan: { name: 'tan θ', latex: '\\tan\\theta', x: 55, y: 135, partner: 'cot', adjRight: 'sin', adjLeft: 'sec' }
};

function setHexagonMode(mode) {
    currentHexagonMode = mode;
    recordInteraction();

    const modes = ['reciprocal', 'quotient', 'pythagorean'];
    modes.forEach(m => {
        const btn = document.getElementById(`hex-mode-${m}-btn`);
        if (btn) {
            if (m === mode) {
                btn.className = "px-3.5 py-1.5 rounded-xl text-xs font-bold bg-amber-500 text-slate-950 shadow-xs border border-amber-600 transition-all";
            } else {
                btn.className = "px-3.5 py-1.5 rounded-xl text-xs font-bold bg-slate-200 text-slate-700 hover:bg-slate-300 transition-all";
            }
        }
    });

    renderSuperHexagon();
}

function selectHexVertex(v) {
    selectedHexVertex = v;
    recordInteraction();
    renderSuperHexagon();
}

function renderSuperHexagon() {
    const container = document.getElementById('hexagon-svg-container');
    if (!container) return;

    const centerX = 170;
    const centerY = 135;

    let highlightLines = '';
    let highlightTriangles = '';
    let badgeTitle = '';
    let formulaLaTeX = '';
    let explanationText = '';

    const v = HEX_VERTICES[selectedHexVertex];

    if (currentHexagonMode === 'reciprocal') {
        const partner = HEX_VERTICES[v.partner];
        highlightLines = `
            <line x1="${v.x}" y1="${v.y}" x2="${partner.x}" y2="${partner.y}" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6 3"/>
            <circle cx="${centerX}" cy="${centerY}" r="18" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
        `;
        badgeTitle = '【對角互倒關係】穿透中心 1 的倒數伴侶';
        formulaLaTeX = `${v.latex} \\cdot ${partner.latex} = 1`;
        explanationText = `穿過中央的「1」，對角線兩端的三角函數互為倒數伴侶！例如：sin 與 csc 互為倒數，cos 與 sec 互為倒數，tan 與 cot 互為倒數！乘積恆等於 1！`;
    } else if (currentHexagonMode === 'quotient') {
        const next1 = HEX_VERTICES[v.adjRight];
        const next2 = HEX_VERTICES[HEX_VERTICES[v.adjRight].adjRight];
        highlightLines = `
            <line x1="${v.x}" y1="${v.y}" x2="${next1.x}" y2="${next1.y}" stroke="#38bdf8" stroke-width="3"/>
            <line x1="${next1.x}" y1="${next1.y}" x2="${next2.x}" y2="${next2.y}" stroke="#38bdf8" stroke-width="3"/>
        `;
        badgeTitle = '【相鄰商數關係】順時針/逆時針皆成立';
        formulaLaTeX = `${v.latex} = \\frac{${next1.latex}}{${next2.latex}}`;
        explanationText = `在六角形中，任意一個頂點等於它相鄰兩點之商！例如 $\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}$，$\\cot\\theta = \\frac{\\cos\\theta}{\\sin\\theta}$，$\\sin\\theta = \\frac{\\cos\\theta}{\\cot\\theta}$ 等，順逆時針環繞皆成立！`;
    } else if (currentHexagonMode === 'pythagorean') {
        highlightTriangles = `
            <!-- 頂部三角形 sin² + cos² = 1 -->
            <polygon points="100,55 240,55 170,135" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2"/>
            <!-- 左下三角形 1 + tan² = sec² -->
            <polygon points="170,135 55,135 100,215" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
            <!-- 右下三角形 1 + cot² = csc² -->
            <polygon points="170,135 285,135 240,215" fill="rgba(99, 102, 241, 0.25)" stroke="#6366f1" stroke-width="2"/>
        `;
        badgeTitle = '【倒三角平方關係】上兩端平方和等於底端';
        formulaLaTeX = `\\begin{gathered} \\sin^2\\theta + \\cos^2\\theta = 1 \\\\[4pt] 1 + \\tan^2\\theta = \\sec^2\\theta \\\\[4pt] 1 + \\cot^2\\theta = \\csc^2\\theta \\end{gathered}`;
        explanationText = `觀察三個帶陰影的「倒三角形」：上面兩個頂點的平方和，等於底端頂點的平方！<br>
        1. $\\sin^2\\theta + \\cos^2\\theta = 1^2 = 1$<br>
        2. $1^2 + \\tan^2\\theta = \\sec^2\\theta$ ($1 + \\tan^2 = \\sec^2$)<br>
        3. $1^2 + \\cot^2\\theta = \\csc^2\\theta$ ($1 + \\cot^2 = \\csc^2$)`;
    }

    const setTxt = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.innerHTML = val;
    };
    setTxt('hex-badge-title', badgeTitle);
    setTxt('hex-explanation-text', explanationText);

    // 用 KaTeX 直接高規格渲染公式
    const formulaEl = document.getElementById('hex-formula-display');
    if (formulaEl) {
        if (window.katex) {
            try {
                katex.render(formulaLaTeX, formulaEl, { displayMode: true, throwOnError: false });
            } catch(e) {
                formulaEl.innerText = formulaLaTeX;
            }
        } else {
            formulaEl.innerText = formulaLaTeX;
        }
    }

    // 重新渲染說明文字中的 KaTeX
    const expEl = document.getElementById('hex-explanation-text');
    if (expEl && window.renderMathInElement) {
        renderMathInElement(expEl, {
            delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }]
        });
    }

    // 繪製六角星 SVG
    container.innerHTML = `
    <svg viewBox="0 0 340 270" class="w-full h-full select-none cursor-pointer">
        <!-- 外圍正六邊形連線 -->
        <polygon points="100,55 240,55 285,135 240,215 100,215 55,135" fill="none" stroke="#475569" stroke-width="2"/>
        
        <!-- 對角線灰色底線 -->
        <line x1="100" y1="55" x2="240" y2="215" stroke="#334155" stroke-width="1.5"/>
        <line x1="240" y1="55" x2="100" y2="215" stroke="#334155" stroke-width="1.5"/>
        <line x1="55" y1="135" x2="285" y2="135" stroke="#334155" stroke-width="1.5"/>

        ${highlightTriangles}
        ${highlightLines}

        <!-- 中心點 1 -->
        <circle cx="${centerX}" cy="${centerY}" r="17" fill="#0f172a" stroke="#f59e0b" stroke-width="2.5"/>
        <text x="${centerX}" y="${centerY + 5}" text-anchor="middle" font-size="14" font-weight="900" fill="#f59e0b">1</text>

        <!-- 6 個頂點節點 -->
        ${Object.keys(HEX_VERTICES).map(key => {
            const item = HEX_VERTICES[key];
            const isSel = (key === selectedHexVertex);
            const fillCol = isSel ? '#f59e0b' : '#1e293b';
            const textCol = isSel ? '#0f172a' : '#ffffff';
            const strokeCol = isSel ? '#ffffff' : '#38bdf8';
            return `
            <g onclick="selectHexVertex('${key}')" class="transition-transform hover:scale-110">
                <circle cx="${item.x}" cy="${item.y}" r="22" fill="${fillCol}" stroke="${strokeCol}" stroke-width="${isSel ? '3' : '2'}"/>
                <text x="${item.x}" y="${item.y + 5}" text-anchor="middle" font-size="12" font-weight="900" fill="${textCol}">${item.name.split(' ')[0]}</text>
            </g>
            `;
        }).join('')}
    </svg>
    `;
}

// ------------------------------------------
// 60秒特別角速算破案挑戰 (Speed Drill)
// ------------------------------------------
function startSpeedDrill() {
    recordInteraction();
    drillSecondsLeft = 60;
    drillScore = 0;
    drillCombo = 0;
    drillMaxCombo = 0;
    drillCorrectCount = 0;

    const startView = document.getElementById('speeddrill-start-view');
    const gameView = document.getElementById('speeddrill-game-view');
    const resultView = document.getElementById('speeddrill-result-view');

    if (startView) startView.classList.add('hidden');
    if (resultView) resultView.classList.add('hidden');
    if (gameView) gameView.classList.remove('hidden');

    renderDrillOptionsGrid();
    nextDrillQuestion();

    if (drillTimer) clearInterval(drillTimer);
    drillTimer = setInterval(() => {
        drillSecondsLeft--;
        const timerEl = document.getElementById('drill-timer-text');
        if (timerEl) timerEl.innerText = `${drillSecondsLeft}s`;

        if (drillSecondsLeft <= 0) {
            clearInterval(drillTimer);
            drillTimer = null;
            finishSpeedDrill();
        }
    }, 1000);
}

function nextDrillQuestion() {
    const randIdx = Math.floor(Math.random() * DRILL_QUESTION_POOL.length);
    currentDrillQuestion = DRILL_QUESTION_POOL[randIdx];

    const card = document.getElementById('drill-question-card');
    if (card) {
        const latexStr = `${currentDrillQuestion.latexQ || currentDrillQuestion.q} = \\ ?`;
        if (window.katex) {
            try {
                katex.render(latexStr, card, { displayMode: true, throwOnError: false });
            } catch(e) {
                card.innerText = `${currentDrillQuestion.q} = ?`;
            }
        } else {
            card.innerText = `${currentDrillQuestion.q} = ?`;
        }
    }
}

function renderDrillOptionsGrid() {
    const grid = document.getElementById('drill-options-grid');
    if (!grid) return;

    grid.innerHTML = DRILL_OPTIONS.map((opt, idx) => `
        <button onclick="handleDrillAnswer('${opt.val}')" class="min-h-[64px] p-2 bg-white hover:bg-amber-400 text-slate-900 hover:text-slate-950 rounded-2xl font-black text-xl border-2 border-slate-300 hover:border-amber-500 shadow-sm transition-all active:scale-95 flex items-center justify-center cursor-pointer">
            <span id="drill-opt-latex-${idx}">${opt.latex}</span>
        </button>
    `).join('');

    DRILL_OPTIONS.forEach((opt, idx) => {
        const el = document.getElementById(`drill-opt-latex-${idx}`);
        if (el && window.katex) {
            try {
                katex.render(opt.latex, el, { displayMode: false, throwOnError: false });
            } catch(e) {
                el.innerText = opt.latex;
            }
        }
    });
}

function handleDrillAnswer(userVal) {
    recordInteraction();
    if (!currentDrillQuestion) return;

    const isCorrect = (userVal === currentDrillQuestion.a);
    const overlay = document.getElementById('drill-feedback-overlay');

    if (isCorrect) {
        drillCombo++;
        if (drillCombo > drillMaxCombo) drillMaxCombo = drillCombo;
        drillCorrectCount++;
        const addScore = 100 + (drillCombo * 20);
        drillScore += addScore;

        if (overlay) {
            overlay.innerHTML = '<span class="text-emerald-600 bg-white/90 px-4 py-2 rounded-xl shadow-lg border border-emerald-400">正確！ +'+addScore+'</span>';
            overlay.style.opacity = '1';
            setTimeout(() => { overlay.style.opacity = '0'; }, 350);
        }
    } else {
        drillCombo = 0;
        if (overlay) {
            overlay.innerHTML = '<span class="text-rose-600 bg-white/90 px-4 py-2 rounded-xl shadow-lg border border-rose-400">答錯！</span>';
            overlay.style.opacity = '1';
            setTimeout(() => { overlay.style.opacity = '0'; }, 350);
        }
    }

    const comboEl = document.getElementById('drill-combo-badge');
    const scoreEl = document.getElementById('drill-score-badge');
    if (comboEl) comboEl.innerText = `Combo x${drillCombo}`;
    if (scoreEl) scoreEl.innerText = `Score: ${drillScore}`;

    nextDrillQuestion();
}

function finishSpeedDrill() {
    const gameView = document.getElementById('speeddrill-game-view');
    const resultView = document.getElementById('speeddrill-result-view');
    if (gameView) gameView.classList.add('hidden');
    if (resultView) resultView.classList.remove('hidden');

    const setTxt = (id, val) => {
        const el = document.getElementById(id);
        if (el) el.innerText = val;
    };

    setTxt('drill-result-correct', `${drillCorrectCount} 題`);
    setTxt('drill-result-combo', `${drillMaxCombo} 連擊`);
    setTxt('drill-result-score', `${drillScore} 分`);

    let rank = '見習搜查員 🕵️';
    if (drillCorrectCount >= 18) rank = '高中生名偵探工藤新一 🏆';
    else if (drillCorrectCount >= 12) rank = '高木警官的好搭檔 🎖️';
    else if (drillCorrectCount >= 6) rank = '少年偵探團精英 🔍';

    const rankEl = document.getElementById('drill-rank-badge');
    if (rankEl) rankEl.innerText = `名偵探級別：${rank}`;
}

// ==========================================
// 9. 少年偵探團升級特訓闖關系統 (Core Rule 8)
// ==========================================
function openChallengeModal() {
    recordInteraction();
    const modal = document.getElementById('challenge-modal');
    if (modal) modal.classList.remove('hidden');
    renderStagesList();
}

function closeChallengeModal() {
    const modal = document.getElementById('challenge-modal');
    if (modal) modal.classList.add('hidden');
}

function renderStagesList() {
    const container = document.getElementById('challenge-stages-view');
    const quizView = document.getElementById('challenge-quiz-view');
    const resultView = document.getElementById('challenge-result-view');
    if (!container) return;

    container.classList.remove('hidden');
    quizView.classList.add('hidden');
    resultView.classList.add('hidden');

    const stages = window.CHALLENGE_STAGES || [];
    container.innerHTML = stages.map((st, idx) => `
    <div class="p-5 rounded-2xl bg-white border-2 border-amber-200 shadow-sm flex items-center justify-between mb-3 hover:border-amber-400 transition-all">
        <div>
            <span class="px-2.5 py-0.5 rounded text-xs font-black bg-amber-600 text-white">STAGE 0${st.stage}</span>
            <h3 class="text-lg font-black text-amber-950 mt-1">${st.title}</h3>
            <p class="text-xs text-slate-600 mt-0.5">${st.desc}（共 ${st.card_ids.length} 題）</p>
        </div>
        <button onclick="startStage(${idx})" class="px-5 py-2.5 rounded-xl font-bold text-sm bg-amber-600 text-white hover:bg-amber-700 shadow-sm transition-colors">
            進入審查
        </button>
    </div>
    `).join('');
}

function startStage(stageIdx) {
    recordInteraction();
    currentStageIndex = stageIdx;
    const stage = window.CHALLENGE_STAGES[stageIdx];
    stageQuizList = stage.card_ids.map(id => ({ id, ...window.QUIZ_DATA[id] })).filter(q => q.question);

    currentQuizQuestionIndex = 0;
    currentLives = 3;
    currentScore = 0;
    currentCombo = 0;
    maxCombo = 0;

    document.getElementById('challenge-stages-view').classList.add('hidden');
    document.getElementById('challenge-quiz-view').classList.remove('hidden');
    document.getElementById('challenge-result-view').classList.add('hidden');

    renderQuizQuestion();
}

function renderQuizQuestion() {
    if (currentQuizQuestionIndex >= stageQuizList.length || currentLives <= 0) {
        showQuizResults();
        return;
    }

    const q = stageQuizList[currentQuizQuestionIndex];
    document.getElementById('quiz-stage-title').innerText = window.CHALLENGE_STAGES[currentStageIndex].title;
    document.getElementById('quiz-progress-text').innerText = `問題 ${currentQuizQuestionIndex + 1} / ${stageQuizList.length}`;
    document.getElementById('quiz-score-badge').innerText = `積分：${currentScore}`;
    document.getElementById('quiz-combo-badge').innerText = `連擊：${currentCombo}`;

    // 麻醉槍指針生命值
    let livesHtml = '';
    for (let i = 0; i < 3; i++) {
        livesHtml += `<i class="fa-solid fa-crosshairs text-lg ${i < currentLives ? 'text-red-500' : 'text-slate-300'} mr-1"></i>`;
    }
    document.getElementById('quiz-lives-container').innerHTML = livesHtml;

    document.getElementById('quiz-question-text').innerHTML = q.question;

    const optContainer = document.getElementById('quiz-options-container');
    optContainer.innerHTML = q.options.map((opt, optIdx) => `
    <button onclick="handleQuizAnswer(${optIdx})" class="w-full text-left p-3.5 rounded-xl border-2 border-slate-200 hover:border-amber-500 bg-slate-50 hover:bg-amber-50 text-sm font-medium transition-all mb-2">
        <span class="inline-block w-6 h-6 rounded-full bg-slate-200 text-slate-700 text-center font-bold mr-2 text-xs leading-6">${['A','B','C','D'][optIdx] || optIdx+1}</span>
        ${opt}
    </button>
    `).join('');

    document.getElementById('quiz-feedback-box').classList.add('hidden');
    renderMath();
}

function handleQuizAnswer(selectedIdx) {
    recordInteraction();
    const q = stageQuizList[currentQuizQuestionIndex];
    const isCorrect = (selectedIdx === q.answer);
    const feedbackBox = document.getElementById('quiz-feedback-box');
    feedbackBox.classList.remove('hidden');

    if (isCorrect) {
        currentCombo++;
        if (currentCombo > maxCombo) maxCombo = currentCombo;
        currentScore += 100 + currentCombo * 20;
        feedbackBox.className = 'p-3 rounded-xl bg-emerald-50 border-2 border-emerald-500 text-emerald-950 text-xs font-bold my-3';
        feedbackBox.innerHTML = `
        <div class="flex items-center gap-1.5 text-sm text-emerald-700 mb-1">
            <i class="fa-solid fa-circle-check"></i>【真相大白！推理正確！】+${100 + currentCombo * 20} 分
        </div>
        <div>${q.explanation}</div>
        `;
    } else {
        currentCombo = 0;
        currentLives--;
        feedbackBox.className = 'p-3 rounded-xl bg-red-50 border-2 border-red-500 text-red-950 text-xs font-bold my-3';
        feedbackBox.innerHTML = `
        <div class="flex items-center gap-1.5 text-sm text-red-700 mb-1">
            <i class="fa-solid fa-circle-xmark"></i>【推理失誤！】麻醉槍指針 -1
        </div>
        <div>${q.explanation}</div>
        `;
    }

    renderMath();

    // 禁用選項避免重複點擊
    document.querySelectorAll('#quiz-options-container button').forEach(b => b.disabled = true);

    setTimeout(() => {
        currentQuizQuestionIndex++;
        renderQuizQuestion();
    }, 1800);
}

function showQuizResults() {
    document.getElementById('challenge-quiz-view').classList.add('hidden');
    const resView = document.getElementById('challenge-result-view');
    resView.classList.remove('hidden');

    const passed = currentLives > 0;
    resView.innerHTML = `
    <div class="text-center py-6">
        <div class="inline-block p-4 rounded-full ${passed ? 'bg-emerald-100 text-emerald-600' : 'bg-red-100 text-red-600'} text-4xl mb-3">
            <i class="fa-solid ${passed ? 'fa-award' : 'fa-skull-crossbones'}"></i>
        </div>
        <h3 class="text-2xl font-black text-amber-950 mb-1">${passed ? '★ 恭喜通過特訓考核！★' : '案件搜查陷入迷霧！'}</h3>
        <p class="text-sm text-slate-600 mb-5">${passed ? '名偵探推理筆記已登錄案卷檔案庫！' : '麻醉槍指針已耗盡，請複習相關圖卡後再次挑戰！'}</p>

        <div class="grid grid-cols-3 gap-3 max-w-sm mx-auto mb-6 text-center">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <div class="text-xs text-slate-500 font-bold">總破案積分</div>
                <div class="text-xl font-black text-amber-600 mt-1">${currentScore}</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <div class="text-xs text-slate-500 font-bold">最高連擊</div>
                <div class="text-xl font-black text-blue-600 mt-1">${maxCombo}</div>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
                <div class="text-xs text-slate-500 font-bold">剩餘生命值</div>
                <div class="text-xl font-black text-red-600 mt-1">${currentLives}</div>
            </div>
        </div>

        <div class="flex justify-center gap-3">
            <button onclick="renderStagesList()" class="px-5 py-2.5 rounded-xl font-bold text-sm bg-slate-200 text-slate-700 hover:bg-slate-300">
                返回關卡清單
            </button>
            <button onclick="startStage(${currentStageIndex})" class="px-5 py-2.5 rounded-xl font-bold text-sm bg-amber-600 text-white hover:bg-amber-700">
                再次挑戰本關
            </button>
        </div>
    </div>
    `;
}

// 正面自檢抽屜
function openCardQuiz(cardId, e) {
    if (e) e.stopPropagation();
    recordInteraction();
    const q = window.QUIZ_DATA[cardId];
    if (!q) return;

    const modal = document.getElementById('card-quiz-modal');
    if (!modal) return;

    modal.classList.remove('hidden');
    document.getElementById('card-quiz-title').innerText = `CASE ${cardId.toString().padStart(2, '0')} 自我檢核`;
    document.getElementById('card-quiz-question').innerHTML = q.question;

    const optBox = document.getElementById('card-quiz-options');
    optBox.innerHTML = q.options.map((opt, idx) => `
    <button onclick="handleSingleCardQuiz(${cardId}, ${idx})" class="w-full text-left p-3 rounded-xl border-2 border-slate-200 hover:border-amber-500 bg-slate-50 hover:bg-amber-50 text-xs font-medium transition-all mb-2">
        <span class="inline-block w-5 h-5 rounded-full bg-slate-200 text-slate-700 text-center font-bold mr-2 text-[10px] leading-5">${['A','B','C','D'][idx] || idx+1}</span>
        ${opt}
    </button>
    `).join('');

    document.getElementById('card-quiz-feedback').classList.add('hidden');
    renderMath();
}

function handleSingleCardQuiz(cardId, selectedIdx) {
    recordInteraction();
    const q = window.QUIZ_DATA[cardId];
    const isCorrect = (selectedIdx === q.answer);
    const fb = document.getElementById('card-quiz-feedback');
    fb.classList.remove('hidden');

    if (isCorrect) {
        fb.className = 'p-3 rounded-xl bg-emerald-50 border-2 border-emerald-500 text-emerald-950 text-xs font-bold my-2';
        fb.innerHTML = `
        <div class="text-emerald-700 font-bold mb-1"><i class="fa-solid fa-circle-check mr-1"></i>回答正確！</div>
        <div>${q.explanation}</div>
        `;
    } else {
        fb.className = 'p-3 rounded-xl bg-red-50 border-2 border-red-500 text-red-950 text-xs font-bold my-2';
        fb.innerHTML = `
        <div class="text-red-700 font-bold mb-1"><i class="fa-solid fa-circle-xmark mr-1"></i>推理有誤，再想想看！</div>
        <div>${q.explanation}</div>
        `;
    }
    renderMath();
}

function closeCardQuizModal() {
    const modal = document.getElementById('card-quiz-modal');
    if (modal) modal.classList.add('hidden');
}

// ==========================================
// 10. 破案心智圖 (Core Rule 6)
// ==========================================
function openMindmapModal() {
    recordInteraction();
    const modal = document.getElementById('mindmap-modal');
    if (modal) modal.classList.remove('hidden');
    renderMath();
}

function closeMindmapModal() {
    const modal = document.getElementById('mindmap-modal');
    if (modal) modal.classList.add('hidden');
}

function toggleMindmapFullscreen() {
    recordInteraction();
    const dialog = document.getElementById('mindmap-modal-dialog');
    if (!dialog) return;

    if (!document.fullscreenElement) {
        dialog.requestFullscreen().catch(() => {});
    } else {
        document.exitFullscreen().catch(() => {});
    }
}

function jumpToCardFromMindmap(cardId) {
    fromMindmap = true;
    closeMindmapModal();
    const cardIdx = allCards.findIndex(c => c.id === cardId);
    if (cardIdx !== -1) {
        openFullscreenModal(cardIdx);
    }
}

function renderMindmapTree() {
    const container = document.getElementById('mindmap-tree-container');
    if (!container) return;

    const sections = [
        {
            title: "一、銳角三角函數定義篇",
            cards: allCards.filter(c => c.id >= 1 && c.id <= 11)
        },
        {
            title: "二、特別角與生活科技篇",
            cards: allCards.filter(c => c.id >= 12 && c.id <= 20)
        },
        {
            title: "三、魔法六角星四大恆等篇",
            cards: allCards.filter(c => c.id >= 21 && c.id <= 35)
        },
        {
            title: "四、三角恆等式核心篇",
            cards: allCards.filter(c => c.id >= 36 && c.id <= 40)
        },
        {
            title: "五、課後習題 ‧ 是非專題篇",
            cards: allCards.filter(c => c.id >= 41 && c.id <= 45)
        },
        {
            title: "六、課後習題 ‧ 基礎進階篇",
            cards: allCards.filter(c => c.id >= 46 && c.id <= 60)
        }
    ];

    container.innerHTML = sections.map((sec, sIdx) => `
    <div class="mb-5 p-4 rounded-2xl bg-slate-50 border border-slate-200">
        <h4 class="text-base font-black text-amber-950 mb-3 flex items-center gap-2">
            <span class="w-6 h-6 rounded-full bg-amber-600 text-white text-xs flex items-center justify-center font-bold">${sIdx + 1}</span>
            ${sec.title}
        </h4>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2">
            ${sec.cards.map(c => `
            <button onclick="jumpToCardFromMindmap(${c.id})" class="text-left p-2.5 rounded-xl bg-white border border-slate-200 hover:border-amber-500 hover:bg-amber-50 text-xs transition-all shadow-2xs">
                <span class="font-bold text-amber-700 block">${c.tag}</span>
                <span class="text-slate-800 line-clamp-1">${c.title}</span>
            </button>
            `).join('')}
        </div>
    </div>
    `).join('');
}

// ==========================================
// 11. 密碼驗證與檔案下載 (Core Rule 9)
// ==========================================
function openTeacherPwdModal() {
    recordInteraction();
    const modal = document.getElementById('teacher-pwd-modal');
    if (modal) modal.classList.remove('hidden');
    const input = document.getElementById('teacher-pwd-input');
    if (input) {
        input.value = '';
        input.focus();
    }
    document.getElementById('teacher-pwd-error').classList.add('hidden');
}

function closeTeacherPwdModal() {
    const modal = document.getElementById('teacher-pwd-modal');
    if (modal) modal.classList.add('hidden');
}

function verifyTeacherPassword() {
    recordInteraction();
    const input = document.getElementById('teacher-pwd-input');
    const err = document.getElementById('teacher-pwd-error');
    if (input && input.value.trim() === '88888888') {
        closeTeacherPwdModal();
        downloadTeacherDocx();
    } else {
        if (err) err.classList.remove('hidden');
    }
}

function downloadStudentDocx() {
    recordInteraction();
    if (window.STUDENT_DOCX_B64 || window.DOCX_STUDENT_B64 || window.B64_STUDENT_DOCX) {
        const b64 = window.STUDENT_DOCX_B64 || window.DOCX_STUDENT_B64 || window.B64_STUDENT_DOCX;
        downloadBase64File(b64, "2-2_三角函數的定義與性質_學生學習單.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    } else {
        alert("找不到學生版學習單資源！");
    }
}

function downloadTeacherDocx() {
    recordInteraction();
    if (window.TEACHER_DOCX_B64 || window.DOCX_TEACHER_B64 || window.B64_TEACHER_DOCX) {
        const b64 = window.TEACHER_DOCX_B64 || window.DOCX_TEACHER_B64 || window.B64_TEACHER_DOCX;
        downloadBase64File(b64, "2-2_三角函數的定義與性質_教師解答版.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    } else {
        alert("找不到教師解答版資源！");
    }
}

function downloadBase64File(base64Data, fileName, mimeType) {
    const byteCharacters = atob(base64Data);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], { type: mimeType });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// ==========================================
// 12. 手機掃碼投影 (QR Code)
// ==========================================
function openQrcodeModal() {
    recordInteraction();
    const modal = document.getElementById('qrcode-modal');
    if (!modal) return;
    modal.classList.remove('hidden');

    const qrContainer = document.getElementById('qrcode-display');
    if (qrContainer) {
        qrContainer.innerHTML = '';
        const url = window.location.href;
        new QRCode(qrContainer, {
            text: url,
            width: 220,
            height: 220,
            colorDark: "#1e3a8a",
            colorLight: "#ffffff",
            correctLevel: QRCode.CorrectLevel.H
        });
        document.getElementById('qrcode-url-input').value = url;
    }
}

function closeQrcodeModal() {
    const modal = document.getElementById('qrcode-modal');
    if (modal) modal.classList.add('hidden');
}

function copyQrcodeUrl() {
    recordInteraction();
    const input = document.getElementById('qrcode-url-input');
    if (input) {
        input.select();
        navigator.clipboard.writeText(input.value);
        alert("已成功複製連線網址！");
    }
}

// ==========================================
// 13. 快捷鍵監聽 (ESC, F, 空白鍵)
// ==========================================
function initKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        // ESC 關閉所有視窗
        if (e.key === 'Escape') {
            closeFullscreenModal();
            closeMindmapModal();
            closeCheatsheetModal();
            closeLabModal();
            closeChallengeModal();
            closeCardQuizModal();
            closeTeacherPwdModal();
            closeQrcodeModal();
        }

        // F 鍵切換全螢幕
        if (e.key === 'f' || e.key === 'F') {
            if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
            if (!document.getElementById('mindmap-modal').classList.contains('hidden')) {
                e.preventDefault();
                toggleMindmapFullscreen();
            } else if (!document.getElementById('fullscreen-modal').classList.contains('hidden')) {
                e.preventDefault();
                toggleModalFullscreen();
            } else {
                e.preventDefault();
                togglePageFullscreen();
            }
        }

        // 劇院視窗內左右箭頭切換卡片
        if (!document.getElementById('fullscreen-modal').classList.contains('hidden')) {
            if (e.key === 'ArrowLeft') prevModalCard();
            else if (e.key === 'ArrowRight') nextModalCard();
        }
    });
}

function togglePageFullscreen() {
    recordInteraction();
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
    } else {
        document.exitFullscreen().catch(() => {});
    }
}

document.addEventListener('fullscreenchange', () => {
    const icon = document.getElementById('fullscreen-toggle-icon');
    const text = document.getElementById('fullscreen-toggle-text');
    if (document.fullscreenElement) {
        if (icon) { icon.classList.remove('fa-expand'); icon.classList.add('fa-compress'); }
        if (text) text.innerText = '結束全螢幕';
    } else {
        if (icon) { icon.classList.remove('fa-compress'); icon.classList.add('fa-expand'); }
        if (text) text.innerText = '全螢幕投影';
    }
});

function toggleModalFullscreen() {
    const modal = document.getElementById('fullscreen-modal');
    if (!document.fullscreenElement) {
        modal.requestFullscreen().catch(() => {});
    } else {
        document.exitFullscreen().catch(() => {});
    }
}

function renderMath() {
    if (window.renderMathInElement) {
        window.renderMathInElement(document.body, {
            delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false }
            ],
            throwOnError: false
        });
    }
}
"""
