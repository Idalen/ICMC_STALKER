import requests

nusp= int(input("NUSP:"))
nusp= nusp*2 +3 
 
url = 'https://www.icmc.usp.br/pessoas?id=' + str(nusp)

print(f"getting {url}...")

response = requests.get(url)
print(response.cookies['imgNome'].replace('+', ' '))
