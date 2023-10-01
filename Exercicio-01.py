# 1) Crie um programa que peça ao usuário para digitar três notas individualmente (uma por vez), faça a média e caso a média seja igual ou maior que 7, mostre uma mensagem "Aprovado!" e a média. Caso seja menor que 7, mostre uma mensagem "Reprovado!" e a média. (DESAFIO: Modificar e incluir condição para recuperação de 5 a 7).


NotaUm = float(input('Informe a primeira nota: '))
NotaDois = float(input('Informe a segunda nota: '))
NotaTres = float(input('Informe a terceira nota: '))

mediaNota = (NotaUm + NotaDois + NotaTres) / 3

if(mediaNota >= 7):
    print(f'Você foi aprovado! Sua média é: {mediaNota:.2f}')
elif(mediaNota >=5 and mediaNota < 7):
    print(f'Você está em recuperação. Sua média é: {mediaNota:.2f}')
else:
    print(f'Você foi reprovado! Sua média é: {mediaNota:.2f}')