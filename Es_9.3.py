def evita():
    parola=input("inserire parola")
    vietate=input("inserie lista lettere vietate")
    i=0
    t=True
    while t:
        i+1
        for lettera in parola:
            if lettera==vietate[i]:
                t=False
                return False
    return True

def evita_conteggio(parola,vietate):
    i=0
    while i<len(vietate):
        i+1
        for lettera in parola:
            if lettera==vietate[i]:
                i=25
                return False
    return True

parole_elenco=113809

vietate=input("inserie lista lettere vietate")

fin = open('words.txt')

riga=fin.readline()

for riga in fin:
    parola = riga.strip()
    risultato=evita_conteggio(parola,vietate) 
    if risultato==False:
        parole_elenco-1

print(parole_elenco)