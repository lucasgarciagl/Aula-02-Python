# 2) Faça um programa para ler o salário anual de um funcionário e o piso salarial mensal da sua categoria. Mostrar o salário mensal do funcionário e dizer se ele recebe de acordo com o piso (salário mensal igual ou maior que o piso da categoria) ou se recebe abaixo do piso.

salarioAnual = 24000
pisoMensal =  200
salarioMensal = salarioAnual / 12

print(f'O salário mensal do funcionario é: {salarioMensal}')

if(salarioMensal >= pisoMensal):
    print('O funcionário recebe de acordo com o piso salarial.')

else:
    print('O funcionário recebe abaixo do piso salarial.')





