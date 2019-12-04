import webbrowser

nusp= int(input("NUSP:"))
nusp= nusp*2 +3 
 
url = 'https://www.icmc.usp.br/pessoas?id=' + str(nusp)

print(f"{url}")
webbrowser.open_new_tab(url)
