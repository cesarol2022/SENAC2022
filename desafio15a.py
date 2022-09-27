'''Crie um programa que leia o número de dias trabalhados em um mês
e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas
por dia e ganha R$25 por hora trabalhada.
'''
dias = float(input('Qual o numero de dias trabalhados? '))
soma = dias * 8
salario = soma * 25
print('O salario e {:.2f}'.format(salario))
