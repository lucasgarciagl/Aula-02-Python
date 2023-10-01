# 1) Crie um programa que leia três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno. Quando os três lados forem iguais trata-se de um triângulo equilátero, dois lados iguais é um triângulo isósceles e os três lados diferentes é um triângulo escaleno.


TrianguloLadoUm = 1
TrianguloLadoDois = 2
TrianguloLadoTres = 5

if(TrianguloLadoUm == TrianguloLadoDois and TrianguloLadoDois == TrianguloLadoTres and TrianguloLadoTres == TrianguloLadoUm ):
    print('Este é um triângulo equilátero')
elif(TrianguloLadoUm == TrianguloLadoDois or TrianguloLadoDois == TrianguloLadoTres or TrianguloLadoTres == TrianguloLadoUm):
     print('Este é um triângulo isósceles')
else:
     print('Este é um triângulo escaleno')

