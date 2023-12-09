import streamlit as st
import pandas as pd
import numpy as np
import pickle
import random
from PIL import Image  # Import the Image module from the Python Imaging Library (PIL)


# Load the model
with open('random_forest_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)



# Streamlit App Header
st.title('PCOS Prediction using Machine Learning')





col1, col2 = st.columns([8, 1])  # Adjust the ratio as needed

col1.subheader('Department of Computer Science and Engineering, National Institute of Technology Srinagar')


# Display logo in col2
# Department name and logo
col2.image('Unknown.png', width=100) 


import streamlit as st





# Sidebar with user input features
st.sidebar.header('User Input Features')

# Create sliders for numeric features
rr = st.sidebar.slider('RR (breaths/min)', 10, 30, 20)
cycle = st.sidebar.slider('Cycle(R/I)', 0, 10, 5)
marriage_status = st.sidebar.slider('Marriage Status (Yrs)', 0.0, 80.0, 25.0)
fsh_lh = st.sidebar.slider('FSH/LH', 0.0, 1500.0, 50.0)
hip = st.sidebar.slider('Hip(inch)', 10, 60, 10)
amh = st.sidebar.slider('AMH(ng/mL)', 0.0, 50.0, 5.0)
rbs = st.sidebar.slider('RBS(mg/dl)', 50.0, 500.0, 150.0)
follicle_L = st.sidebar.slider('Follicle No. (L)', 0, 500, 50)
follicle_R = st.sidebar.slider('Follicle No. (R)', 0, 500, 50)
avg_f_size = st.sidebar.slider('Avg. F size (L) (mm)', 0.0, 50.0, 15.0)

# Create radio buttons for yes/no fields
pregnant = st.sidebar.radio('Pregnant(Y/N)', ['No', 'Yes'])
weight_gain = st.sidebar.radio('Weight gain(Y/N)', ['No', 'Yes'])
hair_growth = st.sidebar.radio('Hair growth(Y/N)', ['No', 'Yes'])
hair_loss = st.sidebar.radio('Hair loss(Y/N)', ['No', 'Yes'])
pimples = st.sidebar.radio('Pimples(Y/N)', ['No', 'Yes'])

# Map radio button values to 0 and 1
pregnant = 0 if pregnant == 'Yes' else 1
weight_gain = 0 if weight_gain == 'Yes' else 1
hair_growth = 0 if hair_growth == 'Yes' else 1
hair_loss = 0 if hair_loss == 'Yes' else 1
pimples = 0 if pimples == 'Yes' else 1

# Create a dictionary with user input
user_input = {
    'RR (breaths/min)': [rr],
    'Cycle(R/I)': [cycle],
    'Marraige Status (Yrs)': [marriage_status],  # Corrected feature name
    'Pregnant(Y/N)': [pregnant],
    'FSH/LH': [fsh_lh],
    'Hip(inch)': [hip],
    'AMH(ng/mL)': [amh],
    'RBS(mg/dl)': [rbs],
    'Weight gain(Y/N)': [weight_gain],
    'hair growth(Y/N)': [hair_growth],
    'Hair loss(Y/N)': [hair_loss],
    'Pimples(Y/N)': [pimples],
    'Follicle No. (L)': [follicle_L],
    'Follicle No. (R)': [follicle_R],
    'Avg. F size (L) (mm)': [avg_f_size]
}

# Create a DataFrame from the user input
user_df = pd.DataFrame(user_input)

# Display the user input
st.subheader('User Input:')
st.write(user_df)

# Make predictions using the loaded model
prediction = loaded_model.predict(user_df)

if st.button('Submit'):
    # Make predictions using the loaded model
    prediction = loaded_model.predict(user_df)
    # Display the prediction
    st.subheader('Prediction:')
    
    if prediction[0] == 0:
        st.write('Our analysis suggests a potential indication of Polycystic Ovary Syndrome (PCOS). While our model achieves up to 96.55% accuracy in predicting PCOS, it is essential to consult with a qualified healthcare professional for a comprehensive examination and accurate diagnosis. Your health is our priority, and professional guidance will provide you with the necessary insights and care.')
    else:
        st.write("While the analysis strongly suggests the absence of Polycystic Ovary Syndrome (PCOS), it is recommended to consult a healthcare professional only if symptoms persist. Your health is our priority, and we encourage seeking medical advice for a more thorough evaluation if necessary.")


# Footer

# Footer
footer = """
<style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        padding: 10px;
        text-align: center;
    }

</style>
<div class="footer">
    <p>Project by <a href="https://www.linkedin.com/in/shivam-krishana-22a239228/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=in">SHIVAM KRISHANA</a> | 2020BCSE011 | Under the Supervision of <a href="https://nitsri.ac.in/Pages/FacultyProfile.aspx?nEmpID=iog&nDeptID=cs">Dr. Sparsh Sharma</a></p></div>
"""
st.markdown(footer, unsafe_allow_html=True)
