import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Carregar o CSV (substitua 'seuarquivo.csv' pelo nome do seu arquivo)
st.title("Nuvem de Palavras Interativa")

uploaded_file = st.file_uploader("Envie um arquivo CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Selecionar coluna para análise (assumindo que o CSV tem uma coluna chamada 'texto')
    column = st.selectbox("Escolha a coluna de texto", df.columns)
    text = " ".join(df[column].astype(str))
    
    # Gerar a nuvem de palavras
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    # Mostrar a nuvem de palavras
    st.subheader("Nuvem de Palavras")
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
    
    # Barra de pesquisa
    search_query = st.text_input("Buscar palavra")
    if search_query:
        occurrences = text.lower().split().count(search_query.lower())
        st.write(f"A palavra '{search_query}' aparece {occurrences} vezes no texto.")