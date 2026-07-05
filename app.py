import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)


# ==================================================
# CUSTOM STYLE INSIDE PYTHON ONLY
# ==================================================
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fb;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .hero-box {
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            padding: 30px;
            border-radius: 22px;
            color: white;
            margin-bottom: 25px;
            box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
        }

        .hero-title {
            font-size: 36px;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .hero-subtitle {
            font-size: 17px;
            color: #e8eefc;
        }

        .metric-card {
            background: white;
            padding: 22px;
            border-radius: 18px;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
            border-left: 6px solid #2a5298;
        }

        .metric-label {
            color: #6b7280;
            font-size: 15px;
            font-weight: 600;
        }

        .metric-value {
            color: #111827;
            font-size: 30px;
            font-weight: 800;
            margin-top: 5px;
        }

        .section-card {
            background: white;
            padding: 24px;
            border-radius: 20px;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.07);
            margin-bottom: 20px;
        }

        .insight-good {
            background: #ecfdf5;
            color: #065f46;
            padding: 16px;
            border-radius: 14px;
            border-left: 5px solid #10b981;
            margin-bottom: 12px;
            font-weight: 600;
        }

        .insight-info {
            background: #eff6ff;
            color: #1e40af;
            padding: 16px;
            border-radius: 14px;
            border-left: 5px solid #3b82f6;
            margin-bottom: 12px;
            font-weight: 600;
        }

        .insight-warning {
            background: #fffbeb;
            color: #92400e;
            padding: 16px;
            border-radius: 14px;
            border-left: 5px solid #f59e0b;
            margin-bottom: 12px;
            font-weight: 600;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111827, #1f2937);
        }

        [data-testid="stSidebar"] * {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# LOAD DATA
# ==================================================
DATA_PATH = Path("StudentPerformanceFactors.csv")


@st.cache_data
def load_data(path):
    return pd.read_csv(path)


if not DATA_PATH.exists():
    st.error("Dataset not found. Keep `StudentPerformanceFactors.csv` in the same folder as `app.py`.")
    st.stop()


df = load_data(DATA_PATH)


# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("📊 Dashboard")
st.sidebar.markdown("Student Performance Analysis")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📁 Dataset Overview",
        "📈 EDA Charts",
        "💡 Insights"
    ]
)


# ==================================================
# HELPER FUNCTIONS
# ==================================================
def metric_card(label, value):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def hero_section(title, subtitle):
    st.markdown(
        f"""
        <div class="hero-box">
            <div class="hero-title">{title}</div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# HOME PAGE
# ==================================================
if page == "🏠 Home":
    hero_section(
        "Student Performance Analysis Dashboard",
        "A clean data analytics dashboard to explore student performance factors and understand what affects exam scores."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        metric_card("Total Students", df.shape[0])

    with col2:
        metric_card("Total Columns", df.shape[1])

    with col3:
        metric_card("Target Variable", "Exam Score")

    with col4:
        metric_card("Best Model R²", "0.825")

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("Project Summary")
    st.write(
        """
        This project analyzes student performance data to identify the most important factors
        affecting exam scores.

        The dashboard focuses on:

        - Dataset overview
        - Missing value analysis
        - Score distribution
        - Feature relationship analysis
        - Correlation study
        - Final business insights
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)


# ==================================================
# DATASET OVERVIEW PAGE
# ==================================================
elif page == "📁 Dataset Overview":
    hero_section(
        "Dataset Overview",
        "Understand dataset structure, columns, missing values, and statistical summary."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metric_card("Rows", df.shape[0])

    with col2:
        metric_card("Columns", df.shape[1])

    with col3:
        missing_count = df.isnull().sum().sum()
        metric_card("Missing Values", missing_count)

    st.subheader("Column Names")
    column_df = pd.DataFrame(df.columns, columns=["Column Name"])
    st.dataframe(column_df, use_container_width=True)

    st.subheader("Missing Values")
    missing_df = df.isnull().sum().reset_index()
    missing_df.columns = ["Column", "Missing Values"]
    st.dataframe(missing_df, use_container_width=True)

    st.subheader("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)


# ==================================================
# EDA PAGE
# ==================================================
elif page == "📈 EDA Charts":
    hero_section(
        "Exploratory Data Analysis",
        "Visual analysis of student scores, attendance, study hours, and correlations."
    )

    required_cols = ["Exam_Score", "Attendance", "Hours_Studied"]
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        st.error(f"Missing required columns: {missing_cols}")
        st.stop()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Exam Score Distribution")
        fig = px.histogram(
            df,
            x="Exam_Score",
            nbins=30,
            marginal="box",
            title="Distribution of Exam Scores"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Attendance vs Exam Score")
        fig = px.scatter(
            df,
            x="Attendance",
            y="Exam_Score",
            title="Attendance vs Exam Score",
            trendline="ols"
        )
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Hours Studied vs Exam Score")
        fig = px.scatter(
            df,
            x="Hours_Studied",
            y="Exam_Score",
            title="Hours Studied vs Exam Score",
            trendline="ols"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.subheader("Correlation Heatmap")
        numeric_df = df.select_dtypes(include=["int64", "float64"])

        if numeric_df.empty:
            st.warning("No numeric columns found for heatmap.")
        else:
            corr = numeric_df.corr()
            fig = px.imshow(
                corr,
                text_auto=True,
                title="Correlation Heatmap",
                aspect="auto"
            )
            st.plotly_chart(fig, use_container_width=True)


# ==================================================
# INSIGHTS PAGE
# ==================================================
elif page == "💡 Insights":
    hero_section(
        "Key Insights",
        "Final observations based on exploratory analysis and machine learning results."
    )

    st.markdown(
        """
        <div class="insight-good">
            Attendance is the strongest predictor of student exam score.
        </div>

        <div class="insight-good">
            Hours studied is the second strongest factor affecting exam performance.
        </div>

        <div class="insight-info">
            Previous scores and tutoring sessions show moderate impact on final exam score.
        </div>

        <div class="insight-warning">
            Sleep hours and physical activity show weak relationship with exam score.
        </div>

        <div class="insight-info">
            Gender has almost no visible effect on student exam score in this dataset.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Final Conclusion")

    st.write(
        """
        Linear Regression performed best with an **R² score of 0.825**.

        This means the dataset mostly follows linear patterns. Attendance, study hours,
        and previous academic performance are the most useful indicators for predicting
        student exam performance.

        From an educational perspective, improving attendance and encouraging consistent
        study hours can directly support better academic outcomes.
        """
    )