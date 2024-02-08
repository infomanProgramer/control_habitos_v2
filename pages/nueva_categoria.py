import streamlit as st
import sqlite3
from pages.Utils.libraryBD import addNewItemDB
from pages.Utils.libraryBD import createObjectDB
#Variables globales

nuevaCategoria = {}



# def getConnectionSQLite():
#     conn = sqlite3.connect("InternetSpeed.db")
#     cursor = conn.cursor()

def nueva_categoria():
    st.title('Nueva Categoria')

    descripcion_habito = st.text_input('Descripcion')
    esBueno = st.toggle('Es bueno')
    color = st.color_picker('Pick A Color', '#00f900')
    resp = st.button("Guardar", type="primary")
    nuevaCategoria = []
    if resp:
        conn = sqlite3.connect("bd/HabitosDB.db")
        cursor = conn.cursor()
        nuevaCategoria.append(createObjectDB("DESCRIPCION", descripcion_habito, "T"))
        nuevaCategoria.append(createObjectDB("ESTADO", True, "B"))
        nuevaCategoria.append(createObjectDB("COLOR", color, "T"))
        nuevaCategoria.append(createObjectDB("ESBUENO", esBueno, "B"))
        nuevaCategoria.append(createObjectDB("ID_USUARIO", 1, "I"))
        cursor.execute(addNewItemDB("CATEGORIA_HABITOS", nuevaCategoria))
        conn.commit()
        conn.close()
