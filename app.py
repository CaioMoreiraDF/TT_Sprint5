import pandas as pd
import streamlit as st
import plotly.express as px

# abrir arquivo de dados em um DataFrame
df_vehicles = pd.read_csv("C:\\Users\\ADM\\TripleTen\\TT_Sprint5\\vehicles_us.csv")

# cabeçalho do app
st.header('Comparativo de Preço de Veículos Anunciados')

# criação de opções para caixa de seleção
build_histogram = st.checkbox('Criar Histograma de Preço dos Veículos')
build_graph = st.checkbox('Criar Gráfico de Preço x Ano do Modelo')

if build_histogram: # se o histograma for escolhido
    # escreva a mensagem
    st.write('Criando um histograma dos preços dos veículos anunciados')

    # criar o histograma
    fig = px.histogram(df_vehicles, x="price")

    # Exibir gráfico plotly interativo
    st.plotly_chart(fig, width='stretch')

if build_graph: # se o gráfico for escolhido
    # escrever mensagem
    st.write('Criando Gráfico comparativo de preço por ano de modelo')

    # criar gráfico
    fig2 = px.scatter(df_vehicles, x='price', y='model_year')
    st.plotly_chart(fig2)