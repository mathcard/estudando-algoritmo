
votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print('Manda embora, já votou')
    else: 
        votaram[nome] = True        
        print('Deixa votar')



verifica_eleitor('Math')
verifica_eleitor('Tom')
verifica_eleitor('Joe')
verifica_eleitor('Math')
print(votaram)
