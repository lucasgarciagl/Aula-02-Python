# 3) Criar um programa que pergunte o nome e a idade da pessoa, e se tem comorbidade (S ou N). Mostrar mensagem "Pode se vacinar!" caso a idade seja maior ou igual a 60 ou tenha comorbidade. Caso contrário, mostrar mensagem "Não pode se vacinar!".


idade = int(input('Informe a idade da pessoa: '))
nome =  str(input('Informe o nome da pessoa: '))
comorbidade = str(input('A pessoa tem comorbidades? (Responda S ou N): '))

if(idade >= 60) or (comorbidade == 'S' or comorbidade == 's'):
    print('Pode se vacinar!')
else:
    print('Não pode se vacinar!')
