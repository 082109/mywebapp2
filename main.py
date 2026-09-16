import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="성격별 개명 이름 추천",
    page_icon="✨",
    layout="centered"
)

# 성격별 이름 데이터
name_data = {
    "🌸 차분하고 따뜻한 성격": [
        ("서윤", "부드럽고 따뜻한 느낌"),
        ("다온", "편안하고 밝은 느낌"),
        ("하윤", "차분하면서도 친근한 느낌"),
        ("지안", "깔끔하고 안정적인 느낌"),
        ("유진", "부드럽고 자연스러운 느낌")
    ],

    "☀️ 밝고 활발한 성격": [
        ("채원", "밝고 사랑스러운 느낌"),
        ("예린", "통통 튀고 밝은 느낌"),
        ("수빈", "친근하고 활기찬 느낌"),
        ("민서", "깔끔하고 긍정적인 느낌"),
        ("아린", "밝고 귀여운 느낌")
    ],

    "🎨 감성적이고 예술적인 성격": [
        ("서아", "감성적이고 세련된 느낌"),
        ("유나", "부드럽고 감각적인 느낌"),
        ("소윤", "차분하면서도 감성적인 느낌"),
        ("윤슬", "반짝이는 분위기의 느낌"),
        ("가온", "독특하면서 자연스러운 느낌")
    ],

    "🔥 자신감 있고 당당한 성격": [
        ("서현", "단정하고 당당한 느낌"),
        ("지우", "깔끔하고 자신감 있는 느낌"),
        ("수아", "세련되고 또렷한 느낌"),
        ("하린", "밝고 당찬 느낌"),
        ("채아", "개성 있고 자신감 있는 느낌")
    ],

    "🐰 귀엽고 친근한 성격": [
        ("다솜", "사랑스럽고 따뜻한 느낌"),
        ("나연", "친근하고 밝은 느낌"),
        ("보민", "귀엽고 편안한 느낌"),
        ("유빈", "활발하고 친근한 느낌"),
        ("아윤", "부드럽고 귀여운 느낌")
    ],

    "🌙 조용하고 신비로운 성격": [
        ("시은", "차분하고 신비로운 느낌"),
        ("은서", "부드럽고 조용한 느낌"),
        ("서린", "맑고 세련된 느낌"),
        ("유림", "차분하고 단정한 느낌"),
        ("다인", "깔끔하고 은은한 느낌")
    ]
}


# CSS
st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
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
    background-color: #fff7fb;
    border: 2px solid #f3dce8;
    border-radius: 25px;
    padding: 25px;
    margin-top: 20px;
    text-align: center;
}

.name-box {
    background-color: white;
    border-radius: 18px;
    padding: 18px;
    margin: 12px 0;
    border: 1px solid #eeeeee;
}

.name {
    font-size: 27px;
    font-weight: bold;
}

.meaning {
    color: #777777;
    margin-top: 5px;
}

</style>
""", unsafe_allow_html=True)


# 제목
st.markdown(
    '<div class="title">✨ 성격별 개명 이름 추천 ✨</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">내 성격과 어울리는 새로운 이름을 찾아보자! 💕</div>',
    unsafe_allow_html=True
)


# 성격 선택
personality = st.selectbox(
    "🌷 친구의 성격을 골라주세요!",
    list(name_data.keys())
)


# 추천 버튼
if st.button("✨ 이름 추천받기!", use_container_width=True):

    # 선택한 성격의 이름 중 3개 랜덤 추천
    recommendations = random.sample(
        name_data[personality],
        3
    )

    st.balloons()

    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        f"### 💌 이런 이름은 어때요?",
        unsafe_allow_html=True
    )

    st.write(f"선택한 성격 : **{personality}**")

    for i, (name, meaning) in enumerate(recommendations, 1):

        st.markdown(
            f"""
<div class="name-box">
<div style="font-size:15px;">추천 {i}</div>
<div class="name">{name} ✨</div>
<div class="meaning">{meaning}</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.info(
        "💡 이름은 성격만으로 정해지는 것은 아니에요! "
        "이름의 뜻, 발음, 가족의 의견 등을 함께 생각해보세요 😊"
    )
