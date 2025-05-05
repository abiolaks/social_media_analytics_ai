import streamlit as st


class Filters:
    def __init__(self, df):
        self.df = df

    def apply_filters(self):
        platforms = self.df["platform"].unique()
        selected_platform = st.sidebar.selectbox("Select Platform", platforms)

        min_date = self.df["date_posted"].min()
        max_date = self.df["date_posted"].max()
        date_range = st.sidebar.date_input("Date Range", [min_date, max_date])

        return self.df[
            (self.df["platform"] == selected_platform)
            & (self.df["date_posted"] >= date_range[0])
            & (self.df["date_posted"] <= date_range[1])
        ]
