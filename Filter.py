lista = [
    {'produto':'Fone de ouvido','preco': 800 },
    {'produto': 'Controle de playstation','preco': 500},
    {'produto':'Playstation','preco':1500},
]

def funcao(produto):
    return produto['preco']>=550


nova_lista = filter(funcao,lista)
print(list(nova_lista))