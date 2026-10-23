
# Strategy Report

## 1. Objective
Measure engagement, virality, audience relatability and content-performance patterns.

## 2. Dataset
This demonstration uses a synthetic dataset of 120 posts. It is not real social-media data.

## 3. Metrics
- Engagement Rate = (Likes + Shares + Saves + Comments) / Impressions
- Viral Coefficient = (2×Shares + 2×Saves + Likes) / Impressions
- Save-to-Share Ratio = Saves / Shares

The Viral Coefficient formula is a project-defined implementation because the PDF describes the weighting concept but does not specify an exact equation.

## 4. NLP
Comments are classified as Relatable or Neutral using TF-IDF and Logistic Regression.

## 5. A/B Testing
Compare two groups where applicable. Use Welch's t-test and p < 0.05.

## 6. Dashboard
Streamlit displays:
- Growth/engagement KPIs
- Topic performance
- Content type performance
- Posting time
- Hook comparison
- Save-to-share ratio
- Audience sentiment
- Top posts

## 7. Final recommendations
Fill this section after running the analysis on real data:
1. Highest-performing topic:
2. Best content format:
3. Best hook:
4. Best posting time:
5. Highest relatability:
6. Recommended strategy:
