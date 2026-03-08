import streamlit as st
import pandas as pd

# 页面设置
st.set_page_config(page_title="Libei (Ivy) Pan - Interactive Resume", layout="wide")

# --- 侧边栏：交互组件 1 (Selectbox) ---
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose a section:", ["Professional Summary", "Experience & Projects", "Skills Analysis"])

# --- 头部个人信息 ---
st.title("🚀 Libei (Ivy) Pan")
st.write("📍 Toronto, ON | 📧 ivyy.pan@rotman.utoronto.ca")
st.write("Master of Management Analytics Candidate @ Rotman School of Management")

# --- 页面内容切换 ---
if page == "Professional Summary":
    st.header("Professional Summary")
    st.write("""
    Aspiring Product Analyst with hands-on experience in data analysis and financial modeling. 
    Proven track record in improving operational efficiency and forecasting accuracy.
    """)
    
    # 交互组件 2: Checkbox 显示联系方式
    if st.checkbox("Show Phone Number & LinkedIn"):
        st.write("📞 (437) 361-9202")
        st.write("🔗 [LinkedIn Profile](https://linkedin.com)")

elif page == "Experience & Projects":
    st.header("Work History & Education")
    
    # 数据准备
    exp_data = {
        "Company/School": ["IG Wealth Management", "PetroChina Canada", "Sinopec", "Rotman (UofT)"],
        "Role": ["Data Analyst Intern", "Finance & Accounting Analyst", "Accounting Summer Analyst", "MMA Candidate"],
        "Focus": ["Client Data & Investment Trends", "GST/HST & Financial Trends", "Migration of Records", "Management Analytics"]
    }
    df = pd.DataFrame(exp_data)
    
    # 展示表格 (Requirement: Display at least one table)
    st.table(df)
    
    st.subheader("Key Project: Alzheimer's Early Detection")
    st.write("Built predictive models using XGBoost and Random Forest to improve classification accuracy.")

elif page == "Skills Analysis":
    st.header("Technical Proficiency")
    
    # 交互组件 3: Slider 模拟技能熟练度过滤
    min_level = st.slider("Filter skills by proficiency level (1-100):", 0, 100, 70)
    
    # 技能数据
    skills = {
        "Python": 90,
        "R": 85,
        "SQL/SAP": 80,
        "Tableau": 75,
        "Financial Modeling": 85
    }
    
    skill_df = pd.DataFrame(list(skills.items()), columns=["Skill", "Level"])
    filtered_skills = skill_df[skill_df["Level"] >= min_level]
    
    # 展示图表 (Requirement: Display at least one chart)
    st.bar_chart(filtered_skills.set_index("Skill"))

st.divider()
st.caption("Built with Streamlit | © 2026 Libei Pan")
