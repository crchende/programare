'''
    Se da un cod format din majusculele literelor din alfabatul limbii engleze
    si un cod asociat:
    A -> 1
    B -> 2
    ...
    Z -> 26
    
    Reguli de decodare:
        - cand urmatoarele 2 cifre din mesaj pot fi interpreteat ca o litera
          se va interpreta in acest fel, ignorand posibilitatea ca o cifra
          sa reprezinte o litera
          
        - daca pe pozitia curenta se afla 0, 0x se va interpreta ca x, cu oricare
          x intre 1 si 9
          
        - 00 se va decoda ca spatiu
    
    Se da un mesaj - sub forma unui sir de cifre
    
    Sa se decodeze mesajul.

    ex: 195318520           -> SECRET
        2671513152000011202 -> ZGOMOT ALB
    
'''

sir_codat = input("Dati sirul codat:")

litere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("DBG: nr litere:", len(litere))

# generare cod
dict_cod = {}
for i in range(len(litere)):
    dict_cod[str(i+1)] = litere[i]
    if i+1 < 10:
        s = "0" + str(i+1)
        dict_cod[s] = litere[i]

#adaugare cheie speciala
dict_cod["00"] = " "

print("DBG: dict_cod: ", dict_cod)

# Decodare
msg_clar = ""
k = ""
for el in sir_codat:
    print("DBG: el:", el)
    if k == "":
        if int(el) > 2:
            msg_clar += dict_cod[el]
            print("DBG: el > 2:", el, "msg_clar:", msg_clar)
        else:
            k = el
            print("DBG: salvez k:", k)
            continue
    else:
        k += el
        msg_clar += dict_cod[k]
        print("DBG: chieie compusa: k:", k, "msg_clar:", msg_clar)
        k = ""
   
print(msg_clar)
   
           



    
