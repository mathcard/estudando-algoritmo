cache = {}

def pega_pagina(url):
    if cache.get(url):
        print('Dados cacheados', url)
        return cache[url]
    else:
        dados = pega_dados_servidor(url)
        cache[url] = dados
        #print(cache)
        return dados
    
def pega_dados_servidor(url):    
    print('Nova request', url)
    return url


pega_pagina('https://fluig.sistemafaeg.org.br')
pega_pagina('https://esenar.sistemafaeg.org.br')
pega_pagina('https://fluig.sistemafaeg.org.br')