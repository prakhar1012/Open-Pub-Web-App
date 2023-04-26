import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Nearest Pub"
)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/7130555/pexels-photo-7130555.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

df = pd.read_csv('data/cleaned_data.csv')
st.title('Nearest Pubs :beers:')


lat = st.number_input('Enter Latitude')
lon = st.number_input('Enter Longitude')
button = st.button("Nearest Pubs")
df_new = df[['latitude', 'longitude']]
new_points = np.array([lat, lon])

# Euclidean distance 
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))

n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.markdown("##### 5 Nearest Pubs from your Location : ")
    st.dataframe(df.iloc[min_indices])
    st.markdown("##### Minimum distances: ")
    st.dataframe(distances.head(5))
    st.map(df.iloc[min_indices])



