l1 = float(input("Me dê o primeiro lado de seu triangulo: "))
l2 = float(input("Agora me dê o segundo lado desse trinagulo: "))
l3 = float(input("Agora. me dê o ultimo lado: "))
print("-"*30)
if (l1 + l2)>l3 and (l1+l3)>l2 and (l2+l3)>l1:
    print("Triangulo valido")
    print("-"*30)
    if l1 == l2 and l2==l3:
        print("Equilátero")
    elif l1 != l2 and l2 != l3:
        print("Escaleno")
    else:
        print("Isoceles")
else:
    print("Triangulo invalido")
