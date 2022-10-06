#\\ Vou calcular o tempo de download em minutos. //#

#Aqui eu usei conversão de valores para variáveis tempo#
print ('Calculo para verificar o tempo de download de um arquivo')

arquivo = float(input("Informe do tamanho do arquivo em MB: "))
velocidade = float(input("Informe a velocidade do link da internet em Mbps: "))
tempo = ((arquivo * 8) / velocidade) / 60
print ("O tempo aproximado de download é de %.2f minutos" %tempo)

