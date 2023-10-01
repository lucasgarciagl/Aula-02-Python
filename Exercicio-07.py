# 7) Criar um programa para calcular a densidade demográfica (habitantes por quilômetro quadrado) de uma região. Sendo, densidade igual a população (total de habitantes) dividida pela área (metros quadrados). Mostrar mensagens para densidade alta (maior ou igual a 100), média (entre 25 e 100), baixa (menor que 25).


totalHabitantes = 2000
area = 50
densidade = float(totalHabitantes / area)

if(densidade >= 100):
    print('Densidade Alta')
elif(densidade >= 25 and densidade < 100):
    print('Densidade média')
elif(densidade < 25):
    print('Densidade Baixa')


