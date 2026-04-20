from services.colheita_service import cadastrar_colheita, calcular_perda, listar_colheitas, gerar_relatorio
from services.txt_service import exportar_para_txt
from services.json_service import exportar_json, carregar_json


MENU_OPCOES = (
    ("1", "Cadastrar Colheita"),
    ("2", "Calcular Perda"),
    ("3", "Listar Colheitas"),
    ("4", "Gerar Relatório"),
    ("5", "Exportar Relatório para TXT"),
    ("6", "Exportar para JSON"),
    ("7", "Sair")
)

def main():
    colheitas = carregar_json()

    opcoes_validas = [op[0] for op in MENU_OPCOES]

    while True:
        print("\nMenu Offline:")
        for codigo, descricao in MENU_OPCOES:
            print(f"{codigo}. {descricao}")

        escolha = input("Escolha uma opção: ")

        if escolha not in opcoes_validas:
            print("Opção inválida. Tente novamente.")
            continue

        if escolha == '1':
            cadastrar_colheita(colheitas, modo="offline")

        elif escolha == '2':
            calcular_perda(colheitas)

        elif escolha == '3':
            listar_colheitas(colheitas)

        elif escolha == '4':
            gerar_relatorio(colheitas)

        elif escolha == '5':
            exportar_para_txt(colheitas)

        elif escolha == '6':
            exportar_json(colheitas)

        elif escolha == '7':
            print("Saindo...")
            break