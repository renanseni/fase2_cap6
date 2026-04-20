from models.colheita import criar_colheita
from services.oracle import inserir_colheita
import services.json_service as json_service
import services.utils as utils
import services.oracle as oracle_service

def cadastrar_colheita(lista_colheitas, modo="offline"):
    dados = coletar_dados()
    if dados is None:
        return 
    
    colheita = criar_colheita(id=len(lista_colheitas)+1, tipo=dados["tipo"], hectares=dados["hectares"], produtividade=dados["produtividade"], perda_percentual=dados["perda_percentual"])
    lista_colheitas.append(colheita)
    
    if(modo == "offline"):
        json_service.salvar_json(lista_colheitas)
    elif(modo == "db"):
        inserir_colheita(colheita)
    
    print("Colheita cadastrada com sucesso!")
    pass

def coletar_dados():
    
    tipo = input("1 - Mecânica | 2 - Manual: ")
    if(tipo not in ['1', '2']):
        print("Tipo inválido. Tente novamente.")
        return
    
    hectares = input("Hectares: ")
    try:
        hectares = float(hectares)
        if hectares <= 0:
            print("O valor deve ser positivo.")
            return
    except ValueError:
        print("Digite um número válido.")
        return
    hectares = int(hectares)
    
    try:
        produtividade = float(input("Produtividade (toneladas por hectare t/ha): "))
        if produtividade <= 0:
            print("Deve ser maior que zero.")
            return
    except ValueError:
        print("Valor inválido.")
        return
    produtividade = int(produtividade)
    
    try:
        perda_percentual = float(input("Perda Percentual (%): "))
        if perda_percentual < 0 or perda_percentual > 100:
            print("Deve estar entre 0 e 100.")
            return
    except ValueError:
        print("Valor inválido.")
        return
    perda_percentual = int(perda_percentual)
    
    return {
        "tipo": "mecanica" if tipo == "1" else "manual",
        "hectares": hectares,
        "produtividade": produtividade,
        "perda_percentual": perda_percentual
    }

def calcular_perda(lista_colheitas):
    colheita_id = input("Digite o ID da colheita para calcular a perda: ")
    try:
        colheita_id = int(colheita_id)
        colheita = next((c for c in lista_colheitas if c["id"] == colheita_id), None)
        if colheita is None:
            print("Colheita não encontrada.")
            return
        
        perda = colheita["hectares"] * colheita["produtividade"] * (colheita["perda_percentual"] / 100)
        
        print("_" * 40)
        print(f"Perda para a colheita ID {colheita_id}: ")
        print(f"{utils.formatar_numero(perda)} toneladas")
        print("-" * 40)
    except ValueError:
        print("ID inválido.")
        return
    

def listar_colheitas(lista_colheitas):
    if not lista_colheitas:
        print("Nenhuma colheita cadastrada.")
        return
    
    for c in lista_colheitas:
        print("_" * 40)
        print(f"ID: {c['id']}")
        print(f"Tipo: {c['tipo'].capitalize()}")
        print(f"Hectares: {utils.formatar_numero(c['hectares'])}")
        print(f"Produtividade: {utils.formatar_numero(c['produtividade'])} t/ha")
        print(f"Perda: {utils.formatar_numero(c['perda_percentual'])}%")
    print("-" * 40)    
    pass



def gerar_relatorio(lista_colheitas):
    perda_total = 0;
    for colheita in lista_colheitas:
        producao_total = colheita["hectares"] * colheita["produtividade"]
        perda = producao_total * (colheita["perda_percentual"] / 100)
        producao_final = producao_total - perda
        perda_total += perda
        
        print("_" * 40)
        print(f"ID: {colheita['id']}")
        print(f"Tipo: {colheita['tipo'].capitalize()}")
        print(f"Hectares: {utils.formatar_numero(colheita['hectares'])}")
        print(f"Produtividade: {utils.formatar_numero(colheita['produtividade'])} t/ha")
        print(f"Perda: {utils.formatar_numero(colheita['perda_percentual'])}%")
        print(f"Produção Total: {utils.formatar_numero(producao_total)} toneladas")
        print(f"Perda: {utils.formatar_numero(perda)} toneladas")
        print(f"Produção Final: {utils.formatar_numero(producao_final)} toneladas")
        
    print("-" * 40)
    print(f"Perda Total: {utils.formatar_numero(perda_total)} toneladas")
    pass



CAMPOS = {
    "1": "tipo",
    "2": "hectares",
    "3": "produtividade",
    "4": "perda_percentual"
}

def atualizar_colheita(id):
    colheita = oracle_service.buscar_colheita_por_id(id)
    if not colheita:
        print(f"Colheita com ID {id} não encontrada.")
        return
    print("Colheita encontrada:")
    print(colheita)
    
    while True:
        print("\nCampos para atualizar:")
        for codigo, campo in CAMPOS.items():
            print(f"{codigo}. {campo}")
        escolha = input("Escolha um campo para atualizar (ou '0' para sair): ")
        
        if escolha == '0':
            break
        elif escolha in CAMPOS:
            novo_valor = input(f"Digite o novo valor para {CAMPOS[escolha]}: ")
            colheita[CAMPOS[escolha]] = novo_valor
            oracle_service.atualizar_colheita(colheita)
            print("Colheita atualizada com sucesso.")
        else:
            print("Opção inválida. Tente novamente.")