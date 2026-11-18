from tkinter import *
# import tkintermapview

def oczywiscie_ze_tak():
    print("oczywiscie ze tak")



root = Tk()
root.geometry("1024x768")
root.title("Mapbook")

# RAMKI
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan = 2)
ramka_mapa.grid(row=2, column=0, columnspan = 7)



# RAMKA LISTA OBIEKTOW
label_lista_obiektow = Label(ramka_lista_obiektow, text = "Lista obiektów: ")
list_box_lista_obiektow = Listbox(ramka_lista_obiektow)

button_pokaz_szczegoly = Button(ramka_lista_obiektow, text = "Pokaż szczegóły")
button_edytuj_obiekt = Button(ramka_lista_obiektow, text = "Edytuj obiekt")
button_usun_obiekt = Button(ramka_lista_obiektow, text = "Usuń obiekt")

label_lista_obiektow.grid(row=0, column=0)
list_box_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt.grid(row=2, column=2)


# RAMKA_FORMULARZ
label_formularz = Label(ramka_formularz, text = "Formularz: ")
label_imie = Label(ramka_formularz, text = "Imię: ")
label_miejscowosc = Label(ramka_formularz, text = "Miejscowość: ")
label_posty = Label(ramka_formularz, text = "Postów: ")

label_formularz.grid(row=0, column=0)
label_imie.grid(row=1, column=0)
label_miejscowosc.grid(row=2, column=0)
label_posty.grid(row=3, column=0)



# ENTRY_IMIE
entry_formularz = Entry(ramka_formularz)
entry_imie = Entry(ramka_formularz)
entry_miejscowosc = Entry(ramka_formularz)
entry_posty = Entry(ramka_formularz)

entry_imie.grid(row=1, column=1)
entry_miejscowosc.grid(row=2, column=1)
entry_posty.grid(row=3, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text = "Dodaj obiekt")
button_dodaj_obiekt.grid(row=4, column=0)


# RAMKA SZCZEGOLY OBIEKTU
label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Szczegóły obiektu")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Imię: ")
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = ".....")
label_miejscowosc_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Miejscowość: ")
label_miejscowosc_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = ".....")
label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text = "Postów: ")
label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text = ".....")

label_szczegoly_obiektu.grid(row=0, column=0)
label_imie_szczegoly_obiektu.grid(row=1, column=1)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=2)
label_miejscowosc_szczegoly_obiektu.grid(row=1, column=3)
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=4)
label_posty_szczegoly_obiektu.grid(row=1, column=5)
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=6)


# RAMKA MAPA - doinstalowac bilbioteke tkintermapview
# RAMKA MAPA - doinstalowac bilbioteke tkintermapview
# RAMKA MAPA - doinstalowac bilbioteke tkintermapview
map_widget = tkintermapview Tkintermapview(ramka_mapa, width = 1050, height = 700, corner_radius = 5)

map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)

map_widget.grid(row=0, column=0, columnspan = 7)










root.mainloop()