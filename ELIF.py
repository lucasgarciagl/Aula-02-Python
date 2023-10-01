#Quando é necessario mais de 2 condiçoes
#condição pense como pergunta, verdadeiro ou falso

numeroUM = 1
numeroDois = 2


if((numeroUM < 1 or numeroDois < 1)):
    print('Informe um número maior que 1')

elif(numeroUM > numeroDois):
    print('Número um é maior que número dois!')

elif((numeroUM == numeroDois)):
    print('Número um é igual ao número dois!')
else:
    print('Número um não é maior que o número dois!')