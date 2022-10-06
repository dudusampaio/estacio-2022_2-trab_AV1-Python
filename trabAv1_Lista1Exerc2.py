##\\ Vou calcular o excesso de peso de peixes pescados pelo Senhor João Papo-de-Pescador. //##

#Aqui eu usei variável para acumular valores#
peso = int(input('Insira o peso dos peixes? '))
excesso = 0
multa = 4 * excesso

if peso > 50:
    excesso = peso - 50
    multa = excesso*4

    print('Quantidade de quilos além do limite permitido: ',excesso, ' quilos. A multa que deverá pagar é de: R$:', multa)
else:
    print('Parabéns! Peso da sua pescaria está dentro do regularmento estabelecido pelo estado de São Paulo')