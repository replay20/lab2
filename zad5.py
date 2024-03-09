def liczDoskonala():
    for liczba in range(1,1000,1):
        a = 1
        b = 2
        while b * b < liczba:
            if liczba % b == 0:
                a += b + liczba / b
            b += 1
        if b * b == liczba:
            a += b
        if a == liczba:
            print(liczba)

liczDoskonala()