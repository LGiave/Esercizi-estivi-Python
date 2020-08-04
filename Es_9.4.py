def usa_solo():
    parola=input("inserire una parola")
    lettere=input("inserire una serie di lettere")
    i=0
    while i<len(lettere):
        i+1
        for lettera in parola:
            if lettera!=lettere[i]:
                i=25
                return False
    return True