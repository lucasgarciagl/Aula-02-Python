# 5) Criar um programa que simule o login de um roteador. O nome de usuário (username) é "admin" e a senha (password) "123". Pedir ao usuário para digitar username e password. Caso os dados estejam corretos, mostrar uma mensagem "Login efetuado!", caso contrário "Login falhou!". (DESAFIO: Mostrar mensagens específicas para erro de username, de password ou de ambos).


username = 'admin'
password = '123'

loginUsername = str(input('Digite o username: '))
loginPassword = str(input('Digite o password: '))

if(loginUsername == username and loginPassword == password):
    print('Login efetuado!')
elif(loginUsername != username and loginPassword == password):
    print('O username está errado!')
elif(loginUsername == username and loginPassword != password ):
    print('O password está errado!')
else:
    print('Username e Password estão errados!')
