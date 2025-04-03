import json
from datetime import datetime
import os

ARQUIVO_JSON = "historico_resultados.json"

def salvar_resultado(nome, respostas, carreira1, carreira2):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro = {
        "data": data_hora,
        "nome": nome,
        "respostas": {
            "logica": respostas[0],
            "visual": respostas[1],
            "dados": respostas[2],
            "seguranca": respostas[3]
        },
        "carreira_principal": carreira1,
        "sugestao_secundaria": carreira2
    }

    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            historico = json.load(f)
    else:
        historico = []

    historico.append(registro)

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)
