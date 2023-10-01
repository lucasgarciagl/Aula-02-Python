#Crie um programa que peça ao usuário para digitar três notas individualmente (uma por vez), faça a média e caso a média seja igual ou maior que 7, mostre a mensagem "Aprovado!" e a média. Caso seja menor que 7, mostre uma mensagem "Reprovado!" e a média.


Nota1 = float(input('Informe a nota 1: '))
Nota2 = float(input('Informe a nota 2: '))
Nota3 = float(input('Informe a nota 3: '))

media = (Nota1 + Nota2 + Nota3) / 3

if(media >= 7):
    print(f'\nAprovado! :)\nSua média é: {media:.2f}')
else:
    print(f'\nReprovado! :(\nSua média é: {media:.2f}')




 














