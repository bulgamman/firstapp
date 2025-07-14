import streamlit as st
import folium
from streamlit_folium import st_folium

# Streamlit 제목
st.title("대륙별 멸종위기종 분포 (상댓값 기준)")

st.markdown("""
- 데이터는 대륙별 멸종위기 동물의 **종 수(예시)**를 기준으로 색상 시각화됩니다.
- 색상이 진할수록 상대적으로 더 많은 멸종위기종이 존재함을 나타냅니다.
""")

# 대륙별 위치 및 멸종위기종 수 (예시)
continent_data = [
    {"name": "아시아", "lat": 34.0479, "lon": 100.6197, "count": 3500},
    {"name": "아프리카", "lat": 1.6508, "lon": 17.6791, "count": 2700},
    {"name": "남아메리카", "lat": -8.7832, "lon": -55.4915, "count": 2200},
    {"name": "북아메리카", "lat": 54.5260, "lon": -105.2551, "count": 1900},
    {"name": "유럽", "lat": 54.5260, "lon": 15.2551, "count": 1200},
    {"name": "오세아니아", "lat": -22.7359, "lon": 140.0188, "count": 1100},
    {"name": "남극", "lat": -82.8628, "lon": 135.0000, "count": 200},
]

# 최댓값 기준 정규화 (0~1로)
max_count = max([c["count"] for c in continent_data])

# 색상 생성 함수 (진한 빨강일수록 위기종이 많음)
def get_color(value):
    ratio = value / max_count
    red = int(255 * ratio)
    green = 50
    blue = 50
    return f"rgb({red},{green},{blue})"

# 지도 생성
m = folium.Map(location=[20, 0], zoom_start=2)

# 마커 추가
for c in continent_data:
    folium.CircleMarker(
        location=[c["lat"], c["lon"]],
        radius=20,
        color=get_color(c["count"]),
        fill=True,
        fill_opacity=0.7,
        popup=f"{c['name']}: {c['count']}종"
    ).add_to(m)

# Streamlit에 지도 출력
st_data = st_folium(m, width=700)
