import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
#import sklearn

@st.cache_data
def get_fvalue(val):    
    feature_dict = {"No":1,"Yes":2}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value

def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
            return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages
st.title ("This is a Home Loan Prediction page")
st.caption("Useing Scikit Learn Random Forest Classifier")
APPROVED = 1

if app_mode=='Home':   
    st.title('LOAN PREDICTION :')      
    st.image('loan.png')    
    st.markdown('Dataset :')    
    data=pd.read_csv('data/loan_sanction_test.csv', low_memory=False)
    st.write(data.head())    
    st.markdown('Applicant Income VS Loan Amount ')    
    st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))
elif app_mode == 'Prediction':    
    #st.image('slider-short-3.jpg')    
    st.subheader('YOU need to fill all necessary informations in order    to get a reply to your loan request !')    
    st.sidebar.header("Informations about the client :")    
    gender_dict = {"Male":1,"Female":2}    
    feature_dict = {"No":1,"Yes":2}    
    edu={'Graduate':1,'Not Graduate':2}    
    prop={'Rural':1,'Urban':2,'Semiurban':3}    
    ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)    
    CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)    
    LoanAmount=st.sidebar.slider('LoanAmount in K$',9.0,700.0,200.0)    
    Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))    
    Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))    
    Gender=st.sidebar.radio('Gender',tuple(gender_dict.keys()))    
    Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))    
    Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))    
    Dependents=st.sidebar.radio('Dependents',options=['0','1' , '2' , '3+'])    
    Education=st.sidebar.radio('Education',tuple(edu.keys()))    
    Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))   
   # class_0 , class_3 , class_1,class_2 = 0,0,0,0   
    dependents_class = 0 
    if Dependents == '0':        
        dependents_class = 0   
    elif Dependents == '1':        
        dependents_class = 1    
    elif Dependents == '2' :        
        dependents_class = 2    
    else:        
        dependents_class = 3    
    
    Rural,Urban,Semiurban=0,0,0    
    if Property_Area == 'Urban' :        
        Urban = 1    
    elif Property_Area == 'Semiurban' :        
        Semiurban = 1    
    else :        
        Rural=1

    if st.button("Predict"):
        file_ = open("6m-rain.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
   
        file = open("green-cola-no.gif", "rb")
        contents = file.read()
        data_url_no = base64.b64encode(contents).decode("utf-8")
        file.close()

        print("-Preparing input-")

        # assign data of lists.  
        #data = {'Married': get_fvalue(Married), 'Dependents': dependents_class, \
        #        'Education': get_value(Education,edu), 'Self_Employed':get_fvalue(Self_Employed), \
        #        'LoanAmount': LoanAmount, 'Loan_Amount_Term': Loan_Amount_Term, \
        #        'Credit_History': Credit_History, 'Total_Income':  ApplicantIncome + CoapplicantIncome, \
        #        'Gender_Male': get_value(Gender,gender_dict), 'PA_Semiurban': Semiurban, \
        #        'PA_Urban': Urban } 

        
        #df = pd.DataFrame(data, index=[0])
        #print(type(df))
        #print(df.head())

        feature_list=[get_fvalue(Married), \
                     dependents_class, \
                     get_value(Education,edu), \
                     get_fvalue(Self_Employed), \
                     LoanAmount, \
                     Loan_Amount_Term, \
                     Credit_History, \
                     ApplicantIncome + CoapplicantIncome, \
                     get_value(Gender,gender_dict), \
                     Semiurban, \
                     Urban
                    ]
        # convert to 1D
        single_sample = np.array(feature_list).reshape(1,-1)
        #print(type(feature_list))
        print(type(single_sample))
   
        pickled_model = pickle.load(open('models/model.pkl', 'rb'))
        prediction = pickled_model.predict(single_sample) # use numpy
        #prediction = pickled_model.predict(df) # use dataframe
        print("{0} prediction={1}".format(type(prediction),prediction[0]))

        if prediction[0] == APPROVED :
            st.success(
    'Congratulations!! you will get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,)
        else:
            st.error(
    'According to our Calculations, you will not get the loan from Bank'
    )
            st.markdown(
    f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',
    unsafe_allow_html=True,)
    