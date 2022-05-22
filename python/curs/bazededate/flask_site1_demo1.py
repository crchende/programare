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
  'raise_on_warnings': True,
  'autocommit': True,
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
#q = "SHOW tables;"
q = "SELECT * from studenti;"

# Variante de citire rezultate interogara

print("\n1. Varianta cu fetchone si iterare rand cu rand")
c.execute(q)
# c.rowcount nu functioneaza - arata -1
print("Rezultat interogare: (fiecare rand este sub forma unui tuplu)")
while True:
    rand = c.fetchone()
    if not rand:
        break
    print(rand)

print("\n2. Varianta cu fetchall:")
c.execute(q)
# print(c.rowcount) - nu functioneaza. arata -1
randuri = c.fetchall();
for r in randuri:
    print(r)

print("\n3. Varianta 3 - cu iterare directa rezultat interogare")
c.execute(q)
for rand in c:
    print(rand)


print("\nRezultatul contine obiecte de tip data / timp")
q = "SELECT * from cursuri"
c.execute(q)
for c_id, id_materie, id_student, dt_obj, tdif_obj in c:
    
    frmt = "{:2} {:2} {:2} {} {:02}:{:02}"
    
    dt = dt_obj.strftime("%Y-%m-%d")
    ora = tdif_obj.seconds // 3600
    mn = tdif_obj.seconds % 3600
    print(frmt.format(c_id, id_materie, id_student, dt, ora, mn))
    

print("\nInterogare compusa, cu date din mai multe tabele:")
q_compus = "SELECT materii.nume, studenti.nume, studenti.prenume, \
            cursuri.data, cursuri.ora \
            FROM materii, studenti, cursuri \
            WHERE materii.id = cursuri.id_materie \
            AND studenti.id=cursuri.id_student;"
            
c.execute(q_compus)

for mat, std_n, std_p, dt_obj, td_obj in c:
    frmt = "{:<20} {:<10} {:10} {} {:02}:{:02}"
    dt = dt_obj.strftime("%Y-%m-%d")
    ora, mn = tdif_obj.seconds // 3600, tdif_obj.seconds % 3600
    print(frmt.format(mat, std_n, std_p, dt, ora, mn))
    
    
    
    
################################################################################
# Terminare program - inchid conexiunea la server
################################################################################
'''
print("\n*******\n")
c.close() # inchid si cursorul

print("Inchid conexiunea la serverul MariaDB")
cnx.close()

'''
