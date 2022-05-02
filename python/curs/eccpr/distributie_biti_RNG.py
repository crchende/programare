'''
    Distributie biti RNG
    (pozitie ghid pregatire python: 4)
   
    Sumar:
    - vrem sa generam o secventa binara aleatoare
    - verificam prim:
        - numar aparitii secvente 00 01 10 11 - aproximativ egale
            Raport R1 = perechea cea mai frecventa / 
                        perechea cea mai putin frecventa
                        
        - numarul de aparitii de 0 si 1 aproximativ egale
            Raport R2 = numar aparitii cel mai frecvent bit / 
                        numar aparitii cel mai putin frecvent bit
                        
    Cerinta:    R1 si R2 <= 110% sau 1.10
                pentru a avea o secventa pseudo-aleatoare
    
    Date de intrare:
        linia 1: n - numar de biti, numar par intre 2 si 10000
        linia 2: secventa de 1 si 0 de lungime n
        
    Date de iesire:
        linia 1: R1 si R2 - in formatul cu 2 zecimale
        linia 2: 0 sau 1 - daca secventa este sau nu pseudo-aleatoare
    
'''
from collections import defaultdict


# n din enunt - reprezinta lungimea secventei de 1 si 0
n = int(input("Dati lungimea secventei: n = "))
secventa_biti = input("Dati secventa de biti de lungime n: ")

def analizeaza_secventa(n, secventa_biti):

    dict_perechi = defaultdict(int)
    dict_biti  = defaultdict(int)

    prev_i = 0
    for i in range(2, len(secventa_biti)+1, 2):
        pereche = secventa_biti[prev_i:i]
        prev_i += 2
        
        dict_perechi[pereche] += 1
        
        b0 = pereche[0]
        b1 = pereche[1]
        
        dict_biti[b0] += 1
        dict_biti[b1] += 1
        
    # print(dict_perechi)
    # print(dict_biti)

    lst_perechi = list(dict_perechi.values())
    lst_biti = list(dict_biti.values())
    
    print("DBG: frecveta perechi: ", lst_perechi)
    print("DBG: freventa biti:    ", lst_biti)

    max_perechi = max(lst_perechi)
    min_perechi = min(lst_perechi)

    max_biti = max(lst_biti)
    min_biti = min(lst_biti)

    R1 = max_perechi / min_perechi
    R2 = max_biti / min_biti

    print("{:.2f} {:.2f}".format(R1, R2))
    
    if R1 > 1.1 or R2 > 1.1:
        print(0)
    else:
        print(1)

# Validare cu valorile din descrierea problemei
analizeaza_secventa(18, "101100110111100001")
analizeaza_secventa(24, "101100110111100001010010")

# decomenteaza daca vrei sa verifici o secventa data de la tastatura
#analizeaza_secventa(n, secventa_biti)
        
