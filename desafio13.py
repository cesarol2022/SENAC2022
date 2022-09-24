'''Faca um algoritmo que leia o salario de um funcionario, calcule
e mostre o seu novo salario, com 15% de aumento.
'''
salario= float(input('Qual o salario do funcionario? R$' ))
novo_salario=salario*1.15
print(f'O novo salario com 15% de aumento e: R${novo_salario:,.2f}')
