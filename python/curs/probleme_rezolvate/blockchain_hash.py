'''
    Blockchain Hash.
    (pozitie ghid pregatire python: 17)
    
    Procedura hashing:
        Pentru un numar natural, se iau cate doua cifre de la stanga spre 
        dreapta si se scade cifra mai mica din cea mai mare. cu rezultatul se 
        formeaza un nou numar.
        Se aplica transformarea de k ori, unde k este dat in problema.
        Numerele cu o singura cifra nu se modifica.
        Hash = suma rezultate obtinute la transformari.
        
        Ex: Nr initial: 5734; nr transformari k = 3
            5734 -> 241 -> 23 -> 1
            
            Hash = 241 + 23 + 1 = 265
            
        Cerinta: fiind date mai multe numere (N numere) si numarul de k de
        transformari, sa se gaseasca rezultatul cu cea mai mare valoare.
        
        Date de intrare:    N - nr numere
                            k - nr transformari
                            cele N numere
        
        Iesire:             Hash-ul cu cea mai mare valoare
        
        Set date de verificare:
        1)  2 2         (linie 1 intrare)
            5734 1234   (linie 2 intrare)
            
            ( Transformari:
                5734 -> 241 -> 23; Hash = 241 + 23 = 264
                1234 -> 111 -> 0); Hash = 111 + 0  = 111 )
            
        2)  2 3         (linie 1 intrare)
            2228 6      (linie 2 intrare)
            
            ( Transformari:
                2228 -> 6 -> 6 -> 6; Hash = 18
                   6 -> 6 -> 6 -> 6; Hash = 18 )
            
'''
#################
# Date de intrare
#################
N_si_k = input("Dati N si k: ")
l_N_si_k = N_si_k.split()
N = int(l_N_si_k[0])
k = int(l_N_si_k[1])

str_numere = input("Dati numerele: ")
lst_str_numere = str_numere.split()

# transformare lista initiala cu list comprehension
lst_numere = [int(nr) for nr in lst_str_numere]  


def invers(nr):
    inv = 0
    c = nr
    while c > 0:
        r = c % 10
        c = c // 10
        inv = inv*10 + r
        
    return inv

def transformare(nr):
    tr = 0
    
    inv = invers(nr)
    #print("DBG: inv: ", inv)
    c = inv
    
    i = 0
    while c > 0:
        r = c % 10
        c = c // 10
        
        # La fiecare iteratie ne intereseaza atat ultimul ca si penultimul 
        # element. 
        # Daca pentru a gasi penultimul element ajungem cu c = 0, inseamna 
        # ca am ajuns la finalul numarului
        if c == 0:
            if tr == 0:
                #print("DBG: numar cu o cifra")
                return inv
            else:
                break

        # print("DBG: c:", c)
        r2 = c % 10
        if r > r2:
            t = r - r2
        else:
            t = r2 -r
        
        tr = tr * 10 + t
        #print("DBG: r, r2, t, tr:", r, r2, t, tr)
        i += 1  
    
    return tr

'''
# Verificare functii transformare si invers
    
print(transformare(5734))
print(transformare(6))
print(transformare(1))
print(transformare(0))
'''

# k: nrtransformari
def myhash(nr, k):
    h = 0
    i = 0
    while i < k:
        nr = transformare(nr)
        h = h + nr
        i += 1
        
    return h
        
'''
# Verificare hash

print("DBG: hash:", hash(5734, 2))
print("DBG: hash:", hash(5734, 3))

print("DBG: hash:", hash(2228, 3))
print("DBG: hash:", hash(6, 3))
'''

# Gasire valoare maxima hash, cu algoritm de gasire max din sir
max_hash = 0
for nr in lst_numere:
    h = myhash(nr, k)
    print("DBG: nr, hash: ", nr, h)
    if h > max_hash:
        max_hash = h
        
print(max_hash)

