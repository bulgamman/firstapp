import streamlit as st
import pandas as pd
import plotly.express as px
import zipfile
import os

# 경로 설정
zip_path = "/mnt/data/archive.zip"
extract_path = "/mnt/data/extracted"
csv_file_name = "Data-Melbourne_F_fixed.csv"
csv_path = os.path.join(extract_path, csv_file_name)

# 압축 해제 (처음 실행 시만)
if not os.path.exists(csv_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# 데이터 로드
df = pd.read_csv(csv_path)

st.title("폐수 방류량 vs 생물학적 산소 요구량 (BOD)")

# 필요한 열만 추출
df = df[["Year", "Month", "Average Outflow", "Biological Oxygen Demand"]].dropna()

# 연도 및 월 필터
years = sorted(df["Year"].dropna().unique().astype(int))
selected_year = st.selectbox("연도 선택", years, index=len(years) - 1)

months = sorted(df[df["Year"] == selected_year]["Month"].dropna().unique().astype(int))
selected_month = st.selectbox("월 선택", months)

# 선택된 데이터 필터링
filtered_df = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

# Plotly 산점도
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
