from classe import *
while True:
    consulta = int(input("Digite [1] para consultar e [2] para sair do programa "))
    while consulta != 2 and consulta != 1:
        consulta = int(input("Digite [1] para consultar e [2] para sair do programa "))

    if consulta == 1:
        endereco = input("Digite o CEP: ")
        cep(endereco)
    else:
        print("Saindo do Programa...")
        break