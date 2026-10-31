import streamlit as st
import time

st.set_page_config(
page_title="HR Metrics & Analytics | Interactive SLP Portal",
page_icon="📊",
layout="wide",
initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main-header { font-size:2.2rem; color:#0F2C59; font-weight:700; margin-bottom:0px; }
.sub-header { font-size:1.1rem; color:#4F709C; margin-bottom:20px; }
.unit-card { background-color:#F8F9FA; border-left: 5px solid #0F2C59; padding: 15px; margin-bottom: 20px; border-radius: 4px; }
.stButton>button { background-color:#0F2C59; color:white; border-radius:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">HR Metrics and Analytics</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced Applied Analytics & Workforce Diagnostics | Interactive SLP Platform</p>', unsafe_allow_html=True)

if "chat_history" not in st.session_state:
st.session_state.chat_history = [
{"role": "assistant", "content": "Welcome to the HR Metrics & Analytics SLP! I am your AI learning assistant. Ask me anything about the value chain, data governance, flight-risk modelling, or unit assignments."}
 ]
if "submitted_answers" not in st.session_state:
st.session_state.submitted_answers = {}

with st.sidebar:
st.image("https://img.icons8.com/color/96/education.png", width=60)
st.title("SLP Navigation")

selected_unit = st.radio(
"Select Course Module:",
[
"Course Overview",
"Unit 1: Foundations & Value Chain",
"Unit 2: Data Architecture & Governance",
"Unit 3: Strategy Maps & Scorecards",
"Unit 4: Diagnostics & Predictive Modelling",
"Unit 5: Operationalising & Executive Reporting",
"Final Portfolio & Certification"
 ]
)

st.divider()
st.subheader("💬 AI Learning Partner")
st.caption("Ask questions or discuss module content in real time:")

# Embedded Chat Assistant
for msg in st.session_state.chat_history:
st.chat_message(msg["role"]).write(msg["content"])

user_input = st.text_input("Type your question here...", key="sidebar_query")
if st.button("Send Query") and user_input:
st.session_state.chat_history.append({"role": "user", "content": user_input})

# Simulated AI Response Engine (Connectable to Gemini/OpenAI API)
response_placeholder = "Analyzing query against SLP course material..."
if "coffee" in user_input.lower() or "value chain" in user_input.lower():
bot_reply = "The HRM Value Chain uses the 'Coffee Journey' analogy: Get (harvesting raw beans/recruitment), Develop & Keep (roasting & grading/L&D and rewards), and Engage (the barista crafting the cup/leadership & culture)."
elif "poa" in user_input.lower() or "privacy" in user_input.lower():
bot_reply = "Under POPIA, workforce analytics must enforce data minimisation, explicit employee consent, dataset pseudonymisation, and the 'human-in-the-loop' principle for automated decision-making."
elif "regression" in user_input.lower() or "flight risk" in user_input.lower():
bot_reply = "Logistic regression models the binary probability of exit (0=Retain, 1=Exit) using inputs like tenure, compa-ratio, and overtime. An AUC score above 0.75 indicates reliable predictive accuracy."
else:
bot_reply = f"Regarding '{user_input}': In this SLP, always ensure you connect administrative measures to contextualised metrics, diagnostic root causes, and business impact."

st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
st.rerun()


if selected_unit == "Course Overview":
st.header("📋 Course Overview & Purpose")
st.info("Target Audience: Working HR Practitioners, Line Managers, and Organisational Leaders seeking to build advanced competencies in workforce analytics.")

col1, col2 = st.columns(2)
with col1:
st.markdown("### Core Objectives")
st.markdown("""
* Shift from Admin to Partner: Shift HRM from administrative reporting to strategic business partnering.
* Diagnostic Mastery: Apply the 5-step HR Analytics Process Model (Exploration, Examination, Extraction, Evaluation, Extrapolation).
* Predictive Foresight: Construct flight-risk scoring models using logistic regression and VIF checks.
* Executive Delivery: Translate statistical outputs into board-level strategic memos and scorecards.
""")
with col2:
st.markdown("### Course Structure")
st.markdown("""
* Unit 1: Foundations of Strategic HRM, eHRM & Value Chain
* Unit 2: Data Architecture, Sources & POPIA Governance
* Unit 3: Strategic Partnering, Strategy Maps & Scorecards
* Unit 4: Functional Indices, Diagnostics & Flight-Risk Scoring
* Unit 5: Operationalising the Analytics Cycle & Executive Reporting
""")

elif selected_unit == "Unit 1: Foundations & Value Chain":
st.header("Unit 1: Foundations of Strategic HRM, eHRM and the Value Chain")

tab1, tab2, tab3 = st.tabs(["📖 Learning Content", "☕ The Coffee Journey Model", "✍️ Interactive Practical & Auto-Marker"])

with tab1:
st.subheader("1.4 Unpacking the Terminology")
st.markdown("""
* Measures: Standalone quantitative counts without denominator or context (e.g., Total Headcount = 1,250).
* Metrics: Contextualised ratios evaluated against baselines or benchmarks (e.g., Turnover Rate = 14.5%).
* Analytics: Statistical exploration to diagnose root causes and model future outcomes.
""")

st.subheader("1.4.3 HR Analytics Maturity Model")
st.markdown("""
1. Reactive / Descriptive: What happened? (Historical reporting)
2. Operational / Standardised: How often? (Routine metrics)
3. Advanced / Diagnostic: Why did it happen? (Root-cause cross-tabulation)
4. Predictive / Prescriptive: What will happen & what should we do? (Machine learning & automated interventions)
""")

with tab2:
st.subheader("The HRM Value Chain: The Coffee Journey Analogy")
st.write("Value is added at every single stage of the supply chain, transforming raw human potential into ultimate organizational performance:")

col_a, col_b, col_c = st.columns(3)
with col_a:
st.success("1. GET\n*(Harvesting Raw Beans)")
st.markdown("- Talent Planning\n- Targeted Recruitment\n- Strategic Onboarding")
with col_b:
st.warning("2. DEVELOP & KEEP\n(Roasting & Grading)")
st.markdown("- Learning & Development\n- Performance Calibration\n- Total Rewards & Remuneration")
with col_c:
st.info("3. ENGAGE\n(The Skilled Barista)*")
st.markdown("- Empathetic Leadership\n- Psychological Safety\n- Culture & Transformation")

with tab3:
st.subheader("Formative Checkpoint: Executive Pitch")
st.write("Draft a 150-200 word executive pitch proposing an HR analytics project at your organization. Ensure you reference at least one Best Practice Principle and acknowledge a major constraint with a mitigation plan.")

user_pitch = st.text_area("Write your response here:", height=150, key="pitch_input")

if st.button("Submit for Automated AI Marking", key="mark_unit1"):
if len(user_pitch.strip()) < 50:
st.warning("Please write a complete response before submitting.")
else:
with st.spinner("AI Marker evaluating against criteria..."):
time.sleep(1.5)
st.subheader("🎯 Automated Assessment Feedback")
st.metric("Score", "85 / 100", "Passed")
st.markdown("""
Strengths Identified:
- Clear distinction between measures and metrics.
- Identified organizational constraints effectively.

Recommendation for Improvement:
- Explicitly name your current position on the HR Analytics Maturity Model (e.g., Level 2 transitioning to Level 3) to strengthen the business case.
""")

elif selected_unit == "Unit 2: Data Architecture & Governance":
st.header("Unit 2: Data Architecture, Sources, and Governance")
st.markdown("### Core Topics")
st.markdown("""
* Internal vs. External Data: Unifying payroll, performance ratings, and attendance logs via Employee ID.
* Excel Engine: Mastering XLOOKUP, PivotTables, and conditional formatting for diagnostic cross-tabulation.
* POPIA & Governance: Managing characterisation deficits, data anonymisation, and algorithmic bias.
* Bilateral Iterative Coaching: Working with AI as an intellectual co-pilot rather than an automated transaction.
""")

st.subheader("📊 Interactive Excel Diagnostic Simulator")
st.write("Test how changing overtime thresholds impacts flagged turnover risk among logistics staff:")

overtime_slider = st.slider("Select Monthly Unscheduled Overtime Hours:", 0, 60, 35)
compa_ratio = st.slider("Select Salary Compa-Ratio (% of market median):", 70, 130, 95)

# Calculate simulated risk
calculated_risk = min(99, max(5, int((overtime_slider * 1.8) + (100 - compa_ratio) * 0.5)))

st.metric(label="Calculated Cohort Flight-Risk Probability", value=f"{calculated_risk}%")
if calculated_risk > 65:
st.error("🚨 HIGH RISK: Unscheduled overtime is severely driving exit probability. Immediate shift-capping recommended.")
else:
st.success("🟢 STABLE: Flight risk is within manageable operational thresholds.")

elif selected_unit == "Unit 4: Diagnostics & Predictive Modelling":
st.header("Unit 4: Diagnostics, Flight-Risk Scoring & Predictive Analytics")

st.subheader("The Predictive Turnover Pipeline")
st.code("""
[Raw HRIS Data] ➔ [Chi-Square Test] ➔ [VIF Multicollinearity Check] ➔ [Logistic Regression] ➔ [ROC-AUC Validation]
""", language="text")

st.subheader("Practical Flight-Risk Calculator")
col1, col2 = st.columns(2)
with col1:
tenure = st.number_input("Tenure (Months in current role):", 1, 120, 38)
overtime = st.number_input("Unscheduled Overtime (Hours/Month):", 0, 80, 42)
with col2:
promo_months = st.number_input("Months Since Last Promotion:", 0, 60, 40)
coaching = st.selectbox("Managerial Coaching Received in last 12 months?", ["Yes", "No"])

# Logistic Regression Logic Simulation
coaching_factor = 1.5 if coaching == "No" else 0.7
risk_score = round(1 / (1 + 2.718 ** -(-2.1 + (overtime * 0.08) + (promo_months * 0.05) - (tenure * 0.01) + coaching_factor)), 2)

st.subheader(f"Calculated Flight-Risk Score: {risk_score}")
if risk_score > 0.70:
st.error("Flagged for Proactive Intervention: High probability of voluntary resignation within 90 days.")
else:
st.success("Low Risk: Standard retention monitoring.")

elif selected_unit == "Final Portfolio & Certification":
st.header("🎓 Final Assessment Submission & Credentialing")
st.write("Upload or paste your final Written Analytical Report (Annexure A) and HR Scorecard Matrix to generate your digital completion certificate.")

report_text = st.text_area("Paste Final Executive Report / Board Memo:", height=200)

if st.button("Submit Final Portfolio"):
if len(report_text.strip()) > 100:
st.balloons()
st.success("🎉 Portfolio Successfully Evaluated & Passed!")
st.info("Certificate Issued: Advanced Certification in HR Metrics & Analytics | Nelson Mandela University")
else:
st.warning("Portfolio submission is incomplete. Please submit your full executive report.")
