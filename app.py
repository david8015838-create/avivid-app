import streamlit as st
import google.generativeai as genai

# 1. 填入你的 API Key
API_KEY = "AIzaSyBSKFSiObhfgUQZoU-zyclLp82hcqZ8TfY"
genai.configure(api_key=API_KEY)

# 改用最通用的 gemini-pro 模型名
model = genai.GenerativeModel('gemini-pro')

# 2. 手機版介面優化
st.set_page_config(page_title="禾多移動分析App", page_icon="🚀")
st.markdown("<style>header {visibility: hidden;} footer {visibility: hidden;} #MainMenu {visibility: hidden;}</style>", unsafe_allow_html=True)

# 3. 公司知識庫
CONTEXT = """你是一位禾多移動(AviviD.ai)專家。
核心產品：Likr RMN (零售媒體網路), Likr CDP (顧客數據平台), AI數位店長。
優勢：MTSTRec推薦系統 (ICML 2025獲獎), 1300萬用戶Web Push專利。
請用繁體中文回答專業案例。"""

# 4. App 介面
st.image("https://www.avivid.ai/wp-content/uploads/2022/07/avivid-logo.png", width=120)
st.title("AviviD 互動分析站")
st.write("---")

st.info("💡 點擊下方主題查看實務案例：")

col1, col2 = st.columns(2)
topic, query = "", ""

with col1:
    if st.button("🛒 零售媒體 RMN", use_container_width=True):
        topic, query = "Likr RMN", "請解釋RMN業務，並給出一個禾多移動如何提升轉換率的案例。"
    if st.button("📊 數據平台 CDP", use_container_width=True):
        topic, query = "Likr CDP", "請解釋CDP如何追蹤足跡，並說明如何進行精準行銷。"

with col2:
    if st.button("🤖 AI 數位店長", use_container_width=True):
        topic, query = "AI 銷售助理", "請解釋數位店長功能，以及它如何優化電商體驗。"
    if st.button("🏆 頂尖推薦技術", use_container_width=True):
        topic, query = "MTSTRec 技術", "請說明MTSTRec技術是什麼？它在推薦系統上的突破點在哪？"

if query:
    st.divider()
    st.subheader(f"🔍 分析：{topic}")
    with st.spinner("AI 正在思考中..."):
        try:
            # 加入安全性與錯誤處理
            response = model.generate_content(f"{CONTEXT}\n\n問題：{query}")
            st.write(response.text)
        except Exception as e:
            st.error(f"連線失敗，請確認 API Key 是否有效。錯誤訊息：{e}")

st.divider()
user_q = st.text_input("💬 自由提問：")
if user_q:
    try:
        res = model.generate_content(f"{CONTEXT}\n\n問題：{user_q}")
        st.write(res.text)
    except:
        st.error("暫時無法連線至 AI，請稍後再試。")
