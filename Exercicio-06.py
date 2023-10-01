#  6) Elaborar um programa que alerte sobre os riscos de animais em extinção. O usuário deve digitar o nome da espécie e a sua população (total de indivíduos). 
# Populações entre 200 e 500 indivíduos, são classificadas como "Espécie criticamente em perigo",
# populações entre 500 e 1000 indivíduos, são classificadas como "Espécie em perigo"
# e populações entre 1000 e 5000 indivíduos, são classificadas como "Espécie vulnerável!"

nomeEspecie = str(input('Digite o nome da espécie: '))
populacaoEspecie = int(input('Digite sua população (total de indivíduos): '))

if(populacaoEspecie >= 200 and populacaoEspecie <= 500):
    print('Espécie criticamente em perigo')
elif(populacaoEspecie >= 500 and populacaoEspecie <= 1000):
    print('Espécie em perigo')
elif(populacaoEspecie >= 1000 and populacaoEspecie <= 5000):
    print('Espécie vulnerável!')


