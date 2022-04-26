'''
    Problema WBS Adaptiv - compresie prin tehnica Wite Block Skipping adaptat
    adica compresie blocuri de 0 sau 1 la o singura valoare.
'''

msg = ""
l_msg = int(input("Dati lungimea measajului: "))
i = 0;
while i < l_msg:
    msg += input()
    i += 1
    
print("DBG: mesajul care trebuie comprimat:", msg)    
