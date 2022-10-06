##\\ Vou informar se o número digitado é INTEIRO ou DECIMAL. //##

#Aqui eu usei comparador // para divisão inteira# 
numero = float(input('Digite um número qualquer: '))
if (numero // 1 == numero):
        print("O número digitado é INTEIRO")
else:
    print("O número digitado é DECIMAL")