import streamlit as st
from pathlib import Path
import base64

# Configuração da página
st.set_page_config(
    page_title="Amor Cacau - Páscoa Gourmet",
    page_icon="🍫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS PARA REMOVER O BOTÃO MANAGE APP E TUDO MAIS
hide_streamlit_style = """
    <style>
        /* Remove o botão Manage App */
        .stAppDeploymentButton {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }
        
        /* Remove qualquer elemento de deploy */
        [data-testid="stToolbar"],
        .stToolbar,
        .st-emotion-cache-1dp5vir,
        .st-emotion-cache-1wrcr25 {
            display: none !important;
        }
        
        /* Remove o menu principal */
        #MainMenu {display: none !important;}
        
        /* Remove footer e header */
        footer {display: none !important;}
        header {display: none !important;}
        
        /* Remove a barra superior inteira */
        .stApp > header {
            display: none !important;
        }
        
        /* Remove qualquer elemento flutuante */
        .st-emotion-cache-1v0mbdj,
        .st-emotion-cache-1r6slb0,
        .st-emotion-cache-1wmy9hl {
            display: none !important;
        }
        
        /* Ajusta o container principal */
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            background-color: #fcf5ec !important;
        }
        
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        /* Remove o fundo do app */
        [data-testid="stAppViewContainer"] {
            background-color: #fcf5ec !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Ajuste de zoom */
        body {
            zoom: 0.75;
            -moz-transform: scale(0.75);
            -moz-transform-origin: 0 0;
            overflow-x: hidden;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Remove qualquer espaço extra no topo */
        .main {
            margin-top: -70px !important;
        }
        
        /* Esconde o botão de deploy em todas as telas */
        button[kind="secondary"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Função para converter imagem para base64
def get_image_base64(image_path):
    if Path(image_path).exists():
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# Carrega o HTML
def load_html():
    html_path = Path("pascoa.html")
    
    if not html_path.exists():
        st.error("❌ Arquivo pascoa.html não encontrado!")
        return None
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Imagens
    imagens = [
        'static/brigadeiro.png.jpeg',
        'static/avela.png.jpeg',
        'static/sensacao.png.jpeg', 
        'static/maracuja.png.jpeg',
        'static/prestigio.png.jpeg',
        'static/trufado.png.jpeg',
        'static/tablet.png.jpeg'
    ]
    
    for img in imagens:
        img_path = Path(img)
        img_base64 = get_image_base64(img_path)
        
        if img_base64:
            html_content = html_content.replace(
                f'src="{img}"', 
                f'src="data:image/jpeg;base64,{img_base64}"'
            )
            html_content = html_content.replace(
                f"src='{img}'", 
                f"src='data:image/jpeg;base64,{img_base64}'"
            )
    
    return html_content

html_content = load_html()

if html_content:
    st.components.v1.html(
        html_content, 
        height=1500, 
        scrolling=True,
        width=None
    )
else:
    st.error("❌ Erro ao carregar o cardápio. Verifique os arquivos.")
