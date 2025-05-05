import streamlit as st


class KPICards:
    def __init__(self, df):
        self.df = df

    def display(self):
        col1, col2, col3 = st.columns(3)
        total_engagement = self.df[["likes", "comments", "shares"]].sum().sum()
        engagement_rate = round(self.df["engagement_rate"].mean() * 100, 2)
        follower_change = (
            self.df["followers_at_time"].iloc[-1] - self.df["followers_at_time"].iloc[0]
        )

        col1.metric("Total Engagement", f"{total_engagement:,}")
        col2.metric("Engagement Rate (%)", f"{engagement_rate}%")
        col3.metric("Followers Growth", f"{follower_change:,}")
