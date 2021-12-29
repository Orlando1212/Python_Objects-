lista = [
    {'produto':'Fone de ouvido','preco': 800 },
    {'produto': 'Controle de playstation','preco': 500},
    {'produto':'Playstation','preco':1500},
]


def Calcula_desconto(produto):
    produto['preco'] = produto['preco'] - 10
    return produto


nova_lista = map(Calcula_desconto,lista)
print(list(nova_lista))