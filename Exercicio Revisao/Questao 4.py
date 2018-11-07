import sys

print ('Bem-Vindo ao Hipermercado \n')
print ('Escolha o tipo de carne que quer levar: \n')

tipo_de_carne = input('[F]ile Duplo\n[A]lcatra\n[P]icanha \n ')

peso = float(input('Quantos Kg de carne deseja levar? \n '))


if float(peso)>(5.0):
    preco_file = 5.80
    preco_alcatra = 6.80
    preco_picanha = 7.80
else:
    preco_file = 4.90
    preco_alcatra = 5.90
    preco_picanha = 6.90

if tipo_de_carne == 'f':
    preco_bruto = preco_file*peso
    tipo_de_carne = 'File Duplo'
elif tipo_de_carne == 'a':
    preco_bruto = preco_alcatra*peso
    tipo_de_carne = 'Alcatra'
elif tipo_de_carne == 'p':
    preco_bruto = preco_picanha*peso
    tipo_de_carne = 'Picanha'
else:
    print ('Escolha errada')
    sys.exit()

cliente_hiper = str(input('Tem cartao do Hipermercado? [s]im/[N]ao\n '))
desconto = preco_bruto*0.05

if cliente_hiper == 's':
    preco_final = preco_bruto-desconto
else:
    preco_final = preco_bruto


print ('',tipo_de_carne,'(',peso,'kg ) ',preco_bruto)
if preco_final != preco_bruto:
    print ('Desconto: SIM (',desconto,')')
    print (' Preco Final:',preco_final)
else:
    print (' Desconto: NAO')
    print (' Preco Final:',preco_final)
