num=int(input("Número:"))

dig1= num%10
dig2= num//10

if dig1==dig2:
    print("Os dígitos são iguais")
else:
    print("Os dígitos são diferentes")

