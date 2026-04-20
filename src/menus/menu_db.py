from services import txt_service
from services import json_service
import services.colheita_service as colheita_service
import services.oracle as oracle_service

MENU_OPCOES = (
    ("1", "Cadastrar Colheita"),
    ("2", "Atualizar Colheita"),
    ("3", "Deletar Colheita"),
    ("4", "Calcular Perda"),
    ("5", "Listar Colheitas"),
    ("6", "Gerar Relatório"),
    ("7", "Exportar Relatório para TXT"),
    ("8", "Exportar para JSON"),
    ("9", "Sair")
)

def main():
    connected = oracle_service.get_connection()
    
    if not connected:
        print("Não foi possível conectar ao banco de dados. Verifique as configurações e tente novamente.")
        return
    
    oracle_service.criar_tabela()
    
    while True:
        print("\nMenu Banco de Dados:")
        for codigo, descricao in MENU_OPCOES:
            print(f"{codigo}. {descricao}")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            colheita_service.cadastrar_colheita(oracle_service.listar_colheitas(), modo="db")

        elif escolha == '2':
            id = input("Digite o ID da colheita a ser atualizada: ")
            try:
                id = int(id)
                colheita_service.atualizar_colheita(id)
            except ValueError:
                print("ID inválido. Digite um número inteiro.")

        elif escolha == '3':
            id = input("Digite o ID da colheita a ser deletada: ")
            try:
                id = int(id)
                oracle_service.deletar_colheita(id)
                print(f"Colheita com ID {id} deletada.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")

        elif escolha == '4':
            colheita_service.calcular_perda(oracle_service.listar_colheitas())

        elif escolha == '5':
            colheita_service.listar_colheitas(oracle_service.listar_colheitas())

        elif escolha == '6':
            colheita_service.gerar_relatorio(oracle_service.listar_colheitas())

        elif escolha == '7':
            txt_service.exportar_para_txt(oracle_service.listar_colheitas())

        elif escolha == '8':
            json_service.exportar_json(oracle_service.listar_colheitas())

        elif escolha == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


    