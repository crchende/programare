import tkinter as tk

mainwin = tk.Tk()

#Varianta 1
#b1 = tk.Button(master = mainwin, text = "Afiseaza", command=print("Afisez ceva"))
# Se afiseaza "Afisez ceva" la pornirea aplicatiei, dupa care nu se mai afiseaza
# nimic chiar daca apas butonul.

# Problema
# - se evalueaza print(...) la apelul functiei Button. La acest moment se afiseaza
#   "Afiseaza ceva"
# - proprietatea 'command' a butonului contine rezultatul apelului pentru print
#   in acest caz

#Varianta 2
b1 = tk.Button(master = mainwin, text = "Afiseaza", command= lambda: print("Afisez ceva"))

# in acest caz, proprietatea 'command' a butonului este asociata cu rezultatul
# apelului 'lambda' care este apelul 'print("Afiseaza ceva")', nu cu rezultatul
# apelului 'print("Afiseaza ceva")'

b1.pack()

mainwin.mainloop()
