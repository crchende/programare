'''
    Cazino
    (pozitie ghid pregatire python: 3)
    
    Sumar:
        Un cazino vrea sa gaseasca trisorii - aici, cei care aduc carti in plus
        Jocul foloseste 2 pachete clasice de carti, totalizand 52 carti.
        (fara Joker)
        
    Cerinta: 
        Detectarea faptului ca o carte nu apare de mai mult de 2 ori.
        
    Intrare:
        linia 1:    n = numar maini jucate
        pe liniile urmatoare sunt cartile in formatul:
                    <numar carte> <semn carte>
                    
    Iesire:
        JOC OK              (daca nu au fost carti detectate de mai multe ori)
        <numar carte> <semn carte> (daca se triseaza cu aceasta carte)
        
    Exemple date verificare:
    
    1)  Intrare:
        5
        2 trefla
        11 caro
        14 cupa
        14 pica
        6 caro
        
        Iesire:
        JOC OK
        
    2)  Intrare:
        7
        2 trefla
        11 caro
        11 caro
        11 caro
        14 cupa
        14 pica
        6 caro

        Iesire:
        11 caro     (carte jucata de 3 ori consecutiv)
        
    3)  Intrare:
        7
        2 trefla
        11 caro
        11 caro
        6 caro
        11 caro
        14 cupa
        14 pica   
         
        Iesire:        
        11 caro     (carte jucata de 3 ori dar nu consecutiv)
        
    4)  Intrare:
        7
        11 caro
        11 pica
        11 caro
        11 pica
        11 pica
        11 caro
        14 pica
        6 caro
    
        Iesire:
        11 pica     (prima carte jucata de 3 ori, 11 caro apare de 3 ori dupa)
        
'''

from collections import defaultdict

set_test_1 = [
        5,
        "2 trefla",
        "11 caro",
        "14 cupa",
        "14 pica",
        "6 caro",
]

set_test_3 = [
        7,
        "2 trefla",
        "11 caro",
        "11 caro",
        "6 caro",
        "11 caro",
        "14 cupa",
        "14 pica",
]

set_test_4 = [
        7,
        "11 caro",
        "11 pica",
        "11 caro",
        "11 pica",
        "11 pica",
        "11 caro",
        "14 pica",
        "6 caro"
]

'''
# Preluare date de la tastatura:

nr_maini_jucate = int)input("Dati numarul de maini jucate: "))

lst_maini_jucate = []

for i in range(nr_maini_jucate):
    info_mana = input("Dati numarul si culoarea cartii: ")
    lst_maini_jucate.append(info_mana)

'''

def verifica_joc(nr_maini_jucate, lst_info_maini):
    ret = ""
    dd_carti = defaultdict(int)

    for i in range(nr_maini_jucate):
        carte = lst_info_maini[i]
        dd_carti[carte] += 1
        if dd_carti[carte] > 2:
            return carte
    
    return "JOC OK"

print(verifica_joc(set_test_1[0], set_test_1[1:]))    
print(verifica_joc(set_test_3[0], set_test_3[1:]))
print(verifica_joc(set_test_4[0], set_test_4[1:]))

