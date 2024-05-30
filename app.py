import pandas as pd
import streamlit as st
from PIL import Image

st.title('Análisis de datos de Sensores en huerta urbana #1')
image = Image.open('Graph.png')
st.image(image)

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)
    
    st.subheader('Contenido del archivo cargado')
    st.write(df1.head())
    #st.write('Columnas del DataFrame:', df1.columns.tolist())  # Muestra las columnas del DataFrame
    
    if 'time' in df1.columns:
        st.subheader('Perfil gráfico de la variable medida.')
        df1 = df1.set_index('time')
        st.line_chart(df1)

        st.subheader('Estadísticos básicos de los sensores.')
        st.dataframe(df1.describe())
        

        st.subheader("Temperaturas superiores al valor configurado.")
        min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=0, max_value=45, value=23, key=1)
        # Filtrar el DataFrame utilizando query
        filtrado_df_min = df1.query(f"`Temperatura` > {min_temp}")
        # Mostrar el DataFrame filtrado
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_min)
        

        st.subheader("Humedades ambiente superiores al valor configurado.")
        max_hum = st.slider('Selecciona valor máximo del filtro ', min_value=0, max_value=100, value=23, key=3)
        # Filtrar el DataFrame utilizando query
        filtrado_df_max = df1.query(f"`Humedad` > {max_hum}")
        # Mostrar el DataFrame filtrado
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)

        st.subheader("Humedades del sustrato superiores al valor configurado.")
        max_humSus = st.slider('Selecciona valor máximo del filtro ', min_value=0, max_value=100, value=23, key=2)
        # Filtrar el DataFrame utilizando query
        filtrado_df_max = df1.query(f"`Humedad Sustrato` > {max_humSus}")
        # Mostrar el DataFrame filtrado
        st.write('Dataframe Filtrado')
        st.write(filtrado_df_max)
    else:
        st.error("La columna 'time' no existe en el archivo cargado. Por favor, verifica el archivo.")
else:
    st.warning('Necesitas cargar un archivo csv excel.')
