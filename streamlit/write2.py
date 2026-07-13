import streamlit as st
import pandas as pd
import altair as alt # 선언형(declarative) 시각화 라이브러리
from numpy.random import default_rng as rng


# - rng(0): 시드(seed)를 0으로 고정한 난수 생성기를 만들어요. (재현 가능한 랜덤값)
# - .standard_normal((200,3)): 평균 0, 표준편차 1인 정규분포에서 200행 × 3열 크기의 난수 배열을 생성
# - 이를 a, b, c 세 개의 컬럼을 가진 데이터프레임으로 만듦
df = pd.DataFrame(rng(0).standard_normal((200,3)), columns=['a','b','c'])

# - alt.Chart(df): df를 데이터 소스로 하는 차트 객체 생성
# - .mark_circle(): 점(원) 마크로 그리겠다는 뜻 → 산점도가 됨
# - .encode(...): 데이터 컬럼을 시각적 요소에 매핑

#   - x="a": x축 = a 컬럼
#   - y="b": y축 = b 컬럼
#   - size="c": 점의 크기를 c 값에 따라 다르게
#   - color="c": 점의 색상도 c 값에 따라 다르게 (색으로 값을 한 번 더 표현)
#   - tooltip=["a","b","c"]: 마우스를 올렸을 때 a, b, c 값을 툴팁으로 표시

# 즉, c값이 클수록 점이 크고 색이 진해지는 3차원(x, y, 크기/색) 정보를 담은 산점도

chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)