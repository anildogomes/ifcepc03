start=0
end=int (input("Número:"))

if end>0:
    while end >=start:
        print(start)
        start=start +1

else:
    while end<=start:
        print(start)
        start=start-1

