import streamlit as st
from pathlib import Path
import base64

# Configuração da página - MODO CLEAN TOTAL
st.set_page_config(
    page_title="Amor Cacau - Páscoa Gourmet",
    page_icon="🍫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS PARA REMOVER ABSOLUTAMENTE TUDO
hide_streamlit_style = """
    <style>
        /* Remove TODOS os elementos do Streamlit */
        #MainMenu {display: none !important;}
        footer {display: none !important;}
        header {display: none !important;}
        .stAppDeploymentButton {display: none !important;}
        
        /* Remove qualquer espaço branco */
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            background-color: #fcf5ec;
        }
        
        .main {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .block-container {
            margin: 0 !important;
            padding: 0 !important;
            max-width: 100% !important;
        }
        
        /* Remove qualquer elemento que possa aparecer */
        .css-1y4p8pa, .css-12oz5g7, .css-1dp5vir, .css-1wrcr25 {
            display: none !important;
        }
        
        /* Garante que o fundo ocupe tudo */
        .stApp, .main, div[data-testid="stAppViewContainer"] {
            background-color: #fcf5ec !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Remove aquele "Manage app" */
        .st-emotion-cache-1dp5vir, .st-emotion-cache-1wrcr25 {
            display: none !important;
        }
        
        /* Ajuste de zoom global */
        body {
            zoom: 0.75;
            -moz-transform: scale(0.75);
            -moz-transform-origin: 0 0;
            overflow-x: hidden;
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

# Carrega o HTML e substitui as imagens por base64
def load_html():
    html_path = Path("pascoa.html")
    
    if not html_path.exists():
        st.error("❌ Arquivo pascoa.html não encontrado!")
        return None
    
    # Lê o conteúdo do HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Lista de todas as imagens
    imagens = [
        'brigadeiro.png.jpeg',
        'avela.png.jpeg',
        'sensacao.png.jpeg', 
        'maracuja.png.jpeg',
        'prestigio.png.jpeg',
        'trufado.png.jpeg',
        'tablet.png.jpeg'
    ]
    
    # Substitui cada imagem pelo base64
    for img in imagens:
        img_path = Path("static") / img
        img_base64 = get_image_base64(img_path)
        
        if img_base64:
            # Substitui no HTML (com e sem aspas)
            html_content = html_content.replace(
                f'src="{img}"', 
                f'src="data:image/jpeg;base64,{img_base64}"'
            )
            html_content = html_content.replace(
                f"src='{img}'", 
                f"src='data:image/jpeg;base64,{img_base64}'"
            )
    
    return html_content

# Carrega o HTML com as imagens em base64
html_content = load_html()

if html_content:
    # Renderiza o HTML - AGORA SEM NENHUMA BARRA
    st.components.v1.html(
        html_content, 
        height=1200, 
        scrolling=True,
        width=None
    )
else:
    st.error("❌ Erro ao carregar o cardápio. Verifique os arquivos.")
