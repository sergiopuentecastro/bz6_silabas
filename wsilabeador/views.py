from wsilabeador import app
from pilengua import pilengua, inversa
from flask import jsonify


@app.route("/<frase>")
def index(frase):
    diccionario = {}
    diccionario["Response"] = True
    diccionario["result"] = {"original": frase, "traducido": pilengua(frase)}

"""
Tambien podemos hacerlo a capon
diccionario = {"Response": True,
            "result":{"original": }
}
"""

    return jsonify(diccionario)

@app.route("/decodifica/<frase>")
def decodifica(frase):
    diccionario = {}
    diccionario["Response"] = True
    diccionario["result"] = {"original": frase, "traducido": inversa(frase)}

    return jsonify(diccionario)
