import streamlit as st
import sqlite3
from pages.nuevo_habito import fetchCategoriaHabitos
from pages.lista_habitos import getListaHabitosAll


def registrar_habitos_diarios():
    conn = sqlite3.connect("bd/HabitosDB.db")
    cursor = conn.cursor()
    st.title('Registro Habitos')
    lista_habitos = getListaHabitosAll(conn, cursor)
    valores_habitos = []
    for habito in lista_habitos:
        valores_habitos.append(habito["value"])


    with st.form("my_form"):
        options = st.multiselect("Registro habitos", valores_habitos)
        saveBtn = st.form_submit_button('Submit my picks')
        
        