
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
import streamlit as st 
import joblib


def getInput():
    
    Gender = st.selectbox('select gender'.title() , ['Male', 'Female'])
    
    Married = st.selectbox('Are you married'.title() , ['No' , 'Yes'])
    
    Dependents = st.select_slider('select number of dependences'.title() , [0 , 1 , 2 , 3])
    
    Education = st.selectbox('What type of your education'.title() , ['Graduate', 'Not Graduate'])
    
    Self_Employed = st.selectbox('Are you self employeed'.title() , ['No' , 'Yes'])
    
    ApplicantIncome = st.slider('what is your income'.title() , min_value=150.0 , max_value=81000.0 , step=100.0)
    
    CoapplicantIncome = st.slider('what is your CoapplicantIncome'.title() , min_value=0.0 , max_value=41667.0 , step=100.0)
    
    LoanAmount = st.slider('what is your LoanAmount'.title() , min_value=9.0 , max_value=700.0 , step=100.0)
        
    Loan_Amount_Term = st.slider('what is your Loan Amount Term' .title(), min_value=12.0 , max_value=480.0 , step=1.0)
    
    Credit_History = st.selectbox('what is your credit history'.title() , [1 , 0])
    
    Property_Area = st.selectbox('what is your Property Area'.title() , ['Urban' ,'Rural' ,'Semiurban'])
    
    return pd.DataFrame(
        data=[ 
            [Gender, Married, Dependents, Education, Self_Employed,
       ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Property_Area]
        ] , 
                 columns=['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area'])
    
test = getInput()
st.dataframe(test)
model = joblib.load('model.h5')

st.write('Accepted' if model.predict(test) == 1 else 'Not Accepted')
