import mysql.connector
from mysql.connector import errorcode

################################################################################
# Informatii pentru conectarea la baza de date:
################################################################################
config = {
  'user': 'flaskdev',
  'password': 'parolaflask123',
  'host': '127.0.0.1',
  'database': 'flask_site1',
  'raise_on_warnings': True
}

################################################################################
# Conectare la baza serverul de baze de date si la baza de date flask_site1
################################################################################
try:
    print("Incerc sa ma conectez la serverul local MySQL/MariaDB si la baza de date flask_site1")
    cnx = mysql.connector.connect(**config)
  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Probleme cu user-ul sau parola")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Baza de date nu exista")
    else:
        print(err)
    
    print("Verificati, va rog problema de conectare !!!")
    # programul se termina daca conexiunea esueaza
    exit()

# obtinere cursor:
c = cnx.cursor()    

################################################################################
# Interogari SQL: SELECT, INSERT, UPDATE, DELETE
################################################################################

# SELECT
#functie de interogare a bazei de date
def executa_si_afiseaza(q, sir_formatare = ""):
    global c
    print("Interogare: q:", q)
    
    c.execute(q);
    r1 = c.fetchone();
    frmt = "{}"
    for i in range(len(r1) - 1):
        frmt += " {}"
        
    print("frmt: ", frmt)
    
    if sir_formatare != "":
        frmt = sir_formatare;
        
    print("r1:", r1)
    print(frmt.format(*r1))
    
    for rand in c:
        print(rand)
        print(frmt.format(*rand))       

def executa_si_afiseaza_cu_data_si_timp(q):
    #(1, 1, 1, datetime.date(2022, 5, 16), datetime.datetime(2022, 5, 13, 9, 0))
    frmt = "{:<10} {:<10} {:<10} {} {:02}:{:02}"
    c.execute(q)
    
    for rand in c:
        data = rand[3].strftime("%Y-%m-%d")
        ora = rand[4].seconds // 3600
        mn = rand[4].seconds % 3600

        print(frmt.format(rand[0], rand[1], rand[2], data, ora, mn))  


# INTEROGARI SELECT:
q_tabele_simple = ["SELECT * from studenti;", 
        "SELECT * from materii;"]
        
q_cu_data_si_timp = "SELECT * from cursuri;"
        
        
q_compus = "SELECT materii.nume, studenti.nume, studenti.prenume, \
            cursuri.data, cursuri.ora \
            FROM materii, studenti, cursuri \
            WHERE materii.id = cursuri.id_materie \
            AND studenti.id=cursuri.id_student;"

q_studenti_mate_ora_9 = "SELECT studenti.nume, studenti.prenume, \
                            cursuri.data, cursuri.ora \
                            FROM `studenti`, `cursuri` \
                            WHERE cursuri.id_materie=1 \
                            AND studenti.id=cursuri.id_student \
                            AND ora='09:00'"

for q in q_tabele_simple:
    executa_si_afiseaza(q)
    
print("\nTabela cursuri cu ID-uri:")
print("-------------")
executa_si_afiseaza_cu_data_si_timp("SELECT * from cursuri;")
print("\nTabela cursuri cu nume, nu ID-uri pentru materii si studenti:")
print("-------------")
executa_si_afiseaza_cu_data_si_timp(q_compus)

print("\nStudenti curs 'Matematica' ora 9:00")
print("-------------")
frmt = "{:<10} {:<10} {} {:02}:{:02}"
c.execute(q_studenti_mate_ora_9)
for rand in c:
    #print(rand)
    data = rand[2].strftime("%Y-%m-%d")
    ora = rand[3].seconds // 3600
    mn = rand[3].seconds % 3600

    print(frmt.format(rand[0], rand[1], data, ora, mn)) 

################################################################################
# Terminare program - inchid conexiunea la server
################################################################################
print("\n*******\n")
c.close() # inchid si cursorul

print("Inchid conexiunea la serverul MariaDB")
cnx.close()

