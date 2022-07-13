
from turtle import color, fillcolor
import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

interactive=st.container()
st.title('Cancer Rate Evolution Over The Years')

df=pd.read_csv("C:/Users/sarwa/OneDrive/Documents/SPU/DS620/streamlit/cancer/cancerdata.csv")

background_color='#F5F5F5'

with interactive:
    st.title('A closer look into the data')

    fig=go.Figure(data=go.Table(header=dict(values=list(df[['Year', 'AgeGroup', 'PctDiagnosed']].columns),
    fill_color='#FD8E72', align='center'), cells=dict(values=[df.Year, df.AgeGroup, df.PctDiagnosed],
    fill_color='#E5ECF6', align='left')))

    fig.update_layout(margin=dict(l=5,r=5,b=10,t=10),
    paper_bgcolor=background_color)

    st.write(fig)




fig=px.pie(df, values="PctDiagnosed", names="Race")
st.write(fig)

year_options=df['Year'].unique().tolist()
year=st.selectbox('Which year would you like to see?', year_options, 0)
#df=df[df['Year']==year]

st.title('How does the rates vary by race?')
fig=px.scatter(df, x="Race", y="PctDiagnosed", animation_frame="Year")
fig.update_layout(width=800)
st.write(fig)


st.title('What effect does age group have?')
fig=px.scatter(df, x="AgeGroup", y="PctDiagnosed", color = "Race", animation_frame="Year")
fig.update_layout(width=800)
st.write(fig)


df=pd.read_csv("C:/Users/sarwa/OneDrive/Documents/SPU/DS620/streamlit/cancer/cancerbysex.csv")

st.title('Is there a diffence in pattern between male and female?')
fig=px.line(df, x="Year", y="AgeAdjustedRatePer100000", color="Sex")
fig.update_xaxes(type="category")
st.write(fig)
