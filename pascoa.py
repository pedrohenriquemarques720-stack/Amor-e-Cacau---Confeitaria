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

# JavaScript para remover o rodapé e outros elementos
st.markdown("""
    <script>
        // Função para remover elementos chatos
        function removerElementos() {
            // Remove o rodapé
            const footer = document.querySelector('footer');
            if (footer) footer.remove();
            
            // Remove o cabeçalho
            const header = document.querySelector('header');
            if (header) header.remove();
            
            // Remove o botão Manage App
            const deployBtn = document.querySelector('.stAppDeploymentButton');
            if (deployBtn) deployBtn.remove();
            
            // Remove a barra de ferramentas
            const toolbar = document.querySelector('.stToolbar');
            if (toolbar) toolbar.remove();
            
            // Remove qualquer elemento com texto "Manage app"
            const allElements = document.querySelectorAll('*');
            allElements.forEach(el => {
                if (el.innerText === 'Manage app' || el.innerText === 'Manage app ') {
                    el.remove();
                }
            });
        }
        
        // Executa quando a página carregar
        setTimeout(removerElementos, 100);
        setTimeout(removerElementos, 500);
        setTimeout(removerElementos, 1000);
        
        // Observa mudanças na página
        const observer = new MutationObserver(function(mutations) {
            removerElementos();
        });
        observer.observe(document.body, { childList: true, subtree: true });
    </script>
""", unsafe_allow_html=True)

# CSS para esconder tudo
st.markdown("""
    <style>
        /* Esconde elementos */
        footer, header, .stAppDeploymentButton, .stToolbar, 
        #MainMenu, .st-emotion-cache-1dp5vir, .st-emotion-cache-1wrcr25,
        [data-testid="stHeader"], [data-testid="stFooter"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            height: 0 !important;
            width: 0 !important;
            position: absolute !important;
            top: -9999px !important;
            left: -9999px !important;
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
        
        /* Ajuste do iframe */
        iframe {
            width: 100% !important;
            height: 100vh !important;
            min-height: 100vh !important;
            border: none !important;
        }
        
        /* Zoom */
        body {
            zoom: 0.75;
            -moz-transform: scale(0.75);
            -moz-transform-origin: 0 0;
            overflow-x: hidden;
            margin: 0;
            padding: 0;
        }
        
        /* Remove espaços extras */
        .main {
            margin-bottom: -100px !important;
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
        height=900, 
        scrolling=True,
        width=None
    )
