'''
    Loturi de componente electronice.
    (pozitie ghid de pregatire python: 6)
    
    Sumar:
        Primim loturi de componente electronice Condensatori, Rezistori, 
        Tranzistori.
        Lotul este valid daca: R >= C >= T
        
    Cerinta:
        De vazut daca lotul este valid sau nu - conform cerintei de mai sus
        
    Intrare:
        linie 1:    3               (nr loturi)
        linie 2:    5               (nr elemente lot 1)
                    R C R T C       (elemente lot 1)
                    5               (la fel pt celelalte loturi)
                    C R T R T
                    6
                    C C T C C T

    Iesire:
        linie 1:    1 6             (1 - nr loturi utile; 6 nr max de elemente
                                     din lot)
'''

nr_loturi = int(input("Dati numarul de loturi: "))

loturi_valide = 0
max_el_lot = 0

for i in range(nr_loturi):
    nr_el_lot = int(input("Dati numarul de elemente din lotul {}: ".format(i+1)))
    el_lot    = input("Dati elemente din lotul {}: ".format(i+1))
    nr_C = el_lot.count("C")
    nr_R = el_lot.count("R")
    nr_T = el_lot.count("T")
    
    if max_el_lot < nr_el_lot:
        max_el_lot = nr_el_lot
        
    if (nr_T >= 1) and (nr_R >= nr_C >= nr_T):
        loturi_valide += 1


print(loturi_valide, max_el_lot)
