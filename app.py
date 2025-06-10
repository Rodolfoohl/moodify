import os
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'

# Garante que a pasta de uploads exista
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    """Renderiza a página inicial com o formulário de upload."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Recebe o arquivo enviado, executa o whisper e exibe a transcrição."""
    file = request.files.get('audio')
    if not file:
        return 'Nenhum arquivo enviado', 400

    # Salva o arquivo enviado na pasta de uploads
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Comando para executar o whisper localmente
    command = [
        'whisper',
        filepath,
        '--model', 'medium',
        '--language', 'pt'
    ]
    # Executa o whisper e aguarda finalizar
    subprocess.run(command, check=True)

    # O whisper gera um arquivo .txt com a transcrição
    transcript_path = os.path.splitext(filepath)[0] + '.txt'

    # Lê o conteúdo do arquivo de transcrição
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcription = f.read()

    # Retorna o texto transcrito em uma página simples
    return render_template('result.html', transcription=transcription)

if __name__ == '__main__':
    app.run(debug=True)
