# Problema da cobertura de conjuntas
# Calcular as melhores estações para abranger cada estado
# Descobrir o menor número de estações para transmitir para maior quantidade de estados

estados_abranger = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
estacoes_finais = set()
estacoes = {}
estacoes['kone'] = set(['id', 'nv', 'ut'])
estacoes['ktwo'] = set(['wa', 'id', 'mt'])
estacoes['kthree'] = set(['or', 'nv', 'ca'])
estacoes['kfour'] = set(['nv', 'ut'])
estacoes['kfive'] = set(['ca', 'az'])

print(estacoes)
print(estacoes_finais)

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        print('estacao', estacao)
        print('estatos', estados)
        print('---')
        cobertos = estados_abranger & estados
        print('cobertos', cobertos)
        print('---')
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)

    print('estados cobertos', estados_cobertos)
    print('estacoes_finais:', estacoes_finais)
    print('estados abranger', estados_abranger)