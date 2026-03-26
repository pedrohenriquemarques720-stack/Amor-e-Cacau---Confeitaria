import streamlit as st
from pathlib import Path
import base64

# Configuração da página
st.set_page_config(
    page_title="Amor Cacau",
    page_icon="🍫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS para esconder elementos do Streamlit
st.markdown("""
    <style>
        /* Esconde cabeçalho, rodapé e menu */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        .stAppDeploymentButton {display: none;}
        .stToolbar {display: none;}
    </style>
""", unsafe_allow_html=True)

# Função para ler e converter imagens
def carregar_html():
    # Caminho do arquivo
    arquivo_html = Path("pascoa.html")
    
    if not arquivo_html.exists():
        st.error("❌ Arquivo pascoa.html não encontrado!")
        return None
    
    # Lê o HTML
    with open(arquivo_html, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Lista de imagens
    imagens = [
        'static/brigadeiro.png.jpeg',
        'static/avela.png.jpeg',
        'static/sensacao.png.jpeg',
        'static/maracuja.png.jpeg',
        'static/prestigio.png.jpeg',
        'static/trufado.png.jpeg',
        'static/tablet.png.jpeg'
    ]
    
    # Converte imagens para base64
    for img in imagens:
        caminho = Path(img)
        if caminho.exists():
            with open(caminho, "rb") as f:
                dados = base64.b64encode(f.read()).decode()
                html = html.replace(f'src="{img}"', f'src="data:image/jpeg;base64,{dados}"')
    
    return html

# Carrega e mostra o HTML
html_content = carregar_html()

if html_content:
    st.components.v1.html(html_content, height=1200, scrolling=True)
