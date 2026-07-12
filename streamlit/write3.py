import streamlit as st
import pandas as pd
import altair as alt # 선언형(declarative) 시각화 라이브러리
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((200,3)), columns=['a','b','c'])

'''
- rng(0): 시드(seed)를 0으로 고정한 난수 생성기를 만들어요. (재현 가능한 랜덤값)
- .standard_normal((200,3)): 평균 0, 표준편차 1인 정규분포에서 200행 × 3열 크기의 난수 배열을 생성
- 이를 a, b, c 세 개의 컬럼을 가진 데이터프레임으로 만듦
'''

chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(chart)