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

# CSS para REMOVER TUDO e ocupar tela cheia
st.markdown("""
    <style>
        /* Remove TODOS os elementos do Streamlit */
        header, footer, .stAppDeploymentButton, .stToolbar, .stDecoration,
        #MainMenu, .st-emotion-cache-1dp5vir, .st-emotion-cache-1wrcr25,
        .st-emotion-cache-1v0mbdj, .st-emotion-cache-1r6slb0,
        .st-emotion-cache-1wmy9hl, .st-emotion-cache-16txtl3,
        .st-emotion-cache-1v7f65g, .st-emotion-cache-1p1m4ay,
        .st-emotion-cache-1y4p8pa, .st-emotion-cache-12oz5g7,
        [data-testid="stHeader"], [data-testid="stFooter"],
        [data-testid="stToolbar"], [data-testid="stDecoration"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            min-height: 0 !important;
            max-height: 0 !important;
            padding: 0 !important;
            margin: 0 !important;
            position: absolute !important;
            top: -9999px !important;
            left: -9999px !important;
        }
        
        /* Remove margens e padding do app */
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            background-color: #fcf5ec !important;
        }
        
        .main {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            width: 100% !important;
        }
        
        /* Remove qualquer espaço */
        [data-testid="stAppViewContainer"] {
            background-color: #fcf5ec !important;
            padding: 0 !important;
            margin: 0 !important;
            width: 100% !important;
        }
        
        /* Ajuste do iframe para ocupar tela toda */
        iframe {
            width: 100% !important;
            height: 100vh !important;
            min-height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            border: none !important;
        }
        
        /* Zoom fixo */
        body {
            zoom: 0.75;
            -moz-transform: scale(0.75);
            -moz-transform-origin: 0 0;
            overflow: hidden;
            margin: 0 !important;
            padding: 0 !important;
            background-color: #fcf5ec !important;
        }
        
        /* Remove scroll do body */
        html, body {
            overflow: hidden;
            height: 100%;
        }
        
        /* Garante que o container do app ocupe tudo */
        .stApp > div {
            width: 100% !important;
            height: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# Função para converter imagem para base64
def get_image_base64(image_path):
    caminho = Path(image_path)
    if caminho.exists():
        with open(caminho, "rb") as img_file:
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
        img_base64 = get_image_base64(img)
        
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

# Carrega e exibe
html_content = load_html()

if html_content:
    st.components.v1.html(
        html_content, 
        height=800, 
        scrolling=True,
        width=None
    )
