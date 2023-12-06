n1 = float(input("Digite um número: "))
n2 = float(input("Digite um segundo número: "))
n3 = float(input("A mesma coisa dos outros, por favor: "))
print("-"*30)
if n1 > n2 and n1 > n3:
    print("{} é o maior número".format(n1))
elif n2 > n1 and n2 >n3:
    print("{} é o maior número".format(n2))
else:
    print("{} é o maior número".format(n3))