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

# Sidebar Navigation Setup
st.sidebar.title("Programme Navigation")
st.sidebar.markdown("**Short Learning Programme Modules**")

selected_unit = st.sidebar.radio(
    "Navigate to:",
    [
        "Programme Overview & Architecture",
        "Unit 1: Foundations & Value Chain",
        "Unit 2: Strategic HR Metrics & Calculators",
        "Unit 3: Workforce Diagnostics & Audit",
        "AI Assistant & Support"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("🎓 **Programme Lead:** Department of Human Resource Management, Nelson Mandela University.")

# Module 0: Programme Overview & Architecture
if selected_unit == "Programme Overview & Architecture":
    st.header("Short Learning Programme Overview & Architecture")
    
    st.markdown("""
    <div class="card">
    <h4>Welcome Delegates</h4>
    This specialized executive portal serves as your diagnostic workbench, interactive study guide, and analytics interface for the 
    <b>Short Learning Programme in HR Metrics and Analytics: Advanced Applied Analytics and Workforce Diagnostics</b>. 
    Designed specifically for South African HR practitioners, senior managers, and organizational leaders, this programme bridges higher 
    education rigor with practical workplace application to transform human resource management into an evidence-based strategic business driver.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Modules", value="4 Core Units")
    col2.metric(label="NQF / Level", value="Advanced / Executive")
    col3.metric(label="Diagnostic Tools", value="Embedded (ZAR)")
    col4.metric(label="Focus Area", value="Workplace Flourishing")
    
    st.markdown("---")
    
    st.subheader("1. Programme Purpose & Strategic Rationale")
    st.write(
        "In modern African and global enterprise contexts, HR professionals are increasingly required to demonstrate the tangible strategic and "
        "financial impact of human capital investments. This programme provides the analytical tools, governance frameworks, and diagnostic "
        "methodologies necessary to evaluate human capital metrics, identify systemic workforce risks, and promote humanised, sustainable workplace flourishing."
    )
    
    st.subheader("2. Core Programme Objectives")
    st.markdown("""
    * **Operationalise the Human Capital Value Chain:** Map the direct relationship between strategic inputs, HR processes, operational outputs, and organizational outcomes.
    * **Master Quantitative & Financial Metrics:** Calculate precision workforce metrics, including voluntary turnover financial loss (in ZAR), absenteeism indices, time-to-fill efficiencies, and Human Capital Return on Investment (HCROI).
    * **Execute Rigorous Workforce Diagnostics:** Apply structured audit frameworks to evaluate organizational compliance, identify operational strengths, and formulate actionable recommendations for improvement.
    * **Leverage Predictive Analytics & Dashboards:** Utilize data visualization to identify retention flight risks, address burnout factors, and optimize talent governance.
    """)
    
    st.subheader("3. Structure of the Short Learning Programme")
    
    overview_data = {
        "Unit Module": [
            "Unit 1: Foundations & Human Capital Value Chain",
            "Unit 2: Strategic HR Metrics & Workforce Calculators",
            "Unit 3: Workforce Diagnostics & HR Audit Frameworks",
            "Unit 4: Advanced Predictive Analytics & Reporting"
        ],
        "Focus & Deliverables": [
            "Value chain alignment, efficiency vs effectiveness, strategic mapping.",
            "Turnover cost calculation (ZAR), HCROI, absenteeism & productivity metrics.",
            "Strengths identified, governance, audit matrices & recommendations for improvement.",
            "Predictive flight risk modeling, interactive dashboarding, strategic reporting."
        ]
    }
    st.table(pd.DataFrame(overview_data))
    
    st.info("💡 **Navigation Tip:** Use the sidebar menu on the left to navigate between modules and access interactive diagnostic tools.")

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
    st.markdown("### Interactive Labour Turnover Cost Calculator")
    
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
