import sqlite3


from pages.lista_categorias import lista_categorias
from pages.lista_habitos import lista_habitos
from pages.nueva_categoria import nueva_categoria
from pages.nuevo_habito import nuevo_habito
import streamlit as st

#@st.cache_resource
#@st.cache_data
def main():

    page_names_to_funcs = {
        "Nueva Categoria": nueva_categoria,
        "Lista Categorias": lista_categorias,
        "Nuevo Habito": nuevo_habito,
        "Lista Habitos": lista_habitos,
    }

    #st.sidebar.radio("Choose a demo", list(page_names_to_funcs.keys()))
    demo_name = st.sidebar.radio("Choose a demo", list(page_names_to_funcs.keys()))
    page_names_to_funcs[demo_name]()

if __name__ == "__main__":
    main()

