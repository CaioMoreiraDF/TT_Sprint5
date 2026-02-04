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
    st.plotly_chart(fig, width='stretch')

# botao de criação do gráfico de dispersão
chart_button = st.button('Criar Gráfico de Dispersão')

if chart_button: # se o botão for clicado
    # escrever mensagem
    st.write('Criando Gráfico de Dispersão')

    # criar gráfico
    fig2 = px.scatter(df_vehicles, x='odometer', y='price')
    st.plotly_chart(fig2)
