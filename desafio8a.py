'''
Desenvolva um programa que leia uma distancia em metros e mostre os 
valores relativos em outras medidas.

Ex:
Digite uma distância em metros: 185.72
A distância de 185.72m corresponde a:

0.18572Km                     1857.2dm
1.18562Hm                     18572.0cm
18.572Dam                     185720.mm
Com o uso do comando format.

'''
numero= float(input('Informe a distância em metros: '), )
n1=numero/1000
n2=numero/100
n3=numero/10
n4=numero*10
n5=numero*100
n6=numero*1000

print('A distância em quilomêtro:',format(n1),'Km','                ','A distância em decímetros:',format(n4),'dm')
print('A distância em hectomêtros:',format(n2),'Hm','                ','A distância em centímetros:',format(n5),'cm')
print('A distância em decimêtros:',format(n3),'Dam','              ','A distância em milímetros:',format(n6),('mm'))

