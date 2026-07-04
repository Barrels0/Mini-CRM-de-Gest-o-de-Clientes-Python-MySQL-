# 💼 Mini CRM - Gestão de Clientes

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
</p>

Sistema de Gestão de Clientes (CRM) desenvolvido para demonstrar habilidades em **engenharia de software**, integração com bancos de dados relacionais e segurança de aplicações. O foco deste projeto foi criar uma arquitetura modular, escalável e resiliente.

---

## 🚀 Funcionalidades Principais

*   **CRUD Completo:** Operações de Criação, Leitura, Atualização e Deleção.
*   **Segurança Robusta:** Consultas parametrizadas que eliminam vulnerabilidades de *SQL Injection*.
*   **Soft Delete (Exclusão Lógica):** Preservação da integridade histórica dos dados ao marcar registros como inativos em vez de apagá-los permanentemente.
*   **Interface Reativa:** Utilização do *Streamlit* para uma experiência de usuário fluida e intuitiva.
*   **Arquitetura Modular:** Separação de responsabilidades entre conexão, inicialização e interface.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python** | Linguagem principal do sistema |
| **Streamlit** | Framework de interface web |
| **MySQL** | Banco de dados para persistência |
| **Pandas** | Manipulação de dados e exibição de tabelas |
| **Connector** | Driver de comunicação MySQL/Python |

## ⚙️ Instalação e Execução

### 1. Pré-requisitos
Certifique-se de ter instalado:
* [Python 3.x](https://www.python.org/)
* Servidor [MySQL](https://www.mysql.com/) rodando localmente.

### 2. Configuração
Clone o repositório e instale as dependências:
```bash
git clone [https://github.com/Barrels0/Mini-CRM-de-Gest-o-de-Clientes-Python-MySQL-](https://github.com/Barrels0/Mini-CRM-de-Gest-o-de-Clientes-Python-MySQL-)
cd NOME_DO_REPO
pip install -r requirements.txt
crie um arquivo connect.py
import mysql.connector

def obter_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="sua_database"
    )

### 3.Execução
streamlit run main.py