import streamlit as st
import pandas as pd
import sqlite3

# def colorear_celda(val):
#     return f'background-color: {val}'

def lista_categorias():
    st.title('Lista categorias')
    conn = sqlite3.connect("bd/HabitosDB.db")
    
    query = """
            SELECT ID_CATEGORIAHABITOS, 
            DESCRIPCION,  
            ESTADO,
            COLOR,
            CASE 
                WHEN ESBUENO = 1 THEN 'SI' 
                WHEN ESBUENO = 0 THEN 'NO'
            END AS ESBUENO 
            from CATEGORIA_HABITOS
            """ 
    df = pd.read_sql(query,conn)
    
    st.dataframe(df)
    conn.close()