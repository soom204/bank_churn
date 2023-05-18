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




image = Image.open("b.jpeg")
st.image(image, width=400) 


st.title("은행 고객 이탈 방지")
st.header(' ')
st.header(' · 주제 선정 배경💭 ')
st.text(' - 은행의 리스크 관리 중 하나 ')
st.text('  - 기존 고객의 이탈을 막는 것이, 신규 고객을 유치하는 것보다 비용 측면에서 효율적')
st.text(' - 어떤 특성을 지닌 고객이 은행 이탈률이 높은 지 분석해, ')
st.text('   이탈 예측 및 방지를 위한 방안 마련 목적 ')
st.header(' ')
st.header(' · 데이터 설명')
st.text(" 2022년 4월 1일 ~ 2022년 5월 1일")
st.text(" 10,000개 행, 18개 열 고객 데이터")
st.text(' ')
st.subheader(' · 독립변수')
st.text(' - 고객 정보: RowNumber / CustomerId / Surname(이름)  ')
st.text('Geography / Gender / Age / EstimatedSalary (연봉)  ')
st.text('- 은행 사용 정보: CreditScore(신용도 점수) / Tenure(신용카드 사용 기간) / Balance / ')
st.text('NumOfProducts (은행에서 산 상품 개수) / HasCrCard(신용카드 보유 유무) / ')
st.text('IsActiveMember(활동고객 여부) / Complain(불만제기 이력) / Satisfaction Score(불만해소 만족도)')
st.text('Card Type(보유 카드 정보) / Point Earned (보유 포인트)        ')
st.subheader(' · 종속변수')
st.text('- Exited(은행 이탈 여부)')
st.subheader(' · 파생변수')
st.text('- AgeGroup (연령대)')
st.text(' ')
st.subheader(" ·  데이터 ")
color= sns.color_palette('pastel')[:10]



# 데이터셋 불러오기(은행 고객 이탈 데이터)
# data1 = pd.read_csv('C:\Users\taewan\Desktop\금융\Customer-Churn-Records.csv',encoding='UTF-8')
#data1 = pd.read_csv('Customer-Churn-Records.csv',encoding='UTF-8')
# 데이터셋 불러오기(은행 고객 이탈 데이터)
data =  pd.read_csv('Customer-Churn-Records.csv',encoding='UTF-8')

st.write(data)

st.subheader(" · data.describe(include='all')")
st.write(data.describe(include='all'))
# 10000개의 행/ 18개의 변수로 이루어진 dataframe
#변수는 행번호 (RowNumber),	고객id(CustomerId), 이름(Surname),	신용점수(CreditScore), 지역(Geography),	성별(Gender),	나이(Age),	신용카드 사용기간(Tenure),	신용카드 사용금액(Balance)
#보유상품의수(NumOfProducts),	신용카드 보유 유무(HasCrCard),	활동고객여부(IsActiveMember),	연봉(EstimatedSalary),	은행이용고객여부(Exited),	불만제기 이력(Complain),	불만해소 만족도(Satisfaction Score),	
#카드 타입(Card Type),	보유 포인트(Point Earned)로 이루어져있음. 
# 변수 중 HasCrCard  / IsActiveMember / Exited/ Complain 는 명목형변수로 수치값에 대한 의미 없음 0과1로 구분함.

# 데이터 전처리

#null값 없음 확인
#관계 없는 변수정리

st.subheader(" · 각 변수 데이터 타입 확인")
# 각 변수 데이터 타입 확인
st.write(data.dtypes)

st.subheader(" · null값 확인")
st.write(data.isnull().sum())

st.subheader(" · 데이터 전처리")
df= data.drop(['RowNumber', 'CustomerId', 'Surname', ], axis=1)
st.write(df)

image = Image.open("aaa.PNG")
st.image(image, width=800) 

st.subheader(" · 상관계수")
image = Image.open("plot1.png")
st.image(image)