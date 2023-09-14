#Testando o streamlit pela primeira vez, seguindo um tutorial
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Barras")




@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("resultados.csv") 
    return tabela

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre os contratos fechados pela Enzo&Corp ao longo de Maio")
    st.write("GitHub do Enzo Bueno [Clique aqui](https://github.com/EnzoBuen0)")
    


with st.container():
    st.write("---")
    st.write("Exibindo Gráfico de Barras:")
    dados = carregar_dados()
    st.bar_chart(dados, x="Data", y="Contratos")
            

    



    






