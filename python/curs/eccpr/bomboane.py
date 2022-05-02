'''
    Bomboane
    (pozitie ghid pregatire python: 9)    
    
    Sumar:
    Un copil primeste zilnic o suma de bani de care cumpara bomboane
    Magazinul vinde in fiecare zi un anume tip de bomboane cu o anume
    aroma.
    Aroma da gradul de fericire.
    
    Daca cumpara bomboana - gradul de fericire creste cu gradul de fericire
    al bomboanei
    
    Fericirea scade doar daca copilul nu a cumparat in oricare din zilele
    trecute cel putin o bomboana cu aroma mai buna decat cea din ziua curenta
    pe care nu si-o permite.
    Gradul de fericire scade cu gradul de fericire al aromei
    
    Date de intrare:

    IN: linia 1: nr zile
        linia 2: suma primite in fiecare zi
        linia 3: pret_bomboana aroma_bomboana (zi 1)
        ...
        linia n: pret_bomboana aroma bomboana (zi n)
        
    OUT: grad fericire 
    
    EX: 1) 
        IN: 3
            10 10 10
            10 20
             9 10
            11 50
            
        OUT: 80
        
        2)
        IN: 4
            10 10 10 4
            10 20
            10 10
            11 50
            15 10
            
        OUT: -20
'''

nr_zile = input("Dati numarul de zile: ")
suma_zi = input("Dati suma pe zi: ")

lst_bomboane = []
for i in range(int(nr_zile)):
    bomboana = input("Dati pret si aroma bomboana: ")
    lst_bomboane.append(bomboana)
    
print(f"DBG: preluat date:\nnr zile: {nr_zile}\n suma pe zi: {suma_zi}\n bomboane disponibile pe zi: {lst_bomboane}")

fericire = 0
max_fericire_b = 0
rest = 0
l_suma_zi = suma_zi.split()
for i in range(int(nr_zile)):
    s = int(l_suma_zi[i]) + rest
    b = lst_bomboane[i].split()
    pret_b = int(b[0])
    fericire_b = int(b[1])
    
    if s >= pret_b:
        fericire += fericire_b
        if max_fericire_b < fericire_b:
            max_fericire_b = fericire_b
        rest = s - pret_b            
       
    elif fericire_b > max_fericire_b:
        fericire -= fericire_b        
        rest = s
        
print(fericire)
