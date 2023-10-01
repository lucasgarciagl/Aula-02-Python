# 3) Em um determinado e-commerce, o frete para produtos possui o valor fixo de R$12,50. A loja possui benefícios para assinantes em três categorias:
# 1) Assinante Premium, ganha 20% de desconto e frete grátis
# 2) Assinante Gold, ganha 20% de desconto mas paga frete 
# 3) Assinante Silver, ganha 10% de desconto mas paga frete. 
# 4) Não assinante, sem benefícios.

# Faça um programa que solicite o valor da compra e a categoria de assinante (1, 2, 3 ou 4). Mostrar na tela o valor da compra de acordo com a opção escolhida.

valorFrete = 12.50
assinanturaPremium = 0.8
assinanturaGold = 0.8
assinanturaSilver = 0.9
assinanteNao = 0



valorCompra = float(input('Informe o valor da sua compra: '))
categoriaAssinante = int(input('Informe sua categoria de beneficios:\n\n1 - Assinante Premium \n\n2 - Assinante Gold \n\n3 - Assinante Silver \n\n4 - Não assinante\n\n'))

if(categoriaAssinante == 1):
    valorFinal = valorCompra * assinanturaPremium
elif(categoriaAssinante == 2):
    valorFinal = (valorCompra * assinanturaGold) + valorFrete
elif(categoriaAssinante == 3):
    valorFinal = (valorCompra * assinanturaSilver) + valorFrete
elif(categoriaAssinante == 4):
    valorFinal = valorCompra + valorFrete


print(f'A valor de sua compra de acordo com sua categoria de assinatura é:{valorFinal}')
