import requests
from bs4 import BeautifulSoup

url = 'https://www.saopaulofc.net/'

resp = requests.get(url)

try: 
    print(resp)
    site = BeautifulSoup(resp.text, 'html.parser')

    img = site.find('img', src= 'https://cdn.saopaulofc.net/2022/09/clube_palmeiras.png')

    prox_jogo = img['alt']

    print(prox_jogo)
except:
    print(resp)
    print('Verifique a conexão com o site')