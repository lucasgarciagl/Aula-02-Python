# 4) Fazer um programa no qual o usuário digite a sua altura e o seu peso, ao final mostre o IMC (índice de massa corporal) e uma mensagem se está abaixo do peso (IMC menor que 18), na faixa de peso ideal (IMC de 18 a 25) ou acima do peso (IMC maior 25). IMC = peso / (altura * altura).


altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))

IMC = peso / (altura * altura)

if(IMC < 18):
    print('Você etá abaixo do peso!')
elif(IMC >=18 and IMC <= 25):
    print('Você está no peso ideal!')
else:
    print('Você está acima do peso!')