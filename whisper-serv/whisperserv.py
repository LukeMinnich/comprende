import time
import torch

start = time.time()
import whisper
end = time.time()
print(f"Finished importing whisper in {(end - start):2.3}s")

start = time.time()
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("tiny").to(device)
end = time.time()
print(f"Finished loading model in {(end - start):2.3}s")

def transcribe(file: str) -> str:
    start = time.time()
    result = model.transcribe(file)["text"]
    end = time.time()
    print(f"Transcribed in {(end - start):2.3}s")
    return result


from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(transcribe(post_data.decode()).encode())

httpd = HTTPServer(('localhost', 8000), SimpleHandler)
print("Server running on http://localhost:8000")
httpd.serve_forever()
