import openai


class LLMInsights:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_summary(self, user_query: str):
        # BASIC GUARDRAIL: Check for off-topic questions
        if not self._is_social_media_query(user_query):
            return "❌ Please ask a question related to social media analytics or the data shown on this dashboard."

        system_prompt = (
            "You are a data assistant specialized in social media analytics. "
            "You only respond to questions about engagement metrics, trends, content performance, ROI, "
            "platform-level statistics, and marketing insights based on the provided dataset. "
            "If the question is unrelated to social media data or analytics, respond with: "
            "'Please ask a question relevant to the data and social media analytics context.'"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query},
                ],
            )
            return response.choices[0].message["content"]
        except Exception as e:
            return f"⚠️ Error: {str(e)}"

    def _is_social_media_query(self, query: str) -> bool:
        """Basic keyword-based check for scope adherence."""
        keywords = [
            "engagement",
            "likes",
            "comments",
            "shares",
            "followers",
            "impressions",
            "reach",
            "campaign",
            "content",
            "platform",
            "ROI",
            "trend",
            "click-through",
            "performance",
            "reels",
            "analytics",
        ]
        return any(kw.lower() in query.lower() for kw in keywords)
