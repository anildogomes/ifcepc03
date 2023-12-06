#terceira questão (5)
base = int(input("Me entregue uma base, vamos fazer potência: "))
print("-"*50)


base1 = int(input("Repita a base, por favor: "))


while base != base1:
    print("Bases diferentes, por favor")
    base1 = int(input("Repita a base, por favor: "))
print("-"*50)


expoente = int(input("Agora me entrege o expoente: "))

print("-"*50)
fin=0

if expoente == 1:
    print(base)
elif expoente == 0:
    print(1)
elif expoente == 2:
    result = base1*base
    print(result)
else:
    while fin <= expoente:
        fin = fin + 2
        base3 = (base1*base)
        base = base3
    print(base)
print("-"*50)
    