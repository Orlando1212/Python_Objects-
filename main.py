def calcula_medias(nota1,nota2,nota3):
    totalNotas = nota1 + nota2 + nota3
    media = totalNotas / 3
    return media


nota1 = int(input('digite um numero:'))
nota2 = int(input('digite um numero2:'))
nota3 = int(input('digite um nuemro3: '))

print(calcula_medias(nota1,nota2,nota3))


