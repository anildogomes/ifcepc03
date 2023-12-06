#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lis =  []
a = 0

while a < 10:
    c = input("digite a letra: ")
    a += 1
    lis.append(c)

letra = 1
for letra in lis:
    if letra.isnumeric():
        pass
    elif letra not in "aeiou":
        print(letra)
    else:
        pass
