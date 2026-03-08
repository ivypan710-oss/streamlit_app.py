
import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Interactive Resume", layout="centered")

# --- HEADER SECTION ---
st.title("Ivy Pan")
st.subheader("Data Analyst | MMA Student")
st.write("Passionate about building intelligent systems and clean code.")

# --- WIDGET 1: Contact Info Checkbox ---
if st.checkbox("Show Contact Information"):
    st.write("📧 Ivyy.pan@rotman.utoronto.ca")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/ivy-pan-7649b92a9/)")

st.divider()

# --- WIDGET 2: Experience Filter (Slider) ---
st.header("Work History")
years_filter = st.slider("Filter by minimum years of experience:", 0, 10, 1)

# --- TABLE: Work Experience ---
experience_data = {
    "Company": ["Tech Corp", "Data Solutions", "Startup Inc"],
    "Role": ["Senior Dev", "Data Analyst", "Junior Dev"],
    "Years": [5, 3, 2],
    "Tech Stack": ["Python, AWS", "SQL, Tableau", "JavaScript"]
}
df_exp = pd.DataFrame(experience_data)
filtered_df = df_exp[df_exp["Years"] >= years_filter]

st.table(filtered_df)

# --- WIDGET 3: Skill Focus (Selectbox) ---
st.header("Skill Proficiency")
skill_category = st.selectbox("Select a focus area:", ["Technical Skills", "Soft Skills"])

# --- CHART: Skill Levels ---
if skill_category == "Technical Skills":
    skills = {"Python": 90, "Machine Learning": 85, "SQL": 80, "Docker": 70}
else:
    skills = {"Communication": 95, "Leadership": 80, "Problem Solving": 90, "Teamwork": 85}

skill_df = pd.DataFrame(list(skills.items()), columns=["Skill", "Level"])
st.bar_chart(skill_df.set_index("Skill"))

st.info("Built with ❤️ using Streamlit")
