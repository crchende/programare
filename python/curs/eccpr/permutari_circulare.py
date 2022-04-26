'''
    Se da un numar natural n
    Se cere numarul natural m care sa fie maximul obtinut din permutarile
    circulare ale lui n scris in baza 2
    
    ex: n = 13 -> 1101
    permutari:
        1110 -> 14
        0111 -> 7
        1011 -> 11
        1101 -> 13
   
    max = 1110 -> 14
'''


def nr_in_lst_bin(numar):
    '''
        Conversie numar natural -> lista elemente binare
    '''
    ret = []
    
    c = numar
    while c > 0:
        r = c % 2
        #print("DBG: r:", r)
        c = c // 2
        ret.insert(0, r)

    return ret
    
def lst_bin_in_nr(lst_bin):
    '''
        Conversie lista elemente binare -> numar natural
    '''
    n = 0;
    l = len(lst_bin) - 1
    #   print("DBG: l: ", l)
    for i in range(l,-1,-1):
        p_2 = 2**(l-i)
        n += p_2 * lst_bin[i]
        #print("DBG: i", i, "p_2: ", p_2, "lst_bin[i]:", lst_bin[i], "n:", n)
    
    return n

def perm_circ_si_max(lst, nr):
    '''
        Generare permutari circulare.
        Determinare numar natural maxim din permutari.
    '''
    max = nr
    n = 1
    p_c = lst[:]
    while n < len(lst):
        e_0 = p_c[-1]
        el = p_c[0:-1]
        p_c = [e_0]
        p_c.extend(el)
        
        nr = lst_bin_in_nr(p_c)
        if nr > max:
            max = nr

        print(f"DBG: {p_c} {nr:-5} max: {max:}") # formatare cu format string
        
        n += 1

    return max
 
str_nr = input("Dati numarul: ")

l_b = nr_in_lst_bin(int(str_nr))
print("DBG: {1} -> {0}".format(l_b, str_nr)) # formatare cu format, si nr ordine
max = perm_circ_si_max(l_b, int(str_nr))
print("DBG: max:", max) # print cu mai multi parametrii
print(max)


