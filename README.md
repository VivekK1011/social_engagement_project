
# Data-Driven Social Engagement Initiative

## Project objective
Build a data science ecosystem that measures engagement, virality, relatability and content performance.

## Important note
The PDF specifies the project modules and deliverables but does not provide an actual social-media dataset or a required mathematical formula for the Viral Coefficient. Therefore, this package uses a clearly marked SYNTHETIC dataset and a project-defined Viral Coefficient formula for demonstration:
    (2*Shares + 2*Saves + Likes) / Impressions

Replace the synthetic CSV with real API/scraped data for a real deployment.

## Folder
- social_media_data.csv       raw synthetic dataset
- analysis.py                 cleaning + metrics + A/B testing
- nlp_model.py                TF-IDF + Logistic Regression
- app.py                      Streamlit dashboard
- social_engagement_analysis.xlsx  Excel data + formulas
- requirements.txt
- processed_social_media_data.csv  created by analysis.py
- sentiment_results.csv            created by nlp_model.py
- relatability_model.joblib        created by nlp_model.py

## Run
1. Install Python 3.10+.
2. Open terminal in this folder.
3. `pip install -r requirements.txt`
4. `python analysis.py`
5. `python nlp_model.py`
6. `streamlit run app.py`

## Excel
Open `social_engagement_analysis.xlsx`. The Data sheet contains formulas for:
- Engagement Rate
- Viral Coefficient
- Save-to-Share Ratio
- Eligibility
- Grade


