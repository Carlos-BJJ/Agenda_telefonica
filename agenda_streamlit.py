"""
agenda_streamlit.py
Interface gráfica (Streamlit) para o CRUD da Agenda Telefônica.
Usa as funções já existentes em menu_agenda.py — nenhuma lógica de banco
é reescrita aqui, só a camada visual.

Instalação necessária:
    pip install streamlit

Como rodar (streamlit não roda com "python arquivo.py"):
    streamlit run agenda_streamlit.py
"""

import streamlit as st

from menu_agenda import (
    adicionar,
    listar,
    buscar,
    editar,
    remover,
)

st.set_page_config(page_title="Agenda Telefônica", page_icon="📇", layout="centered")

st.title("📇 Agenda Telefônica")

# Estado: guarda o contato selecionado para edição

if "nome_selecionado" not in st.session_state:
    st.session_state.nome_selecionado = ""
if "telefone_selecionado" not in st.session_state:
    st.session_state.telefone_selecionado = ""
if "email_selecionado" not in st.session_state:
    st.session_state.email_selecionado = ""


def selecionar_contato(nome, telefone, email):
    st.session_state.nome_selecionado = nome
    st.session_state.telefone_selecionado = telefone
    st.session_state.email_selecionado = email or ""


def limpar_selecao():
    st.session_state.nome_selecionado = ""
    st.session_state.telefone_selecionado = ""
    st.session_state.email_selecionado = ""


# -----------------------------------------------------
# Formulário (Adicionar / Editar / Remover)
st.subheader("Contato")

with st.form("form_contato", clear_on_submit=False):
    nome = st.text_input("Nome", value=st.session_state.nome_selecionado)
    telefone = st.text_input("Telefone", value=st.session_state.telefone_selecionado)
    email = st.text_input("Email", value=st.session_state.email_selecionado)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        clicou_adicionar = st.form_submit_button("Adicionar", use_container_width=True)
    with col2:
        clicou_editar = st.form_submit_button("Editar", use_container_width=True)
    with col3:
        clicou_remover = st.form_submit_button("Remover", use_container_width=True)
    with col4:
        clicou_limpar = st.form_submit_button("Limpar campos", use_container_width=True)

if clicou_adicionar:
    if not nome.strip() or not telefone.strip():
        st.error("Nome e telefone são obrigatórios.")
    elif adicionar(nome.strip(), telefone.strip(), email.strip() or None):
        st.success(f"Contato '{nome}' adicionado.")
        limpar_selecao()
        st.rerun()
    else:
        st.error(f"Já existe um contato com o nome '{nome}'.")

if clicou_editar:
    if not nome.strip():
        st.error("Informe o nome do contato a editar.")
    elif editar(nome.strip(), telefone.strip() or None, email.strip() or None):
        st.success(f"Contato '{nome}' atualizado.")
        limpar_selecao()
        st.rerun()
    else:
        st.error(f"Contato '{nome}' não encontrado.")

if clicou_remover:
    if not nome.strip():
        st.error("Informe o nome do contato a remover.")
    elif remover(nome.strip()):
        st.success(f"Contato '{nome}' removido.")
        limpar_selecao()
        st.rerun()
    else:
        st.error(f"Contato '{nome}' não encontrado.")

if clicou_limpar:
    limpar_selecao()
    st.rerun()

st.divider()

# -----------------------------------------------------
# Busca + listagem
st.subheader("Contatos")

termo_busca = st.text_input("🔎 Buscar por nome", value="")
dados = buscar(termo_busca.strip()) if termo_busca.strip() else listar()

if not dados:
    st.info("Nenhum contato encontrado.")
else:
    for nome_c, telefone_c, email_c in dados:
        col_nome, col_tel, col_email, col_btn = st.columns([3, 2, 3, 1.3])
        col_nome.write(nome_c)
        col_tel.write(telefone_c)
        col_email.write(email_c or "—")
        if col_btn.button("Selecionar", key=f"sel_{nome_c}"):
            selecionar_contato(nome_c, telefone_c, email_c)
            st.rerun()