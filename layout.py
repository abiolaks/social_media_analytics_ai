from filters import Filters
from kpis import KPICards
from charts import Charts
from insights import LLMInsights, PROMPT_TEMPLATES
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
        query = st.text_input(
            "Ask a question about the data:",
            value="Summarize this week's campaign performance.",
        )
        prompt_type = st.selectbox(
            "Select Insight Type", options=["summary", "diagnosis", "recommendation"]
        )

        if st.button("🔍 Ask LLM"):
            try:
                api_key = st.secrets["OPENAI_API_KEY"]
                llm = LLMInsights(api_key)

                prompt_template = PROMPT_TEMPLATES[prompt_type]
                insight_prompt = prompt_template.format(
                    engagement=filtered_df["engagement"].sum(),
                    engagement_rate=filtered_df["engagement_rate"].mean(),
                    platform=filtered_df["platform"].value_counts().idxmax(),
                    content_type=filtered_df["content_type"].value_counts().idxmax(),
                    start_date=filtered_df["date_posted"].min().date(),
                    end_date=filtered_df["date_posted"].max().date(),
                    query=query,
                )

                summary = llm.get_summary(insight_prompt)
                st.success(summary)

                with st.expander("🔍 Show Generated Prompt"):
                    st.code(insight_prompt, language="markdown")

            except KeyError:
                st.error("❌ OPENAI_API_KEY is missing from your secrets.toml.")
            except Exception as e:
                st.error(f"⚠️ An error occurred while generating insight: {str(e)}")
