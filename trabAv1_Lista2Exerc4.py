##\\ Vou informar a idade e a altura na odem inversa da lida. //##

#Aqui eu implementei a função RANGE #
idades = []
alturas = []
for i in range(1, 6):
    print('%dª Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)

print('Ordem inversa')
print('Alturas')
print(alturas[::-1])
print('Idades')
print(idades[::-1])

print('Ordem lida')
print('Alturas')
print(alturas)

print('Idades')
print(idades)
