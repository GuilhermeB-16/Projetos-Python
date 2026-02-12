import json
import re
from pathlib import Path

#Definição do caminho do arquivo JSON
BASE_DIR = Path(__file__).resolve().parent.parent.parent
JSON_PATH = BASE_DIR / "dados.json"

def verificar_palavroes(message):
    #Leitura do arquivo JSON
    with open(JSON_PATH, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    
    lista_proibida = dados["PalavrasProibidas"] 

    texto_original = message.content
    texto_limpo = re.sub(r'[^\w\s]', '', texto_original)

    for padrao in lista_proibida:
        match = re.search(padrao, texto_limpo, re.IGNORECASE)
        if match:
            return match.group()
    return None