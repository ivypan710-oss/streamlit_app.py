import streamlit as st
import pandas as pd

# 页面配置：设置标题、图标和布局
st.set_page_config(page_title="Ivy Pan | Interactive Resume", page_icon="📈", layout="centered")

# --- 自定义 CSS 样式 (让网页更好看) ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #004b87;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 头部个人信息 ---
st.title("🎓 Libei (Ivy) Pan")
st.subheader("Master of Management Analytics Candidate @ Rotman School of Management")

col1, col2 = st.columns([2, 1])
with col1:
    st.write("📍 Toronto, ON")
    st.write("📧 ivyy.pan@rotman.utoronto.ca")
with col2:
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("💻 [GitHub](https://github.com/ivypan710-oss)")

st.divider()

# --- 1. 职业总结 ---
st.header("🎯 Professional Summary")
st.info("""
Aspiring Product Analyst with a background in Economics and Statistics. 
Experienced in improving operational efficiency, forecasting accuracy (up by 10%), 
and managing large-scale budgets ($200,000+).
""")

# --- 2. 领导力经验 (交互组件 1: Checkbox) ---
st.header("🏆 Leadership & Campus Life")
if st.checkbox("Explore my roles at UTCSSA"):
    st.markdown("""
    **Finance Director @ University of Toronto Chinese Students and Scholars Association**
    * **Budget Mastery:** Managed a $200,000+ annual budget with 100% transparency.
    * **Event Leadership:** General Director for the Beijing Freshman Orientation (200+ attendees).
    * **Crisis Management:** Led communication and problem-solving during the Spring Festival Gala.
    * *Skills: Strategic Planning, Negotiation, Team Coordination.*
    """)

# --- 3. 工作经历 (交互组件 2: Slider + Table) ---
st.header("💼 Professional Experience")

# 使用 Slider 控制显示的内容深度
detail_level = st.slider("Adjust detail level (Number of roles):", 1, 3, 3)

exp_data = {
    "Organization": ["IG Wealth Management", "PetroChina Canada", "Sinopec"],
    "Position": ["Data Analyst Intern", "Finance Analyst", "Summer Analyst"],
    "Key Focus": ["Client Data & Trends", "GST/HST Compliance", "Software Migration"]
}
df_exp = pd.DataFrame(exp_data)

# 展示表格 (Requirement: Table)
st.table(df_exp.head(detail_level))

# --- 4. 技能分析 (交互组件 3: Selectbox + Chart) ---
st.header("📊 Skills & Proficiency")

# 使用 Selectbox 切换图表视图
category = st.selectbox("View skills by category:", ["Technical Stack", "Soft Skills"])

if category == "Technical Stack":
    skill_map = {"Python": 90, "R": 85, "SQL/SAP": 80, "Tableau": 75, "Excel/VBA": 95}
else:
    skill_map = {"Data Analysis": 95, "Financial Modeling": 90, "Budgeting": 85, "Leadership": 90}

skill_df = pd.DataFrame(list(skill_map.items()), columns=["Skill", "Level"])

# 展示图表 (Requirement: Chart)
# 使用深蓝色调（Rotman 风格）展示
st.bar_chart(skill_df.set_index("Skill"))

# --- 项目简介 ---
st.header("🧪 Technical Projects")
with st.expander("Early Detection of Alzheimer's Disease (Python/R)"):
    st.write("Built predictive models using XGBoost and Random Forest to improve early diagnosis classification.")

st.divider()
st.caption("Built with ❤️ using Streamlit | © 2026 Libei Pan")
