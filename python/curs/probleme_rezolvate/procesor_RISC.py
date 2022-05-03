'''
    Procesor RISC.
    (pozitie ghid pregatire python: 5)

    Simulare procesor RISC.
    Simulatorul primeste o secventa de instructiuni care trebuie executata
    si starea finala a datelor trebuie afisata la iesire. 

    Instructiuni suportate:
    
    lconst <dst> <val>     – se scrie valoarea <val> în registrul <dst>;
    
    add <dst> <src0> <src> – se adună valorile din registrele <src0> și 
                             <src1> și rezultatul se scrie în registrul <dst>;
                             
    mul <dst> <src0> <src> – se înmulțesc valorile din registrele <src0> și
                             <src1> și rezultatul se scrie în registrul <dst>;
                              
    div <dst> <src0> <src> – se împart valorile din registrele <src0> și <src1> 
                             și câtul se scrie în registrul <dst>;
                             
    print <reg> - se afișează valoarea din registrul <reg>.
    
    Tratare eroare impartire la 0 - operatiunea div:
        - se afiseaza "Exception <index>";
        - index - numarul instructiunii care nu a putut fi executata;
        - programul se incheie.
        
    Toate registrele au valoarea initiala 0.
    
    Cerinta: - se da o lista de instructiuni care trebuie executate si afisate
               mesajele printate de program
               
    Set date de verificare:
    1)  Intrare:
            8
            lconst 0 10
            print 0
            lconst 2 1
            add 1 0 2
            mul 2 0 1
            lconst 1 2
            div 0 2 1
            print 0

        Iesire:
            10
            55
        
    2)  Intrare
            7
            lconst 0 10
            lconst 1 -1
            print 0
            add 0 0 1
            print 0
            add 0 0 1
            print 0
            
        Iesire:
            10
            9
            8
            
    3)  Intrare:
            5
            lconst 0 0
            lconst 1 1
            print 0
            div 3 1 0
            print 3
        Iesire:
            0
            Exception: line 4
'''

#reprezentam registrele ca o lista
registre = [0, 0, 0]

# Implementarea functiilor procesorului RISC
# Fiecare functie are ca prim parametru numarul registrului folosit
def lconst(dst, val):
    registre[dst] = val
    print("DBG registre: ", registre)

def add(dst, src0, src):
    registre[dst] = registre[src0] + registre[src]
    print("DBG registre: ", registre)

    
def mul(dst, src0, src):
    registre[dst] = registre[src0] * registre[src]
    print("DBG registre: ", registre)

    
def div(dst, src0, src):
    registre[dst] = registre[src0] // registre[src]
    print("DBG registre: ", registre)

def risc_print(reg):
    print(registre[reg])
    print("DBG registre: ", registre)

    
nr_instructiuni = int(input("Dati numarul de instructiuni de executat: "))

nr_instructiune = 1

while nr_instructiune <= nr_instructiuni:
    msg = "Dati instructiunea {:3}: ".format(nr_instructiune)
    sir_instr = input(msg)

    lst_el_instr = sir_instr.split()

    #obligatoriiu trebuie sa avem numele instructiunii si registrul folosit
    #aici, reprezentat prin pozitia in lista de registre care este o variabila
    #globaa
    nume_instr = lst_el_instr[0]
    poz_registru = int(lst_el_instr[1])
    #print("DBG: nume_instr:   ", nume_instr)
    #print("DBG: poz_registru: ", poz_registru)
    
    # operand pentru instructiune cu 2 parametrii 
    if len(lst_el_instr) == 3:
        op1 = int(lst_el_instr[2])
        print("DBG: op1: ", op1)
    
    # operanzi pentru instructiunea cu 2 parametrii
    # numele instructiunii si destinatia ocupa primele doua pozitii in 
    # instructiune
    if len(lst_el_instr) == 4:
        op1 = int(lst_el_instr[2])
        print("DBG: op1: ", op1)
    
        op2 = int(lst_el_instr[3])
        print("DBG: op2: ", op2)
    
    if(nume_instr == "lconst"):
        lconst(poz_registru, op1)
        
    elif(nume_instr == "add"):
        add(poz_registru, op1, op2)
        
    elif(nume_instr == "mul"):
        mul(poz_registru, op1, op2)
        
    elif(nume_instr == "div"):
        try:
            div(poz_registru, op1, op2)
        except ZeroDivisionError:
            print("Exception line {}".format(nr_instructiune))
            exit()
            
    elif(nume_instr == "print"):
        risc_print(poz_registru)

    nr_instructiune += 1
        
