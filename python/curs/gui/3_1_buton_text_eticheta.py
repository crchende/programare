import tkinter as tk

top_win = tk.Tk()

e1_txt_var = tk.StringVar()
l1_txt_var = tk.StringVar()

def print_salut():
    print("Salut")


def print_altceva(sir1):
    print(sir1)

#
# Afiseaza text din entry box pe ecran si in label-ul de sub entry box
#
def print_continut_e1(entry_var, label_txt_var):
    print("Apasat pe b1")
    global s
    s = e1.get()
    print(s)
    label_txt_var.set(s)
    
    
x_var = "buna"

#afiseaza Salut la pornirea aplicatiei apoi nu mai afiseaza nimic
#b1 = tk.Button(top_win, text = "Salut", command = print("Salut"))

#print_salut nu are parametrii
#b1 = tk.Button(top_win, text = "Salut", command = print_salut)

#vreau sa configurez butonul cu o functie cu parametrii
#
# Nu merge asa. Eroare: print_altceva cere parametru
# Nu merge nici: print_altceva(x_var) - va afisa x_var doar la inceput
# Trebuie gasita o metoda sa invoce functia print_var(param) la fiecare apasare, nu doar la creerea butonului
# 
#b1 = tk.Button(top_win, text = "Salut", command = print_altceva)

# V1 - folosire 'lambda'

# fara lambda, da eroare, e1 fiind definit dupa b1. Cu lambda se va executa codul la apasare buton
b1 = tk.Button(top_win, text="Salut", command = lambda: print_continut_e1(e1, l1_txt_var))

e1 = tk.Entry(top_win, textvariable = e1_txt_var)
l1 = tk.Label(top_win, text = "eticheta", textvariable = l1_txt_var)

b1.pack()
e1.pack()
l1.pack()

e1_txt_var.set("Text Final")

s = e1_txt_var.get()

print("__name__ = ", __name__)
if __name__ == "__main__":
    top_win.mainloop()
