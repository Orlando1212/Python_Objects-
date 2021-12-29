lista = [
    {'produto':'Fone de ouvido','preco': 800 },
    {'produto': 'Controle de playstation','preco': 500},
    {'produto':'Playstation','preco':1500},
]


funcao = lambda acumulador,produto: acumulador + produto['preco']
nova_lista  = reduce(funcao,lista,0)
print(list(nova_lista))

