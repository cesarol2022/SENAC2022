'''
Crie um programa que leia o preço de um produto, calcule e 
mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.

'''

produto=float(input('Inserir o valor do produto: '))
valor_dc=(produto*5)/100
valor_final=produto-valor_dc
print('O valor do produto com desconto e de:',valor_final)