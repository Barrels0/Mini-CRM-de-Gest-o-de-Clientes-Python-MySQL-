import os, mysql.connector
from dotenv import load_dotenv
load_dotenv()
def obter_conexao():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
            port=os.getenv("PORT")
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"\n[✖] ERRO: Falha ao conectar ao banco de dados: {erro}")
        return None