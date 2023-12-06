#num = int(input("numero:"))
#print(" 1 tabuada de soma")
#print(" 2 tabuada de subtracao")
#print(" 3 tabuada de multiplicacao")
#print(" 4 tabuada de divisao")
#operacao = int(input("operacao:"))

#contador = 1

#if operacao == 1:
    #while contador <=10:
       # print(f"{contador} + {num} = {contador+num}")
        #contador = contador +1
#elif operacao == 2:
    #while contador <=10:
      #  print(f"{contador} - {num} = {contador-num}")
      #  contador = contador +1
#elif operacao == 3:
    #while contador <=10:
      #  print(f"{contador} x {num} = {contador*num}")
       # contador = contador +1
#elif operacao == 4:
    #while contador <=10:
    #    print(f"{contador} / {num} = {contador/num}")
      #  contador = contador +1
#else:
   # print("numero invalido")       






menor = 10
maior = 0

n1= float(input(" primeira nota:"))

if n1 > maior:
    maior = n1
if n1 < menor:
    menor = n1

n2= float(input(" segunda nota:"))

if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

n3= float(input(" terceira nota:"))

if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

n4= float(input(" quarta nota:"))

if n4 > maior:
    maior = n4
if n4 < menor:
    menor = n4

n5= float(input(" quinta nota:"))

if n5 > maior:
    maior = n5
if n5 < menor:
    menor = n5

if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
    maior= n1
if n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
    maior= n2
if n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
    maior= n3
if n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
    maior= n4
if n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
    maior= n5
if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
    menor= n1
if n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
    menor= n2
if n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
    menor= n3
if n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
    menor= n4
if n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
    menor= n5

mp = (n1 + n2 + n3 + n4 + n5 - maior - menor )/3 
print(f"media parcial : {mp}")

if mp >= 6:
    print("aprovado")
elif mp < 3:
    print("reprovado")

else:
    pr = float(input(" nota de recuperacao:"))
    mf = (pr + mp)/2
    print(f"media final: {mf}")
    if mf >= 5 :
        print(" voce passou na recuperacao.")
    else:
        print("voce nao passou na recuperacao.")




      


