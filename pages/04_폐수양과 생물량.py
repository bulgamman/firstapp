import streamlit as st
import pandas as pd
import zipfile
import os
import plotly.express as px
import tempfile

st.title("폐수 방류량 vs 생물학적 산소 요구량 (BOD)")

# 파일 업로더
uploaded_file = st.file_uploader("📦 압축된 ZIP 파일 업로드 (예: archive.zip)", type="zip")

# 파일이 업로드된 경우에만 실행
if uploaded_file is not None:
    with tempfile.TemporaryDirectory() as tmpdir:
        try:
            # zip 파일 저장
            zip_path = os.path.join(tmpdir, "uploaded.zip")
            with open(zip_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # zip 파일 열기
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(tmpdir)

            # 압축 해제 후 CSV 파일 찾기
            target_csv = "Data-Melbourne_F_fixed.csv"
            csv_path = os.path.join(tmpdir, target_csv)

            if not os.path.exists(csv_path):
                st.error(f"❌ 압축 파일 안에 `{target_csv}` 파일이 없습니다.")
            else:
                # 데이터 불러오기
                df = pd.read_csv(csv_path)
                df = df[["Year", "Month", "Average Outflow", "Biological Oxygen Demand"]].dropna()

                # 필터 선택
                years = sorted(df["Year"].unique().astype(int))
                selected_year = st.selectbox("연도 선택", years, index=len(years)-1)

                months = sorted(df[df["Year"] == selected_year]["Month"].unique().astype(int))
                selected_month = st.selectbox("월 선택", months)

                # 필터링
                filtered_df = df[(df["Year"] == selected_year) & (df["Month"] == selected_month)]

                # 시각화
                fig = px.scatter(
                    filtered_df,
                    x="Average Outflow",
                    y="Biological Oxygen Demand",
                    title=f"{selected_year}년 {selected_month}월 폐수 방류량 vs BOD",
                    labels={
                        "Average Outflow": "평균 폐수 방류량 (ML/day)",
                        "Biological Oxygen Demand": "생물학적 산소 요구량 (mg/L)"
                    },
                    trendline="ols"
                )

                st.plotly_chart(fig, use_container_width=True)

        except zipfile.BadZipFile:
            st.error("❌ 유효하지 않은 ZIP 파일입니다.")
else:
    st.info("⬆️ 분석할 ZIP 파일을 먼저 업로드해주세요.")
