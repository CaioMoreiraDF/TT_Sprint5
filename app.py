import pandas as pd
import streamlit as st
import plotly.express as px

# abrir arquivo de dados em um DataFrame
df_vehicles = pd.read_csv(r"C:\Users\ADM\TripleTen\TT_Sprint5\vehicles.csv")

# cabeçalho do app
st.header('Anúncios de Carros')

# criação de opções para caixa de seleção
build_histogram = st.checkbox('Criar Histograma')
build_graph = st.checkbox('Criar Gráfico de Dispersão')

if build_histogram: # se o histograma for escolhido
    # escreva a mensagem
    st.write('Criando um histograma dos anúncios de carros')

    # criar o histograma
    fig = px.histogram(df_vehicles, x="odometer")

    # Exibir gráfico plotly interativo
    st.plotly_chart(fig, width='stretch')

if build_graph: # se o gráfico for escolhido
    # escrever mensagem
    st.write('Criando Gráfico de Dispersão')

    # criar gráfico
    fig2 = px.scatter(df_vehicles, x='odometer', y='price')
    st.plotly_chart(fig2)