def Dividir(n1,n2):
    try:
        print(f'O resultado e : {n1/n2}')
    except ZeroDivisionError as erro:
        print(erro)


try:
    Dividir(10,0)
except IndexError as erro:
    print("erro ao desenvolver")