#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lis = []
lis_par =[]
lis_im =[]
a = 0

while a < 20:
    num = int(input('numero: '))
    a += 1
    lis.append(num)
    
    if num % 2 == 0:
        lis_par.append(num)
    else:
        lis_im.append(num)

print(f"{lis} \n {lis_par} \n {lis_im}")