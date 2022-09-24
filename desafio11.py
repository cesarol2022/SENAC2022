'''
Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta.

Ex:
O valor de Delta é: D = B² - 4 x A x C

'''


a=float(input('Digite o valor de A:' ))
b=float(input('Digite o valor de B:' ))
c=float(input('Digite o valor de C'  ))
delta = ((b**2)-(4*a*c))
print(f'O valor de Delta é {delta:,.2f}')