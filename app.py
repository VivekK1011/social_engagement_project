import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Social Engagement Analytics", layout="wide")
st.title("Data-Driven Social Engagement Dashboard")
st.caption("Analytics dashboard for growth, virality, sentiment and content performance.")

DATA = "processed_social_media_data.csv"
RAW = "social_media_data.csv"

if not os.path.exists(DATA):
    st.warning("Run analysis.py first to create processed_social_media_data.csv.")
    st.stop()

df = pd.read_csv(DATA)

if os.path.exists("sentiment_results.csv"):
    sent = pd.read_csv("sentiment_results.csv")
else:
    sent = pd.DataFrame()

st.sidebar.header("Filters")
topics = ["All"] + sorted(df["Topic"].dropna().unique().tolist())
selected_topic = st.sidebar.selectbox("Topic", topics)

if selected_topic != "All":
    view = df[df["Topic"] == selected_topic].copy()
else:
    view = df.copy()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Posts", len(view))
c2.metric("Avg Engagement", f"{view['Engagement_Rate'].mean()*100:.2f}%")
c3.metric("Avg Viral Coefficient", f"{view['Viral_Coefficient'].mean():.4f}")
c4.metric("Avg Retention", f"{view['Retention_Rate'].mean()*100:.2f}%")

st.subheader("Topic Performance")
topic_summary = (view.groupby("Topic")[["Engagement_Rate","Viral_Coefficient","Retention_Rate"]]
                 .mean().sort_values("Viral_Coefficient", ascending=False))
st.bar_chart(topic_summary)

st.subheader("Content Type")
content_summary = view.groupby("Content_Type")["Engagement_Rate"].mean().sort_values(ascending=False)
st.bar_chart(content_summary)

st.subheader("Posting Time")
time_summary = view.groupby("Posting_Time")["Engagement_Rate"].mean().sort_values(ascending=False)
st.bar_chart(time_summary)

st.subheader("Hook A/B Comparison")
hook_summary = view.groupby("Hook_Type")["Engagement_Rate"].mean().sort_values(ascending=False)
st.bar_chart(hook_summary)

st.subheader("Save-to-Share Ratio")
ratio_summary = view.groupby("Topic")["Save_to_Share_Ratio"].mean().sort_values(ascending=False)
st.bar_chart(ratio_summary)

if not sent.empty:
    st.subheader("Audience Sentiment")
    sentiment_summary = sent["Predicted_Label"].value_counts()
    st.bar_chart(sentiment_summary)

st.subheader("Top Performing Posts")
top = view.sort_values("Viral_Coefficient", ascending=False).head(10)
st.dataframe(top[
    ["Post_ID","Date","Topic","Content_Type","Hook_Type",
     "Engagement_Rate","Viral_Coefficient","Save_to_Share_Ratio","Retention_Rate"]
], use_container_width=True)

st.subheader("Recommendation")
if len(view):
    best_topic = view.groupby("Topic")["Viral_Coefficient"].mean().idxmax()
    best_time = view.groupby("Posting_Time")["Engagement_Rate"].mean().idxmax()
    best_content = view.groupby("Content_Type")["Engagement_Rate"].mean().idxmax()
    best_hook = view.groupby("Hook_Type")["Engagement_Rate"].mean().idxmax()
    st.write(
        f"Based on the selected data, prioritize **{best_topic}** topics, "
        f"post mainly during **{best_time}**, use **{best_content}** content, "
        f"and test **{best_hook}** hooks."
    )
