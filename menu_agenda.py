import json

#encoding="utf-8" garante que caracteres com acento sejam lidos corretamente. 
#Sem isso, em alguns sistemas o Python pode usar uma codificação diferente e bagunçar o texto
try:
    #leio o "contatos.json" caso dê erro de não existir um arquivo json o código vai para a exceção
    with open("contatos.json", "r", encoding="utf-8") as arquivo:
        #O método .load é para ler o arquivo
        contatos = json.load(arquivo)

#Caso não exista o dicionario, a exceção criará
except FileNotFoundError:
    contatos = {}

#Criei funções para cada função da agenda (salvar, adicionar, buscar, listar e remover)

def salvar():
    #Leitura do arquivo "contatos.json"
    with open("contatos.json", "w", encoding="utf-8") as arquivo:
                #adicionado o arquivo atualizado no arquivo "contatos.json" com o método .dump
                json.dump(contatos, arquivo)

def adicionar():
    nome = input("Digite o nome: ")
    telefone = input(f"Digite o numero do {nome}: ")
    email = input(f"Digite o email do {nome}: ")

    if nome not in contatos:
        contatos[nome] = {"telefone": telefone, "email": email}
        salvar()
        print(f"\n{contatos[nome]}\n")
        
    else:
        print("\nNome já utilizado, adicione um sobrenome ou um usuario diferente\n")

def buscar():
    busca = input("Digite o nome que deseja buscar: ")
    if busca in contatos:
        print(f"\n{contatos[busca]}\n")
    else:
        print("\nValor não encontrado\n")

def listar():
    for nome, contato in contatos.items():
        print(f"\n{nome, contato}\n")

    if not contatos:
        print("\nNão há contatos na Agenda\n")

def remover():
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in contatos:
        contatos.pop(nome_remover)#Removendo a chave desejada
        salvar()

        print(f"\n{nome_remover} removido da agenda\n")
    else:
        print("\nNome não encontrado\n")