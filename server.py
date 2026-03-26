from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Muda para o diretório atual
os.chdir('.')

# Configura o servidor
port = 8501
server = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)

print(f"🍫 Servidor Amor Cacau rodando!")
print(f"📱 Acesse: http://localhost:{port}/pascoa.html")
print(f"❌ Pressione Ctrl+C para parar o servidor")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\n👋 Servidor encerrado.")
