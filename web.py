import streamlit as st
import base64
import os

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Puppeteer Modding Wiki", layout="wide")

# --- FUNCIÓN MEJORADA PARA BUSCAR IMÁGENES ---
def cargar_imagen(nombre_base):
    # Esto buscará el nombre con todas las combinaciones posibles de extensiones
    posibilidades = [
        nombre_base, 
        nombre_base + ".png", 
        nombre_base + ".jpg", 
        nombre_base + ".jpeg",
        nombre_base + ".PNG",
        nombre_base + ".JPG",
        nombre_base + ".png.png", # Por si Windows duplicó la extensión
        nombre_base + ".jpg.jpg"
    ]
    for ruta in posibilidades:
        if os.path.exists(ruta):
            return ruta
    return None

# --- CONFIGURACIÓN DE FONDO Y COLORES ---
def set_bg_hack(main_bg):
    ruta_fondo = cargar_imagen(main_bg)
    if ruta_fondo:
        with open(ruta_fondo, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/png;base64,{encoded_string});
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            .main-container {{
                background-color: rgba(0, 0, 0, 0.85);
                padding: 25px;
                border-radius: 15px;
                margin-bottom: 25px;
                border: 1px solid #ffcc00;
            }}
            /* FUERZA TODO EL TEXTO A BLANCO */
            html, body, [data-testid="stWidgetLabel"], .stMarkdown, p, li, span, h1, h2, h3, div {{
                color: white !important;
            }}
            /* TÍTULOS Y NEGRILLAS EN DORADO */
            h1, h2, h3, strong {{
                color: #ffcc00 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Ejecutar fondo (busca un archivo llamado 'fondo')
set_bg_hack('fondo') 

st.title("🎭 Puppeteer PS3 Modding Project")

# --- SECCIÓN 1: INTRODUCCIÓN ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("introduccion")
        if img: st.image(img, use_container_width=True)
        else: st.warning("⚠️ No se halló 'introduccion'")
    with col_txt:
        st.header("Bienvenido a la página de información de modder de Puppeteer para PS3")
        st.write("""
        El día de hoy diré lo que he descubierto sobre el **dddd.img** del juego 
        (archivo en donde están modelos 3D, texturas, animaciones, etc). 
        
        **Ojo:** esto es mi conclusión. Si tú tienes tu propia conclusión, bien. 
        
        Bueno, comencemos:
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN 2: ¿QUÉ ES EL DDDD.IMG? ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_info")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_info'")
    with col_txt:
        st.subheader("📊 ¿Qué es el archivo dddd.img?")
        st.write("""
        **dddd.img** es un archivo de Puppeteer el cual pesa **1.3 GB**. Contiene los modelos 3D, 
        texturas y animaciones de todo el juego. 
        
        En el motor **PhyreEngine**, Japan Studio puso todos estos recursos en este único archivo 
        contenedor masivo para que el juego los cargue durante la partida.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN 3: CÓMO USAR HXD ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_hxd")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_hxd'")
    with col_txt:
        st.subheader("🛠️ Cómo usar HxD en el dddd.img")
        st.write("""
        Para usar **dddd.img** en **HxD** tenemos que descargar el programa en su página oficial. 
        Una vez instalado, simplemente arrastramos el archivo **dddd.img** dentro del programa. 
        
        Aquí podremos ver los valores hexadecimales y las cadenas de texto que nos permiten 
        identificar dónde empiezan los modelos y las texturas del juego.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN 4: COMO LEER EL ARCHIVO CORRECTAMENTE ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_settings")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_hxd'")
    with col_txt:
        st.subheader("🛠️ COMO LEER EL ARCHIVO CORRECTAMENTE")
        st.write("""
        1) al iniciar el archivo veremos algo de **stereo 3d setting** todo esto de texto descodificado no es relevante. ya que solo se trata de configuraciones 3d de profundidad del escenario, camara etc.
        """)
    st.markdown('</div>', unsafe_allow_html=True)


# --- SECCIÓN 5: COMO LEER EL ARCHIVO CORRECTAMENTE ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_nombres")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_hxd'")
    with col_txt:
        st.subheader("🛠️ Nombres de objetos")
        st.write("""
        2)  mas abajo donde vemos **Lt_CS_CUT1 Lt_CS_CUT3 Lt_CS_GetLight1** etc, podemos ver ya los nombres de posibles modelos 3d.animaciones o texturas incluyendo personajes, escenario y fondos, **OJO** solo los nombres nada mas.
        """)
    st.markdown('</div>', unsafe_allow_html=True)


# --- SECCIÓN 5: COMO LEER EL ARCHIVO CORRECTAMENTE ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_cordenadas")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_cordenadas'")
    with col_txt:
        st.subheader("🛠️ lo mas importante (mas abajo en el archivo)")
        st.write("""
        3) al bajar mas podemos ver lo siguiente: son letras "aleatorias" pues no lo son, esto literalmente es el **esqueleto de todo**, aqui esta todo lo de los modelos de una forma que solo el ps3 reconoce gracias a diferentes funciones que hizo **japan studio** aqui esta las cordenadas X, Y, Z, vertices,esqueletos,animaciones, texturas y mas. 

**IMPORTANTE**

si deseas extraer todo esto. es un poco dificil, ya que tienes que indentificar el **offset** donde inicia y termina cada bloque de cada objeto. siguiendo todo lo del objeto. como resultado. tendras probablemente el modelo 3d con su textura o una animacion. esto aun no ha sido posible.
        """)
    st.markdown('</div>', unsafe_allow_html=True)


# --- SECCIÓN 5: COMO LEER EL ARCHIVO CORRECTAMENTE ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_p")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_cordenadas'")
    with col_txt:
        st.subheader("🛠️ P y I")
        st.write("""
        4) para terminar tenemos en algunos bloques de letras aleatorias, el inicio con varias **P** que significa esto? hasta el momento y mis concluciones es para separar los bloques de cada objeto. luego de mas nombres de objetos y puntos podremos ver esto. pero esto es totalmente diferente al paso anterior. ya que saldran las cordenadas vertices etc pero de otra forma. un poco mas dificil de desifrar. el bloque de letras locas termina con muchas **I**
        """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECCIÓN 5: COMO LEER EL ARCHIVO CORRECTAMENTE ---
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    col_img, col_txt = st.columns([1, 2])
    with col_img:
        img = cargar_imagen("archivo_i")
        if img: st.image(img, use_container_width=True)
        else: st.info("ℹ️ No se halló 'archivo_cordenadas'")
    with col_txt:
        st.subheader("🛠️ FOTO DE QUE TERMINA EN MUCHAS I")
        st.write(""" y eso ha sido todo. espero que esta informacion sea util para alguien. si es que quiere extraer o ver lo que contiene el juego fuera de la ps3. **como dije esta es mi conclucion, asi que la informacion puede ser incorrecta** gracias por leer :D""")
    st.markdown('</div>', unsafe_allow_html=True)



st.sidebar.markdown("### Navegación")
st.sidebar.write("Wiki creada por Rad el slime")