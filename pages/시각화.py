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

st.markdown("# 시각화👩‍💻 ")
st.text(' ')
st.text(' ')
st.text(' ')

color= sns.color_palette('pastel')[:10]



# 데이터셋 불러오기(은행 고객 이탈 데이터)
# data1 = pd.read_csv('C:\Users\taewan\Desktop\금융\Customer-Churn-Records.csv',encoding='UTF-8')
#data1 = pd.read_csv('Customer-Churn-Records.csv',encoding='UTF-8')
# 데이터셋 불러오기(은행 고객 이탈 데이터)
data =  pd.read_csv('Customer-Churn-Records.csv',encoding='UTF-8')


st.subheader(" · 이탈률")

# 이탈률
churn_counts = data['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts, labels=['stay ', 'Exited'], autopct='%1.1f%%', startangle=90, colors=color)
plt.axis('equal')
st.pyplot(fig)
st.text(' ')

st.subheader(" · 연령대별 이탈분포")
st.text(' ')
image = Image.open("aa.PNG")
st.image(image, width=1000) 
import streamlit as st
import numpy as np
import plotly.figure_factory as ff


data['AgeGroup'] = pd.cut(data['Age'], bins=[0, 19, 29, 39, 49, 59, np.inf], labels=['10','20', '30', '40', '50', '60~'])
fig, axs = plt.subplots()
sns.countplot(data, x='AgeGroup', hue='Exited',  palette= 'pastel', ax=axs)

#ax.hist(arr)

st.pyplot(fig)
st.text(' ')

st.subheader(" · 성별 이탈분포")
st.text(' ')
fig, axs = plt.subplots()
sns.countplot(data, x='Gender', hue='Exited', palette= 'pastel',ax=axs) #문자변수 관련 원핫인코딩시 countplot오류발생
st.pyplot(fig)


st.text(' ')
st.subheader(" · 성별 이탈분포")
st.text(' ')
df_exited = data[data.Exited == 1]
churn_counts1 = df_exited['Gender'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts1, labels=['female', 'male'], autopct='%1.1f%%', startangle=90, colors=['#fcc5c0','#c6dbef'])
plt.axis('equal')
st.pyplot(fig)

st.text(' ')
st.subheader(" · 여성 이탈률")
st.text(' ')
data_fe_gender = data[data.Gender=='Female']

churn_counts2 = data_fe_gender['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts2, labels=['stay ', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)
st.text(' ')
st.subheader(" · 남성 이탈률")
st.text(' ')
data_ma_gender = data[data.Gender=='Male']

churn_counts3 = data_ma_gender['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts3, labels=['stay', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)






st.text(' ')
st.subheader(" · 지역별 이탈분포")
st.text(' ')
fig, axs = plt.subplots()
sns.countplot(data, x='Geography', hue='Exited', palette= 'pastel',ax=axs)
st.pyplot(fig)







# geography (exited ==1)
st.text(' ')
st.subheader(" · 국가별 이탈률")
st.text(' ')
df_exited = data[data.Exited == 1]

churn_counts4 = df_exited['Geography'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts4, labels=['Germany', 'France', 'Spain'], autopct='%1.1f%%', startangle=90, colors=['#fcc5c0','#c6dbef','#a1d99b'])
plt.axis('equal')
st.pyplot(fig)


###
st.text(' ')
st.subheader(" · 독일 이탈률")
st.text(' ')
data_germ = data[data.Geography=='Germany']

churn_counts5 = data_germ['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts5, labels=['stay', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)

###
st.text(' ')
st.subheader(" · 프랑스 이탈률")
st.text(' ')
data_fran = data[data.Geography=='France']

churn_counts6 = data_fran['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts6, labels=['stay', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)

st.text(' ')
st.subheader(" · 스페인 이탈률")
st.text(' ')
data_spa = data[data.Geography=='Spain']

churn_counts7 = data_spa['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts7, labels=['stay', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)

st.text(' ')
st.subheader(" · 잔고에 따른 이탈분포")
st.text(' ')
fig, axs = plt.subplots()
sns.boxplot(data, x='Exited', y='Balance',  palette= 'pastel',ax=axs)
st.pyplot(fig)

st.text(' ')

st.subheader(" · 활동상태에 따른 이탈분포")
st.text(' ')
fig, axs = plt.subplots()
sns.countplot(data, x='IsActiveMember', hue='Exited', palette= 'pastel',ax=axs)
st.pyplot(fig)



# 활성 고객
st.text(' ')
st.subheader(" · 활성고객 이탈률")
st.text(' ')
data_notact = data[data.IsActiveMember==1]

churn_counts9 = data_notact['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts9, labels=['stay', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)

# 비활성 고객
st.text(' ')
st.subheader(" · 비활성고객 이탈률")
st.text(' ')
data_notact = data[data.IsActiveMember==0]

churn_counts8 = data_notact['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts8, labels=['stay', 'Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9','#fc9272'])
plt.axis('equal')
st.pyplot(fig)





st.text(' ')

st.subheader(" · 불만 발생에 따른 이탈분포")
st.text(' ')
churn_complain = data['Complain'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_complain, labels=['satisfy', 'dissatisfaction'], autopct='%1.1f%%', startangle=90, colors=color)
plt.axis('equal')
st.pyplot(fig)


# 불만있는 고객
st.text(' ')
st.subheader(" · 불만고객 이탈률")
st.text(' ')
data_comp = data[data.Complain==1]

churn_counts10 = data_comp['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts10, labels=['Exited', 'stay'], autopct='%1.1f%%', startangle=90, colors=['#fc9272','#d9d9d9'])
plt.axis('equal')
st.pyplot(fig)
# 불만없는 고객
st.text(' ')
st.subheader(" · 불만없는 고객 이탈률")
st.text(' ')
data_notcomp = data[data.Complain==0]

churn_counts11 = data_notcomp['Exited'].value_counts()
fig, axs = plt.subplots()
plt.pie(churn_counts11, labels=['stay','Exited'], autopct='%1.1f%%', startangle=90, colors=['#d9d9d9', '#fc9272'])
plt.axis('equal')
st.pyplot(fig)






#complain
st.text(' ')
st.subheader(" · 불만발생에 따른 이탈분포")
st.text(' ')
fig, axs = plt.subplots()
sns.countplot(data, x='Complain', hue='Exited', palette= 'pastel',ax=axs)
st.pyplot(fig)

#연령대별 불만분포
st.text(' ')
st.subheader(" · 연령대별 불만분포")
st.text(' ')
fig2 = sns.catplot(data, x='Complain', kind="count", col="AgeGroup",
            col_wrap=3, height=2.5, aspect=.8, palette=color)

st.pyplot(fig2)
#data =  pd.read_csv('Customer-Churn-Records.csv',encoding='UTF-8')
#st.write(data)

