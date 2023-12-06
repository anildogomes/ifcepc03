n = int(input("Me dê um número de qualquer ano: "))
if (n%4) == 0 and (n%100) != 0:
 print("Esse ano é bissexto")
elif (n%100) == 0 and (n%400) == 0:
 print("Esse ano é bissexto")
else:
 print("Esse ano não é bissexto")
