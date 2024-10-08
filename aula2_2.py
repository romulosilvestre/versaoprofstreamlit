
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title('DASHBOARD DE VENDAS :shopping_trolley:')

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

st.data_editor(dados)
