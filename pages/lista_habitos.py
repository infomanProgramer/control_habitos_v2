import streamlit as st
import pandas as pd
import sqlite3

def getListaHabitosById(conn, cursor, id):
    query = """
            select ID_HABITO, DESCRIPCION
            FROM HABITOS
            where ID_CATEGORIAHABITOS = """+str(id)+""" AND ESTADO = 1
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    habitos = []
    for row in rows:
        habitos.append({"key": row[0], "value": row[1]})
    return habitos

def getListaHabitosAll(conn, cursor):
    query = """
            SELECT ID_HABITO, DESCRIPCION FROM HABITOS WHERE ESTADO = 1
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    habitos = []
    for row in rows:
        habitos.append({"key": row[0], "value": row[1]})
    return habitos


def lista_habitos():
    st.title('Lista Habitos')
    conn = sqlite3.connect("bd/HabitosDB.db")
    cursor = conn.cursor()

    query = """
            SELECT C.DESCRIPCION AS CATEGORIA, 
            H.DESCRIPCION AS HABITO,
            H.COLOR
            FROM HABITOS H
            INNER JOIN CATEGORIA_HABITOS C ON H.ID_CATEGORIAHABITOS = C.ID_CATEGORIAHABITOS
            WHERE H.ESTADO = True and C.ESTADO = True AND C.ID_USUARIO = 1
            ORDER BY CATEGORIA, HABITO
            """ 
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        elemento_html = f'<div style="background-color:{row[2]}; padding: 10px; margin: 5px; border-radius: 5px;">{row[1]}</div>'
        st.markdown(elemento_html, unsafe_allow_html=True)
    conn.close()