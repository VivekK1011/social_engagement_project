import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

DATA_FILE = "social_media_data.csv"
df = pd.read_csv(DATA_FILE)

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df = df.drop_duplicates()
numeric_cols = ["Impressions","Likes","Shares","Saves","Comments_Count","Retention_Rate"]
for c in numeric_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

df["Engagement_Rate"] = (
    df["Likes"] + df["Shares"] + df["Saves"] + df["Comments_Count"]
) / df["Impressions"]

df["Viral_Coefficient"] = (
    2*df["Shares"] + 2*df["Saves"] + df["Likes"]
) / df["Impressions"]

df["Save_to_Share_Ratio"] = np.where(
    df["Shares"] > 0, df["Saves"] / df["Shares"], 0
)

df["Eligible"] = np.where(
    (df["Engagement_Rate"] >= 0.10) &
    (df["Viral_Coefficient"] >= 0.08) &
    (df["Retention_Rate"] >= 0.60),
    "Eligible", "Not Eligible"
)

df.to_csv("processed_social_media_data.csv", index=False)

print("\nTOP TOPICS")
print(df.groupby("Topic")[["Engagement_Rate","Viral_Coefficient","Retention_Rate"]]
      .mean().sort_values("Viral_Coefficient", ascending=False))

print("\nTOP CONTENT TYPES")
print(df.groupby("Content_Type")["Engagement_Rate"].mean().sort_values(ascending=False))

print("\nTOP POSTING TIMES")
print(df.groupby("Posting_Time")["Engagement_Rate"].mean().sort_values(ascending=False))

def ab_test(column, metric="Engagement_Rate"):
    groups = df[column].dropna().unique()
    if len(groups) != 2:
        print(f"\n{column}: A/B test skipped; exactly two groups required.")
        return
    a = df.loc[df[column] == groups[0], metric]
    b = df.loc[df[column] == groups[1], metric]
    stat, p = ttest_ind(a, b, equal_var=False)
    print(f"\nA/B TEST: {column}")
    print(f"{groups[0]} mean = {a.mean():.4f}")
    print(f"{groups[1]} mean = {b.mean():.4f}")
    print(f"p-value = {p:.4f}")
    print("Statistically significant" if p < 0.05 else "Not statistically significant")

ab_test("Hook_Type")
ab_test("Content_Type")  # may be skipped because there are 3 groups

print("\nBest single post:")
print(df.sort_values("Viral_Coefficient", ascending=False).head(5)[
    ["Post_ID","Topic","Viral_Coefficient","Engagement_Rate","Retention_Rate"]
])
