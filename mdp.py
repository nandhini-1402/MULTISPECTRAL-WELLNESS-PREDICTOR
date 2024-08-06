# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 23:31:04 2024

@author: saila
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import joblib

diabetes_model = pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/parkinsons_model.sav','rb'))

breast_cancer_model=joblib.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/breast_cancer_model.sav','rb'))

lung_cancer_model=pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/lung_cancer_model.sav','rb'))

#sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Lung Cancer Prediction',
                           'Breast Cancer Prediction',
                           'Tips'
                          ],
                          icons=['activity','heart','person','activity','person','align-top'],
                          default_index=0)
 
    

    # Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1: 
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Sorry!! You have diabetes,Take Care!'
        else:
          diab_diagnosis = 'NO !! You are Healthy!!'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Sorry,You might have a Heart disease!! Kindly take care of yourself'
          
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "Sorry!! You might have a parkinsons disease.Take Care"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    

    
    # Lung Cancer Prediction Page
if (selected == "Lung Cancer Prediction"):
    
    # page title
    st.title("Lung Cancer Prediction using ML")
    
    col1, col2, col3 = st.columns(3)  
    
        
    with col1:
        yel = st.number_input('YELLOW_FINGERS')
        
    with col2:
        anx = st.number_input('ANXIETY')
        
    with col3:
        pee = st.number_input('PEER_PRESSURE')
        
    with col1:
        chr = st.number_input('CHRONIC DISEASE')
        
    with col2:
        fat = st.number_input('FATIGUE ')
        
    with col3:
        all = st.number_input('ALLERGY ')
        
    with col1:
        whe = st.number_input('WHEEZING')
        
    with col2:
        alc = st.number_input('ALCOHOL CONSUMING')
        
    with col3:
        cou = st.number_input('COUGHING')
        
    with col1:
        sho = st.number_input('SHORTNESS OF BREATH')
        
    with col2:
        swa = st.number_input('SWALLOWING DIFFICULTY')
        
    with col3:
        che = st.number_input('CHEST PAIN')
     
        
    # code for Prediction
    lung_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Lung Cancer Test Result"):
        lung_prediction = lung_cancer_model.predict([[yel, anx, pee, chr, fat,all,whe,alc,cou,sho,swa,che]])                          
        
        if (lung_prediction[0] == 1):
          lung_diagnosis = "Sorry!! You might have a lung cancer.Take Care"
        else:
          lung_diagnosis = "The person does not have lung cancer"
        
    st.success(lung_diagnosis)
    
    # Breast Cancer Prediction
if (selected == "Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
        
    with col1:
        ef = st.number_input('id')
        
    with col2:
        gh = st.number_input('radius_mean') 
        
    with col3:
        a = st.number_input('texture_mean')
        
    with col4:
        b = st.number_input('perimeter_mean')
        
    with col5:
        c = st.number_input('area_mean')
        
    with col1:
        d = st.number_input('smoothness_mean')
        
    with col2:
        e = st.number_input('compactness_mean')
        
    with col3:
        f = st.number_input('concavity_mean ')
        
    with col4:
        g = st.number_input('concave points_mean')
        
    with col5:
        h = st.number_input('symmetry_mean')
        
    with col1:
        i = st.number_input('fractal_dimension_mean')
        
    with col2:
        j = st.number_input('radius_se')
        
    with col3:
        k = st.number_input('texture_se')
        
    with col4:
        l = st.number_input('perimeter_se')

    with col5:
        m = st.number_input('area_se')
        
    with col1:
        n = st.number_input('smoothness_se')
        
    with col2:
        o = st.number_input('concavity_se')
        
    with col3:
        p = st.number_input('concave points_se')
        
    with col4:
        q = st.number_input('symmetry_se')
        
    with col5:
        r = st.number_input('fractal_dimension_se')
        
    with col1:
        s = st.number_input('radius_worst')
        
    with col2:
        t = st.number_input('texture_worst')
        
    with col3:
        u = st.number_input('perimeter_worst')
        
    with col4:
        v = st.number_input('area_worst')
        
    with col5:
        w = st.number_input('smoothness_worst')
        
    with col1:
        x = st.number_input('compactness_worst')

    with col2:
        y = st.number_input('concavity_worst')
        
    with col3:
        z = st.number_input('concave points_worst')
        
    with col4:
        ab = st.number_input('symmetry_worst')
        
    with col5:
        bcd = st.number_input('fractal_dimension_worst')
        


     # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer_model.predict([[ef,gh,a, b, c, d, e, f, g, h, i, j, k, l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,ab,bcd]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "Sorry!! You might have a breast cancer.Take Care"
        else:
          breast_cancer_diagnosis = "The person does not have breast cancer"
        
    st.success(breast_cancer_diagnosis)
    
# Tips page
if selected == 'Tips':
    # Page title
    st.title('Tips')

    # Placeholder for tips
    tips = {}

    # Define tips for each disease
    tips = {
        'Diabetes Tips': "Whole Grains  \nVegetables  \nLean Proteins  \nHealthy Fats  \nFruits in Moderation  \nLow-Fat Dairy  \nPortion Control  \nLimit Processed Foods  \nHydration  \nRegular Meal Timing",
        'Heart Disease Tips': "Fruits and Vegetables \nWhole Grains  \nLean Proteins  \nHealthy Fats  \nLow-Fat Dairy  \nLimit Sodium \nPortion Control  \nOmega-3 Fatty Acids  \nHydration  \nLimit Alcohol  \nFiber-Rich Foods",
        'Parkinsons Disease Tips':"Antioxidant-Rich Foods  \nOmega-3 Fatty Acids  \nProtein Sources  \nWhole Grains  \nHydration  \nVitamin-D  \nCalcium-Rich Foods \nLimit Processed Foods  \nB-Vitamins  \nLimit Saturated and Trans Fats",
        'Lung Cancer Tips':"High-Calorie, High-Protein Foods  \nFruits and Vegetables  \nWhole Grains  \nHealthy Fats  \nHydration  \nSmall, Frequent Meals  \nLimit Salt Intake  \nAvoid Highly Processed Foods  \nDiscuss Dietary Supplements  \nAddress Specific Needs",
        'Breast Cancer Tips':"High-Quality Protein  \nWhole Grains  \nHealthy Fats  \nHydration  \nLimit Processed Foods and Added Sugars \nCalcium and Vitamin D  \nSmall, Frequent Meals \nRegular Physical Activity  \nAdequate Sleep \nStress Management  \nSupport System  \nLimit Alcohol Intake"
    
    }

    # Display tips based on user selection
    selected_tip = st.selectbox('Select a tip category', list(tips.keys()))
    st.write(tips[selected_tip])
    
    
    
#background image
import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load the first image
img_base64_1 = get_img_as_base64(r"C:\Users\91959\Desktop\PROJECT\ELITE\MULTIPLE DISEASE PREDICTION\image1.webp")

# Load the second image
img_base64_2 = get_img_as_base64(r"C:\Users\91959\Desktop\PROJECT\ELITE\MULTIPLE DISEASE PREDICTION\image3.webp")

# Define the CSS styles with the two images
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_base64_1}");
background-size: cover; /* Cover the entire container */
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img_base64_2}");
background-size: cover; /* Cover the entire container */
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

# Display the CSS styles
st.markdown(page_bg_img, unsafe_allow_html=True)



    
    
             


    
    





    
    
             


    
    

