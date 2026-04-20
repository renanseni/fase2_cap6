from menus import menu_offline, menu_db

MENU_OPCOES = (
    ("1", "Modo Offline (JSON)"),
    ("2", "Modo Banco de Dados (Oracle)"),
    ("3", "Sair")
)

def iniciar():
    while True:
        print("\nMenu Principal:")
        for codigo, descricao in MENU_OPCOES:
            print(f"{codigo}. {descricao}")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            menu_offline.main()

        elif escolha == '2':
            menu_db.main()

        elif escolha == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")