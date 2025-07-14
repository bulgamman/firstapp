import streamlit as st
import pandas as pd
import plotly.express as px

# CSV 로드 (Streamlit Cloud에선 경로 확인 필요)
df = pd.read_csv("Data-Melbourne_F_fixed.csv")

st.title("폐수 방류량 vs 생물학적 산소 요구량 (BOD)")

# 필요한 열만 추출
df = df[["Year", "Month", "Average Outflow", "Biological Oxygen Demand"]].dropna()

# 날짜 필터 추가
years = sorted(df["Year"].dropna().unique().astype(int))
selected_year = st.selectbox("연도 선택", years, index=len(years)-1)

months = sorted(df[df["Year"] == selected_year]["Month"].dropna().unique().astype(int))
selected_month = st.selectbox("월 선택", months)

# 선택된 연/월에 따라 필터링
filtered_df = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

# Plotly 산점도 그리기
fig = px.scatter(
    filtered_df,
    x="Average Outflow",
    y="Biological Oxygen Demand",
    title=f"{selected_year}년 {selected_month}월 폐수 방류량 vs BOD",
    labels={
        "Average Outflow": "평균 폐수 방류량 (ML/day)",
        "Biological Oxygen Demand": "생물학적 산소 요구량 (mg/L)"
    },
    trendline="ols",  # 추세선 추가
    color_discrete_sequence=["#1f77b4"]
)

st.plotly_chart(fig, use_container_width=True)
