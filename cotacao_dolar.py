import requests
from bs4 import BeautifulSoup

# API pública da cotação do dólar
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

try:
    # Para retornar com os dados da url
    resp = requests.get(url)

    # Transforma os dados para json
    dados = resp.json()

    # print(dados)
    
    # Pega a cotação navegando pelo dicionário
    cotacao = dados['USDBRL']['bid']

    # Pega a data navegando pelo dicionário
    data = dados['USDBRL']['create_date']

    # Formata o print
    print(f'A cotação do dólar na data de {data} é de {cotacao}')

except:
    print('Erro! Verifique a conexão com URL')