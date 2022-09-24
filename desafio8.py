'''
Desenvolva um programa que leia uma distancia em metros e mostre os 
valores relativos em outras medidas.

Ex:
Digite uma distância em metros: 185.72
A distância de 85.7m corresponde a:

0.18572Km                     1857.2dm
1.18562Hm                     18572.0cm
18.572Dam                     185720.mm

'''
numero= float(input('Informe a distância em metros: '), )
print((numero/1000),('Km'),'                ',(numero*10),('dm'))
print((numero/100),('Hm'),'                 ',(numero*100),('cm'))
print((numero/10),('Dam'),'                ',(numero*1000),('mm'))

