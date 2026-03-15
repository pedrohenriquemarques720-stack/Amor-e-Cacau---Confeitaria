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

# Esconde elementos padrão do Streamlit
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { margin-top: -80px; }
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
    # Renderiza o HTML
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.error("❌ Erro ao carregar o cardápio. Verifique os arquivos.")

# Rodapé
st.markdown("---")
st.caption("🍬 Amor Cacau - Cardápio de Páscoa")
