import streamlit as st
import pandas as pd
from pathlib import Path

st.title("👤 Avaliação do Paciente")

nome = st.text_input("Nome")

glicose = st.number_input(
    "Glicose (mg/dL)",
    min_value=0.0
)

if st.button("Avaliar"):

    if glicose < 100:
        status = "Normal"
        st.success("Glicose normal")

    elif glicose <= 125:
        status = "Pré-diabetes"
        st.warning("Pré-diabetes")

    else:
        status = "Diabetes"
        st.error("Diabetes")

    novo = pd.DataFrame([{
        "nome": nome,
        "glicose": glicose,
        "status": status
    }])

    arquivo = Path("usuarios.csv")

    if arquivo.exists():

        historico = pd.read_csv("usuarios.csv")

        historico = pd.concat(
            [historico, novo],
            ignore_index=True
        )

    else:

        historico = novo

    historico.to_csv(
        "usuarios.csv",
        index=False
    )

    st.success("Paciente registrado com sucesso!")