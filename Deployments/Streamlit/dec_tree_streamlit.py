import pickle
import streamlit as st
from streamlit_option_menu import option_menu

dectr = pickle.load(open("/home/sravani/Documents/datasets/Decision_Tree_fastapi/cardio_deci.pkl",'rb'))

st.title('Cardiovasular diseasae prediction using Decision Tree')

c1, c2, c3 = st.columns(3)

with c1:
  age = st.text_input('Age in days')
with c2: 
  gender = st.text_input('Gender 1-women, 2-men')
with c3:
  height = st.text_input('Height (cm)')
with c1:
  weight = st.text_input('weight (kg)')
with c2:  
  ap_hi = st.text_input('Bp_hi')
with c3:
  ap_lo = st.text_input('Bp_low')
with c1:
  cholestrol = st.selectbox('Cholestrol',["1","2","3"])
with c2:
  gluc = st.selectbox('Glucose',["1","2","3"])
with c3:
  smoke = st.text_input('Smoking')
with c1:
  alco = st.text_input('Alcohol')
with c2:
  active = st.text_input('Active')

diag = ''

if st.button('Cardiovascular test'):
  dectr_predict = dectr.predict([[age, gender, height, weight, ap_hi, ap_lo, int(cholestrol), int(gluc), smoke, alco, active]])
  if dectr_predict[0]==1:
    diag = "Patient has cardiovascular disease"
  else:
    diag = "Patient has no cardiovascular disease"

st.success(diag)
