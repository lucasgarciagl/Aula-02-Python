# 2) Desenvolva um programa no qual o usuário deve digitar o nome e a idade de 5 pessoas. Ao final mostrar a soma das idades e a média das idades.

pessoaNome1 = str(input('Informe o nome: '))
pessoaIdade1 = int(input('Informe a idade: '))

pessoaNome2 = str(input('Informe o nome: '))
pessoaIdade2 = int(input('Informe a idade: '))

pessoaNome3 = str(input('Informe o nome: '))
pessoaIdade3 = int(input('Informe a idade: '))

pessoaNome4 = str(input('Informe o nome: '))
pessoaIdade4 = int(input('Informe a idade: '))

pessoaNome5 = str(input('Informe o nome: '))
pessoaIdade5 = int(input('Informe a idade: '))

somaIdade = pessoaIdade1 + pessoaIdade2 + pessoaIdade3 + pessoaIdade5 + pessoaIdade5
mediaIdade = somaIdade / 5

print(f'A soma de todas as idades é: {somaIdade}.\nE a média de idades é: {mediaIdade}')