'''
    cip_chende@yahoo.com
    
    Dependinte:
        1) Biblioteca selenium din Python
           
           Instalare cu pip:
            pip install selenium
            
           Verificare instalare:
            pip show selenium
        
        2) gecodriver - programul care gestioneaza interactiunea dintre selenium
                        si Firefox- browser care are la baza motorul 'gecko' 
                        dezvoltat de mozilla.
                        
            Download si install:
            https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
    
    Executie program:
        Pornire interpretor python cu parametru numele scriptului.
        Scriptul a fost facut cu python 3.8 si nu a fost testat cu alte 
        versiuni de python.
     
        ex:
            python3 cauta_pe_altex.py
    
    Codul a fost testat in mai 2022.
    Site-urile WEB pot sa-si modifice structura.
    Obiectele din pagina WEB folosite in acest program este posibil sa nu mai 
    existe sau sa fie altfel identificate.
    
    
    
'''

import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


browser_folosit = "Firefox"
wb = wd.Firefox()
wb.delete_all_cookies()

url = "https://altex.ro/home"

de_cautat = "telefoane" #- merge cautarea fara probleme
#de_cautat = "masina de spalat" #- merge cautarea fara probleme

#de_cautat = "laptopuri"; # In aceleasi conditii ca si mai sus, cautarea esueaza
###############
# Mesaj generat:
#Access Denied
#You don't have permission to access "http://altex.ro/laptopuri/cpl/" on this server.

#Reference #18.1fa13554.1622636557.58af80a4
##############

print("\n1) INFO: Pornire Browser: {}. Cautare URL: {}".format(browser_folosit, url))
web_pg = wb.get(url)
altex_logo = WebDriverWait(wb, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'Header-logo'))

print(altex_logo.text)

print("Pagina Incarcata")

# identificare meniu principal
# locator - numele clasei
mmgw = wb.find_element(By.CLASS_NAME, "MainMenuGeneralWrapper")

# Identificare meniu produse din meiul principal printr-un
# locator de tip CSS_SEECTOR
# href - adica link-ul asociat cu obiectul din pagina web
prod_menu_item = mmgw.find_element(By.CSS_SELECTOR, '[href="#produse"]')
# Merge si varianta cu identificare dupa clasa
# prod_menu_item = mmgw.find_element(By.CLASS_NAME, "ProductsMenu")
prod_menu_item.click()

# Identificare si acces submeniuri dupa text sau href

# Meniu laptopuri
print("Navigam in meniul laptop-uri")
laptopuri_m = mmgw.find_element(By.LINK_TEXT, "Laptop, Desktop, IT, Birotica")
laptopuri_m.click()
time.sleep(3)

print("Navigam in meniul Electrocasnice mari")
# Meniu Electrocasnice mari
el_mari_m = mmgw.find_element(By.CSS_SELECTOR, '[href="/electrocasnice-mari-clima/cpl/"]')
el_mari_m.click()
time.sleep(3)

print("Inapoi la laptopuri")
laptopuri_m.click()
time.sleep(2)

print("Dam click pe link-ul 'Laptopuri' din meniu")
laptopuri_m_link = mmgw.find_element(By.CSS_SELECTOR, '[href="https://altex.ro/laptopuri/cpl/"]')
laptopuri_m_link.click()

print("Inchidem fereastra 'Abonament'")
x_abonament = wb.find_element(By.TAG_NAME, "polygon")
x_abonament.click()

print("Accept cookie-urile")
time.sleep(2)
div_cookie = wb.find_element(By.ID, "notice-cookie-block")
btn_accepta = div_cookie.find_element(By.XPATH, "div/button")
print("Gasit buton:", btn_accepta.text, "si dau click")
btn_accepta.click()

print("Gasesc cate calculatoare DELL sunt")
brand_dell_filtru = wb.find_element(By.CSS_SELECTOR, '[href="https://altex.ro/laptopuri/cpl/filtru/brand-3334/dell/"]')

nr_calc_dell_el = brand_dell_filtru.find_element(By.XPATH, 'span[2]/span[2]')
nr_calc_dell = nr_calc_dell_el.text
print("DBG: nr_calc_dell:", nr_calc_dell)
nr_c_dell = nr_calc_dell.strip("()")
print("Total calculatoare DELL: ", nr_c_dell)
print("Selectare brand DELL")
brand_dell_filtru.click()
# pot verifica ca mi-a aparut filtrul selectat deasupra produselor
# wait By.CSS_SELECTOR '[data-filtervalue="dell"]'


print("Div FILTRE")
div_filtre = wb.find_element(By.ID, "catalog-filters-container")
print("Selectare rezolutie ecran")
# cautarea doar in filtre nu in toata pagina este mult mai rapida
dim_ecran_14_filtru = div_filtre.find_element(By.CSS_SELECTOR, '[href="https://altex.ro/laptopuri/cpl/filtru/brand-3334/dell/dimensiune-ecran-inch-8641/14-14-9/"]')

print("Calc cu dim ecran 14'", dim_ecran_14_filtru.text)
dim_ecran_14_filtru.click()
# pot verifica ca mi-a aparut filtrul selectat deasupra produselor
# wait By.CSS_SELECTOR '[data-filtervalue="14-14-9"]'

print("Astept 3 sec pentru incarcarea paginii")
time.sleep(3)
# gasire elemente in pagina
ul_produse = wb.find_element(By.CLASS_NAME,"Products")
if ul_produse.tag_name != 'ul':
    print("Eroare identificare lista produse")
    exit()


print("Am identificat lista de produse")

lst_prod = ul_produse.find_elements(By.TAG_NAME, "li")
lst_txt_prod = []

for el in lst_prod:
    lst_txt_prod.append(el.text)


print("Am gasit urmatoarele produse:\n")
for el in lst_txt_prod:
    print("\n---\n{}\n".format(el))


