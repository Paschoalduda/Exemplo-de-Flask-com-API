import os

#Diretórios para arquivo JSON

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FILE = os.path.join(BASE_DIR, "models", "data", "dados.json")

#Diretório para upload de imagem
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads", "image")
