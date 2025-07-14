import streamlit as st
import pandas as pd

# 데이터
players = [
    "마이크 트라웃",
    "후안 소토",
    "브라이스 하퍼",
    "애런 저지",
    "프레디 프리먼",
    "조이 보토",
    "폴 골드슈미트",
    "무키 베츠",
    "넬슨 크루즈",
    "호세 알투베"
]

wrc_plus = [170, 154, 145, 163, 142, 144, 140, 138, 135, 132]

# DataFrame 생성
df = pd.DataFrame({
    "선수": players,
    "wRC+": wrc_plus
})

# 인덱스 설정
df.set_index("선수", inplace=True)

# 제목 및 설명
st.title("2010년 이후 MLB 최고의 타자 (wRC+ 기준)")

st.markdown("""
- **wRC+**는 타자의 공격 기여도를 나타내는 대표적인 지표입니다.
- 평균은 100, 수치가 높을수록 더 좋은 성적을 의미합니다.
""")

# 그래프 출력
st.bar_chart(df)
