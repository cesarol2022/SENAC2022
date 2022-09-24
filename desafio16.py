'''
Escreva um programa para calcular a reducao do tempo de vida de
um fumante. Pergunte a quantidade de cigarros fumados por dias e
quantos anos ele ja fumou. Considere que um fumante perde 10 min. 
ded vida a cada cigarro.

Calcule quantos dias de vida um fumante perdera e exiba o total 
em dias.
'''
cigarrosdia=float(input('Qual a quantidade de cigarros fumados por dia? '))
anos_cigarro_fumou=float(input('Quantos anos ja fumou? '))
menos_dia_vida=((cigarrosdia/144)*(anos_cigarro_fumou*365))
print('O numero de dias a menos de vida e: ', menos_dia_vida)


