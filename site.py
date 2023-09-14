#Testando o streamlit pela primeira vez, seguindo um tutorial
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Teste Site Streamlit")

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Enzo&Corp ao longo de Maio")
    st.write("GitHub do Enzo Bueno [Clique aqui](https://github.com/EnzoBuen0)")


@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv") 
    return tabela


with st.container():
    st.write("---")
    qtde_dias = st.selectbox("Selecione o período", ["7D", "15D", "21D", "30D"])
    qtde_dias= str(qtde_dias)
    num_dias = int(qtde_dias.replace('D',''))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x="Data", y="Contratos")