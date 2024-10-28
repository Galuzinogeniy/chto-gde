from http.server import HTTPServer, SimpleHTTPRequestHandler

class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Добавляем необходимые заголовки для Godot 4
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        SimpleHTTPRequestHandler.end_headers(self)

# Запускаем сервер на порту 8000
httpd = HTTPServer(('localhost', 8000), Handler)
print("Сервер запущен на http://localhost:8000")
httpd.serve_forever()