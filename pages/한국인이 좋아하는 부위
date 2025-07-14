import streamlit as st
import plotly.graph_objects as go

# 데이터
parts = ["삼겹살", "목살", "앞다리살", "갈비", "등심"]
consumption = [35, 25, 15, 13, 12]  # 단위: %

# 웹앱 제목
st.title("한국인이 가장 많이 소비하는 돼지고기 부위 TOP 5")

# plotly 막대그래프 생성
fig = go.Figure(data=[
    go.Bar(x=parts, y=consumption, marker_color='salmon')
])

# 그래프 레이아웃 설정
fig.update_layout(
    title="부위별 소비 비율 (%)",
    xaxis_title="부위",
    yaxis_title="소비율 (%)",
    yaxis=dict(range=[0, 40]),
    template="simple_white"
)

# 그래프 출력
st.plotly_chart(fig)
