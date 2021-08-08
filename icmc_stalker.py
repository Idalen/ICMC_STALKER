import requests
import sys


for nusp in sys.argv[1:]:
    
    nusp= int(nusp)
    nusp= nusp*2 +3 
    
    url = 'https://www.icmc.usp.br/pessoas?id=' + str(nusp)
    

    response = requests.get(url)
    try:
        print(response.cookies['imgNome'].replace('+', ' '))
    except:
        print('Aluno nao encontrado.')
