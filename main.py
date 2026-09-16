import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 여행지 추천 🌈",
    page_icon="✈️",
    layout="centered"
)

# 여행지 데이터
travel_data = {
    "INFP": {
        "emoji": "🌿",
        "type": "감성 여행자",
        "place": "스위스 인터라켄 🇨🇭",
        "description": "조용한 자연 속에서 여유롭게 생각을 정리하고 감성을 충전하기 좋은 곳!",
        "spots": ["호수 산책 🌊", "알프스 풍경 🏔️", "예쁜 카페 ☕"],
        "color": "#E8F5E9"
    },
    "INFJ": {
        "emoji": "🌙",
        "type": "힐링 여행자",
        "place": "일본 교토 🇯🇵",
        "description": "고즈넉한 골목과 사찰을 천천히 둘러보며 마음의 여유를 찾기 좋은 곳!",
        "spots": ["아라시야마 🎋", "전통 거리 🏮", "조용한 카페 🍵"],
        "color": "#F3E5F5"
    },
    "INTP": {
        "emoji": "🔭",
        "type": "탐험하는 여행자",
        "place": "영국 런던 🇬🇧",
        "description": "새로운 지식과 독특한 문화를 발견하는 재미가 가득한 도시!",
        "spots": ["박물관 🏛️", "서점 📚", "과학관 🔬"],
        "color": "#E3F2FD"
    },
    "INTJ": {
        "emoji": "🧠",
        "type": "계획형 여행자",
        "place": "스위스 취리히 🇨🇭",
        "description": "깔끔한 도시와 효율적인 교통을 즐기며 알찬 여행을 계획하기 좋은 곳!",
        "spots": ["구시가지 🏘️", "호수 🚤", "미술관 🎨"],
        "color": "#E8EAF6"
    },
    "ISFP": {
        "emoji": "🎨",
        "type": "감각적인 여행자",
        "place": "이탈리아 피렌체 🇮🇹",
        "description": "아름다운 예술과 맛있는 음식, 따뜻한 분위기를 느끼기 좋은 도시!",
        "spots": ["미술관 🖼️", "두오모 ⛪", "젤라또 🍦"],
        "color": "#FFF3E0"
    },
    "ISFJ": {
        "emoji": "🏡",
        "type": "편안한 여행자",
        "place": "일본 오사카 🇯🇵",
        "description": "편안한 분위기 속에서 맛있는 음식과 다양한 볼거리를 즐길 수 있는 곳!",
        "spots": ["도톤보리 🍜", "오사카성 🏯", "시장 🥢"],
        "color": "#FFF8E1"
    },
    "ISTP": {
        "emoji": "🏄",
        "type": "자유로운 여행자",
        "place": "호주 골드코스트 🇦🇺",
        "description": "바다와 액티비티를 마음껏 즐기며 자유로운 여행을 하기 좋은 곳!",
        "spots": ["서핑 🏄", "해변 🏖️", "테마파크 🎢"],
        "color": "#E0F7FA"
    },
    "ISTJ": {
        "emoji": "🗺️",
        "type": "꼼꼼한 여행자",
        "place": "싱가포르 🇸🇬",
        "description": "깔끔하고 체계적인 도시에서 계획대로 알차게 여행하기 좋은 곳!",
        "spots": ["마리나베이 🌃", "가든스 바이 더 베이 🌳", "야시장 🍴"],
        "color": "#ECEFF1"
    },
    "ENFP": {
        "emoji": "✨",
        "type": "신나는 여행자",
        "place": "미국 뉴욕 🇺🇸",
        "description": "새로운 사람과 문화, 재미있는 경험을 끊임없이 만날 수 있는 도시!",
        "spots": ["타임스스퀘어 🌃", "센트럴파크 🌳", "브로드웨이 🎭"],
        "color": "#FFF0F5"
    },
    "ENFJ": {
        "emoji": "💖",
        "type": "함께하는 여행자",
        "place": "프랑스 파리 🇫🇷",
        "description": "친구나 가족과 함께 아름다운 풍경과 문화를 즐기기 좋은 낭만적인 도시!",
        "spots": ["에펠탑 🗼", "센강 🌊", "카페 ☕"],
        "color": "#FCE4EC"
    },
    "ENTP": {
        "emoji": "⚡",
        "type": "도전하는 여행자",
        "place": "미국 라스베이거스 🇺🇸",
        "description": "평범한 여행보다 새롭고 자극적인 경험을 좋아한다면 딱 맞는 곳!",
        "spots": ["화려한 거리 ✨", "공연 🎤", "그랜드캐니언 🏜️"],
        "color": "#FFF3E0"
    },
    "ENTJ": {
        "emoji": "👑",
        "type": "리더 여행자",
        "place": "아랍에미리트 두바이 🇦🇪",
        "description": "화려한 건축물과 다양한 경험을 빠르게 즐길 수 있는 도시!",
        "spots": ["부르즈 할리파 🏙️", "두바이몰 🛍️", "사막 투어 🏜️"],
        "color": "#FFF8E1"
    },
    "ESFP": {
        "emoji": "🎉",
        "type": "즐거운 여행자",
        "place": "스페인 바르셀로나 🇪🇸",
        "description": "맛있는 음식과 음악, 아름다운 건축물을 신나게 즐길 수 있는 곳!",
        "spots": ["사그라다 파밀리아 ⛪", "해변 🏖️", "타파스 🍴"],
        "color": "#FFFDE7"
    },
    "ESFJ": {
        "emoji": "🥰",
        "type": "사교적인 여행자",
        "place": "태국 방콕 🇹🇭",
        "description": "맛있는 음식과 활기찬 거리에서 사람들과 즐거운 시간을 보내기 좋은 곳!",
        "spots": ["야시장 🌙", "사원 🛕", "길거리 음식 🍜"],
        "color": "#FBE9E7"
    },
    "ESTP": {
        "emoji": "🔥",
        "type": "액티비티 여행자",
        "place": "미국 하와이 🇺🇸",
        "description": "답답한 일상에서 벗어나 바다와 다양한 활동을 즐기기 좋은 곳!",
        "spots": ["스노클링 🤿", "해변 🏖️", "하이킹 🥾"],
        "color": "#E0F2F1"
    },
    "ESTJ": {
        "emoji": "📋",
        "type": "알찬 여행자",
        "place": "대한민국 서울 🇰🇷",
        "description": "맛집부터 쇼핑, 문화생활까지 다양한 활동을 효율적으로 즐길 수 있는 도시!",
        "spots": ["한강 🌉", "성수동 ☕", "궁궐 🏯"],
        "color": "#E8F5E9"
    }
}

# CSS
st.markdown("""
<style>
    .main {
        background-color: #FFF9FC;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .result {
        padding: 25px;
        border-radius: 25px;
        text-align: center;
        margin-top: 20px;
        border: 2px solid #eeeeee;
    }

    .place {
        font-size: 30px;
        font-weight: bold;
        margin: 12px 0;
    }

    .description {
        font-size: 17px;
        line-height: 1.7;
    }

    .spot {
        font-size: 16px;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">✈️ MBTI 여행지 추천 🌈</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">나의 MBTI와 찰떡궁합인 여행지를 찾아보자! 🧳</div>',
    unsafe_allow_html=True
)

# MBTI 선택
mbti_list = list(travel_data.keys())

mbti = st.selectbox(
    "🧡 나의 MBTI를 선택해주세요!",
    mbti_list
)

# 추천 버튼
if st.button("🌟 여행지 추천받기!", use_container_width=True):

    data = travel_data[mbti]

    st.balloons()

    st.markdown(
        f"""
        <div class="result" style="background-color:{data['color']}">
            <div style="font-size:55px;">{data['emoji']}</div>
            <div style="font-size:20px;">{mbti} · {data['type']}</div>
            <div class="place">{data['place']}</div>
            <div class="description">{data['description']}</div>
            <hr>
            <div style="font-size:20px; font-weight:bold;">
                🌷 추천 코스
            </div>
            <div class="spot">
                {'　'.join(data['spots'])}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.info("💡 MBTI는 재미로 참고하고, 실제 여행 계획은 취향과 상황을 함께 고려해보세요!")
