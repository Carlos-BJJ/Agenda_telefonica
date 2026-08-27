import menu_agenda

while True:
    print("[1]Adicionar")
    print("[2]Buscar")
    print("[3]Listar")
    print("[4]Remover")
    print("[5]Editar")
    print("[6]Contato Existe")
    print("[7]Sair")
    opcao = input("Digite sua opção: ")

    match opcao:
        case "1":
            nome = input("Adicionar nome: ")
            telefone = input("Adicionar telefone: ")
            email = input("Adicionar email: ")
            menu_agenda.adicionar(nome, telefone, email)

        case "2":
            nome = input("Buscar nomes parecidos: ") 
            menu_agenda.buscar(nome)

        case "3":
            menu_agenda.listar()

        case "4":
            nome = input("Remover nome: ")
            menu_agenda.remover(nome)

        case "5":
            nome = input("Editar o contato do: ")
            telefone = input("Editar telefone: ")
            email = input("Editar email: ")
            menu_agenda.editar(nome, telefone=None, email=None)

        case "6":
            nome = input("Buscar se nome exato existe: ")
            menu_agenda.contato_existe(nome)

        case "7":
            break