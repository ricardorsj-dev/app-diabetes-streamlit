import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📊 Dashboard")

# Verifica se o arquivo existe
if not os.path.exists("usuarios.csv"):
    st.warning("Nenhum paciente cadastrado ainda.")
    st.stop()

# Carrega os dados
df = pd.read_csv("usuarios.csv")

# Verifica se há dados
if df.empty:
    st.warning("O arquivo usuarios.csv está vazio.")
    st.stop()

# =========================
# INDICADORES
# =========================

st.subheader("📈 Indicadores")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total de Pacientes",
    len(df)
)

col2.metric(
    "Média de Glicose",
    round(df["glicose"].mean(), 1)
)

col3.metric(
    "Maior Glicose",
    round(df["glicose"].max(), 1)
)

st.divider()

# =========================
# DISTRIBUIÇÃO DOS DIAGNÓSTICOS
# =========================

st.subheader("🥧 Distribuição dos Diagnósticos")

diagnosticos = pd.DataFrame(
    df["status"].value_counts()
).reset_index()

diagnosticos.columns = [
    "status",
    "quantidade"
]

fig_pizza = px.pie(
    diagnosticos,
    names="status",
    values="quantidade",
    title="Distribuição dos Diagnósticos"
)

st.plotly_chart(
    fig_pizza,
    use_container_width=True
)

st.divider()

# =========================
# GLICOSE POR PACIENTE
# =========================

st.subheader("📊 Glicose por Paciente")

fig_barra = px.bar(
    df,
    x="nome",
    y="glicose",
    title="Nível de Glicose dos Pacientes",
    text="glicose"
)

st.plotly_chart(
    fig_barra,
    use_container_width=True
)

st.divider()

# =========================
# HISTOGRAMA DE GLICOSE
# =========================

st.subheader("📉 Distribuição da Glicose")

fig_hist = px.histogram(
    df,
    x="glicose",
    nbins=10,
    title="Distribuição dos Valores de Glicose"
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

st.divider()

# =========================
# TABELA DE PACIENTES
# =========================

st.subheader("📋 Pacientes Cadastrados")

st.dataframe(
    df,
    use_container_width=True
)