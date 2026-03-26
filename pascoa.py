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

# JAVASCRIPT PARA REMOVER RODAPÉ E ELEMENTOS FIXOS
st.markdown("""
    <script>
        // Remove o rodapé assim que a página carregar
        setTimeout(() => {
            const footer = document.querySelector('footer');
            if (footer) footer.remove();
            
            const deployButton = document.querySelector('.stAppDeploymentButton');
            if (deployButton) deployButton.remove();
            
            const toolbar = document.querySelector('.stToolbar');
            if (toolbar) toolbar.remove();
            
            // Remove qualquer elemento fixo
            const fixedElements = document.querySelectorAll('[style*="position: fixed"]');
            fixedElements.forEach(el => {
                if (el.tagName !== 'IFRAME') el.remove();
            });
        }, 100);
    </script>
""", unsafe_allow_html=True)

# CSS EXTREMO - REMOVE TUDO
hide_streamlit_style = """
    <style>
        /* Remove todos os elementos do Streamlit */
        #MainMenu {display: none !important;}
        .stAppDeploymentButton {display: none !important;}
        .stToolbar {display: none !important;}
        .stDecoration {display: none !important;}
        .stAlert {display: none !important;}
        .st-emotion-cache-1s5fgy6 {display: none !important;}
        .st-emotion-cache-1dp5vir {display: none !important;}
        .st-emotion-cache-1wrcr25 {display: none !important;}
        .st-emotion-cache-1v0mbdj {display: none !important;}
        .st-emotion-cache-1r6slb0 {display: none !important;}
        
        /* Remove o cabeçalho */
        header {display: none !important;}
        
        /* REMOVE O RODAPÉ COMPLETAMENTE */
        footer {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            height: 0 !important;
            min-height: 0 !important;
            max-height: 0 !important;
            padding: 0 !important;
            margin: 0 !important;
            position: fixed !important;
            bottom: -100px !important;
            left: -100px !important;
            z-index: -9999 !important;
            pointer-events: none !important;
        }
        
        /* Remove o container do rodapé */
        [data-testid="stFooter"] {
            display: none !important;
        }
        
        /* Remove a barra de scroll do rodapé */
        .st-emotion-cache-1v7f65g {
            display: none !important;
        }
        
        /* Ajusta o app para ocupar tela toda */
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            background-color: #fcf5ec !important;
        }
        
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            padding-bottom: 0 !important;
            margin-bottom: 0 !important;
        }
        
        /* Remove qualquer espaço no final */
        .main {
            margin-bottom: -100px !important;
        }
        
        /* Ajusta o iframe para ocupar toda altura */
        iframe {
            height: calc(100vh - 20px) !important;
            min-height: 800px !important;
            margin-bottom: -80px !important;
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
        
        /* Remove qualquer elemento fixo */
        [style*="position: fixed"] {
            display: none !important;
        }
        
        /* Remove qualquer fundo extra */
        [data-testid="stAppViewContainer"] {
            background-color: #fcf5ec !important;
            padding: 0 !important;
            margin: 0 !important;
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
    # Renderiza o HTML
    st.components.v1.html(
        html_content, 
        height=1600, 
        scrolling=True,
        width=None
    )
else:
    st.error("❌ Erro ao carregar o cardápio. Verifique os arquivos.")
