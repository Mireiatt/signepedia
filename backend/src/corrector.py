import requests
import logging
from src import cercador

# Obtenim les correccions ortogràfiques d'una "paraula" a través de LanguageTool.
# Si no hi ha correcció, retornem "None".
# En cas de no podernos connectar al servidor, creem un log amb informacio al respecte.
# Cal evitar saturar el servidor.


def create_log(paraula,req,resposta,missatge):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
    log_filename = paraula
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logging.error(paraula + "/" + req + "/" + resposta + "/" + missatge)

def get_correccio(paraula):
    try:
        req = requests.get("https://languagetool.org/api/v2/check?text=" + paraula + "&language=ca&enabledOnly=false")
        resposta = req.json()["matches"][0]
        missatge = resposta["shortMessage"]
        correccions = resposta["replacements"]
        if (correccions) and missatge == "Error ortogràfic":
            paraules = []
            for correccio in correccions:
                paraules.append(correccio["value"])
            return paraules
        return None
    except:
        create_log(paraula,req,resposta,missatge)

# Retornem un mapa amb la possible correcció d'una "paraula" si la tenim registrada.

def corregeix_paraula(paraula):
    correccions = get_correccio(paraula)
    if correccions != None:
        for correccio in correccions:
            paraula_correcte =  cercador.tenim_entrada(correccio)
            if paraula_correcte != None:
                return dict(paraula=paraula, correccio=paraula_correcte)
    
    return dict(paraula=paraula)
