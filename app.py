import streamlit as st
import google.generativeai as genai

# 1. 配置您的 API Key
API_KEY = "AIzaSyBSKFSiObhfgUQZoU-zyclLp82hcqZ8TfY"
genai.configure(api_key=API_KEY)

# 2. 定義模型 (使用最穩定的型號)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 手機版介面優化
st.set_page_config(page_title="禾多移動分析站", page_icon="🚀")
st.markdown("""
    <style>
    header {visibility: hidden;} 
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    .stButton>button {width: 100%; border-radius: 10px; height: 3em; background-color: #f0f2f6;}
    </style>
    """, unsafe_allow_html=True)

# 4. 公司知識庫
CONTEXT = """
你是一位禾多移動(AviviD.ai)專家。
核心重點：
- 產品：Likr RMN (零售媒體網路), Likr CDP (顧客數據平台), AI數位店長。
- 技術：MTSTRec推薦系統 (ICML 2025獲獎), 1300萬用戶Web Push專利。
- 特色：解決Cookie消失後的數據追蹤，全台最大流量池。
請用繁體中文回答，口吻專業且積極。
"""

# 5. App 介面
st.image("https://www.avivid.ai/wp-content/uploads/2022/07/avivid-logo.png", width=120)
st.title("AviviD 互動分析站")
st.write("---")

st.info("💡 點擊下方按鈕探索業務細節")

# 6. 互動按鈕區域
col1, col2 = st.columns(2)
topic = ""
query = ""

with col1:
    if st.button("🛒 零售媒體 RMN"):
        topic = "Likr RMN"
        query = "請解釋 RMN 業務，並提供一個電商轉換率提升的實務案例。"
    if st.button("📊 數據平台 CDP"):
        topic = "Likr CDP"
        query = "請解釋 CDP 如何追蹤足跡，並說明品牌如何利用它進行精準行銷。"

with col2:
    if st.button("🤖 AI 數位店長"):
        topic = "AI 銷售助理"
        query = "請解釋數位店長功能，以及它如何優化電商的購物體驗。"
    if st.button("🏆 頂尖推薦技術"):
        topic = "MTSTRec 技術"
        query = "請說明 MTSTRec 技術是什麼？他在推薦系統上的突破點在哪？"

# 7. AI 邏輯處理
if query:
    st.divider()
    st.subheader(f"🔍 專家分析：{topic}")
    with st.spinner("AI 正在分析數據..."):
        try:
            response = model.generate_content(f"{CONTEXT}\n\n問題：{query}")
            st.write(response.text)
        except Exception as e:
            st.error("連線異常，請確認 API Key 權限。")
            st.caption(f"錯誤細節: {e}")

st.divider()
user_input = st.text_input("💬 自由提問：", placeholder="例如：這間公司的優勢是什麼？")
if user_input:
    with st.spinner("思考中..."):
        try:
            res = model.generate_content(f"{CONTEXT}\n\n用戶問題：{user_input}")
            st.write(res.text)
        except Exception as e:
            st.warning("暫時無法取得回應。")

st.caption("由 Gemini 1.5 Flash 驅動 | 展示者：[您的姓名]")
