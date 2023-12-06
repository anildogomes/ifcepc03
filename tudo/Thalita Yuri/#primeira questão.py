#primeira questão
fim = int(input("Por favor, insira um número para ser a quantidade de números na sequência: "))
n1 = -1
n2 = 1
final = 0
while final <= fim:
    n3 = n2 + n1
    if n3 != 0:
        print(n3)
    n1=n2
    n2=n3
    final = final + 1