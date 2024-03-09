print("Podaj 10 liczb: ")
lista = []
i=0
while i<10:
    liczba = input()
    liczba = int(liczba)

    if liczba % 2 == 0:
        lista.append(liczba)

    i +=1
else:
    print(lista)
