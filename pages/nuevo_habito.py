import streamlit as st
import sqlite3
from pages.Utils.libraryBD import addNewItemDB
from pages.Utils.libraryBD import createObjectDB


def fetchCategoriaHabitos(conn, cursor):
    query = """
            SELECT ID_CATEGORIAHABITOS, 
            DESCRIPCION
            from CATEGORIA_HABITOS
            """ 
    cursor.execute(query)
    rows = cursor.fetchall()
    categoria = []
    for row in rows:
        categoria.append({"key": row[0], "value": row[1]})
    return categoria

def nuevo_habito():
    conn = sqlite3.connect("bd/HabitosDB.db")
    cursor = conn.cursor()
    st.title('Nuevo habito')
    categoria_habitos = fetchCategoriaHabitos(conn, cursor)
    valores = []
    for categoria in categoria_habitos:
        valores.append(categoria["value"])
    with st.form("my_form"):
        categoriaElegidaValor = st.selectbox('Seleccionar un categoria',valores)
        categoriaElegidaClave = -1
        for categoriah in categoria_habitos:
            if categoriah["value"] == categoriaElegidaValor:
                categoriaElegidaClave = categoriah["key"]
        descripcion_habito = st.text_input('Descripcion')
        color = st.color_picker('Pick A Color')
        saveBtn = st.form_submit_button('Submit my picks')

    nuevoHabito = []
    if saveBtn:
        nuevoHabito.append(createObjectDB("DESCRIPCION", descripcion_habito, "T"))
        nuevoHabito.append(createObjectDB("ESTADO", True, "B"))
        nuevoHabito.append(createObjectDB("COLOR", color, "T"))
        nuevoHabito.append(createObjectDB("ID_CATEGORIAHABITOS", categoriaElegidaClave, "I"))
        cursor.execute(addNewItemDB("HABITOS", nuevoHabito))
        conn.commit()
        conn.close()