
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page Configuration & Professional Academic Theme
st.set_page_config(
    page_title="HR Metrics & Analytics SLP Portal",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for Academic Executive Design
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #002B49; margin-bottom: 0px; }
    .sub-header { font-size: 1.1rem; color: #555555; margin-bottom: 20px; }
    .card { background-color: #F8F9FA; border-left: 5px solid #002B49; padding: 18px; border-radius: 6px; margin-bottom: 20px; }
    .academic-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-left: 4px solid #0284C7; padding: 16px; border-radius: 6px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.markdown('<p class="main-header">📊 HR Metrics & Analytics: Advanced Applied Analytics & Workforce Diagnostics</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Nelson Mandela University | Short Learning Programme (SLP) Interactive Portal</p>', unsafe_allow_html=True)
st.markdown("---")

# Session State Initialization
if "tutor_history" not in st.session_state:
    st.session_state.tutor_history = []
if "general_chat_history" not in st.session_state:
    st.session_state.general_chat_history = []

# Sidebar Navigation Setup
st.sidebar.title("Programme Navigation")
st.sidebar.markdown("**Short Learning Programme Modules**")

selected_unit = st.sidebar.radio(
    "Navigate to:",
    [
        "Programme Overview & Architecture",
        "Unit 1: Foundations & Human Capital Value Chain",
        "Unit 2: Strategic HR Metrics & Workforce Calculators",
        "Unit 3: Workforce Diagnostics & HR Audit",
        "Unit 4: Predictive Analytics & Reporting",
        "Interactive AI Assistant & Delegate Support"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("🎓 **Programme Lead:** Department of Human Resource Management, Nelson Mandela University.")

# ------------------------------------------------------------------------------
# PROGRAMME OVERVIEW
# ------------------------------------------------------------------------------
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
            "Value chain architecture, Resource-Based View (RBV), metric classification, alignment diagnostics.",
            "Turnover cost calculation (ZAR), HCROI, absenteeism & productivity metrics.",
            "Strengths identified, governance, audit matrices & recommendations for improvement.",
            "Predictive flight risk modeling, interactive dashboarding, strategic reporting."
        ]
    }
    st.table(pd.DataFrame(overview_data))

# ------------------------------------------------------------------------------
# UNIT 1: FOUNDATIONS & HUMAN CAPITAL VALUE CHAIN
# ------------------------------------------------------------------------------
elif selected_unit == "Unit 1: Foundations & Human Capital Value Chain":
    st.header("Unit 1: Foundations & Human Capital Value Chain Architecture")
    st.caption("Advanced Academic Theory, Strategic Metric Classification & Diagnostic Workbench")
    st.markdown("---")

    tab_theory, tab_diagnostic, tab_classifier, tab_tutor = st.tabs([
        "📖 Advanced Academic Theory", 
        "🕸️ Interactive Value Chain Diagnostic", 
        "📊 Strategic Metric Classifier", 
        "🤖 Unit 1 Socratic AI Tutor"
    ])

    # TAB 1: ACADEMIC THEORY
    with tab_theory:
        st.subheader("1. Strategic Rationale & Theoretical Foundations")
        st.markdown("""
        Historically, Human Resource Management (HRM) operated primarily as an administrative function focused on transaction processing, 
        regulatory compliance, and operational record-keeping. In modern knowledge-driven economies, this traditional orientation creates a 
        significant strategic disconnect. 
        
        To establish human capital as a strategic business driver, HR practitioners must transition from measuring **activity** 
        to measuring **value creation**.
        """)

        st.markdown("""
        <div class="card">
        <h4>The Strategic Shift in HR Analytics</h4>
        <ul>
            <li><b>Traditional HR Accounting:</b> Focuses exclusively on costs, administrative efficiency, and historical compliance (e.g., total training spend, headcount numbers).</li>
            <li><b>Strategic HR Analytics:</b> Evaluates how human capital investments directly influence organizational capabilities, customer outcomes, operational velocity, and financial returns (e.g., Human Capital ROI, quality-of-hire impact).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("2. The Human Capital Value Chain Architecture")
        st.markdown("""
        Pioneered by **Huselid, Becker, and Beatty (2005)**, the **Human Capital Value Chain** provides the architectural logic for 
        linking HR practices directly to the execution of organizational strategy. The value chain operates as a multi-stage causal model:
        """)

        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown("""
            <div class="academic-box">
            <b>Stage 1: HR Inputs & Investments</b><br>
            The financial, technological, and human resources allocated to HR (e.g., HR operational budget, HRIS infrastructure, talent acquisition spend).
            <hr style="margin: 8px 0;">
            <b>Stage 2: HR Processes & Activities</b><br>
            Core functional practices designed and executed by HR (e.g., onboarding programs, competency-based training, performance management cycles).
            </div>
            """, unsafe_allow_html=True)
            
        with col_v2:
            st.markdown("""
            <div class="academic-box">
            <b>Stage 3: HR Deliverables & Capabilities</b><br>
            Intermediate workforce capabilities produced by HR processes (e.g., employee engagement, psychological safety, leadership depth, workforce agility).
            <hr style="margin: 8px 0;">
            <b>Stage 4: Strategic Business Outcomes</b><br>
            Tangible financial and operational results (e.g., Revenue per FTE, customer retention rates, net profit margins, Human Capital ROI).
            </div>
            """, unsafe_allow_html=True)

        st.subheader("3. Resource-Based View (RBV) & VRIO Framework in HR")
        st.markdown("""
        Grounded in **Barney’s (1991) Resource-Based View (RBV)**, organizational competitiveness depends on resources that are:
        * **Valuable (V):** Neutralizing threats or exploiting market opportunities.
        * **Rare (R):** Possessed by very few competing enterprises.
        * **Inimitable (I):** Costly or impossible for competitors to duplicate (often due to complex social dynamics and culture).
        * **Organised (O):** Supported by institutional structures capable of absorbing and deploying the asset.

        When applied to workforce metrics, standard administrative processes (like payroll or template job descriptions) are rarely 
        *Inimitable*. True competitive advantage stems from **Stage 3 Deliverables**—such as high psychological safety, deep tacit knowledge, 
        and an authentic humanised work environment.
        """)

        st.subheader("4. Categorising HR Metrics: Efficiency, Effectiveness, and Business Impact")
        
        metrics_summary_data = {
            "Metric Category": ["HR Efficiency Metrics", "HR Effectiveness Metrics", "Strategic Business Impact Metrics"],
            "Core Focus": ["'Doing Things Right' (Cost & Speed)", "'Doing the Right Things' (Quality & Capability)", "Financial & Operational Value Created"],
            "Primary Audience": ["HR Operational Managers", "HR Business Partners & Line Managers", "Executive Board, CEO & CFO"],
            "Examples (ZAR / Operational)": [
                "Cost per hire (R), Time to fill vacancies, HR staff-to-employee ratio.",
                "Quality of hire (12-month rating), Competency gap closure %, Retention of critical talent.",
                "Human Capital ROI (HCROI), Revenue per FTE (R), Profit per employee (R)."
            ]
        }
        st.table(pd.DataFrame(metrics_summary_data))

    # TAB 2: INTERACTIVE DIAGNOSTIC
    with tab_diagnostic:
        st.subheader("Workforce Value Chain Maturity Diagnostic")
        st.write("Evaluate your organization across all four stages of the Human Capital Value Chain to generate a real-time maturity index and gap analysis.")

        c_d1, c_d2 = st.columns([1, 1])

        with c_d1:
            st.markdown("#### Diagnostic Input Sliders")
            s_inputs = st.slider("Stage 1: HR Inputs & Resource Allocation (1-10)", 1, 10, 6, help="Rate adequacy of HR budget, tech tools, and operational staffing.")
            s_processes = st.slider("Stage 2: HR Process Standardization & Execution (1-10)", 1, 10, 5, help="Rate quality of recruitment, onboarding, and performance management.")
            s_deliverables = st.slider("Stage 3: Intermediate Capabilities & Engagement (1-10)", 1, 10, 7, help="Rate levels of workforce competence, well-being, and leadership depth.")
            s_outcomes = st.slider("Stage 4: Strategic Impact & HCROI Measurement (1-10)", 1, 10, 4, help="Rate capability to link workforce metrics directly to financial results.")

            total_score = s_inputs + s_processes + s_deliverables + s_outcomes
            maturity_pct = (total_score / 40) * 100
            
            st.markdown("---")
            st.metric("Overall Value Chain Maturity Score", f"{maturity_pct:.1f}%")

        with c_d2:
            st.markdown("#### Value Chain Radar Profile")
            radar_data = pd.DataFrame({
                "Stage": ["1. Inputs", "2. Processes", "3. Deliverables", "4. Business Impact"],
                "Maturity Score": [s_inputs, s_processes, s_deliverables, s_outcomes]
            })
            fig_radar = px.line_polar(
                radar_data, r="Maturity Score", theta="Stage", line_close=True,
                range_r=[0, 10], title="Human Capital Value Creation Profile"
            )
            fig_radar.update_traces(fill='toself', fillcolor='rgba(2, 132, 199, 0.2)', line_color='#0284C7')
            st.plotly_chart(fig_radar, use_container_width=True)

        st.markdown("---")
        st.subheader("Diagnostic Feedback & Action Plan")
        
        gap = max(s_inputs, s_processes) - min(s_deliverables, s_outcomes)
        
        if s_outcomes < 5:
            st.warning("""
            ⚠️ **Measurement Disconnect Detected (Stage 4 Deficiency):**
            Your organization demonstrates operational activity in Stages 1 and 2, but lacks analytical mechanisms to prove 
            financial or strategic outcome impact (Stage 4). 
            
            *Recommended Action:* Prioritize building metrics for Human Capital ROI (HCROI) and critical skill retention impact.
            """)
        elif gap > 3:
            st.info("""
            ℹ️ **Activity-Capability Gap Identified:**
            High effort/spend in HR processes is not translating proportionally into Stage 3 workforce capabilities or engagement.
            
            *Recommended Action:* Audit the quality and relevance of learning, development, and onboarding interventions.
            """)
        else:
            st.success("""
            ✅ **Balanced Strategic Alignment:**
            Your Value Chain profile demonstrates strong alignment between operational inputs and strategic business outcomes.
            """)

    # TAB 3: METRIC CLASSIFIER WORKBENCH
    with tab_classifier:
        st.subheader("Strategic Metric Classifier Workbench")
        st.write("Test your diagnostic capability by classifying real-world metrics into their correct Value Chain categories.")

        metrics_db = {
            "Cost per Hire (R)": {
                "category": "HR Efficiency Metric",
                "explanation": "Measures the operational expenditure required to recruit a single worker. Focuses purely on cost and resource speed (Stage 1/2)."
            },
            "Quality of Hire (12-Month Performance Index)": {
                "category": "HR Effectiveness Metric",
                "explanation": "Evaluates the actual output quality and capability delivered by a new hire over time, moving beyond simple speed of recruitment (Stage 3)."
            },
            "Human Capital Return on Investment (HCROI)": {
                "category": "Strategic Business Impact Metric",
                "explanation": "Directly links workforce expenditure to overall organizational revenue and operating profitability (Stage 4)."
            },
            "Average Training Hours per Employee": {
                "category": "HR Efficiency Metric",
                "explanation": "Tracks activity volume. High training hours do not guarantee skill acquisition unless outcome capabilities are measured (Stage 2)."
            },
            "Voluntary Turnover Rate in Critical Roles": {
                "category": "HR Effectiveness Metric",
                "explanation": "Measures the retention of key capability assets that directly protect core organizational competencies (Stage 3)."
            },
            "Revenue per Full-Time Equivalent (FTE)": {
                "category": "Strategic Business Impact Metric",
                "explanation": "Measures financial productivity per unit of human capital deployed (Stage 4)."
            }
        }

        selected_metric_name = st.selectbox("Select a Workforce Metric to Audit:", list(metrics_db.keys()))
        user_selection = st.radio(
            f"Classify **'{selected_metric_name}'**:",
            ["HR Efficiency Metric", "HR Effectiveness Metric", "Strategic Business Impact Metric"]
        )

        if st.button("Submit Classification Audit"):
            actual = metrics_db[selected_metric_name]["category"]
            explanation = metrics_db[selected_metric_name]["explanation"]

            if user_selection == actual:
                st.success(f" Correct! **'{selected_metric_name}'** is an **{actual}**.")
                st.write(f"**Academic Rationale:** {explanation}")
            else:
                st.error(f"❌ Incorrect Classification. You selected **{user_selection}**, but it is actually an **{actual}**.")
                st.write(f"**Academic Rationale:** {explanation}")

    # TAB 4: SOCRATIC AI TUTOR
    with tab_tutor:
        st.subheader("🤖 Unit 1 Socratic AI Academic Tutor")
        st.write("Ask nuanced theoretical questions regarding the Value Chain, VRIO framework, or HR metric classification.")

        st.markdown("**Suggested Discussion Prompts:**")
        col_p1, col_p2, col_p3 = st.columns(3)
        
        prompt_input = ""
        if col_p1.button("How do I explain HCROI to my CFO?"):
            prompt_input = "How do I explain HCROI to my CFO?"
        if col_p2.button("Difference between Efficiency & Effectiveness?"):
            prompt_input = "What is the core difference between HR efficiency and HR effectiveness metrics?"
        if col_p3.button("How does VRIO relate to HR metrics?"):
            prompt_input = "How does Barney's VRIO framework apply to human capital metrics?"

        user_tutor_query = st.text_input("Enter your question for the Unit 1 Tutor:", value=prompt_input)

        if st.button("Ask Unit 1 Tutor"):
            if user_tutor_query:
                query_low = user_tutor_query.lower()

                if "cfo" in query_low or "hcroi" in query_low or "financial" in query_low:
                    tutor_response = """
                    **Unit 1 Tutor Response:**
                    
                    When presenting to a CFO, you must bridge the gap between **Stage 1 (HR Expenditure)** and **Stage 4 (Financial Return)**:
                    
                    1. **Acknowledge the CFO's Lens:** CFOs view traditional HR metrics (like cost-per-hire) as overhead expenses to be minimized.
                    2. **Reframe Human Capital as a Profit Driver:** Introduce **Human Capital Return on Investment (HCROI)**. Explain that HCROI measures how many Rands of profit are generated for every R 1.00 invested in total workforce compensation.
                    3. **The Value Chain Argument:** Explain that cutting HR budgets in Stage 1 directly degrades Stage 3 capabilities (engagement, technical competency), which ultimately reduces Stage 4 Revenue per FTE.
                    
                    *Socratic Follow-Up Question:* What specific financial data points from your current balance sheet would you need to calculate HCROI accurately?
                    """
                elif "efficiency" in query_low or "effectiveness" in query_low:
                    tutor_response = """
                    **Unit 1 Tutor Response:**
                    
                    The distinction rests on **Speed & Cost** versus **Quality & Capability**:
                    
                    * **HR Efficiency ('Doing Things Right'):** Measures administrative speed and operational cost minimization. *Example:* Reducing Time-to-Fill from 45 days to 30 days.
                    * **HR Effectiveness ('Doing the Right Things'):** Measures the capability and strategic value delivered. *Example:* Ensuring the person hired scores in the top 20% for performance at 12 months.
                    
                    **The Pitfall:** An HR department can be highly efficient (filling jobs fast and cheap) while being deeply ineffective (hiring poor fits who leave within six months).
                    
                    *Socratic Follow-Up Question:* Can you identify an HR metric currently used in your organization that measures efficiency, but fails to measure effectiveness?
                    """
                elif "vrio" in query_low or "barney" in query_low or "rbv" in query_low:
                    tutor_response = """
                    **Unit 1 Tutor Response:**
                    
                    Barney’s **Resource-Based View (RBV)** states that competitive advantage comes from resources that are **Valuable, Rare, Inimitable, and Organised (VRIO)**:
                    
                    * **Standard HR Processes are NOT Inimitable:** Any competitor can buy the same HR software or copy a recruitment advertisement.
                    * **Culture & Capability ARE Inimitable:** High psychological safety, deep team trust, and specialized organizational routines are socially complex and impossible to copy easily.
                    
                    **Analytics Takeaway:** Metrics must evaluate whether your talent management practices are creating unique capabilities, rather than just tracking standardized process compliance.
                    
                    *Socratic Follow-Up Question:* What capability within your workforce would you classify as truly 'Inimitable' by competitors?
                    """
                else:
                    tutor_response = f"""
                    **Unit 1 Tutor Response:**
                    
                    Thank you for your inquiry regarding **"{user_tutor_query}"**. 
                    
                    In the context of **Unit 1: Foundations & Human Capital Value Chain Architecture**, keep these three core principles in mind:
                    1. Always map metrics back to the 4-stage causal chain (Input → Process → Capability → Outcome).
                    2. Avoid relying solely on administrative efficiency metrics; ensure effectiveness and business impact are measured.
                    3. Ensure human capital analytics support workplace dignity, psychological safety, and sustainable flourishing.
                    
                    *Socratic Follow-Up Question:* How does your question relate to connecting HR practices directly to strategic business performance?
                    """

                st.session_state.tutor_history.append({"user": user_tutor_query, "tutor": tutor_response})

        if st.session_state.tutor_history:
            st.markdown("---")
            st.markdown("### Academic Dialogue History")
            for chat in reversed(st.session_state.tutor_history):
                st.markdown(f"**🙋‍♂️ Delegate Question:** {chat['user']}")
                st.info(chat['tutor'])

# ------------------------------------------------------------------------------
# UNIT 2: STRATEGIC HR METRICS & CALCULATORS
# ------------------------------------------------------------------------------
elif selected_unit == "Unit 2: Strategic HR Metrics & Workforce Calculators":
    st.header("Unit 2: Strategic HR Metrics & Workforce Calculators")
    st.caption("Quantitative Workforce Evaluation & Embedded ZAR Financial Estimators")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["💰 Labour Turnover Cost Calculator", "📈 Human Capital ROI (HCROI)"])
    
    with tab1:
        st.subheader("Labour Turnover Financial Loss Calculator")
        st.caption("Calculate the total economic impact of voluntary separations, accounting for direct recruitment fees, onboarding costs, and lost productivity.")
        
        col1, col2 = st.columns(2)
        with col1:
            total_headcount = st.number_input("Total Employee Headcount", value=250, step=10)
            annual_departures = st.number_input("Annual Voluntary Separations", value=20, step=1)
            avg_annual_salary = st.number_input("Average Annual Salary (ZAR / R)", value=420000, step=10000)
            replacement_cost_pct = st.slider("Estimated Replacement Cost Multiplier (% of Annual Salary)", 20, 150, 50)
            
        with col2:
            turnover_rate = (annual_departures / total_headcount) * 100 if total_headcount > 0 else 0
            cost_per_exit = avg_annual_salary * (replacement_cost_pct / 100)
            total_turnover_cost = annual_departures * cost_per_exit
            
            st.markdown("#### Diagnostic Output")
            st.metric("Annual Turnover Rate", f"{turnover_rate:.1f}%")
            st.metric("Cost per Departing Employee", f"R {cost_per_exit:,.2f}")
            st.metric("Total Annual Loss to Turnover", f"R {total_turnover_cost:,.2f}", delta="- Financial Impact", delta_color="inverse")

    with tab2:
        st.subheader("Human Capital Return on Investment (HCROI)")
        st.caption("Evaluates the net profitability generated for every Rand spent on employee total remuneration.")
        
        rev = st.number_input("Total Annual Revenue (R)", value=50000000, step=500000)
        operating_exp = st.number_input("Total Operating Expenses [Excluding Remuneration] (R)", value=30000000, step=500000)
        total_comp = st.number_input("Total Employee Remuneration & Benefits (R)", value=12000000, step=250000)
        
        if total_comp > 0:
            hcroi = (rev - (operating_exp - total_comp)) / total_comp
            st.metric("Human Capital ROI (HCROI Ratio)", f"{hcroi:.2f}")
            st.info(f"Interpretation: For every R 1.00 spent on employee remuneration, the organisation generates R {hcroi:.2f} in operating profitability.")

# ------------------------------------------------------------------------------
# UNIT 3: WORKFORCE DIAGNOSTICS & HR AUDIT
# ------------------------------------------------------------------------------
elif selected_unit == "Unit 3: Workforce Diagnostics & HR Audit":
    st.header("Unit 3: Workforce Diagnostics & HR Audit Frameworks")
    st.caption("Governance Evaluation, Capabilities Matrix, and Diagnostic Action Planning")
    st.markdown("---")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card">
        <h4>✅ Strengths Identified</h4>
        <ul>
            <li><b>Strategic Alignment:</b> High integration between talent acquisition strategies and core departmental objectives.</li>
            <li><b>Governance & Compliance:</b> Robust compliance tracking across Employment Equity, BCEA, and Labour Relations policies.</li>
            <li><b>Learning Infrastructure:</b> Strong participation rates in internal skills development programs.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="card">
        <h4>💡 Recommendations for Improvement</h4>
        <ul>
            <li><b>Predictive Analytics Adoption:</b> Move from descriptive reporting to predictive modeling for critical skill retention.</li>
            <li><b>Exit Interview Action Loops:</b> Systematically analyze qualitative exit data to address systemic turnover causes.</li>
            <li><b>Psychological Safety Audits:</b> Embed routine pulse surveys measuring workplace psychological safety and employee flourishing.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# UNIT 4: PREDICTIVE ANALYTICS & REPORTING
# ------------------------------------------------------------------------------
elif selected_unit == "Unit 4: Predictive Analytics & Reporting":
    st.header("Unit 4: Advanced Predictive Analytics & HR Dashboards")
    st.caption("Flight Risk Modeling, Talent Visualization, and Executive Reporting")
    st.markdown("---")
    
    np.random.seed(42)
    n_samples = 100
    df_risk = pd.DataFrame({
        "Tenure_Years": np.random.uniform(0.5, 10, n_samples),
        "Performance_Rating": np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.1, 0.15, 0.5, 0.15, 0.1]),
        "Satisfaction_Score": np.random.uniform(1, 10, n_samples),
        "Department": np.random.choice(["HR", "Finance", "Operations", "Marketing", "IT"], n_samples)
    })
    df_risk["Flight_Risk_Score"] = (100 - (df_risk["Satisfaction_Score"] * 8 + df_risk["Performance_Rating"] * 4)).clip(5, 95)
    
    fig_scatter = px.scatter(
        df_risk, x="Tenure_Years", y="Satisfaction_Score", size="Flight_Risk_Score", color="Department",
        title="Predictive Retention Risk Model: Satisfaction vs Tenure (Bubble Size = Flight Risk)"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# ------------------------------------------------------------------------------
# INTERACTIVE AI ASSISTANT & SUPPORT
# ------------------------------------------------------------------------------
elif selected_unit == "Interactive AI Assistant & Delegate Support":
    st.header("Interactive SLP AI Assistant & Support")
    st.write("Ask questions regarding course formulas, diagnostic tools, module manuals, or assessment guidelines.")
    
    user_input = st.text_input("Enter your query:")
    if st.button("Submit Query"):
        if user_input:
            st.session_state.general_chat_history.append(("User", user_input))
            resp = f"Thank you for your inquiry regarding '{user_input}'. Please consult your unit study guide or contact your programme coordinator for assessment criteria."
            st.session_state.general_chat_history.append(("Assistant", resp))
            
    if st.session_state.general_chat_history:
        for sender, text in reversed(st.session_state.general_chat_history):
            st.write(f"**{sender}:** {text}")


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
