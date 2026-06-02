# 🩺 Analisador de Diabetes

Aplicação web desenvolvida com Python e Streamlit para auxiliar na avaliação glicêmica de pacientes e análise de alimentos com foco em diabetes.

## 🚀 Funcionalidades

### 👤 Avaliação do Paciente

* Cadastro de pacientes
* Classificação automática da glicemia
* Identificação de:

  * Normal
  * Pré-diabetes
  * Diabetes
* Armazenamento dos dados em arquivo CSV

### 🥗 Análise de Alimentos

* Consulta de alimentos cadastrados
* Visualização de:

  * Teor de açúcar
  * Carboidratos
  * Calorias
  * Índice glicêmico
* Recomendação automática para diabéticos

### 📊 Dashboard Interativo

* Total de pacientes cadastrados
* Média glicêmica
* Maior nível de glicose registrado
* Distribuição dos diagnósticos
* Gráficos interativos com Plotly
* Histórico completo dos pacientes

---

## 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Plotly

---

## 📂 Estrutura do Projeto

```bash
app-diabetes/
│
├── app.py
├── alimentos.csv
├── usuarios.csv
├── requirements.txt
│
└── pages/
    ├── 1_Avaliacao_Paciente.py
    ├── 2_Analise_Alimentos.py
    └── 3_Dashboard.py
```

---

## ▶️ Executando Localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

---

## 🌐 Deploy

Aplicação hospedada no Streamlit Community Cloud.

---

## 📈 Próximas Melhorias

* Banco de dados SQLite
* Sistema de login
* API para consulta de alimentos
* Exportação de relatórios PDF
* Machine Learning para previsão de risco glicêmico
* Dashboard avançado com filtros

---

## 👨‍💻 Autor

Ricardo Rodrigues dos Santos Junior

Desenvolvedor Python em formação, focado em análise de dados, automação e desenvolvimento de aplicações web.
