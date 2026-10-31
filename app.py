import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page Configuration & Styling
st.set_page_config(
    page_title="HR Metrics & Analytics SLP Portal",
    page_icon="📊",
    layout="wide"
)

# Application Header
st.title("📊 HR Metrics & Analytics: Advanced Applied Analytics & Workforce Diagnostics")
st.subheader("Nelson Mandela University | Short Learning Programme Portal")
st.markdown("---")

# Session State Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar Navigation
st.sidebar.header("Navigation & Modules")
selected_unit = st.sidebar.radio(
    "Select Learning Unit:",
    [
        "Overview & Value Chain",
        "Unit 1: Foundations & Value Chain",
        "Unit 2: Strategic HR Metrics & Calculators",
        "Unit 3: Workforce Diagnostics & Audit",
        "AI Assistant & Support"
    ]
)

# Main Content Display
if selected_unit == "Overview & Value Chain":
    st.header("Program Overview")
    st.write(
        "Welcome to the interactive executive portal for HR Metrics and Analytics. "
        "Use the sidebar navigation to explore calculation tools, diagnostic frameworks, and course modules."
    )
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Core Modules", value="4 Units")
    col2.metric(label="Diagnostic Tools", value="Interactive")
    col3.metric(label="Target Audience", value="HR Practitioners & Leaders")

elif selected_unit == "Unit 1: Foundations & Value Chain":
    st.header("Unit 1: Foundations & Value Chain")
    st.markdown("### The HR Value Chain Architecture")
    st.info("Explore how human capital investments directly drive strategic organizational outcomes.")
    
    # Sample visualization
    df = pd.DataFrame({
        "Metric": ["Efficiency", "Effectiveness", "Business Impact"],
        "Score": [75, 82, 88]
    })
    fig = px.bar(df, x="Metric", y="Score", title="HR Value Chain Performance Indicators")
    st.plotly_chart(fig, use_container_width=True)

elif selected_unit == "Unit 2: Strategic HR Metrics & Calculators":
    st.header("Unit 2: Strategic HR Metrics & Calculators")
    st.markdown("### Interactive Labor Turnover Cost Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        emp_count = st.number_input("Total Headcount", value=500, step=10)
        departures = st.number_input("Annual Separations", value=45, step=1)
        avg_salary = st.number_input("Average Annual Salary (R)", value=350000, step=10000)
    
    with col2:
        turnover_rate = (departures / emp_count) * 100 if emp_count > 0 else 0
        est_cost = departures * (avg_salary * 0.5)  # Estimating 50% replacement cost
        
        st.metric(label="Annual Turnover Rate", value=f"{turnover_rate:.1f}%")
        st.metric(label="Est. Annual Replacement Cost", value=f"R {est_cost:,.2f}")

elif selected_unit == "Unit 3: Workforce Diagnostics & Audit":
    st.header("Unit 3: Workforce Diagnostics & Audit")
    
    st.markdown("### Strengths Identified")
    st.success("• High strategic alignment in talent acquisition frameworks.\n• Well-defined HR metrics reporting structure.")
    
    st.markdown("### Audit Recommendations for Improvement")
    st.warning("• Enhance predictive analytics capabilities for employee retention.\n• Integrate real-time dashboard tracking across key business units.")

elif selected_unit == "AI Assistant & Support":
    st.header("HR Analytics AI Assistant")
    st.write("Ask questions regarding formulas, metric interpretations, or course module materials.")
    user_query = st.text_input("Enter your query:")
    if st.button("Submit Query"):
        st.write(f"**Response:** Processing query for: *{user_query}*")
