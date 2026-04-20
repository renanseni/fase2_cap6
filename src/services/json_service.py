import json

def carregar_json():
    try:
        with open("data/dados.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def salvar_json(colheitas):
    with open("data/dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(colheitas, arquivo, indent=4, ensure_ascii=False)
        
        
def exportar_json(colheitas):
    with open("relatorios/colheitas.json", "w", encoding="utf-8") as arquivo:
        json.dump(colheitas, arquivo, indent=4, ensure_ascii=False)
    print("Relatório exportado para colheitas.json")