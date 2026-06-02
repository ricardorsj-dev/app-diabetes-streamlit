import streamlit as st

st.set_page_config(
    page_title="Analisador de Diabetes",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Analisador de Diabetes")

st.write("""
Sistema para avaliação glicêmica e análise de alimentos.

Utilize o menu lateral para navegar entre as páginas:
- 👤 Avaliação do Paciente
- 🥗 Análise de Alimentos
- 📊 Dashboard
""")

st.success("Aplicação carregada com sucesso!")