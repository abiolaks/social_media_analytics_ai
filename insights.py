import openai
import streamlit as st

PROMPT_TEMPLATES = {
    "summary": """
You are a social media analytics assistant.
Summarize the following performance metrics from {start_date} to {end_date}:

- Total Engagement: {engagement}
- Avg Engagement Rate: {engagement_rate:.2%}
- Top Platform: {platform}
- Top Content Type: {content_type}

Question: {query}

Only respond with insights relevant to social media analytics.
""",
    "diagnosis": """
You are a data analyst specializing in social media metrics.
Analyze the following data from {start_date} to {end_date} and explain any drops or inconsistencies in engagement:

- Total Engagement: {engagement}
- Avg Engagement Rate: {engagement_rate:.2%}
- Top Platform: {platform}
- Top Content Type: {content_type}

User's Question: {query}

If no drop is detected, respond with a performance stability comment. Keep the response focused on platform or content causes.
""",
    "recommendation": """
You are a digital strategist AI assistant.
Based on the performance from {start_date} to {end_date}, suggest actionable ways to improve engagement and content performance.

Here are the data points:
- Total Engagement: {engagement}
- Avg Engagement Rate: {engagement_rate:.2%}
- Top Platform: {platform}
- Top Content Type: {content_type}

User's Request: {query}

Provide practical social media strategy tips based on the data.
""",
}


class LLMInsights:
    def __init__(self, api_key):
        """Initialize the LLM with the provided API key."""
        self.api_key = st.secrets["OPENAI_API_KEY"]
        openai.api_key = self.api_key

    def get_summary(self, user_query: str) -> str:
        if not self._is_social_media_query(user_query):
            return "❌ Please ask a question relevant to social media analytics or the data provided."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a social media analytics assistant. Only respond with insights about trends, performance, "
                        "campaign impact, engagement metrics, ROI, or content effectiveness based on the provided prompt."
                    ),
                },
                {"role": "user", "content": user_query},
            ],
        )
        return response.choices[0].message["content"]

    def _is_social_media_query(self, query: str) -> bool:
        keywords = [
            "engagement",
            "likes",
            "comments",
            "shares",
            "followers",
            "impressions",
            "reach",
            "platform",
            "campaign",
            "trend",
            "ROI",
            "click",
            "performance",
            "analytics",
            "content",
        ]
        return any(kw in query.lower() for kw in keywords)
