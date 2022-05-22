'''
    cip_chende@yahoo.com

    Examplu site flask cu citire date din baza de date si actualizare nume
    materii 'inline', fara folosire formular.    
    
'''


from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap

# Baza de date folosita este MariaDB sau MySQL
# Pentru alte tipuri de baze de date trebuie folosite alte module.
import mysql.connector
from mysql.connector import errorcode

####################################################
# Functii pentru preluarea datelor din baza de date flask_site1
####################################################

################################################################################
# Informatii pentru conectarea la baza de date:
################################################################################
db_info = {
  'user': 'flaskdev',
  'password': 'parolaflask123',
  'host': '127.0.0.1',
  'database': 'flask_site1',
  'autocommit': True,
  'raise_on_warnings': True
}

################################################################################
# Legatura cu baza de date flask_site1. Conectare si procesare date.
################################################################################
def conectare_db(config):
    try:
        print("Incerc sa ma conectez la serverul local MySQL/MariaDB si la baza de date flask_site1")
        conexiune = mysql.connector.connect(**config)
      
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
    
    cursor_db = conexiune.cursor()

    return conexiune, cursor_db

'''
# TBD - de inchis conexiunea explicit la iesirea din program
def inchide_conexiune_db(conexiune, cursor):
    print("Inchid cursorul baza de date")
    cursor.close() # inchid si cursorul

    print("Inchid conexiunea la serverul de baza de date")
    conexiune.close()
'''

def db_select(str_interogare, cursor_db):
    cursor_db.execute(str_interogare)
    date = cursor_db.fetchall()
    return date
            
def db_gaseste_studenti(cursor_db):
    q = "SELECT * FROM studenti;"
    date = db_select(q, cursor_db)
    print("DBG: db_gaseste_studenti: info studenti:", date)
    return date
    
def db_gaseste_materii(str_interogare):
    q = "SELECT * from materii;"
    date = db_select(q, cursor_db)
    return date

def db_gaseste_cursuri(cursor_db):
   
    # interogare compusa, care foloseste date din mai multe tabele
    q = "SELECT materii.nume, studenti.nume, studenti.prenume, \
            cursuri.data, cursuri.ora \
            FROM materii, studenti, cursuri \
            WHERE materii.id = cursuri.id_materie \
            AND studenti.id=cursuri.id_student;"

    date = db_select(q, cursor_db)
    
    # data si ora apar intr-un format special de obiect datetime
    # trebuie prelucrate pentru o afisare corespunzatoare
    
    ret = []
    
    for rand in date:
        # 0        1       2      3                            4
        #(Fizica, Ionescu, Ion, datetime.date(2022, 5, 16), datetime.datetime(2022, 5, 13, 9, 0))
        el_ret = []
        for i in range(len(rand)):
            if i == 3:
                an_luna_zi = rand[i].strftime("%Y-%m-%d")
                el_ret.append(an_luna_zi)
            elif i == 4:
                ora = rand[i].seconds // 3600
                mn =     rand[i].seconds % 3600
                el_ret.append("{:02}:{:02}".format(ora, mn))
            else:
                el_ret.append(rand[i])
        
        ret.append(el_ret)
    
    # Rezultat - o lista de liste pentru afisare in pagina WEB            
    return ret


################################################################################
# Functii care prelucreaza datele si le pregatesc pentru a fi afisate
################################################################################
def actualizeaza_nume_materie(id_el, nume_nou, cursor_db):
    global conex_db
    print("AICI1")
    q = "UPDATE materii SET nume = '{}' WHERE id = {};".format(nume_nou, id_el)
    #q = "UPDATE materii SET nume = 'MATE_Z' WHERE id = 1;"
    #q = "UPDATE materii SET nume = %s WHERE id = %d;"
    print("DBG: q:", q, "-")
    
    #modific numele materiei
    #daca interogarea esueaza, rezultatul este un generator
    try:
        #g1 = cursor_db.execute(q, nume_nou, id_el)
        cursor_db.execute(q)
        conex_db.commit()
    except Exception as e:
        print("Eroare UPDATE:", e)
       
    print("AICI2")
    #citesc numele modificat
    q = "SELECT nume FROM materii WHERE id = {};".format(id_el)
    #q = "SELECT nume FROM materii WHERE id = 1;"
    print("DBG: interogare valoare modificata")
    
    try:
        cursor_db.execute(q)
    except Exception as e:
        print("DBG: Eroare citire dupa actualizare: ", e)
    
    d = cursor_db.fetchone()
    print("DBG: rezultat select: ", d)
    nume_nou_db = d[0]

    print("DBG: nume_nou_db:", nume_nou_db)
    return nume_nou_db
    
    #return "ACK from DB"
    
    
    


####################################################
# Conectarea la baza de date + testare legatura cu baza de date
####################################################
conex_db, cursor_db = conectare_db(db_info)

# DBG - verificare functionare legatura cu baza de date
print("DBG studenti: ", db_gaseste_studenti(cursor_db))
print("DBG materii:  ", db_gaseste_materii(cursor_db))
print("DBG cursuri:  ", db_gaseste_cursuri(cursor_db))


# EXEMPLE ALTE INTEROGARI BAZA DE DATE:
# UPDATE `studenti` SET `comentarii` = '*********' WHERE `studenti`.`id` = 2; 
# INSERT INTO `studenti` (`id`, `nume`, `prenume`, `comentarii`) VALUES (NULL, 'Radulescu', 'Radu', '');
# DELETE FROM `studenti` WHERE `studenti`.`id` = 9

# Pentru debugging DB decomenteaza linia exit().
# nu se va mai trece la partea de program cu interfata WEB
# exit()



####################################################
# Pornirea aplicatiei FLASK si definirea tabelei de rutare
####################################################
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    #return '<h1>BUNA</h1>'
    return render_template('index.html', page="HHH")
    
@app.route('/materii')
def materii():
    lst_materii = [("ID", "Nume")]
    lst_materii.extend(db_gaseste_materii(cursor_db))
    print(lst_materii)
    return render_template('index.html', page="materii", materii=lst_materii)

@app.route('/modifica/materie')
def modifica_materie():
    global cursor_db    
    id_el = request.values['id']
    val_n = request.values['valnoua'].strip()   
    #print("DBG: request.values:", request.values)
    #print("DBG: val_n, id_el", id_el, val_n)
    #print("DBG: modific materie: id, valoare: ", id_el, val_n)
    ret = actualizeaza_nume_materie(id_el, val_n, cursor_db)
    #ret = "DBG"
    return(ret)

@app.route('/studenti')
def studenti():
    lst_studenti = [("ID", "Nume", "Prenume", "Comentarii")]
    lst_studenti.extend(db_gaseste_studenti(cursor_db))
    #print(lst_studenti)
    return render_template('index.html', page="studenti", studenti=lst_studenti)

@app.route('/cursuri')
def cursuri():
    lst_cursuri = [("Materie", "Nume", "Prenume", "Data", "Ora")]
    lst_cursuri.extend(db_gaseste_cursuri(cursor_db))
    return render_template('index.html', page="cursuri", cursuri=lst_cursuri)


