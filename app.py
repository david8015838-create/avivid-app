import streamlit as st
import google.generativeai as genai

# 1. 配置您的 API Key
API_KEY = "AIzaSyBSKFSiObhfgUQZoU-zyclLp82hcqZ8TfY"
genai.configure(api_key=API_KEY)

# 2. 定義模型 (使用最穩定的 flash 版本)
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

# 4. 公司知識庫 (Context)
CONTEXT = """
你是一位禾多移動(AviviD.ai)專家。
核心重點：
- 產品：Likr RMN (零售媒體網路), Likr CDP (顧客數據平台), AI數位店長。
- 技術：MTSTRec推薦系統 (ICML 2025獲獎), 1300萬用戶Web Push專利。
- 特色：解決Cookie消失後的數據追蹤，全台最大流量池。
請用繁體中文回答，口吻專業且積極。
"""

# 5. App 標題
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
        topic, query = "Likr RMN", "請解釋 RMN 業務，並提供一個電商轉換率提升的實務案例。"
    if st.button("📊 數據平台 CDP"):
        topic, query = "Likr CDP", "請解釋 CDP 如何追蹤足跡，並說明品牌如何利用它進行精準行銷。"

with col2:
    if st.button("🤖 AI 數位店長"):
        topic, query = "AI
