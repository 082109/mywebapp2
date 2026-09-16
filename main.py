import streamlit as st
from datetime import date

# 페이지 설정
st.set_page_config(
    page_title="오늘 뭐 먹지? 🍴",
    page_icon="🍀",
    layout="centered"
)

# 기분별 음식 목록
food_data = {
    "😊 행복해": [
        ("치킨 🍗", "오늘의 행복을 더 크게 만들어줄 바삭한 치킨!"),
        ("피자 🍕", "맛있는 피자와 함께 기분 좋은 하루를 보내보자!"),
        ("떡볶이 🌶️", "달콤매콤한 떡볶이로 신나는 기분을 이어가자!")
    ],

    "😢 조금 우울해": [
        ("김치찌개 🍲", "따뜻하고 든든한 김치찌개로 마음까지 따뜻하게!"),
        ("돈까스 🍱", "바삭한 돈까스를 먹으며 기분을 조금 달래보자!"),
        ("우동 🍜", "따뜻한 국물 한 그릇으로 편안한 시간을 가져보자.")
    ],

    "😡 화가 나": [
        ("마라탕 🌶️", "얼얼하고 매콤한 맛으로 기분을 확 바꿔보자!"),
        ("제육볶음 🥘", "매콤하고 든든한 제육볶음으로 기분 전환!"),
        ("닭갈비 🍗", "친구와 함께 먹으면 더 즐거운 매콤한 닭갈비!")
    ],

    "😤 짜증나": [
        ("매운 떡볶이 🌶️", "오늘의 짜증을 맛있는 매콤함으로 날려보자!"),
        ("치즈 돈까스 🧀", "바삭한 돈까스와 쭉 늘어나는 치즈로 기분 전환!"),
        ("닭강정 🍗", "달콤바삭한 닭강정으로 짜증나는 하루를 조금 잊어보자!")
    ],

    "😔 억울해": [
        ("치즈 닭갈비 🧀", "오늘은 맛있는 거 먹으면서 속상한 마음을 잠깐 내려놓자!"),
        ("초밥 🍣", "다양한 초밥을 하나씩 골라 먹으며 기분을 달래보자!"),
        ("불고기 덮밥 🍚", "든든하게 한 그릇 먹고 다시 힘내보자!")
    ],

    "😴 피곤해": [
        ("국밥 🍚", "뜨끈한 국밥 한 그릇으로 든든하게 충전!"),
        ("칼국수 🍜", "따뜻한 국물과 면으로 편안하게 쉬어가자."),
        ("죽 🥣", "부담 없이 따뜻하게 먹기 좋은 오늘의 메뉴!")
    ],

    "🤩 신나": [
        ("햄버거 🍔", "신나는 날에는 맛있는 햄버거가 딱!"),
        ("분식 세트 🍢", "떡볶이, 튀김, 김밥까지 골라 먹는 재미!"),
        ("초밥 🍣", "다양한 초밥을 골라 먹으며 신나는 하루를 보내자!")
    ],

    "😌 평범해": [
        ("비빔밥 🥗", "오늘처럼 평범한 날에는 든든하고 맛있는 비빔밥!"),
        ("파스타 🍝", "부담 없이 즐기기 좋은 맛있는 파스타!"),
        ("김밥 🍙", "간단하지만 맛있는 국민 메뉴 김밥!")
    ]
}


# CSS
st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #777777;
    font-size: 17px;
    margin-bottom: 30px;
}

.result-card {
    background-color: #fff9e6;
    border: 2px solid #f1df9a;
    border-radius: 25px;
    padding: 30px;
    margin-top: 25px;
    text-align: center;
}

.food {
    font-size: 32px;
    font-weight: bold;
    margin: 15px 0;
}

.reason {
    font-size: 17px;
    line-height: 1.7;
    color: #555555;
}
</style>
""", unsafe_allow_html=True)


# 제목
st.markdown(
    '<div class="title">🍴 오늘 뭐 먹지? 🍀</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">오늘의 기분에 딱 맞는 음식 하나를 추천해줄게!</div>',
    unsafe_allow_html=True
)


# 오늘 날짜
today = date.today()

st.write("")
st.write(
    f"📅 오늘은 **{today.year}년 {today.month}월 {today.day}일**"
)


# 기분 선택
mood = st.selectbox(
    "💭 오늘 기분은 어때?",
    list(food_data.keys())
)


# 추천 버튼
if st.button("🍽️ 오늘의 음식 추천받기!", use_container_width=True):

    foods = food_data[mood]

    # 날짜 + 기분에 따라 매일 다른 음식 추천
    day_number = today.toordinal()
    mood_number = list(food_data.keys()).index(mood)

    food_index = (day_number + mood_number) % len(foods)

    food, reason = foods[food_index]

    st.balloons()

    st.markdown(
        f"""
<div class="result-card">
<div style="font-size:50px;">🍀</div>
<div style="font-size:18px;">오늘의 기분에 맞는 음식은...</div>
<div class="food">{food}</div>
<div class="reason">{reason}</div>
<hr>
<div>✨ 오늘도 맛있는 하루 보내자! ✨</div>
</div>
""",
        unsafe_allow_html=True
    )

    st.write("")
    st.success("💚 내일 다시 방문하면 새로운 음식이 추천돼요!")
