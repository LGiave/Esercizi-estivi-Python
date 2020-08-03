fin = open('words.txt')

riga=fin.readline()

for riga in fin:

    parola = riga.strip()
    lunghezza = len(parola)

    if lunghezza>20:

        print(parola)

