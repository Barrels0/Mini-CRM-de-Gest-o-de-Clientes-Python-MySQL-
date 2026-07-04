#streamlit run main.py
from bnc_dados import inicializar
import streamlit as st
from connect import obter_conexao
import mysql.connector
import pandas as pd

inicializar()
st.title("💼 Mini CRM - Gestão de Clientes")
st.success("Banco de dados conectado e tabela criada com sucesso!")
    
try:
    conexao = obter_conexao()
    cursor = conexao.cursor()
    with st.expander("Novo Cliente!"):
        st.subheader("Cadastro!")
        with st.form(key="form_cadastro"):
            nome = st.text_input("Nome completo *")
            email = st.text_input("E-mail *")
            telefone = st.text_input("Telefone")
            botao_cadastrar = st.form_submit_button("Cadastrar Cliente")
        if botao_cadastrar:
            if nome == "" or email == "":
                st.warning("Por favor. Preencha o Nome e E-mail (são obrigatórios!)")
            else:
                cursor.execute("INSERT INTO clientes (nome,email,telefone) VALUES (%s,%s,%s)",(nome,email,telefone,))
                conexao.commit()
                st.success("Cliente cadastrado com sucesso!")
            
    st.divider()
    with st.expander("📋 Lista de Clientes"):
        st.subheader("Nossos clientes:")
        cursor.execute("SELECT id,nome,email,telefone FROM clientes WHERE ativo = 1")
        clientes_bnc = cursor.fetchall()
        if len (clientes_bnc) == 0:
            st.info("Nenhum cliente cadastrado!")
        else:
            df_clientes = pd.DataFrame(clientes_bnc, columns=["ID", "Nome", "E-mail", "Telefone"])
            st.dataframe(df_clientes, hide_index=True, use_container_width=True)
    st.divider()
    with st.expander("❌ Excluir Cliente"):
        st.subheader("❌ Excluir Cliente")
        with st.form(key="form_excluir"):
            id_excluir = st.number_input("Digite o ID do cliente que deseja excluir",min_value=1, step=1)
            botao_excluir = st.form_submit_button("Excluir cliente")
        if botao_excluir:
            cursor.execute("UPDATE clientes SET ativo = 0 WHERE id = %s",(id_excluir,))
            conexao.commit()
            st.success("Cliente excluido com sucesso!")
            st.rerun()
    st.divider()
    with st.expander("✏️ Atualizar Cliente"):
        st.subheader("✏️ Atualizar Cliente")
        with st.form(key="form_editar"):
            id_editar = st.number_input("ID do Cliente que será editado", min_value=1, step=1)

            st.write("Digite os novos dados do cliente: ")
            novo_nome = st.text_input("Novo Nome *")
            novo_email = st.text_input("Novo E-mail *")
            novo_telefone = st.text_input("Novo Telefone")
            
            botao_editar = st.form_submit_button("Atualizar cadastro!")
        if botao_editar:
            if novo_nome == "" or novo_email =="":
                st.warning("Por favor, preencha o Novo Nome e Novo E-mail!")
            else:
                cursor.execute("UPDATE clientes SET nome = %s, email = %s, telefone = %s WHERE id = %s AND ativo = 1",(novo_nome,novo_email,novo_telefone,id_editar))
                conexao.commit()
                if cursor.rowcount > 0: #rowcount conta quantas linhas do mysql foram alteradas!
                    st.success("Dados do cliente atualizados com sucesso!")
                    st.rerun()
                else:
                    st.error("ERRO: ID não encontrado ou cliente inativo!")
except mysql.connector.Error as e:
    st.warning(f"Ocorreu um erro no banco de dados: {e}")
finally:
    cursor.close()
    conexao.close()
