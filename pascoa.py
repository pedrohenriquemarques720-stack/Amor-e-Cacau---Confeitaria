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

# CSS EXTREMO - REMOVE ABSOLUTAMENTE TODOS OS ELEMENTOS
hide_streamlit_style = """
    <style>
        /* Remove TODOS os elementos do Streamlit */
        #MainMenu {display: none !important;}
        footer {display: none !important;}
        header {display: none !important;}
        .stAppDeploymentButton {display: none !important;}
        .stToolbar {display: none !important;}
        .stDecoration {display: none !important;}
        .stAlert {display: none !important;}
        
        /* Remove o botão Manage App e tudo relacionado */
        button[kind="secondary"] {display: none !important;}
        [data-testid="baseButton-header"] {display: none !important;}
        [data-testid="stToolbar"] {display: none !important;}
        .st-emotion-cache-1dp5vir {display: none !important;}
        .st-emotion-cache-1wrcr25 {display: none !important;}
        .st-emotion-cache-1v0mbdj {display: none !important;}
        .st-emotion-cache-1r6slb0 {display: none !important;}
        .st-emotion-cache-1wmy9hl {display: none !important;}
        .st-emotion-cache-16txtl3 {display: none !important;}
        .st-emotion-cache-1v7f65g {display: none !important;}
        .st-emotion-cache-1p1m4ay {display: none !important;}
        .st-emotion-cache-1y4p8pa {display: none !important;}
        .st-emotion-cache-12oz5g7 {display: none !important;}
        
        /* Remove o cabeçalho inteiro */
        header[data-testid="stHeader"] {
            display: none !important;
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Remove a barra superior */
        .stApp > header {
            display: none !important;
            height: 0 !important;
        }
        
        /* Remove qualquer espaço no topo */
        .stApp {
            margin-top: -80px !important;
            background-color: #fcf5ec !important;
        }
        
        /* Ajusta o container principal */
        .main {
            margin-top: -70px !important;
        }
        
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        /* Remove fundo padrão */
        [data-testid="stAppViewContainer"] {
            background-color: #fcf5ec !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Remove o rodapé fixo */
        footer {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            position: fixed !important;
            bottom: -100px !important;
        }
        
        /* Ajuste de zoom */
        body {
            zoom: 0.75;
            -moz-transform: scale(0.75);
            -moz-transform-origin: 0 0;
            overflow-x: hidden;
            margin: 0 !important;
            padding: 0 !important;
            background-color: #fcf5ec !important;
        }
        
        /* Remove qualquer iframe extra */
        iframe {
            margin-top: -70px !important;
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
    
    return html_content

html_content = load_html()

if html_content:
    # Usa HTML com altura que compensa o espaço removido
    st.components.v1.html(
        html_content, 
        height=1600, 
        scrolling=True,
        width=None
    )
