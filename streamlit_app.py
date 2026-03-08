import streamlit as st
import pandas as pd

# 页面配置
st.set_page_config(page_title="Ivy Pan - Interactive Resume", layout="centered")

# --- 头部个人信息 ---
st.title("🚀 Libei (Ivy) Pan")
st.subheader("Master of Management Analytics Candidate | Rotman School of Management") [cite: 10]
st.write("📍 Toronto, ON | 📧 ivyy.pan@rotman.utoronto.ca") [cite: 1, 2]
st.write("---")

# --- 1. 职业总结 & 交互组件 (Checkbox) ---
st.header("Professional Summary")
st.write("Aspiring Product Analyst with hands-on experience in data analysis and financial modeling within the energy and wealth management sectors.") [cite: 3]

# 交互组件 1: Leadership Checkbox (你的新要求)
if st.checkbox("View Leadership & Campus Involvement"):
    st.markdown("""
    **Finance Director @ UTCSSA (2022-2025)** [cite: 35]
    * Managed $200,000+ annual budget and financial planning for large-scale events. [cite: 35]
    * **General Director:** Coordinated logistics and sponsors for the Freshman Welcome Event. [cite: 37]
    * **Crisis Management Lead:** Handled unexpected issues and team communication during the Spring Festival Gala.
    """)

# --- 2. 工作经历 & 交互组件 (Slider + Table) ---
st.header("Professional Experience")

# 交互组件 2: Slider (用于过滤显示的工作条数)
num_jobs = st.slider("Select number of roles to display:", 1, 3, 3)

# 数据准备 (包含你的新实习经历)
experience_data = {
    "Company": ["IG Wealth Management", "PetroChina Canada", "Sinopec"],
    "Role": ["Data Analyst Intern", "Finance & Accounting Analyst", "Accounting Summer Analyst"], [cite: 16, 24]
    "Location": ["Toronto, ON", "Calgary, AB", "Beijing, China"], [cite: 14, 22]
    "Key Impact": [
        "Analyzed client investment trends and cleaned financial datasets for advisors.",
        "Improved forecasting accuracy by 10% and reduced reporting time by 15%.", [cite: 19, 21]
        "Ensured 100% seamless transition during financial record software migration." [cite: 25]
    ]
}
df_exp = pd.DataFrame(experience_data)

# 展示表格 (Requirement: Display at least one table)
st.table(df_exp.head(num_jobs))

# --- 3. 技能分析 & 交互组件 (Selectbox + Chart) ---
st.header("Technical Skills & Projects")

# 交互组件 3: Selectbox (切换技能图表)
skill_type = st.selectbox("Select skill category to visualize:", ["Programming & Tools", "Core Competencies"])

if skill_type == "Programming & Tools":
    # 基于你的简历技能 [cite: 7, 8]
    skills = {"Python": 90, "R": 85, "SQL/SAP": 80, "Tableau": 75, "Excel (VBA)": 95}
else:
    # 基于你的核心胜任力 [cite: 8, 36]
    skills = {"Data Modeling": 90, "Financial Analysis": 85, "Budget Management": 95, "Leadership": 90}

skill_df = pd.DataFrame(list(skills.items()), columns=["Skill", "Proficiency"])

# 展示图表 (Requirement: Display at least one chart)
st.bar_chart(skill_df.set_index("Skill"))

# --- 项目简述 ---
st.subheader("Key Project: Alzheimer's Early Detection") [cite: 28]
st.write("Built predictive models using XGBoost and Random Forest in Python to improve diagnostic accuracy.") [cite: 29, 30]

st.divider()
st.info("Built with ❤️ by Ivy Pan using Streamlit")
