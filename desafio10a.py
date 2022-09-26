'''
Faça um algoritmo que leia a largura e altura de uma parede, calcule e 
mostre a área a ser pintada e a quantidade de tinta necessáriapara o 
serviço, sabendo que cada litro de tinta pinta uma área de 2 metros 
quadrados.
'''
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = (larg * alt)
lataTinta = area / 2
print('Sua parede tem a dimensão de altura:',
      alt, 'e sua area é de :', area, 'm2.')
print('Voce vai precisar {:.2f} latas de tinta'.format(lataTinta))
