import streamlit as st

# 대륙별 돼지고기 튀김 요리를 즐기는 나라들 (예시 기반 데이터)
continent_pork_fry = {
    "아시아": ["대한민국 (삼겹살튀김, 돈가스)", "필리핀 (Lechon Kawali)", "중국 (Sweet and Sour Pork)", "태국 (Moo Tod)", "베트남 (Thịt Chiên)"],
    "유럽": ["독일 (Schnitzel)", "오스트리아 (Wiener Schnitzel)", "폴란드 (Kotlet Schabowy)", "스페인 (Torreznos)"],
    "북아메리카": ["미국 (Deep-fried pork chops)", "멕시코 (Chicharrón)", "캐나다 (Deep-fried bacon)"],
    "남아메리카": ["브라질 (Torresmo)", "콜롬비아 (Chicharrón Colombiano)", "페루 (Chicharrón de cerdo)"],
    "아프리카": ["남아프리카공화국 (Deep-fried pork belly)", "나이지리아 (Pork stir fry – 일부 지역)"],
    "오세아니아": ["호주 (Deep-fried pork schnitzel)", "뉴질랜드 (Pork belly bites – 일부 식당 메뉴)"]
}

# 웹앱 제목
st.title("대륙별 돼지고기 튀김 요리를 즐기는 나라들")

# 대륙 선택
continent = st.selectbox("대륙을 선택하세요:", list(continent_pork_fry.keys()))

# 결과 출력
if continent:
    st.subheader(f"{continent}에서 돼지를 기름에 튀겨 먹는 나라들:")
    for country in continent_pork_fry[continent]:
        st.markdown(f"- {country}")

