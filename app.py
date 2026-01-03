import streamlit as st
import google.generativeai as genai

# 1. 填入你提供的 API Key
API_KEY = "AIzaSyBSKFSiObhfgUQZoU-zyclLp82hcqZ8TfY"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash-latest')
# 2. 手機版介面優化（隱藏上方選單與底部標籤）
st.set_page_config(page_title="禾多移動分析App", page_icon="🚀")
st.markdown("""
    <style>
    header {visibility: hidden;} 
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. 公司知識庫（Context）
CONTEXT = """
你是一位禾多移動(AviviD.ai)專家。
核心重點：
- 產品：Likr RMN (零售媒體網路), Likr CDP (顧客數據平台), AI數位店長。
- 技術：MTSTRec推薦系統 (ICML 2025獲獎), 1300萬用戶Web Push專利。
- 特色：全台最大流量池，解決Cookie消失後的數據追蹤。
請用繁體中文回答，口吻要專業、積極，並適時提供實務案例。
"""

# 4. App 介面設計
st.image("https://www.avivid.ai/wp-content/uploads/2022/07/avivid-logo.png", width=120)
st.title("AviviD 互動分析站")
st.write("---")

st.info("💡 點擊下方按鈕，即刻探索公司業務細節：")

# 5. 互動按鈕（兩欄式排列，適合手機點擊）
col1, col2 = st.columns(2)
topic = ""
query = ""

with col1:
    if st.button("🛒 零售媒體 RMN", use_container_width=True):
        topic, query = "Likr RMN", "請解釋禾多移動的 RMN 業務，並提供一個提升電商轉換率的實務案例與數據解釋。"
    if st.button("📊 數據平台 CDP", use_container_width=True):
        topic, query = "Likr CDP", "請解釋 Likr CDP 如何跨媒體追蹤足跡，並說明品牌如何利用它進行精準再行銷。"

with col2:
    if st.button("🤖 AI 數位店長", use_container_width=True):
        topic, query = "AI 銷售助理", "請解釋數位店長如何自動化推薦商品，以及它如何優化行動端的購物體驗。"
    if st.button("🏆 頂尖推薦技術", use_container_width=True):
        topic, query = "MTSTRec 技術", "請詳細說明 MTSTRec 技術是什麼？這項獲得 ICML 肯定技術在商業應用上的優勢為何？"

# 6. AI 內容顯示區
if query:
    st.divider()
    st.subheader(f"🔍 專家分析：{topic}")
    with st.spinner("AI 正在根據最新資料分析中..."):
        # 合併背景知識與點擊的問題
        full_prompt = f"{CONTEXT}\n\n現在請回答以下問題：{query}"
        response = model.generate_content(full_prompt)
        st.write(response.text)
    
    # 貼心的面試加分提示
    st.info(f"💡 面試小撇步：你可以針對 {topic} 詢問面試官目前公司的佈局進度，展現你的主動性。")

# 7. 自由問答區
st.divider()
st.subheader("💬 自由提問")
user_q = st.text_input("輸入任何關於禾多移動的問題：", placeholder="例如：這間公司的競爭對手是誰？")
if user_q:
    with st.spinner("思考中..."):
        res = model.generate_content(f"{CONTEXT}\n\n用戶問題：{user_q}")
        st.write(res.text)

st.caption("展示者：[你的名字] | 技術驅動：Gemini 1.5 Flash")
