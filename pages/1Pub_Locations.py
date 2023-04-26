import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Pub Locations"
)

df = pd.read_csv('data/cleaned_data.csv')
st.title('Pub Locations :round_pushpin:')


loc_opt = df['local_authority'].unique()
title=st.selectbox("Select Local Authority - ", loc_opt)

fetching_local_data = df.loc[df.local_authority == title,['latitude','longitude']]
st.map(fetching_local_data)

fetching_local_name = df.loc[df.local_authority == title,['name','address']].reset_index(drop=True)
st.markdown('###### :blue[Name and Address of Pubs in this Area : ]')
st.dataframe(fetching_local_name)

 