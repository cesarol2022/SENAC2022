''' A locadora de carros precisa da sua ajuda para
para cobrar seus servicos. 
Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preco total a 
pagar, sabendo que o carro custa R$90 por dia e R$0,20 
por Km rodado.'''

dias=float(input('qual a quantidade de dias?'))
km=float(input('Qual a quilometragem? '))
print('O valor total do aluguel e R$:', ((dias*90)+(km*0.20)))
