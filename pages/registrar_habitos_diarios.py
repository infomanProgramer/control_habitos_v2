import streamlit as st
import sqlite3
from pages.nuevo_habito import fetchCategoriaHabitos
from pages.lista_habitos import getListaHabitosAll
from pages.Utils.libraryBD import addNewItemDB
from pages.Utils.libraryBD import createObjectDB


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
        saveBtn = st.form_submit_button('Guardar')
        optionsIndex = []
        if saveBtn:
            print(options)
            for option in options:
                for habito in lista_habitos:
                    if habito["value"] == option:
                        optionsIndex.append(habito["key"])
            print(optionsIndex)
            for optionsI in optionsIndex:
                registroHabitos = []
                registroHabitos.append(createObjectDB("ID_HABITO", optionsI, "I"))
                registroHabitos.append(createObjectDB("ESTADO", True, "B"))
                registroHabitos.append(createObjectDB("FECHA_REGISTRO", "datetime('now', 'localtime')", "I"))
                cursor.execute(addNewItemDB("SEGUIMIENTOHABITOS", registroHabitos))
            conn.commit()
            conn.close()
            

        