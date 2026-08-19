import menu_agenda

while True:
    print("[1]Adicionar")
    print("[2]Buscar")
    print("[3]Listar")
    print("[4]Remover")
    print("[5]Sair")
    opcao = input("Digite sua opção: ")

    match opcao:
        case "1": 
            menu_agenda.adicionar()
        case "2": 
            menu_agenda.buscar()
        case "3":
            menu_agenda.listar()
        case "4":
            menu_agenda.remover()
        case "5":
            break