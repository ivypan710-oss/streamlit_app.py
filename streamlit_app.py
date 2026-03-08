import streamlit as st
import pandas as pd

# 1. 页面基本设置 (Rotman 风格的蓝白配色)
st.set_page_config(
    page_title="Libei (Ivy) Pan | Interactive Portfolio",
    page_icon="🎓",
    layout="wide"
)

# 2. 自定义视觉样式
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    h1 { color: #002D72; } /* Rotman Blue */
    h2 { color: #0056b3; border-bottom: 2px solid #0056b3; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 头部：个人名片 ---
col_title, col_info = st.columns([2, 1])
with col_title:
    st.title("Libei (Ivy) Pan")
    st.markdown("#### **Master of Management Analytics Candidate**")
    st.write("📍 Rotman School of Management, University of Toronto")

with col_info:
    st.write("📧 [ivyy.pan@rotman.utoronto.ca](mailto:ivyy.pan@rotman.utoronto.ca)")
    st.write("🔗 [LinkedIn Profile](https://linkedin.com)")
    st.write("💻 [GitHub Repository](https://github.com/ivypan710-oss)")

st.divider()

# --- 第一部分：交互式概览 ---
st.header("🎯 Professional Impact & Summary")
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Budget Managed", "$200K+", "UTCSSA")
col_m2.metric("Forecasting Accuracy", "+10%", "PetroChina")
col_m3.metric("Reporting Efficiency", "+15%", "Process Optimization")

st.info("**Aspiring Product Analyst** with a strong foundation in Statistics and Economics. Expert in leveraging Python, R, and SQL to drive strategic decision-making and operational excellence.")

# --- 第二部分：领导力深度展示 (交互组件 1: Checkbox) ---
st.header("🏆 Leadership & Social Responsibility")
with st.container():
    show_leadership = st.checkbox("Expand UTCSSA Executive Experience & Crisis Management Details")
    if show_leadership:
        l_col1, l_col2 = st.columns(2)
        with l_col1:
            st.markdown("### **Finance Director (2022-2025)**")
            st.write("""
            - Managed $200,000+ annual budget for 200+ members.
            - Optimized fund allocation for large-scale cultural events.
            - Streamlined reimbursement processes and financial transparency.
            """)
        with l_col2:
            st.markdown("### **General Director & Crisis Lead**")
            st.write("""
            - **Orientation:** Led venue selection and contract negotiation for 200+ attendees.
            - **Spring Festival Gala:** Served as Crisis Management Lead, resolving unexpected logistical conflicts in real-time.
            """)

# --- 第三部分：职业履历 (交互组件 2: Slider + Table) ---
st.header("💼 Professional Journey")
# 交互：动态调整展示的深度
job_count = st.slider("Select experience depth to view:", 1, 3, 3)

exp_data = {
    "Organization": ["IG Wealth Management", "PetroChina Canada", "Sinopec"],
    "Role": ["Data Analyst Intern", "Finance Analyst", "Accounting Summer Analyst"],
    "Core Contribution": [
        "Analyzed client data to identify investment patterns and support financial planning.",
        "Prepared Corporate GST/HST returns via SAP; optimized raw data for senior management.",
        "Led record migration to new financial software with zero operational downtime."
    ]
}
df_exp = pd.DataFrame(exp_data).head(job_count)
st.table(df_exp)

# --- 第四部分：技能图表 (交互组件 3: Selectbox + Chart) ---
st.header("📊 Skills & Technical Stack")
c1, c2 = st.columns([1, 2])

with c1:
    view_type = st.selectbox("Switch View:", ["Data Science Tools", "Core Competencies"])
    st.write("As a student at **Rotman**, I focus on the intersection of data and business strategy.")

with c2:
    if view_type == "Data Science Tools":
        skills = {"Python": 90, "R": 85, "SQL/SAP": 80, "Tableau": 75, "Excel/VBA": 95}
    else:
        skills = {"Financial Modeling": 90, "Budget Management": 95, "Data Cleaning": 85, "Negotiation": 80}
    
    skill_df = pd.DataFrame(list(skills.items()), columns=["Skill", "Level"])
    # 这里的图表会自动匹配页面布局
    st.bar_chart(skill_df.set_index("Skill"))

# --- 第五部分：学术项目 ---
st.header("🧪 Advanced Analytics Projects")
with st.expander("Explore: Early Detection of Alzheimer's Disease (2025)"):
    st.write("""
    **Tools:** Python, XGBoost, Random Forest.
    - Built a robust classification pipeline to identify early-stage biomarkers.
    - Achieved significant improvement in diagnostic sensitivity through feature engineering.
    """)

with st.expander("Explore: 2025 Canadian Federal Election Prediction"):
    st.write("""
    **Tools:** R, Logistic Regression.
    - Developed models with post-stratification to adjust for survey bias.
    - Improved reliability of election outcome predictions.
    """)

st.divider()
st.caption("Developed by Libei Pan | Candidate, Master of Management Analytics (MMA) 2026")
