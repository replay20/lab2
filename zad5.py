def liczDoskonala(liczba):
    a = 1
    b = 2
    while b*b < liczba:
        if liczba % b == 0:
            a += b + liczba/b
        b += 1
    if b*b == liczba:
        a += k
    return a == liczba

liczba = int(input("Podaj liczbe: "))
if liczDoskonala(liczba):
    print(f"Liczba {liczba} jest doskonala")
else:
    print(f"Liczba {liczba} nie jest doskonala")