import streamlit as st
import pandas as pd
import sqlite3

# def colorear_celda(val):
#     return f'background-color: {val}'

def lista_categorias():
    st.title('Lista categorias')
    conn = sqlite3.connect("bd/HabitosDB.db")
    cursor = conn.cursor()
    
    query = """
            SELECT ID_CATEGORIAHABITOS, 
            DESCRIPCION,  
            ESTADO,
            COLOR,
            CASE 
                WHEN ESBUENO = 1 THEN 'SI' 
                WHEN ESBUENO = 0 THEN 'NO'
            END AS ESBUENO 
            FROM CATEGORIA_HABITOS
            WHERE ESTADO = True AND ID_USUARIO = 1
            """ 
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        elemento_html = f'<div style="background-color:{row[3]}; padding: 10px; margin: 5px; border-radius: 5px;">{row[1]}</div>'
        st.markdown(elemento_html, unsafe_allow_html=True)
    conn.close()