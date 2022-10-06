##\\ Vou calcular o peso ideal de uma pessoa conforme as fórmulas: (a) Para homens: (72.7*h) - 58 // (b) Para mulheres: (62.1*h) - 44.7 . //##

#Aqui eu usei variável de acumulação#
peso = int(input('Qual o peso de peixes pescado hoje ?  :'))
pesoexcedente = 0
multa = 4*pesoexcedente

if peso > 50:
    pesoexcedente = peso - 50
    multa = pesoexcedente*4

    print('Olá, você ultrapassou o limite de quilos pescado em: ', pesoexcedente, ' quilos, sua multa será de: R$:', multa)
else:
    print('Tudo normal na pescaria de hoje')