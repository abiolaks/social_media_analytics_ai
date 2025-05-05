import plotly.express as px
import streamlit as st


class Charts:
    def __init__(self, df):
        self.df = df

    def show_engagement_over_time(self):
        fig = px.line(self.df, x="date_posted", y="likes", title="Likes Over Time")
        st.plotly_chart(fig)

    def show_engagement_by_type(self):
        chart_df = (
            self.df.groupby("content_type")[["likes", "comments", "shares"]]
            .sum()
            .reset_index()
        )
        fig = px.bar(
            chart_df,
            x="content_type",
            y=["likes", "comments", "shares"],
            barmode="group",
            title="Engagement by Content Type",
        )
        st.plotly_chart(fig)

    def show_top_posts(self):
        top_posts = self.df.sort_values(
            by=["likes", "comments", "shares"], ascending=False
        ).head(5)
        st.dataframe(
            top_posts[
                [
                    "post_id",
                    "content_type",
                    "likes",
                    "comments",
                    "shares",
                    "engagement_rate",
                ]
            ]
        )
