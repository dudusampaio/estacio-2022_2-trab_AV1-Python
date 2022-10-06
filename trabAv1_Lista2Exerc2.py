##\\ Vou informar se o número digitado inteiro é PAR ou ÍMPAR. //##

#Aqui eu usei operador de comparação ==#
numero = float(input('Digite um número para saber se é par ou ímpar: '))
resto = numero % 2

if resto == 0:
    print(f'O número digitado é PAR.')
else:
    print(f'O número digitado é ÍMPAR')