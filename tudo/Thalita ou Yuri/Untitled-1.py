n1 = float(input("Me dê um número: "))
n2 = float(input("Me dê um número: "))
n3 = float(input("Me dê um número: "))
print("-"*30)
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
maior = n1
if n2 > maior:
    maior = n2
if n3>maior:
    maior = n3
meio = (n1+n2+n3) - menor - maior
print(f"A sequencia ficou como {menor}, {meio}, {maior}")
