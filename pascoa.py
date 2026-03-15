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

# Função para ler e carregar o HTML com as imagens em base64
def load_html_with_images():
    html_path = Path("pascoa.html")
    
    if not html_path.exists():
        st.error("❌ Arquivo pascoa.html não encontrado!")
        return None
    
    # Lê o conteúdo do HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Converte as imagens para base64 e substitui no HTML
    imagens = [
        'brigadeiro.png.jpeg',
        'avela.png.jpeg', 
        'sensacao.png.jpeg',
        'maracuja.png.jpeg',
        'prestigio.png.jpeg',
        'trufado.png.jpeg',
        'tablet.png.jpeg'
    ]
    
    for img in imagens:
        img_path = Path("static") / img
        if img_path.exists():
            with open(img_path, "rb") as f:
                data = base64.b64encode(f.read()).decode()
                # Substitui o src da imagem no HTML
                html_content = html_content.replace(
                    f'src="{img}"', 
                    f'src="data:image/jpeg;base64,{data}"'
                )
                html_content = html_content.replace(
                    f"src='{img}'", 
                    f"src='data:image/jpeg;base64,{data}'"
                )
    
    return html_content

# Carrega o HTML com as imagens
html_content = load_html_with_images()

if html_content:
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.warning("⚠️ Verifique se o arquivo pascoa.html e as imagens estão na pasta correta.")

st.markdown("---")
st.caption("🍬 Amor Cacau - Cardápio de Páscoa")