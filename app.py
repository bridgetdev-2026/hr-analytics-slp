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
    st.header("Unit 1: Foundations & Human Capital Value Chain Architecture")
    st.caption("Theoretical Frameworks, Strategic Alignment Metrics, and Interactive Value Mapping")
    st.markdown("---")

    # Tabs for Theory, Diagnostics, and AI Tutor
    tab_theory, tab_diagnostic, tab_classifier, tab_tutor = st.tabs([
        "📚 Academic Theory & Frameworks", 
        "🕸️ Interactive Value Chain Diagnostic", 
        "📊 Efficiency vs Effectiveness Classifier", 
        "🤖 Unit 1 Socratic AI Tutor"
    ])

    # Tab 1: Academic Theory & Frameworks
    with tab_theory:
        st.subheader("1. The Human Capital Value Chain Architecture")
        st.markdown("""
        The **Human Capital Value Chain** (Huselid, Becker & Beatty) provides the strategic architecture for linking human resource 
        investments directly to organizational performance and sustainable value creation. Rather than treating HR as an administrative 
        cost centre, the value chain models human capital as an integrated strategic driver.
        """)

        st.markdown("""
        <div style="background-color: #F8F9FA; border-left: 5px solid #002B49; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
        <h4>The Four Stages of Human Capital Value Creation</h4>
        <ol>
            <li><b>HR Inputs & Investments:</b> Financial, technological, and human resources allocated to HR operations (e.g., HR budget, staffing, HRIS platforms).</li>
            <li><b>HR Processes & Activities:</b> Core functional practices (e.g., recruitment, learning and development, performance management, remuneration).</li>
            <li><b>HR Deliverables & Capabilities:</b> Intermediate outcomes produced by HR practices (e.g., employee engagement, leadership depth, psychological safety, skill competency).</li>
            <li><b>Strategic Business Outcomes:</b> Tangible organizational results (e.g., revenue growth, customer retention, operational efficiency, Human Capital ROI).</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("2. Resource-Based View (RBV) & VRIO Framework")
        st.write(
            "Grounded in Barney's (1991) Resource-Based View of the firm, human capital generates sustainable competitive advantage "
            "when workforce capabilities are **Valuable**, **Rare**, **Inimitable** (costly to imitate), and **Organised** effectively. "
            "Metrics must therefore measure not just workforce capacity, but strategic capability and uniqueness."
        )

        st.subheader("3. Differentiating Measurement Levels")
        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.markdown("**HR Efficiency Metrics**")
            st.caption("Doing things right (Cost & Speed)")
            st.markdown("- Cost per hire (ZAR)\n- Time to fill critical posts\n- HR staff-to-employee ratio\n- Training administration cost")
        with col_t2:
            st.markdown("**HR Effectiveness Metrics**")
            st.caption("Doing the right things (Quality & Impact)")
            st.markdown("- Quality of hire (12-month performance)\n- Competency gap closure rate (%)\n- Employee engagement & well-being index\n- First-year turnover rate")
        with col_t3:
            st.markdown("**Strategic Business Impact**")
            st.caption("Value created for the organisation")
            st.markdown("- Human Capital ROI (HCROI)\n- Revenue per Full-Time Equivalent (FTE)\n- Profit per employee\n- Critical skill retention rate")

    # Tab 2: Interactive Value Chain Diagnostic
    with tab_diagnostic:
        st.subheader("Interactive Value Chain Maturity Diagnostic")
        st.write("Rate your organisation's current capability across each stage of the value chain to generate a real-time capability radar chart.")

        c_diag1, c_diag2 = st.columns([1, 1])

        with c_diag1:
            s_input = st.slider("1. HR Inputs & Budget Alignment Score (1-10):", 1, 10, 6)
            s_proc = st.slider("2. HR Process Quality & System Integration (1-10):", 1, 10, 5)
            s_deliv = st.slider("3. Workforce Capabilities & Engagement (1-10):", 1, 10, 7)
            s_out = st.slider("4. Strategic Business Impact Measurement (1-10):", 1, 10, 4)

            maturity_index = ((s_input + s_proc + s_deliv + s_out) / 40) * 100
            st.metric("Overall Value Chain Maturity Index", f"{maturity_index:.1f}%")

        with c_diag2:
            radar_df = pd.DataFrame({
                "Stage": ["1. Inputs", "2. Processes", "3. Deliverables", "4. Business Impact"],
                "Score": [s_input, s_proc, s_deliv, s_out]
            })
            fig_radar = px.line_polar(
                radar_df, r="Score", theta="Stage", line_close=True,
                title="Human Capital Value Chain Maturity Profile",
                range_r=[0, 10]
            )
            fig_radar.update_traces(fill='toself')
            st.plotly_chart(fig_radar, use_container_width=True)

        if maturity_index < 50:
            st.warning("⚠️ **Diagnostic Insight:** Your value chain is currently skewed toward operational activities with limited measurement of strategic business impact. Focus on building metrics for Stage 3 and Stage 4.")
        else:
            st.success("✅ **Diagnostic Insight:** Strong balanced alignment across the value chain. Ensure continuous monitoring of predictive lead indicators.")

    # Tab 3: Metric Classifier Workbench
    with tab_classifier:
        st.subheader("Interactive Metric Classifier Workbench")
        st.write("Test your strategic knowledge by classifying standard workforce metrics into the correct Value Chain category.")

        sample_metric = st.selectbox(
            "Select a Workforce Metric to Evaluate:",
            [
                "Time-to-Fill Critical Vacancies",
                "Quality of Hire (Performance Rating at 12 Months)",
                "Human Capital Return on Investment (HCROI)",
                "Total Training Hours per Employee",
                "Voluntary Turnover Rate in Critical Skills",
                "Employee Net Promoter Score (eNPS)"
            ]
        )

        user_choice = st.radio(
            f"Classification for '{sample_metric}':",
            ["HR Efficiency Metric", "HR Effectiveness Metric", "Strategic Business Impact Metric"]
        )

        if st.button("Check Classification"):
            # Logic validation
            correct_mappings = {
                "Time-to-Fill Critical Vacancies": "HR Efficiency Metric",
                "Quality of Hire (Performance Rating at 12 Months)": "HR Effectiveness Metric",
                "Human Capital Return on Investment (HCROI)": "Strategic Business Impact Metric",
                "Total Training Hours per Employee": "HR Efficiency Metric",
                "Voluntary Turnover Rate in Critical Skills": "HR Effectiveness Metric",
                "Employee Net Promoter Score (eNPS)": "HR Effectiveness Metric"
            }
            
            correct_answer = correct_mappings[sample_metric]
            if user_choice == correct_answer:
                st.success(f" Correct! '{sample_metric}' is classified as a **{correct_answer}**.")
            else:
                st.error(f"❌ Not quite. '{sample_metric}' is actually classified as a **{correct_answer}**.")

    # Tab 4: Unit 1 Socratic AI Tutor
    with tab_tutor:
        st.subheader("🤖 Unit 1 Socratic AI Tutor")
        st.write("Engage with your virtual tutor on Human Capital Value Chain concepts, strategic alignment, and metric positioning.")

        tutor_query = st.text_input("Ask the Unit 1 Tutor a question (e.g., 'How do I explain the Value Chain to my CFO?'):")

        if st.button("Submit to Tutor"):
            if tutor_query:
                st.session_state.chat_history.append(("User", tutor_query))
                
                # Rule-based intelligent responses for Unit 1 concepts
                q_lower = tutor_query.lower()
                if "cfo" in q_lower or "financial" in q_lower or "business" in q_lower:
                    ans = ("**Unit 1 Tutor:** When speaking to a CFO, frame HR metrics using the Value Chain architecture. "
                           "Acknowledge that while efficiency metrics (like cost-per-hire) track operational cost control, "
                           "the true ROI lies in Stage 4 Business Impact metrics—specifically how human capital investments directly "
                           "drive Revenue per FTE and Human Capital ROI (HCROI).")
                elif "efficiency" in q_lower or "effectiveness" in q_lower:
                    ans = ("**Unit 1 Tutor:** The key distinction is that Efficiency measures operational speed and cost ('doing things right'), "
                           "whereas Effectiveness measures outcome quality and capability closure ('doing the right things'). "
                           "High efficiency with low effectiveness means doing the wrong things faster!")
                elif "barney" in q_lower or "rbv" in q_lower or "vrio" in q_lower:
                    ans = ("**Unit 1 Tutor:** Barney's VRIO framework reminds us that workforce metrics should evaluate resources that are "
                           "Valuable, Rare, Inimitable, and Organised. HR metrics must measure whether your talent management systems create "
                           "unique organizational capabilities that competitors cannot easily duplicate.")
                else:
                    ans = (f"**Unit 1 Tutor:** That is an excellent query regarding '{tutor_query}'. Within Unit 1, always remember to connect "
                           "HR processes directly to intermediate deliverables (capabilities, well-being, engagement) before demonstrating "
                           "financial outcomes on the balance sheet.")

                st.session_state.chat_history.append(("Unit 1 Tutor", ans))

        if st.session_state.chat_history:
            st.markdown("---")
            st.markdown("### Tutor Conversation History")
            for sender, text in reversed(st.session_state.chat_history):
                if "Tutor" in sender:
                    st.info(text)
                else:
                    st.write(f"**🙋‍♂️ You:** {text}")
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
