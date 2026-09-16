import streamlit as st
from datetime import date

# -------------------------------
# 페이지 설정
# -------------------------------
st.set_page_config(
    page_title="오늘 뭐 먹지? 🍴",
    page_icon="🍀",
    layout="centered"
)

# -------------------------------
# 기분별 음식 데이터
# -------------------------------
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
        ("닭강정 🍗", "달콤바삭한 닭강정으로 기분을 조금 풀어보자!")
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
        ("비빔밥 🥗", "평범한 날에는 든든하고 맛있는 비빔밥!"),
        ("파스타 🍝", "부담 없이 즐기기 좋은 맛있는 파스타!"),
        ("김밥 🍙", "간단하지만 맛있는 국민 메뉴 김밥!")
    ],

    "💗 설레": [
        ("딸기 케이크 🍰", "설레는 기분에는 보기만 해도 기분 좋아지는 달콤한 디저트!"),
        ("파스타 🍝", "특별한 날처럼 느껴지는 오늘, 분위기 있게 파스타를 먹어보자!"),
        ("와플 🧇", "달콤한 와플과 함께 설레는 기분을 즐겨보자!")
    ],

    "😵 스트레스받아": [
        ("치즈 피자 🍕", "맛있는 치즈 피자로 잠깐 쉬면서 기분을 풀어보자!"),
        ("돈까스 🍱", "바삭한 돈까스를 먹으며 스트레스를 잠시 내려놓자!"),
        ("라멘 🍜", "뜨끈한 국물 한 그릇으로 편안하게 기분 전환!")
    ],

    "🥱 졸려": [
        ("김밥 🍙", "간단하고 맛있게 먹고 편하게 쉬어보자!"),
        ("샌드위치 🥪", "부담 없이 먹기 좋은 간단한 오늘의 메뉴!"),
        ("우동 🍜", "따뜻한 우동으로 든든하게 배를 채워보자!")
    ],

    "🥺 외로워": [
        ("삼겹살 🥓", "친구와 함께 구워 먹으면서 이야기를 나누기 좋은 음식!"),
        ("치킨 🍗", "친구와 나눠 먹으면 더 맛있는 치킨!"),
        ("떡볶이 🌶️", "친구와 함께 먹으면 더 즐거운 국민 간식!")
    ],

    "🤤 배고파": [
        ("제육덮밥 🍚", "배고플 때 든든하게 한 그릇 먹기 좋은 메뉴!"),
        ("햄버거 🍔", "배고픈 날에는 푸짐한 햄버거로 든든하게!"),
        ("김치볶음밥 🍳", "간단하지만 든든하게 배를 채울 수 있는 메뉴!")
    ],

    "🥱 심심해": [
        ("마라탕 🌶️", "재료를 직접 골라 먹는 재미가 있는 마라탕!"),
        ("초밥 🍣", "여러 종류를 골라 먹다 보면 심심할 틈이 없어요!"),
        ("분식 세트 🍢", "떡볶이부터 튀김까지 이것저것 골라 먹어보자!")
    ],

    "😎 자신감 뿜뿜": [
        ("스테이크 🥩", "오늘의 자신감에 어울리는 근사하고 든든한 메뉴!"),
        ("파스타 🍝", "기분 좋은 자신감과 잘 어울리는 분위기 있는 음식!"),
        ("햄버거 🍔", "오늘은 내가 원하는 메뉴를 당당하게 골라보자!")
    ]
}

# -------------------------------
# 귀여운 디자인
# -------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #fff8fb 0%, #fffdf5 100%);
}

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
    margin-bottom: 25px;
}

.date-box {
    background-color: white;
    border-radius: 15px;
    padding: 12px;
    text-align: center;
    border: 1px solid #eeeeee;
    margin-bottom: 20px;
}

.result-card {
    background-color: #fff7df;
    border: 2px solid #f1d98b;
    border-radius: 28px;
    padding: 30px;
    margin-top: 25px;
    text-align: center;
}

.food {
    font-size: 34px;
    font-weight: bold;
    margin: 15px 0;
}

.reason {
    font-size: 17px;
    line-height: 1.7;
    color: #555555;
}

.small-text {
    color: #888888;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# 제목
# -------------------------------
st.markdown(
    '<div class="title">🍴 오늘 뭐 먹지? 🍀</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">오늘의 기분을 알려주면 음식을 하나 골라줄게!</div>',
    unsafe_allow_html=True
)

# -------------------------------
# 날짜
# -------------------------------
today = date.today()

st.markdown(
    f"""
<div class="date-box">
📅 오늘은 <b>{today.year}년 {today.month}월 {today.day}일</b>이에요!
</div>
""",
    unsafe_allow_html=True
)

# -------------------------------
# 기분 선택
# -------------------------------
mood = st.selectbox(
    "💭 지금 내 기분은?",
    list(food_data.keys())
)

# -------------------------------
# 추천 버튼
# -------------------------------
if st.button("🍽️ 오늘의 음식 추천받기!", use_container_width=True):

    foods = food_data[mood]

    # 날짜와 기분에 따라 매일 다른 음식
    day_number = today.toordinal()
    mood_number = list(food_data.keys()).index(mood)

    food_index = (day_number + mood_number) % len(foods)

    food, reason = foods[food_index]

    st.balloons()

    # 결과 카드
    st.markdown(
        f"""
<div class="result-card">

<div style="font-size:55px;">🍀</div>

<div style="font-size:18px;">
오늘의 기분은 <b>{mood}</b>
</div>

<div style="font-size:18px; margin-top:15px;">
오늘의 추천 음식은...
</div>

<div class="food">
{food}
</div>

<div class="reason">
{reason}
</div>

<hr>

<div class="small-text">
✨ 오늘도 맛있는 하루 보내자! ✨
</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.write("")

    st.success(
        "💚 내일 다시 방문하면 오늘과 다른 음식이 추천될 수 있어요!"
    )
