import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

st.title('Popular Names')

st.header('Name Trend')
selected_name = st.text_input('Enter a name to plot', 'John')
regex = st.checkbox('Check if your name search is a regular expression')
name_df = df[df['name'] == selected_name]
if name_df.empty:
    st.write('Name not found')
else:
    fig = px.line(name_df, x='year', y='n', color='sex',
                  color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig)

st.header('Popular Names by Year')
year = st.slider('Select Year', 1910, 2021, 2000)

year_df = df[df['year'] == year]

girls_names = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
boys_names = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']

top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], 
          ignore_index=True, axis=1)
top_names.columns = ['Girls','Boys']

st.write(f"Top Names in {year}")

st.dataframe(top_names)