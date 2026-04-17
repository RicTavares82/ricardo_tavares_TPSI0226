import os as fsos
import json

filename = "./ricardo_tavares_TPSI0226/Aula7/Dados/data.json"
dicionario = {}


if fsos.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as manipfile:
        dicionario = json.load(manipfile)


dicionario = {"nome": "Ricardo", "tel": 2}

with open(filename, "w", encoding="utf-8") as manipfile:
    json.dump(dicionario, manipfile, ensure_ascii=True, indent=4)
