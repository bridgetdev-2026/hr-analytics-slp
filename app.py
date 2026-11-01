import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ==============================================================================
# 1. PAGE CONFIGURATION & STYLING (Top of File)
# ==============================================================================
st.set_page_config(
    page_title="HR Metrics & Analytics SLP Portal",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Academic Theme
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #002B49; margin-bottom: 0px; }
    .sub-header { font-size: 1.1rem; color: #555555; margin-bottom: 20px; }
    .card { background-color: #F8F9FA; border-left: 5px solid #002B49; padding: 18px; border-radius: 6px; margin-bottom: 20px; }
    .academic-box { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-left: 4px solid #0284C7; padding: 16px; border-radius: 6px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# Main Application Title
st.markdown('<p class="main-header">📊 HR Metrics and Analytics: Advanced Applied Analytics and Workforce Diagnostics</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Nelson Mandela University | Faculty of Business and Economic Sciences | School of Industrial Psychology and HR Management</p>', unsafe_allow_html=True)
st.markdown("---")

# ==============================================================================
# 2. SESSION STATE INITIALISATION
# ==============================================================================
if "tutor_history" not in st.session_state:
    st.session_state.tutor_history = []
if "general_chat_history" not in st.session_state:
    st.session_state.general_chat_history = []

# ==============================================================================
# 3. SIDEBAR NAVIGATION (MUST COME BEFORE ANY IF STATEMENTS)
# ==============================================================================
st.sidebar.title("Programme Navigation")
st.sidebar.markdown("**Short Learning Programme Units**")

selected_unit = st.sidebar.radio(
    "Navigate to:",
    [
        "Programme Course Outline & Overview",
        "Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain",
        "Unit 2: Data Architecture, Sources and Governance",
        "Unit 3: Strategic Partnering, Balanced Scorecards, and Dashboards",
        "Unit 4: HRM Practice Indices, Diagnostics and Predictive Modelling",
        "Unit 5: Operationalising the HR Analytics Cycle",
        "Annexures & Case Studies",
        "Interactive AI Assistant & Socratic Tutor"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("🎓 **School of Industrial Psychology & Human Resource Management**\nNelson Mandela University")

# ==============================================================================
# 4. MODULE PAGES (THIS IS WHERE selected_unit IS USED)
# ==============================================================================

# ------------------------------------------------------------------------------
# PROGRAMME OVERVIEW & COURSE OUTLINE
# ------------------------------------------------------------------------------
if selected_unit == "Programme Course Outline & Overview":
    st.header("Course Outline & Programme Overview")
    st.caption("Nelson Mandela University | Faculty of Business and Economic Sciences")
    st.markdown("---")
    
    st.markdown("""
    <div class="card">
    <h4>Programme Purpose & Target Audience</h4>
    <b>SLP Title:</b> HR Metrics and Analytics: Advanced Applied Analytics and Workforce Diagnostics<br>
    <b>Programme Type:</b> Short Learning Programme, offered as a standalone professional certification for industry practitioners.<br>
    <b>Target Audience:</b> Working HR Practitioners, Line Managers, and Organisational Leaders seeking to build advanced competencies in workforce analytics.<br>
    <b>Prerequisites:</b> An Advanced Diploma or Degree or an equivalent qualification; or relevant workplace experience.<br><br>
    <b>Purpose:</b> To enable participants to use HR metrics and analytics as a diagnostic tool for operational and strategic decision-making, thereby optimising organisational human capital investments and shifting the HRM function from an administrative role to a strategic business partner.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Units", value="5 Core Units")
    col2.metric(label="Programme Type", value="Standalone Certification")
    col3.metric(label="Assessment", value="Formative & Diagnostic")
    col4.metric(label="School", value="IOP & HRM")

# ------------------------------------------------------------------------------
# UNIT 1: FOUNDATIONS OF STRATEGIC HRM, eHRM AND THE VALUE CHAIN
# ------------------------------------------------------------------------------
elif selected_unit == "Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain":
    st.header("Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain")
    st.caption("Official Nelson Mandela University SLP Learner Guide & Interactive Diagnostic Workbench")
    # [Unit 1 tabs and code sit here...]

# ------------------------------------------------------------------------------
# OTHER UNITS FOLLOW BELOW (Unit 2, Unit 3, Unit 4, Unit 5, Annexures, Assistant)
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# PROGRAMME OVERVIEW & COURSE OUTLINE
# ------------------------------------------------------------------------------
if selected_unit == "Programme Course Outline & Overview":
    st.header("Course Outline & Programme Overview")
    st.caption("Nelson Mandela University | Faculty of Business and Economic Sciences")
    st.markdown("---")
    
    st.markdown("""
    <div class="card">
    <h4>Programme Purpose & Target Audience</h4>
    <b>SLP Title:</b> HR Metrics and Analytics: Advanced Applied Analytics and Workforce Diagnostics<br>
    <b>Programme Type:</b> Short Learning Programme, offered as a standalone professional certification for industry practitioners.<br>
    <b>Target Audience:</b> Working HR Practitioners, Line Managers, and Organisational Leaders seeking to build advanced competencies in workforce analytics.<br>
    <b>Prerequisites:</b> An Advanced Diploma or Degree or an equivalent qualification; or relevant workplace experience.<br><br>
    <b>Purpose:</b> To enable participants to use HR metrics and analytics as a diagnostic tool for operational and strategic decision-making, thereby optimising organisational human capital investments and shifting the HRM function from an administrative role to a strategic business partner.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Units", value="5 Core Units")
    col2.metric(label="Programme Type", value="Standalone Certification")
    col3.metric(label="Assessment", value="Formative & Diagnostic")
    col4.metric(label="School", value="IOP & HRM")
    
    st.markdown("---")
    st.subheader("Core Learning Outcomes & Assessment Criteria")
    
    with st.expander("Outcome 1: Theoretical & Practical Foundations (Value Chain & eHRM)", expanded=True):
        st.markdown("""
        **Outcome:** Apply theoretical and practical knowledge to evaluate the purpose, evolution, and value of HR metrics, analytics, electronic human resource management (eHRM), and Human Resource Information Systems (HRIS) from a value chain perspective.
        
        *Assessment Criteria:*
        * The role and evolution of HRM, eHRM, and HRISs are demonstrated through an exposition of relevant theory pertaining to HR metrics within the HRM value chain.
        * Fundamental concepts (measures, metrics, descriptive vs. predictive/prescriptive analytics) are clearly defined and applied.
        * A sound business case is made for adopting a value chain approach to HRM supported by metrics and analytics.
        """)

    with st.expander("Outcome 2: Data Architecture, Maturity Models & Process Workflow"):
        st.markdown("""
        **Outcome:** Assess the value of HR metrics, the analytics maturity model, and data architectures in business diagnostics and decision-making processes.
        
        *Assessment Criteria:*
        * Organisational readiness is evaluated using the HR Analytics Maturity Model, identifying critical success factors and constraints.
        * The selection and evaluation of HR analytics technologies, enterprise HCM platforms, and software vendor demonstrations are assessed against organisational maturity, local compliance, and budget alignment.
        * The structured 5-step HR Analytics Process Model (Exploration, Examination, Extraction, Evaluation, Extrapolation) is applied to business scenarios.
        * The nature of internal data sources (tenure, compensation, performance appraisals) and external benchmarks are analysed while navigating data quality, ethics, and governance.
        """)

    with st.expander("Outcome 3: Scorecards, Strategy Maps & Dashboards"):
        st.markdown("""
        **Outcome:** Formulate and implement an integrated HR metrics, scorecard, and analytics framework as an efficient diagnostic tool for operational and strategic decision-making.
        
        *Assessment Criteria:*
        * Balanced Business Scorecards, HRM Scorecards, and Strategy Mapping are utilised to align workforce metrics with broader organisational objectives.
        * Relevant index dashboards covering lifecycle areas (recruitment efficiency, employee retention/turnover, training ROI, and absenteeism) are developed and interpreted using appropriate analysis and graphing techniques.
        * Gap analysis, alignment inventories, and predictive insights are successfully employed to solve operational problems and drive strategic interventions.
        * Formal written analytical reports, periodic monthly/quarterly scorecard reviews, and executive presentation frameworks are formulated and applied to communicate workforce insights effectively.
        """)

    with st.expander("Outcome 4: Functional Indices & Advanced Predictive Modelling"):
        st.markdown("""
        **Outcome:** Formulate and evaluate comprehensive HRM functional indices (efficiency, effectiveness, and impact) and construct advanced diagnostic models and lifecycle dashboards to drive strategic decision-making.
        
        *Assessment Criteria:*
        * HRM functional and practice indices are rigorously categorised and evaluated across administrative efficiency, operational effectiveness, and strategic impact dimensions.
        * Granular functional metrics across planning, attraction, retention, motivation, productivity, and eHRM/HRIS technology are integrated into multi-dimensional dashboards.
        * Descriptive reporting is successfully transitioned into advanced diagnostic analyses and predictive modelling (such as flight-risk scoring and regression) to anticipate operational bottlenecks and workforce turnover.
        """)

    st.markdown("---")
    st.subheader("Short Learning Programme Curriculum Structure")
    
    overview_data = {
        "Unit Module": [
            "Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain",
            "Unit 2: Data Architecture, Sources and Governance",
            "Unit 3: Strategic Partnering, Balanced Scorecards, and Dashboards",
            "Unit 4: HRM Practice Indices, Diagnostics and Predictive Modelling",
            "Unit 5: Operationalising the HR Analytics Cycle",
            "Annexures & Case Studies"
        ],
        "Focus & Core Deliverables": [
            "Strategic evolution, Coffee Journey value chain, Measures vs Metrics vs Analytics, Maturity Model, Best practice principles.",
            "HCM platforms, internal data silos, external benchmarks, Excel diagnostic models, POPIA & GenAI Bilateral Coaching.",
            "Strategic business partnering, HR Strategy Maps, 4-Perspective Scorecard, Google (PiLab) & Birmingham City Council case studies.",
            "Efficiency vs Effectiveness vs Impact indices, Logistic regression, p-values, VIF, ROC-AUC, Apex HiPo flight risk pipeline.",
            "HR team sensitisation, analytical culture, small-scale pilot execution, legal collaboration, board memo presentation framework.",
            "Annexure A: Apex HiPo Technical Specialist Audit & Annexure B: The Practitioner's Journey (Phases 1–3)."
        ]
    }


# ------------------------------------------------------------------------------
# UNIT 1: FOUNDATIONS OF STRATEGIC HRM, eHRM AND THE VALUE CHAIN
# ------------------------------------------------------------------------------
elif selected_unit == "Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain":
    st.header("Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain")
    st.caption("Official Nelson Mandela University SLP Learner Guide & Interactive Diagnostic Workbench")
    st.markdown("---")

    # Module Tabs
    tab_theory, tab_coffee, tab_video, tab_diagnostic, tab_classifier, tab_tutor, tab_checkpoint = st.tabs([
        "📖 1.1-1.6 Module Content", 
        "☕ The Coffee Journey",
        "🎥 Video Lecture & Media",
        "🕸️ Apex Call Centre Workbench", 
        "📊 Unpacking Terminology", 
        "🤖 Socratic AI Tutor",
        "✍️ Formative Checkpoint"
    ])

    # --------------------------------------------------------------------------
    # TAB 1: ACADEMIC THEORY & CONTENT (1.1 - 1.6)
    # --------------------------------------------------------------------------
    with tab_theory:
        st.subheader("1.1 Learning Objectives")
        st.markdown("""
        By the end of this unit, you will be able to:
        * Outline the role and evolution of the Human Resource Management (HRM) function from a value chain and strategic business partnering perspective.
        * Differentiate clearly between foundational data concepts: measures, metrics, analytics, and predictive/prescriptive analytics.
        * Evaluate organisational data readiness using the HR Analytics Maturity Model and identify critical success factors, constraints, and best practice principles.
        * Explain the nature, purpose, and integration of Electronic HRM (eHRM) and Human Resource Information Systems (HRIS) architectures in supporting data-driven decisions.
        * Navigate the 5-Step HR Analytics Process Model (Exploration to Extrapolation) as the overarching roadmap for the course.
        * Evaluate and select HR analytics technologies, HCM suites, and mid-market tools tailored to organisational needs, budget, and local regulatory environments.
        * Understand the role of Generative AI and Bilateral Iterative Coaching as collaborative tools in accelerating data preparation and analytical workflows.
        """)

        st.markdown("---")
        st.subheader("1.2 The Strategic Evolution of HRM")
        st.write(
            "Historically, human resources operated primarily as an administrative, compliance-driven, and transactional department. "
            "In this traditional personnel-management paradigm, the function focused almost exclusively on record-keeping, payroll administration, "
            "contract execution, and enforcing labour regulations. Modern organisational success, however, demands a fundamental paradigm shift: "
            "the recognition of human capital as the ultimate core driver of sustainable competitive advantage. Because physical assets, "
            "technology, and capital can easily be replicated by competitors, a skilled, engaged, and strategically aligned workforce remains "
            "the sole inimitable asset an organisation possesses."
        )

        st.markdown("""
        <div class="card">
        <h4>The Strategic Shift & Imperative</h4>
        <ul>
            <li><b>The Shift:</b> HR has evolved from a reactive record-keeping and payroll unit into a proactive strategic business partner, co-creating business strategy alongside executive leadership.</li>
            <li><b>The Imperative:</b> To sit legitimately at the executive table, HR practitioners must abandon intuition-based decision-making. They must empirically measure and demonstrate how people decisions (talent acquisition, leadership development, compensation, workflow design) directly impact operational performance, customer satisfaction, and financial returns.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("1.3 The HRM Value Chain Approach")
        st.write(
            "Adopting a value chain perspective means viewing the human resource management function not as a siloed, administrative department, "
            "but as an interconnected series of strategic, value-adding processes. Drawing from strategic management theory (such as Michael Porter’s "
            "value chain framework adapted for human capital), this approach conceptualises HR as an operational pipeline that transforms raw "
            "organisational inputs into sustainable competitive outputs."
        )

        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.markdown("""
            <div class="academic-box">
            <b>Inputs:</b> The foundational resources entering the system, including human capital (talent, skills, and competencies), financial capital, technological infrastructure (HRIS/eHRM), and intellectual property.<br><br>
            <b>Throughputs (The Employee Lifecycle):</b> The core operational processes managed by HR, spanning workforce planning, talent acquisition, onboarding, training and development, performance management, remuneration, and retention.
            </div>
            """, unsafe_allow_html=True)
        with col_v2:
            st.markdown("""
            <div class="academic-box">
            <b>Outputs:</b> The ultimate strategic results generated by the system, including enhanced employee productivity, organisational innovation, heightened customer satisfaction, reduced operational risk, and long-term revenue growth.<br><br>
            <b>Connecting the Chain:</b> Metrics and analytics serve as the vital connective tissue:
            <ul>
                <li><i>Tracking Efficiency:</i> Measuring speed, cost, and resource utilisation (e.g., time-to-fill, administrative cost per employee).</li>
                <li><i>Assessing Effectiveness:</i> Evaluating intermediate programme goals (e.g., training transfer rates, quality of hire).</li>
                <li><i>Proving Ultimate Impact:</i> Demonstrating direct causal links to business outcomes (e.g., how engagement correlates with customer retention).</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("1.5 Building the Business Case & Best Practice Principles")
        
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            st.markdown("""
            <div class="card">
            <h4>1.5.1 HRM Best Practice Principles</h4>
            <ul>
                <li><b>Strategic Alignment (Line-of-Sight):</b> Metrics must directly support broader strategic goals.</li>
                <li><b>Evidence-Based Decision Making:</b> Replacing gut-feel with verifiable data.</li>
                <li><b>Data Integrity & Governance:</b> Ensuring accuracy and consistent definitions.</li>
                <li><b>Ethical Stewardship & Privacy:</b> Balancing analytics with strict POPIA compliance and employee trust.</li>
                <li><b>Actionable Insight:</b> Avoiding 'analysis paralysis' by driving concrete interventions.</li>
                <li><b>Cross-Functional Collaboration:</b> Active partnership between HR, IT, line management, and legal.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col_p2:
            st.markdown("""
            <div class="card">
            <h4>1.5.2 Criticisms & Operational Constraints</h4>
            <ul>
                <li><b>Lack of Inclination/Readiness:</b> Cultural resistance among traditional practitioners.</li>
                <li><b>Characterisation Deficits:</b> Unstandardised records across regional branches.</li>
                <li><b>The 'Quality vs Quantity' Trap:</b> Gathering excessive metrics without purpose.</li>
                <li><b>Insufficient Software/Tools:</b> Outdated legacy systems yielding incomplete outcomes.</li>
                <li><b>Over-Reliance on Quantification:</b> Losing human empathy and qualitative context.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("1.5.3 The HR Analytics Maturity Model")
        maturity_table = {
            "Level": ["Level 1: Reactive / Administrative Reporting", "Level 2: Operational / Standardised Reporting", "Level 3: Advanced / Strategic Analytics", "Level 4: Predictive & Prescriptive Modelling"],
            "Focus": ["Operational tracking, headcount counts, compliance monitoring, and manual processing.", "Routine tracking of standard historical metrics (e.g., monthly turnover figures, cost-per-hire averages).", "Linking HR metrics directly to business outcomes and conducting root-cause analyses.", "Utilising advanced statistical modelling and algorithms to forecast future workforce behaviour and prescribe automated interventions."],
            "Diagnostic Value & Limitation": ["Answers only 'What happened?' retrospectively, with HR acting purely as an administrative cost centre.", "Provides baseline data across departments but lacks strategic context or root-cause diagnosis.", "Answers 'Why did it happen?' by connecting HR interventions to productivity and financial performance.", "Answers 'What will happen next and what should we do about it?', transforming HR into a fully predictive strategic partner."]
        }
        st.table(pd.DataFrame(maturity_table))

        st.markdown("---")
        st.subheader("1.6 eHRM and HRIS: The Digital Backbone")
        st.write(
            "To gather, clean, and analyse workforce data effectively, organisations cannot rely on manual spreadsheets; "
            "they require a robust technological architecture formed by two interdependent pillars:"
        )
        st.markdown("""
        * **Human Resource Information Systems (HRIS):** The core database architectures and back-end software platforms used to store, manage, and process master employee data (tenure, compensation, appraisal ratings, compliance).
        * **Electronic HRM (eHRM):** The front-end administrative, operational, and transactional execution of HR functions using web-based portals and networks (self-service leave, goal tracking, personal updates).
        * **The Strategic Link:** eHRM and HRIS work in tandem to provide clean, centralised data pipelines. Without this digital architecture, analytics initiatives collapse due to poor data quality and characterisation deficits.
        """)

    # --------------------------------------------------------------------------
    # TAB 2: THE COFFEE JOURNEY ANALOGY
    # --------------------------------------------------------------------------
    with tab_coffee:
        st.subheader("1.3 The HRM Value Chain: The Coffee Journey Analogy")
        st.info(
            "When you buy a cup of coffee, you are experiencing a carefully crafted product where value has been added at every single stage "
            "of the supply chain. The HRM value chain operates in the exact same way, transforming raw human potential into ultimate organisational performance."
        )

        c_c1, c_c2, c_c3 = st.columns(3)
        with c_c1:
            st.markdown("""
            <div class="card">
            <h4>Stage 1: 'GET'</h4>
            <b>Harvesting Raw Beans</b><br><br>
            <i>The Analogy:</i> A farmer must forecast demand, select soil, and harvest high-grade beans. You cannot make exceptional coffee with low-quality raw materials.<br><br>
            <i>In Practice:</i>
            <ul>
                <li><b>Talent Planning:</b> Forecasting commercial demand and structural gaps.</li>
                <li><b>Targeted Recruitment:</b> Sourcing and vetting high-potential human capital.</li>
                <li><b>Strategic Onboarding:</b> Transitioning raw talent smoothly into the operational ecosystem.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with c_c2:
            st.markdown("""
            <div class="card">
            <h4>Stage 2: 'DEVELOP & KEEP'</h4>
            <b>Processing & Roasting into Grades</b><br><br>
            <i>The Analogy:</i> Raw beans taste bitter. They must be roasted, graded, and blended. If equipment isn't maintained or millers paid fairly, skills go elsewhere.<br><br>
            <i>In Practice:</i>
            <ul>
                <li><b>Learning & Development:</b> Elevating baseline competencies via continuous coaching.</li>
                <li><b>Performance Tracking:</b> Calibrating outputs and cascading KPIs.</li>
                <li><b>Total Rewards:</b> Structuring equitable grading, remuneration, and career management.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with c_c3:
            st.markdown("""
            <div class="card">
            <h4>Stage 3: 'ENGAGE'</h4>
            <b>The Skilled Barista Crafting the Final Cup</b><br><br>
            <i>The Analogy:</i> Even with fine beans, a poor barista ruins the product. A skilled barista extracts an espresso that delights the customer.<br><br>
            <i>In Practice:</i>
            <ul>
                <li><b>Empathetic Leadership:</b> Forging relational trust and organizational justice.</li>
                <li><b>Psychological Safety:</b> Protecting employee wellness and mitigating change fatigue.</li>
                <li><b>Culture & Transformation:</b> Fostering industrial stability, equity, and deep motivation.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="background-color: #002B49; color: white; padding: 15px; border-radius: 6px; text-align: center;">
        <h4>Integrated HRIS Data Flows</h4>
        Running beneath this entire coffee journey is the digital plumbing—predictive analytics, compliance metrics, and interconnected employee data linking the entire value chain into a single strategic intelligence hub.
        </div>
        """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TAB 3: EMBEDDED VIDEO LECTURE & MEDIA PLAYER
    # --------------------------------------------------------------------------
    with tab_video:
        st.subheader("🎥 Unit 1 Video Lecture & Curriculum Walkthrough")
        st.caption("Nelson Mandela University | Executive HR Analytics Lecture Series")
        
        # Interactive Video Player
        st.markdown("#### Watch Unit 1 Lecture: Foundations of Strategic HRM & The Value Chain")
        
        # Video URL Input / Default Placeholder Lecture
        video_url = st.text_input(
            "Video Stream Source URL (YouTube / Vimeo / MP4):", 
            value="https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # Configurable module video URL
            help="Paste your hosted lecture recording, slide walkthrough, or MP4 video link here."
        )
        
        try:
            st.video(video_url)
        except Exception:
            st.info("📺 Enter a valid MP4 or YouTube URL above to load your custom lecture stream.")

        st.markdown("---")
        with st.expander("📝 View Video Lecture Script & Executive Summary Notes"):
            st.markdown("""
            ### Executive Lecture Summary: Unit 1 Key Takeaways
            1. **The Administrative Shift:** Why HR must abandon gut-feel and intuitively driven policy changes in favour of empirical value-chain evidence.
            2. **The Coffee Journey Architecture:** How 'GET', 'DEVELOP & KEEP', and 'ENGAGE' stages interact to build organisational capability.
            3. **The Call Centre Dilemma:** Why raw measures (30 exits) trigger panic, metrics (24% turnover) highlight operational problems, and predictive analytics (call volume & coaching breaks) prescribe solutions.
            4. **POPIA Compliance:** Ensuring employee data privacy and ethical stewardship while building integrated HRIS data pipelines.
            """)

    # --------------------------------------------------------------------------
    # TAB 4: APEX CALL CENTRE WORKBENCH (MATURITY & PREDICTIVE DIAGNOSTIC)
    # --------------------------------------------------------------------------
    with tab_diagnostic:
        st.subheader("1.4.3 & 1.5.3 Interactive Workbench: Apex Logistics Call Centre Scenario")
        st.markdown("Simulate the 4 levels of the HR Analytics Maturity Model using the official Call Centre case study.")

        col_w1, col_w2 = st.columns(2)
        
        with col_w1:
            st.markdown("#### Scenario Inputs & Operational Controls")
            daily_calls = st.slider("Average Daily Calls per Agent:", 40, 120, 85, help="Baseline call volume per customer service agent.")
            coaching_breaks = st.radio("Structured Coaching Break Policy:", ["No Structured Breaks", "30-Min Structured Rotational Break"])
            shift_fatigue = st.slider("Unscheduled Overtime Hours / Month:", 0, 50, 25)

            # Predictive flight risk calculation logic from Section 1.4.3
            risk_score = (daily_calls * 0.8) + (shift_fatigue * 1.2)
            if coaching_breaks == "30-Min Structured Rotational Break":
                risk_score -= 30
            risk_score = max(5, min(95, risk_score))

        with col_w2:
            st.markdown("#### Maturity Model Diagnostic Output")
            
            st.metric(label="Predicted 60-Day Exit Likelihood", value=f"{risk_score:.1f}%")
            
            if risk_score > 75:
                st.error("🚨 **Level 4 Prescriptive Intervention Required:** Agents handling high call volumes without structured coaching breaks exhibit a >75% exit probability within 60 days. *Prescription:* Cap daily call volumes at 80 and mandate rotational breaks immediately.")
            elif risk_score > 45:
                st.warning("⚠️ **Level 3 Diagnostic Finding:** Moderate turnover risk detected. Multivariate regression indicates call volumes and unmanaged overtime correlate strongly with stress-related absenteeism.")
            else:
                st.success("✅ **Level 2 Operational Baseline:** Turnover risk sits within acceptable industry benchmarks (<15%). Ensure shift coverage remains stable.")

        st.markdown("---")
        st.markdown("#### The 4 Maturity Levels Applied to this Scenario:")
        st.markdown("""
        * **Level 1 (Measure):** *"We had 30 customer service agents resign this quarter."* (Raw count triggering panic without context).
        * **Level 2 (Metric):** *"Our quarterly call centre turnover rate is 24%, which is 8% higher than our industry benchmark."* (Contextualised performance).
        * **Level 3 (Diagnostic Analytics):** *"Multivariate regression reveals high turnover is driven by agents handling >80 calls/day without coaching breaks."* (Root cause isolated).
        * **Level 4 (Predictive & Prescriptive):** *"We predict losing 45 agents next quarter unless we cap daily call volumes and introduce rotational breaks."* (Actionable foresight).
        """)

    # --------------------------------------------------------------------------
    # TAB 5: UNPACKING TERMINOLOGY WORKBENCH
    # --------------------------------------------------------------------------
    with tab_classifier:
        st.subheader("1.4 Unpacking Terminology: Interactive Classifier")
        st.write("Test your understanding of Measures, Metrics, and Analytics by evaluating workplace scenarios.")

        term_db = {
            "Total Monthly Payroll = R25,000,000": {
                "type": "Measure",
                "reason": "Standalone raw quantitative count. Tells you absolute volume, but provides no relational context or denominator (Section 1.4.1)."
            },
            "Cost-per-Hire = R12,000 (vs Industry Benchmark of R10,000)": {
                "type": "Metric",
                "reason": "Measures put into context with a denominator (Total Spend / Total Hires) to evaluate performance against a baseline (Section 1.4.2)."
            },
            "Agents handling >80 calls/day without breaks have a 90% likelihood of exit within 60 days": {
                "type": "Analytics (Predictive / Prescriptive)",
                "reason": "Statistical exploration that uncovers root causes, forecasts probabilities, and prescribes optimized interventions (Section 1.4.3)."
            },
            "4,500 Total Training Hours Delivered": {
                "type": "Measure",
                "reason": "Raw physical observation. Tells you nothing about efficiency, skill transfer, or performance quality (Section 1.4.1)."
            },
            "Absenteeism Rate = 6.5% of Scheduled Workdays": {
                "type": "Metric",
                "reason": "Percentage ratio comparing lost workdays to scheduled workdays to standardize performance across branches (Section 1.4.2)."
            }
        }

        selected_term = st.selectbox("Select a Workplace Data Statement to Classify:", list(term_db.keys()))
        user_term_choice = st.radio(
            f"Classify **'{selected_term}'**:",
            ["Measure", "Metric", "Analytics (Predictive / Prescriptive)"]
        )

        if st.button("Audit Classification"):
            correct_type = term_db[selected_term]["type"]
            reasoning = term_db[selected_term]["reason"]

            if user_term_choice == correct_type:
                st.success(f" Correct! **'{selected_term}'** is a **{correct_type}**.")
                st.write(f"**NMU Curriculum Explanation:** {reasoning}")
            else:
                st.error(f"❌ Incorrect. You selected **{user_term_choice}**, but it is actually a **{correct_type}**.")
                st.write(f"**NMU Curriculum Explanation:** {reasoning}")

    # --------------------------------------------------------------------------
    # TAB 6: SOCRATIC AI ACADEMIC TUTOR
    # --------------------------------------------------------------------------
    with tab_tutor:
        st.subheader("🤖 Unit 1 Socratic AI Academic Tutor")
        st.write("Engage with your virtual tutor on the Coffee Journey, Call Centre scenario, POPIA ethics, and the Maturity Pyramid.")

        st.markdown("**Select a Discussion Prompt or Ask Your Own Question:**")
        col_tp1, col_tp2, col_tp3 = st.columns(3)
        
        t_prompt = ""
        if col_tp1.button("Explain the Coffee Journey"):
            t_prompt = "Explain how the Coffee Journey analogy illustrates the HRM Value Chain."
        if col_tp2.button("Difference: Measure vs Metric?"):
            t_prompt = "What is the core difference between a measure and a metric using the Call Centre scenario?"
        if col_tp3.button("How to move Level 1 to Level 4?"):
            t_prompt = "How does an organisation transition from Level 1 Reactive reporting to Level 4 Predictive modelling?"

        user_tutor_query = st.text_input("Enter your question for the Unit 1 Tutor:", value=t_prompt)

        if st.button("Ask Unit 1 Tutor"):
            if user_tutor_query:
                q_low = user_tutor_query.lower()

                if "coffee" in q_low:
                    ans = """
                    **Unit 1 Socratic Tutor:**
                    
                    The **Coffee Journey Analogy** (Section 1.3) illustrates that value is added at every single stage of human resource management:
                    
                    1. **Stage 1: 'GET' (Harvesting Raw Beans):** Talent planning, targeted recruitment, and strategic onboarding. You cannot brew great coffee with poor raw beans.
                    2. **Stage 2: 'DEVELOP & KEEP' (Roasting & Grading):** Learning & development, performance tracking, and total rewards. Raw beans taste bitter until roasted and graded.
                    3. **Stage 3: 'ENGAGE' (The Skilled Barista):** Empathetic leadership, psychological safety, and culture. A poor barista ruins good beans; a skilled barista extracts customer satisfaction and value.
                    
                    *Socratic Reflection Question:* Which stage of the coffee journey is currently experiencing the biggest operational bottleneck in your organisation?
                    """
                elif "measure" in q_low or "metric" in q_low or "call centre" in q_low:
                    ans = """
                    **Unit 1 Socratic Tutor:**
                    
                    Let's unpack the distinction using the Call Centre scenario (Section 1.4):
                    
                    * **Measure (Raw Count):** *"30 agents resigned."* This triggers panic because it lacks context, denominators, or baselines.
                    * **Metric (Contextual Ratio):** *"24% quarterly turnover rate (8% above benchmark)."* This introduces a denominator and highlights a clear operational problem.
                    * **Analytics (Root Cause & Prediction):** *"Agents handling >80 calls/day without breaks have a 90% exit probability."* This diagnoses why it happens and prescribes automated rotational breaks.
                    
                    *Socratic Reflection Question:* Can you convert one raw measure currently reported in your department into an evaluative metric?
                    """
                elif "level" in q_low or "maturity" in q_low or "transition" in q_low:
                    ans = """
                    **Unit 1 Socratic Tutor:**
                    
                    Transitioning up the **HR Analytics Maturity Model** (Section 1.5.3) requires a deliberate shift:
                    
                    * **Level 1 → Level 2:** Eliminate manual processing errors, establish standard definitions, and implement an HRIS dashboard.
                    * **Level 2 → Level 3:** Stop looking at metrics in isolation; join payroll, attendance, and performance tables using a universal Employee ID to answer *why* problems occur.
                    * **Level 3 → Level 4:** Apply multivariate regression and machine learning to project trends forward and prescribe proactive interventions before resignations occur.
                    
                    *Socratic Reflection Question:* What is the primary data governance constraint holding your organisation at its current maturity level?
                    """
                else:
                    ans = f"""
                    **Unit 1 Socratic Tutor:**
                    
                    Thank you for your inquiry regarding **"{user_tutor_query}"**. 
                    
                    In **Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain**, keep these core principles in mind:
                    1. Always map HR practices back to the 3-stage value chain (GET → DEVELOP & KEEP → ENGAGE).
                    2. Move away from raw measures to evaluative metrics and predictive foresight.
                    3. Ensure all analytics align with POPIA privacy rules, data integrity, and ethical employee stewardship.
                    
                    *Socratic Reflection Question:* How does this concept support shifting HR from an administrative cost centre to a strategic business partner?
                    """

                st.session_state.tutor_history.append({"user": user_tutor_query, "tutor": ans})

        if st.session_state.tutor_history:
            st.markdown("---")
            st.markdown("### Academic Dialogue History")
            for chat in reversed(st.session_state.tutor_history):
                st.markdown(f"**🙋‍♂️ Delegate Question:** {chat['user']}")
                st.info(chat['tutor'])

    # --------------------------------------------------------------------------
    # TAB 7: FORMATIVE ASSESSMENT CHECKPOINT (SECTION 1.8)
    # --------------------------------------------------------------------------
    with tab_checkpoint:
        st.subheader("1.8 Formative Assessment Checkpoint")
        st.markdown("""
        <div class="card">
        <h4>Self-Assessment Task</h4>
        Draft a 300-word executive pitch for a proposed HR analytics project in your organisation (or simulated enterprise).<br><br>
        <b>Required Criteria:</b>
        <ol>
            <li>Explicitly integrate at least two <b>Best Practice Principles</b> (e.g., Line-of-sight alignment, Evidence-based decision making).</li>
            <li>Acknowledge at least one major <b>Operational Constraint</b> (e.g., Characterisation deficits, System tools) with a clear mitigation plan.</li>
            <li>Reference your organisation's current position on the <b>HR Analytics Maturity Model</b> and how the project advances maturity.</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

        pitch_text = st.text_area("Draft your 300-word Executive Pitch here:", height=200)
        
        if st.button("Submit Pitch for Formative Review"):
            word_count = len(pitch_text.split())
            if word_count < 50:
                st.warning(f"⚠️ Submission too brief ({word_count} words). Please expand your pitch to address all required criteria.")
            else:
                st.success(f" Pitch submitted successfully ({word_count} words)! Reviewing against Section 1.8 assessment criteria...")
                
                # Check criteria
                has_principles = "alignment" in pitch_text.lower() or "evidence" in pitch_text.lower() or "governance" in pitch_text.lower()
                has_constraints = "constraint" in pitch_text.lower() or "data" in pitch_text.lower() or "system" in pitch_text.lower()
                has_maturity = "level" in pitch_text.lower() or "maturity" in pitch_text.lower()
                
                st.markdown("#### Formative Criteria Check:")
                st.write(f"• **Best Practice Principles Included:** {'✅ Yes' if has_principles else '❌ Missing explicit reference'}")
                st.write(f"• **Operational Constraints & Mitigation:** {'✅ Yes' if has_constraints else '❌ Missing explicit reference'}")
                st.write(f"• **Maturity Model Level Referenced:** {'✅ Yes' if has_maturity else '❌ Missing explicit reference'}")

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
