def niente_e(parola):
    for lettera in parola:
        print(lettera)
        if lettera=="e":
            return False
    return True

def niente_e_percentuale(parola):
    con_e=0
    for lettera in parola:
        con_e=con_e+1
        if lettera=="e":
            return False
    print(parola)
    return con_e
    
    
#parola=input("Inserire una parola \n")
#print(niente_e(parola))

parole_elenco=113809

fin = open('words.txt')

riga=fin.readline()

for riga in fin:

    parola = riga.strip()
    con_e=niente_e_percentuale(parola) 

percentuale=(con_e/parole_elenco)*100
print("La percentuale di parole con e:")
print(percentuale)



