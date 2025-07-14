import streamlit as st
import pandas as pd
import plotly.express as px

st.title("폐수 방류량 vs 생물학적 산소 요구량 (BOD)")

# 정확한 경로 지정
df = pd.read_csv("/mnt/data/extracted/Data-Melbourne_F_fixed.csv")

# 필요한 열만 추출
df = df[["Year", "Month", "Average Outflow", "Biological Oxygen Demand"]].dropna()

# 연/월 필터
years = sorted(df["Year"].dropna().unique().astype(int))
selected_year = st.selectbox("연도 선택", years, index=len(years) - 1)

months = sorted(df[df["Year"] == selected_year]["Month"].dropna().unique().astype(int))
selected_month = st.selectbox("월 선택", months)

# 필터링
filtered_df = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

# 산점도
fig = px.scatter(
    filtered_df,
    x="Average Outflow",
    y="Biological Oxygen Demand",
    title=f"{selected_year}년 {selected_month}월 폐수 방류량 vs BOD",
    labels={
        "Average Outflow": "평균 폐수 방류량 (ML/day)",
        "Biological Oxygen Demand": "생물학적 산소 요구량 (mg/L)"
    },
    trendline="ols",
    color_discrete_sequence=["#1f77b4"]
)

st.plotly_chart(fig, use_container_width=True)

