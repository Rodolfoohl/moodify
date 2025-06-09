# Moodify

Moodify é uma página web simples que detecta e exibe seu humor.

## Como usar

1. Em um terminal, execute `python3 -m http.server` na pasta do projeto para abrir um servidor local.
2. Acesse `http://localhost:8000/index.html` (ou outro endereço seguro/HTTPS) no navegador.
3. Permita o acesso à câmera quando solicitado.
4. Clique em **Detectar Meu Humor** para que a aplicação analise sua expressão facial.
5. O vídeo usado para análise fica oculto na página.

O sistema utiliza a biblioteca [face-api.js](https://github.com/justadudewhohacks/face-api.js) para detectar emoções e ajusta a página conforme o resultado.

É necessária uma conexão com a internet para carregar o script e os modelos utilizados pelo face-api.js a partir do CDN.

## Personalização

Para adicionar ou editar humores ou alterar o mapeamento das expressões faciais, modifique o array `moods` e o objeto `map` em `index.html`.

## Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).


## Transcrição de Áudio

Este projeto também inclui um pequeno servidor Flask para transcrever arquivos MP3 usando o whisper local.

### Executando

1. Instale o Flask e o openai-whisper (ex.: `pip install flask openai-whisper`).
2. Execute `python app.py` na pasta do projeto.
3. Acesse `http://localhost:5000` em seu navegador e envie um arquivo MP3.
4. A transcrição será exibida na tela após o processamento.
