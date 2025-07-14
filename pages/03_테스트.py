import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("국가별 멸종위기종 분포 시각화")

# 예시 데이터 (국가, 위도, 경도, 멸종위기종 수)
country_data = [
    {"name": "브라질", "lat": -14.2350, "lon": -51.9253, "count": 1200},
    {"name": "인도네시아", "lat": -0.7893, "lon": 113.9213, "count": 950},
    {"name": "인도", "lat": 20.5937, "lon": 78.9629, "count": 870},
    {"name": "중국", "lat": 35.8617, "lon": 104.1954, "count": 820},
    {"name": "콩고민주공화국", "lat": -4.0383, "lon": 21.7587, "count": 780},
    {"name": "호주", "lat": -25.2744, "lon": 133.7751, "count": 750},
    {"name": "미국", "lat": 37.0902, "lon": -95.7129, "count": 700},
    {"name": "멕시코", "lat": 23.6345, "lon": -102.5528, "count": 640},
    {"name": "남아프리카공화국", "lat": -30.5595, "lon": 22.9375, "count": 600},
    {"name": "러시아", "lat": 61.5240, "lon": 105.3188, "count": 580}
]

# 정규화를 위한 최대값
max_count = max([c["count"] for c in country_data])

# 색상 계산
def get_color(count):
    ratio = count / max_count
    red = int(255 * ratio)
    return f"rgb({red}, 50, 50)"

# 지도 생성
m = folium.Map(location=[10, 10], zoom_start=2)

# 국가별 마커 추가
for c in country_data:
    folium.CircleMarker(
        location=[c["lat"], c["lon"]],
        radius=10 + (15 * c["count"] / max_count),
        color=get_color(c["count"]),
        fill=True,
        fill_opacity=0.7,
        popup=f"{c['name']}: {c['count']}종"
    ).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)
