import requests
print("Verificando Endereço")

def cep(opcao):
    if len(opcao) != 8:
        exit()
    else:
        consulta = requests.get(f'https://viacep.com.br/ws/{opcao}/json/')
        dados = consulta.json()
        print(dados['cep'])
        print(dados['logradouro'])
        print(dados['bairro'])
        print(dados['localidade'])
        print(dados['uf'])