import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Data Analysis Dashboard",
    layout="wide"
)

# Title
st.title("📊 Data Analysis Internship Project")
st.write("Interactive Data Analytics Dashboard using Streamlit")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    # Read data
    df = pd.read_csv(uploaded_file)

    # Dataset preview
    st.subheader("📋 Dataset Preview")
    st.dataframe(df)

    # Dataset information
    st.subheader("📌 Dataset Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Total Columns",
            df.shape[1]
        )

    with col3:
        st.metric(
            "Missing Values",
            df.isnull().sum().sum()
        )

    # Summary statistics
    st.subheader("📈 Statistical Summary")
    st.write(df.describe())

    # Missing values chart
    st.subheader("🔍 Missing Values Analysis")

    missing = df.isnull().sum()

    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    fig = px.bar(
        missing_df,
        x="Column",
        y="Missing Values",
        title="Missing Values by Column"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Numeric columns visualization
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) > 0:

        st.subheader("📊 Data Visualization")

        selected_column = st.selectbox(
            "Select Column",
            numeric_columns
        )

        chart = px.histogram(
            df,
            x=selected_column,
            title=f"Distribution of {selected_column}"
        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )

else:
    st.info("👆 Please upload a CSV file to start analysis")
