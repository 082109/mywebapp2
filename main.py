import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="MBTI 음식 추천 🍴",
    page_icon="🍕",
    layout="centered"
)

# MBTI별 음식 데이터
food_data = {
    "INFP": {
        "emoji": "🌷",
        "food": "딸기 케이크 🍰",
        "reason": "감성적이고 부드러운 분위기를 좋아하는 INFP에게 달콤하고 예쁜 디저트가 잘 어울려요!",
        "menu": "딸기 케이크 + 따뜻한 아메리카노 ☕",
        "color": "#FFF0F5"
    },
    "INFJ": {
        "emoji": "🌙",
        "food": "파스타 🍝",
        "reason": "차분하게 혼자만의 시간을 즐기는 INFJ에게 여유롭게 먹기 좋은 파스타를 추천해요!",
        "menu": "크림 파스타 + 레몬에이드 🍋",
        "color": "#F3E5F5"
    },
    "INTP": {
        "emoji": "🔬",
        "food": "초밥 🍣",
        "reason": "새로운 것을 탐구하는 INTP에게 다양한 재료와 조합을 즐길 수 있는 초밥이 잘 어울려요!",
        "menu": "모둠 초밥 + 우동 🍜",
        "color": "#E3F2FD"
    },
    "INTJ": {
        "emoji": "🧠",
        "food": "스테이크 🥩",
        "reason": "효율적이고 확실한 것을 선호하는 INTJ에게 깔끔하고 든든한 스테이크를 추천해요!",
        "menu": "스테이크 + 샐러드 🥗",
        "color": "#E8EAF6"
    },
    "ISFP": {
        "emoji": "🎨",
        "food": "마카롱 🧁",
        "reason": "감각적이고 아름다운 것을 좋아하는 ISFP에게 알록달록하고 예쁜 마카롱이 잘 어울려요!",
        "menu": "마카롱 + 아이스티 🧊",
        "color": "#FCE4EC"
    },
    "ISFJ": {
        "emoji": "🏡",
        "food": "김치찌개 🍲",
        "reason": "따뜻하고 편안한 분위기를 좋아하는 ISFJ에게 익숙하고 든든한 집밥 느낌의 음식이 잘 어울려요!",
        "menu": "김치찌개 + 계란말이 🥚",
        "color": "#FFF3E0"
    },
    "ISTP": {
        "emoji": "🛹",
        "food": "햄버거 🍔",
        "reason": "자유롭고 실용적인 ISTP에게 간편하면서도 맛있게 즐길 수 있는 햄버거를 추천해요!",
        "menu": "치즈버거 + 감자튀김 🍟",
        "color": "#E0F7FA"
    },
    "ISTJ": {
        "emoji": "📚",
        "food": "돈까스 🍱",
        "reason": "꼼꼼하고 안정적인 것을 좋아하는 ISTJ에게 익숙하면서도 든든한 돈까스를 추천해요!",
        "menu": "등심 돈까스 + 냉모밀 🍜",
        "color": "#ECEFF1"
    },
    "ENFP": {
        "emoji": "✨",
        "food": "떡볶이 🌶️",
        "reason": "활발하고 새로운 경험을 좋아하는 ENFP에게 친구들과 함께 즐기기 좋은 떡볶이를 추천해요!",
        "menu": "떡볶이 + 튀김 + 김밥 🍙",
        "color": "#FFF8E1"
    },
    "ENFJ": {
        "emoji": "💖",
        "food": "피자 🍕",
        "reason": "사람들과 함께하는 것을 좋아하는 ENFJ에게 여러 명이 나눠 먹기 좋은 피자가 잘 어울려요!",
        "menu": "치즈 피자 + 콜라 🥤",
        "color": "#FBE9E7"
    },
    "ENTP": {
        "emoji": "⚡",
        "food": "마라탕 🌶️",
        "reason": "새로운 것에 도전하는 ENTP에게 취향대로 재료를 골라 먹는 마라탕을 추천해요!",
        "menu": "마라탕 + 꿔바로우 🥢",
        "color": "#FFF3E0"
    },
    "ENTJ": {
        "emoji": "👑",
        "food": "스테이크 🥩",
        "reason": "자신감 있고 목표 지향적인 ENTJ에게 든든하고 만족감 있는 스테이크를 추천해요!",
        "menu": "채끝 스테이크 + 감자튀김 🍟",
        "color": "#FFF8E1"
    },
    "ESFP": {
        "emoji": "🎉",
        "food": "치킨 🍗",
        "reason": "즐겁고 활기찬 ESFP에게 친구들과 함께 신나게 먹기 좋은 치킨을 추천해요!",
        "menu": "후라이드 치킨 + 치즈볼 🧀",
        "color": "#FFFDE7"
    },
    "ESFJ": {
        "emoji": "🥰",
        "food": "삼겹살 🥓",
        "reason": "사람들과 어울리는 것을 좋아하는 ESFJ에게 함께 구워 먹으며 대화하기 좋은 삼겹살이 잘 어울려요!",
        "menu": "삼겹살 + 된장찌개 + 볶음밥 🍚",
        "color": "#FBE9E7"
    },
    "ESTP": {
        "emoji": "🔥",
        "food": "닭발 🌶️",
        "reason": "활동적이고 자극적인 경험을 좋아하는 ESTP에게 매콤하고 강렬한 닭발을 추천해요!",
        "menu": "매운 닭발 + 주먹밥 🍙",
        "color": "#FFEBEE"
    },
    "ESTJ": {
        "emoji": "📋",
        "food": "제육볶음 🍖",
        "reason": "현실적이고 확실한 것을 좋아하는 ESTJ에게 든든하고 익숙한 제육볶음을 추천해요!",
        "menu": "제육볶음 + 계란찜 🥚",
        "color": "#E8F5E9"
    }
}

# CSS
st.markdown("""
<style>
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777777;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .result {
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        margin-top: 25px;
        border: 2px solid #eeeeee;
    }

    .food {
        font-size: 32px;
        font-weight: bold;
        margin: 15px 0;
    }

    .reason {
        font-size: 17px;
        line-height: 1.7;
    }

    .menu {
        font-size: 18px;
        font-weight: bold;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)


# 제목
st.markdown(
    '<div class="title">🍴 MBTI 음식 추천 🍴</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">나의 MBTI와 찰떡궁합인 음식을 찾아보자! 💕</div>',
    unsafe_allow_html=True
)


# MBTI 선택
mbti = st.selectbox(
    "💭 나의 MBTI를 선택해주세요!",
    list(food_data.keys())
)


# 추천 버튼
if st.button("🍽️ 음식 추천받기!", use_container_width=True):

    data = food_data[mbti]

    # 풍선 효과
    st.balloons()

    # 결과 출력
    st.markdown(
        f"""
        <div class="result" style="background-color:{data['color']}">

            <div style="font-size:55px;">
                {data['emoji']}
            </div>

            <div style="font-size:20px;">
                {mbti} 유형에게 어울리는 음식은...
            </div>

            <div class="food">
                {data['food']}
            </div>

            <div class="reason">
                {data['reason']}
            </div>

            <hr>

            <div class="menu">
                🍽️ 추천 조합<br><br>
                {data['menu']}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "💡 MBTI 음식 추천은 재미로 즐겨주세요! "
        "실제로는 자신이 좋아하는 음식이 가장 맛있는 음식이에요 😋"
    )
