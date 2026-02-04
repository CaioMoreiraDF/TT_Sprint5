import streamlit as st
import pandas as pd
import plotly.express as px

# abrir arquivo de dados em um DataFrame
df_vehicles = pd.read_csv(r"C:\Users\ADM\TripleTen\TT_Sprint5\vehicles.csv")

# cabeçalho do app
st.header('Anúncios de Carros')

# Botão de criação do histograma
hist_button = st.button('Criar histograma')

if hist_button: # se o botão for clicado
    # escreva a mensagem
    st.write('Criando um histograma dos anúncios de carros')

    # criar o histograma
    fig = px.histogram(df_vehicles, x="odometer")

    # Exibir gráfico plotly interativo
    st.plotly_chart(fig, use_container_width=True)

