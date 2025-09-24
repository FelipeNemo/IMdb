# ==========================================
# utils.py - Funções de suporte
# ==========================================

import json

def save_to_json(data, filepath):
    """
    - Recebe dados (lista de dicionários)
    - Salva em um arquivo JSON formatado
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
