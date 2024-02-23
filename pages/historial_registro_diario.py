import streamlit as st
import sqlite3

def historial_registro_diario():
    st.title('Registro Habitos')
    conn = sqlite3.connect("bd/HabitosDB.db")
    cursor = conn.cursor()

    query = """
            select date(SEG.FECHA_REGISTRO) as 'DATE()', HAB.DESCRIPCION, HAB.COLOR
            from SEGUIMIENTOHABITOS SEG
            INNER JOIN HABITOS HAB ON SEG.ID_HABITO = HAB.ID_HABITO
            WHERE SEG.ESTADO = True
            ORDER BY SEG.FECHA_REGISTRO DESC
            """
    
    cursor.execute(query)

    rowsSeg = cursor.fetchall()
    fecha_pivot = rowsSeg[0][0]
    print("fecha pivot", fecha_pivot)
    elemento_html = f'<div style="background-color:white; color: black; padding: 10px; margin: 5px; border-radius: 5px;"> {rowsSeg[0][0]}'
    print(len(rowsSeg))
    cont = 0
    while cont < len(rowsSeg):
        if rowsSeg[cont][0] == fecha_pivot:
            elemento_html = elemento_html + f' <span style="background-color: {rowsSeg[cont][2]}">{rowsSeg[cont][1]}</span> '
            cont += 1
        else:
            elemento_html = elemento_html + '</div>'
            st.markdown(elemento_html, unsafe_allow_html=True)
            elemento_html = f'<div style="background-color:white; color: black; padding: 10px; margin: 5px; border-radius: 5px;"> {rowsSeg[cont][0]}'
            fecha_pivot = rowsSeg[cont][0]
    conn.close()
    