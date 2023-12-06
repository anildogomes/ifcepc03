#segunda questão (3)
senha = input("Por favor, faça uma senha forte, de no mínimo 8 algorismos: ")
num = len(senha)
while num <8:
    print("Senha inválida")
    senha = input("Por favor, faça essa senha denovo: ")
    num = len(senha)
print("Senha válida, Obrigada")
print(":D")