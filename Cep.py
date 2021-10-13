import requests

arq = open('Cep.txt','r') #arquivo de origem dos ceps

while True:
    for i in arq:
        cep = i
        print(len(cep))
        response = requests.get('https://viacep.com.br/ws/'+ cep +'/json/')
        if response.status_code == 200: 
            dados_cep = response.json()
            print(dados_cep)
        else:
            print('Erro na Execução da API')
            break

