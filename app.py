import streamlit as st
import plotly.express as px
from dataset import df

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("Dashboard de Vendas :shopping_trolley:")

tab1, tab2, tab3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])

with tab1:
    st.dataframe(df)
