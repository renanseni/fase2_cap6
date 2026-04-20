from services import utils

def exportar_para_txt(lista_colheitas):
    with open("relatorios/colheitas.txt", "w") as arquivo:
        for colheita in lista_colheitas:
            producao_total = colheita["hectares"] * colheita["produtividade"]
            perda = producao_total * (colheita["perda_percentual"] / 100)
            producao_final = producao_total - perda
            
            arquivo.write("_" * 40 + "\n")
            arquivo.write(f"ID: {colheita['id']}\n")
            arquivo.write(f"Tipo: {colheita['tipo'].capitalize()}\n")
            arquivo.write(f"Hectares: {utils.formatar_numero(colheita['hectares'])}\n")
            arquivo.write(f"Produtividade: {utils.formatar_numero(colheita['produtividade'])} t/ha\n")
            arquivo.write(f"Perda: {utils.formatar_numero(colheita['perda_percentual'])}%\n")
            arquivo.write(f"Produção Total: {utils.formatar_numero(producao_total)} toneladas\n")
            arquivo.write(f"Perda: {utils.formatar_numero(perda)} toneladas\n")
            arquivo.write(f"Produção Final: {utils.formatar_numero(producao_final)} toneladas\n")
        arquivo.write("-" * 40 + "\n")
        
    print("Relatório exportado para colheitas.txt")
    pass