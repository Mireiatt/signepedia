import requests
from src import cercador

# Obtenim les correccions ortogràfiques d'una "paraula" a través de LanguageTool.
# Si no hi ha correcció, retornem "None".
# Cal evitar saturar el servidor.

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
        return None

# Retornem un mapa amb la possible correcció d'una "paraula" si la tenim registrada.

def corregeix_paraula(paraula, cnx):
    correccions = get_correccio(paraula)
    if correccions is not None:
        for correccio in correccions:
            if cercador.tenim_entrada(correccio, cnx):
                return dict(paraula=paraula, correccio=correccio)
    
    return dict(paraula=paraula)
