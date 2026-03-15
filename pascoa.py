import streamlit as st
from pathlib import Path
import base64

# Configuração da página - AGORA SEM BORDAS
st.set_page_config(
    page_title="Amor Cacau - Páscoa Gourmet",
    page_icon="🍫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS PARA REMOVER TODAS AS BORDAS BRANCAS E AJUSTAR ZOOM
hide_streamlit_style = """
    <style>
        /* Remove elementos do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Remove todas as bordas brancas e padding */
        .stApp {
            margin-top: -80px;
            background-color: #fcf5ec;
        }
        
        .main > div {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        
        /* Remove qualquer fundo branco */
        .stApp, .main, .css-1y4p8pa, .css-12oz5g7 {
            background-color: #fcf5ec !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Ajuste de zoom global */
        body {
            zoom: 0.75;
            -moz-transform: scale(0.75);
            -moz-transform-origin: 0 0;
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
    # Renderiza o HTML - AGORA SEM BORDAS
    st.components.v1.html(
        html_content, 
        height=1200, 
        scrolling=True,
        width=None  # Isso faz ocupar toda largura
    )
else:
    st.error("❌ Erro ao carregar o cardápio. Verifique os arquivos.")
