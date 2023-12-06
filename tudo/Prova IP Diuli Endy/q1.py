n1=float(input("Sua nota:"))
n2=float(input("Sua nota:"))
n3=float(input("Sua nota:"))
n4=float(input("Sua nota:"))
n5=float(input("Sua nota:"))

medi=n1+n2+n3+n4+n5/5

maior=medi/10
ma=maior-10

menor =medi/10
me=menor-10

mp=(medi-menor)-maior

if mp>=6:
    print("Aprovado")

elif mp>=3 and mp<6:
   print("Recuperação")

pr=float(input("Sua nota:"))

mf=pr+mp/2

if mf>=5:
    print("Aprovado")


    
