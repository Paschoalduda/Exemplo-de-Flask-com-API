import os
import json
import config
import requests
import uuid

# Lista de usuários armazenada na memória
usuarios = []

#-- Funções para manipular arquivos
def load_data():
    """Carrega os dados do arquivo JSON."""
    if not os.path.exists(config.DATA_FILE):
        return []
    with open(config.DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    """Salva os dados no arquivo JSON."""
    with open(config.DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

#---------------------------------------------------------------------------------------------------
# Funções para interagir com a API
API_KEY = "215a27be3da7c8535b6d59ea2b6ebfcf"

def escolhaS(opcao):   
    url = "https://api.themoviedb.org/3/discover/tv"
    
    generos = {
        'kids': 10762,
        'drama': 18,
        'comedy': 35,
        "Documentary": 99,
        "Reality": 10764,
        "Mystery": 9648,
    }

    genero_id = generos.get(opcao)
    parametros = {
        "api_key": API_KEY,
        "with_genres": genero_id,
        "language": "pt-BR",
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        series = resposta.json().get("results", [])
        mensagem = f"Séries de {opcao}"
    else:
        series = []
        mensagem = "Erro ao buscar as séries."

    return series, mensagem


#---------------------------------------------------------------------------------------------------
# Funções de gerenciamento de usuários
def novoUsuario(usuario, senha):
    """Adiciona um novo usuário à lista de usuários."""
    usuarioExistente = False
    for u in usuarios:
        if u['usuario'] == usuario:
            save_data(usuarios)
            usuarioExistente = True
            break
    if usuarioExistente:
        return False
    usuarios.append({"usuario": usuario, "senha": senha})
    return True    

def logandoUsuario(usuario, senha):
    """Verifica se o usuário e senha são válidos."""
    for u in usuarios:
        if usuario == u["usuario"] and senha == u["senha"]:
            return True
    return False

#---------------------------------------------------------------------------------------------------
#----------------- Função para upload de imagem---------------#

#-- Função para verificar formato de imagem
def verificarArquivos(imagem):
	return ('.' in imagem.filename and imagem.filename.rsplit('.', 1)[1].lower() in config.TIPOS_IMAGEM)
    #Verifica se o arquivo está em um dos formatos permitidos 

#-- Função para upload de imagem
def upload_imagem(imagem):  
    # Garante que a pasta de upload exista
    os.makedirs(config.UPLOAD_FOLDER, exist_ok=True) #garante que o diretório upload existe ou, caso contrário, ele é criado
    
    if (imagem.filename == ''):
        return (None)
    elif (not verificarArquivos(imagem)):
        return (None)
    else:
        # Gera um nome ÚNICO para a imagem e salva no diretório de uploads
        filename = f"{uuid.uuid4()}.{imagem.filename.rsplit('.', 1)[1].lower()}"
        filepath = os.path.join(config.UPLOAD_FOLDER, filename)
        imagem.save(filepath)
        return (f"uploads/image/{filename}") 
        # Caminho relativo para salvar no JSON, junto ao dados do contato	
