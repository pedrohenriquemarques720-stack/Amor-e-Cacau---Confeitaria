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

# Função para ler e carregar o HTML
def load_html():
    html_path = Path("pascoa.html")
    
    # Verifica se o arquivo existe
    if not html_path.exists():
        st.error("❌ Arquivo pascoa.html não encontrado!")
        st.info("Certifique-se de que o arquivo está na mesma pasta que este script Python.")
        return None
    
    # Lê o conteúdo do HTML
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    return html_content

# Função para obter imagens como base64 (se necessário)
def get_image_base64(image_path):
    if Path(image_path).exists():
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# Carrega o HTML
html_content = load_html()

if html_content:
    # Se quiser garantir que as imagens funcionem mesmo em subpastas,
    # você pode processar o HTML para incluir base64 ou ajustar caminhos
    
    # Opção 1: Renderizar o HTML diretamente (mais simples)
    st.components.v1.html(html_content, height=1200, scrolling=True)
    
    # Opção 2: Se precisar ajustar caminhos das imagens (descomente se necessário)
    # html_content = html_content.replace('src="', 'src="./')
    # st.components.v1.html(html_content, height=1200, scrolling=True)
    
else:
    st.warning("⚠️ Coloque o arquivo pascoa.html na mesma pasta deste script.")

# Informação adicional
st.markdown("---")
st.caption("🍬 Amor Cacau - Cardápio de Páscoa")
