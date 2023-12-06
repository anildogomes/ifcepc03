print("-"*50)
print("Se você quiser galosina, digite g")
print("Se você quiser Álcool, digite a")
print("-"*50)
r = str(input("Qual dos dois você quer?: ").lower())
print("-"*50)
if r == "a":
    l = float(input("Quantos litros você quer?: "))
    la = l*4.90
    if l > 20:
        desconto = 0.05 * la
        total = la - desconto
        print(f"O total da conta é {total}")
    else:
        desconto = 0.03 * la
        total = la - desconto
        print(f"O total da conta é {total}")
else:
    l = float(input("Quantos litros você quer?: "))
    lg = l*5.50
    if l > 20:
        desconto = lg * 0.06
        total = lg - desconto
        print(f"O total da conta é {total}")
    else:
        desconto = lg * 0.04
        total = lg - desconto
        print(f"O total da conta é {total}")