import streamlit as st
import pandas as pd

st.title("🥗 Análise de Alimentos")

try:
    df = pd.read_csv("alimentos.csv")

    alimento = st.selectbox(
        "Selecione um alimento",
        df["nome"].sort_values()
    )

    dados = df[df["nome"] == alimento].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Açúcar (g)", dados["acucar"])
        st.metric("Carboidratos (g)", dados["carboidratos"])

    with col2:
        st.metric("Calorias", dados["calorias"])
        st.metric("Índice Glicêmico", dados["ig"])

    st.divider()

    score = 0

    if dados["acucar"] > 15:
        score += 2

    if dados["carboidratos"] > 30:
        score += 2

    if dados["ig"] >= 70:
        score += 2

    if dados["calorias"] > 300:
        score += 1

    st.subheader("Avaliação")

    if score >= 5:
        st.error("❌ Não recomendado para diabéticos ou pré-diabéticos")

    elif score >= 3:
        st.warning("⚠️ Consumir com moderação")

    else:
        st.success("✅ Recomendado")

    st.info(
        f"Categoria: {dados['categoria']}"
    )

except FileNotFoundError:
    st.error(
        "Arquivo alimentos.csv não encontrado."
    )