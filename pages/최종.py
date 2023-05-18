import streamlit as st
import streamlit as st
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
st.markdown("# 결론👍 ")


st.subheader(' · 분석 결과(요약) ')
st.text('1) 고객 이탈의 원인 총 6가지: :  ')
st.text(' Age / Complain / Geography / Gender / Balance / IsActiveMember')
st.text('2) 이탈(exited)와 불만(complain) 간 높은 상관관계 (약 0.99) ')
st.text(' 3) 특히, 불만을 가진 고객의 특성을 파악하고자, ')
st.text('불만(complain)과 가장 높은 연관성(상관관계)을 가진 변수인 연령(age) 칼럼 ')
st.text(' -> 40대 고객이 가장 많은 불만을 보임 ')
st.text(' 4) 따라서 이 연령대의 특성을 고객이 불만을 갖지 않도록, ')
st.text(' 은행에서 제도적 차원의 지원을 제공해 이탈률을 막기 위한 조치를 취해야 할 것')
st.text(' ')
st.text(' ')

st.subheader(' · 애먹었던 점, 개선 방안')
st.text('1) get_dummies() 함수 사용해 Geography, Gender, Card Type 명목형 -> 수치형으로 변환')
st.text('-> 해당 변수들이 세부적으로 나뉨에 따라 다시 하나로 합쳐야 깔끔하게 보일 수 있음')
st.text('-> 굳이 그런 과정 거칠 바엔, 기본 데이터를 사용하는 게 나음')
st.text(' ')
st.text('2) 불만발생에 따른 이탈 분포 시각화 당시, 불만변수의 이탈 여부 데이터를 ')
st.text(' value_counts() 했을 때, 이 함수를 쓰면 내림차순화 됨 ')
st.text('-> 이전까진, 잔류 고객이 당연하게 먼저 나온다고 생각하여  label에 대한 신경을 안썼고, ')
st.text(' -> 해당 변수의 데이터가 지닌 의미를 알고 있기에 임으로 변경 과정을 거쳤지만, ')
st.text(' 추후 데이터 양이 많아지고 복잡해 질 경우, 이러한 방법을 사용하면 오류를 범할 수 있음 ')
st.text(' ')
st.text(' => 따라서 category(명목형변수를 순서를 부여해주는 파라미터)')
st.text(' 변수를 미리 설정하는 과정을 미리 수행해야만 함')
st.text(' ')
st.text('3) 확보한 데이터가 단조롭고, 개수가 한정적이어서 다양한 시각화를 하지 못한 점 ')
st.text(' ')
st.text(' ')
st.text(' ')
st.text(' ')

