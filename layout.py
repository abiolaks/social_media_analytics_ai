from filters import Filters
from kpis import KPICards
from charts import Charts
from insights import LLMInsights
import streamlit as st


class DashboardLayout:
    def __init__(self, df):
        self.df = df

    def render(self):
        # Apply filters
        filters = Filters(self.df)
        filtered_df = filters.apply_filters()

        # Display KPIs
        st.subheader("🔹 Executive Summary")
        KPICards(filtered_df).display()

        # Show Charts
        st.subheader("📊 Engagement Trends")
        Charts(filtered_df).show_engagement_over_time()
        Charts(filtered_df).show_engagement_by_type()
        st.subheader("🔥 Top Posts")
        Charts(filtered_df).show_top_posts()

        # Add LLM Insights
        st.subheader("🧠 AI-Powered Insight")
        if st.button("🔍 Generate Summary"):
            api_key = st.secrets.get(
                "OPENAI_API_KEY", "sk-..."
            )  # Or replace with your real key
            llm = LLMInsights(api_key)
            summary = llm.get_summary(
                f"Summarize this data:\n{filtered_df.head(50).to_string()}"
            )
            st.success(summary)
