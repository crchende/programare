'''
    WBS Adaptiv 
    (pozitie ghid pregatire python: 15)
    
    Compresie prin tehnica Wite Block Skipping adaptat
    adica compresie blocuri de 0 sau 1 la o singura valoare.
    
    Se da lungimea blocului de biti care se analizeaza. De ex se iau blocuri
    de doi biti, 4 biti etc.
    
    Reguli compresie:
    A) Compresie blocuri de '0'
       Se analizeaza bloc cu bloc, cu lungimea data in cerinte.
        1) Sirul comprimat incepe cu un bit de 0 
        2) Blocurile de 0 (doar 0) se reduc la un bit de 0
        3) Daca blocul contine cel putin un 1, bitii se copiaza si in fata se
           adauga 1 ca prefix
           
    B) Compresie blocuri de '1'
       Algoritmul este similar ca la compresia dupa blocuri de 0, cu urmatoarele
       particularitati:
       1) Sirul comprimat incepe cu un bit de 1
       2) La fel ca la '0' dar in acest caz regula este pentru blocuri de '1'
       3) Daca blocul contine cel putin un 0, se copiaza si se 
          adauga 0 ca prefix
          
    Daca sirul de intrare nu poate fi impartit in grupe de n biti (n lungimea
    blocului), ultimii biti se trateaza ca si cum ar face parte dintr-un grup
    neuniform (adica si cu 1 si cu 0), fara a se adauga biti de completare sa-l
    aducem la lungimea n. De ex daca se codeaza dupa 0, se adauga 1 in fata si se 
    copiaza blocul. Daca codarea se face dupa 1 - se repeta blocul cu 0 ca prefix.
    
    Date de intrare:
        - numar elemente in sir
        - lungime bloc
        - sir
        
    Date de iesire:
        - raportul de compresie lungime sir initial / lungime sir final 
          rotunjit la doua zecimale
        - sirul comprimat
        
    EX: IN: 8, 2, 10000011;    OUT: 0.82, 011000111
                  (10 00 00 11)          (0 11 00 01 11)
                  
           10, 5, 0000000011;  OUT: 1.25, 00100011
                  (00 00 00 00 11)       (0 01 00 01 1)
                  
           10, 3, 1110001110;  OUT: 1.11, 110000100
                  (00 01 11 00 01)        (1 10 00 01 00)
    
'''

msg = ""
l_msg = int(input("Dati lungimea measajului: "))

l_blc = int(input("Dati lungimea blocului: "))

i = 0
while i < l_msg:
    msg += input()
    i += 1
    
print("DBG: mesajul care trebuie comprimat:", msg)


def comprima(sir, lungime_bloc, simbol_p):
    '''
        Functia care va face compresia pe baza simbolului preferat
    '''
    print(f"DBG: === Compresie === sir: {sir}, lungime bloc: {lungime_bloc}, simbol: {simbol_p}")
    sir_comprimat = ""

    if simbol_p == "0":
        prefix = "1"
        simbol_n = "1"
    else:
        prefix = "0"
        simbol_n = "0"
        
    sir_comprimat += simbol_p
        
    poz_start = 0
    
    nr_bloc_uri = len(sir)//lungime_bloc
    bloc_extra = len(sir)%lungime_bloc
    
    i = 0
    while i < nr_bloc_uri:
        poz_sfarsit = poz_start + lungime_bloc
        b = sir[poz_start:poz_sfarsit]
        print("DBG: bloc:", b)

        if simbol_n in b:
            b = simbol_n + b
        else:
            b = simbol_p
            
        sir_comprimat += b
        
        poz_start += lungime_bloc
        i += 1
        
    # tratare caz ultim bloc
    if bloc_extra:
        b = sir[poz_start:]
        print("DBG: bloc extra:", b)
        sir_comprimat += simbol_n + b
    
    r_compr = round(100*len(sir)/len(sir_comprimat))/100
  
    return sir_comprimat, r_compr


print("\nVerificare pentru sirurile date ca exemplu:\n")
for c in (("10000011", 2),("0000000011", 5), ("1110001110", 3)):
    
    c_0 = comprima(c[0], c[1], "0")
    c_1 = comprima(c[0], c[1], "1")

    print(f"DBG: compresie 0: {c_0}, compresie 1: {c_1}")

    if (c_0[1] >= c_1[1]):
        print(c_0[0])
    else:
        print(c_1[0])


print("\nCompresie pentru parametrii dati in linie de comanda\n")

c_0 = comprima(msg, l_blc, "0")
c_1 = comprima(msg, l_blc, "1")

print(f"DBG: compresie 0: {c_0}, compresie 1: {c_1}")

if (c_0[1] >= c_1[1]):
    print(c_0[0])
else:
    print(c_1[0])
        
        
