import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
    
st.title('Open Pub Web Application 	:clinking_glasses:')
image = Image.open('image.png')
st.image(image)

st.header(':violet[About the Dataset]')
st.markdown('##### Sample 5 rows from the dataset.. ')
df = pd.read_csv('data/cleaned_data.csv')
st.dataframe(df.head())

st.markdown('##### Shape of the dataset..')
st.write('Rows :',df.shape[0])
st.write('Columns :',df.shape[1])

st.markdown('##### :violet[According to the dataset, Total] :red[50,563 Pubs] :violet[are active in United Kingdom.]')

st.markdown('##### Descriptive statistics summary of dataset:')
st.write(df.describe())