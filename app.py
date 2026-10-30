
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Pakistani Social Media Detective",
    page_icon="📊",
    layout="wide"
)

st.title("🇵🇰 Pakistani Social Media Content Detective")
st.write("Analyze social media engagement across platforms.")

# Load dataset
df = pd.read_csv("dataset/social_media_data.csv")

# Calculate engagement
df["engagement"] = df["likes"] + df["comments"] + df["shares"]

# Sidebar
st.sidebar.header("Filters")

platforms = st.sidebar.multiselect(
    "Select Platform",
    df["platform"].unique(),
    default=df["platform"].unique()
)

filtered_df = df[df["platform"].isin(platforms)]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Posts", len(filtered_df))
col2.metric("Total Likes", int(filtered_df["likes"].sum()))
col3.metric("Total Engagement", int(filtered_df["engagement"].sum()))

st.divider()

# Platform chart
st.subheader("Engagement by Platform")

platform_data = filtered_df.groupby("platform")["engagement"].sum().reset_index()

fig1 = px.bar(
    platform_data,
    x="platform",
    y="engagement",
    color="platform",
    title="Total Engagement by Platform"
)

st.plotly_chart(fig1, use_container_width=True)

# Content type chart
st.subheader("Content Type Performance")

content_data = filtered_df.groupby("content_type")["engagement"].sum().reset_index()

fig2 = px.pie(
    content_data,
    names="content_type",
    values="engagement",
    title="Engagement by Content Type"
)

st.plotly_chart(fig2, use_container_width=True)

# Dataset
st.subheader("Social Media Dataset")
st.dataframe(filtered_df, use_container_width=True)

st.caption("Note: This is a small synthetic sample dataset, not real Pakistani social media data.")