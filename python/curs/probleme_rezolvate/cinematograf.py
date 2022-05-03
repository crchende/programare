'''
    Cinematograf
    (pozitie in ghid pregatire python: 10)
    
    Sumar:
        De facut un program care ma ajua sa aleg cel mai potrivit film dupa
        urmatoarele criterii.
        1) incepe cat mai aproape de ora la care ajung la cinema
        2) daca sunt mai mule filme care incep la aceeasi ora, aleg filmul
           care costa mai putin
           
    Cerinta: fiind data ora a care ajung la cinema programul si pretul filelor
             sa se aleaga filmul cel mai potriit dupa criteriile din sumar.
            
             Ora - atat cea la care ajung la cinema cat si ora filmului sunt in
             formatul: hh:mm
             
             Numele filmului - cuvinte separate prin cratima (-). 
             
    Intrare:
        linia 1: 16:45                               (ora cand ajung la cinema)
        linia 2: 4                                   (filme disponibile)
        linia 3: 18:00 15 Bohemian-Rhapsody          (film1: ora_start cost nume)
        linia 4: 16:50 20 Mos-Craciun-in-misiune     (film2: - la fel ca mai sus)
        linia 5: 12:00 13 Creed-II                   (film3: ...)
        linia 6: 16:55 20 Grinch                     (film4: ...)

    Iesire:
        Mos-Craciun-in-misiune              (filmul cel mai potrivit
                                             criteriul aici este ora cea mai
                                             apropiata de ora sosiri la cinema)
        
    
    Alt set de date de verificat:
    Intrare:
                22:00
                4
                17:00 15 Overlord
                16:50 20 Morometii-2
                23:05 13 Covorul-zburator
                23:05 19 Bohemian-Rhapsody
                
    Iesire:
                Covorul-zburator           (fiind la aceeasi ora cu alt film
                                            criteriul de departajare este costul)

                
'''
# biblioteca pentru procesarea timpului in Pyton
# putem converti timpul singuri din string-ul data de la tastatura
# sau putem folosi biblioteca datetime din Pyton

from datetime import datetime
from collections import defaultdict

'''
ora_min_sosire = input("Dati ora si minutul sosirii la cinema (hh:mm): ")
numar_filme = ("Dati numarul de filme disponibile: ")

lst_filme = []
for i in rage(numar_filme):
    info_film = input("Dati informatiile despre filmul {}".format(i+1))
    lst_filme.append(info_film)
'''

set_date_1 = [
    "16:45",
    4,
    "18:00 15 Bohemian-Rhapsody",
    "16:50 20 Mos-Craciun-in-misiune",
    "12:00 13 Creed-II",
    "16:55 20 Grinch"
]

set_date_2 = [
    "22:00",
    4,
    "17:00 15 Overlord",
    "16:50 20 Morometii-2",
    "23:05 13 Covorul-zburator",
    "23:05 19 Bohemian-Rhapsody"  
]

# Pentru compararea timpului, in loc sa descompunem sirul HH:SS si sa comparam
# ora cu ora si min cu min, putem folosi libraria pentru procesarea timpului
# din python.
# Se genereaza un obiect timp din sirul timp dat ca parametru
# Obiectele timp permit operatii de comparare.

def dif_timp(hh_mm1, hh_mm2):
    o_t1 = datetime.strptime(hh_mm1, "%H:%M")
    o_t2 = datetime.strptime(hh_mm2, "%H:%M")
   
    ret = None 
     
    if o_t1 > o_t2:
        return (o_t1 - o_t2).seconds
    elif o_t1 == o_t2:
        return 0
    else:
        return -(o_t2 - o_t1).seconds


def gaseste_film(str_ora_min_sosire, nr_filme, lst_filme):
    dd_dif_t_cost = defaultdict(list)

    for el in lst_filme:
        l_el = el.split()
        h_m_film = l_el[0]
        pret = int(l_el[1])
        film = l_el[2]
        
        dif_t = dif_timp(h_m_film, str_ora_min_sosire)
        
        if dif_t < 0:
            continue
        
        dd_dif_t_cost[dif_t].append((pret, film))
        
    min_dif_t = min(dd_dif_t_cost.keys())
    
    lst_timp_min = dd_dif_t_cost[min_dif_t]
    print("DBG: filme timp min: ", lst_timp_min)
    
    # gasire cost min pentru diferenta minima de timp
    i = 0
    poz_min = 0
    v_min = lst_timp_min[0][0]
    for el in lst_timp_min:
        if el[0] < v_min:
            v_min = el[0]
            poz_min = i
        i += 1 
        
    return lst_timp_min[poz_min][1]
        
        
print(gaseste_film(set_date_1[0], set_date_1[1], set_date_1[2:]))
print(gaseste_film(set_date_2[0], set_date_2[1], set_date_2[2:]))


    
    
