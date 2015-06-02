from tkinter import *

# Stanja
NEVTRALNO = 0
OVAL_ZAC = 1
OVAL_RISEM = 2


class Slikar():
    def __init__(self, master):

        self.stanje = NEVTRALNO
        self.tocka = None
        self.trenutni = None
        # Glavni menu
        menu = Menu(master)
        master.config(menu=menu) # Dodamo menu

        # Naredimo podmenu "File"
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        # Dodamo izbire v file_menu
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_separator() # To doda separator v menu
        file_menu.add_command(label="Izhod", command=master.destroy)


        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.grid(row=0, column=0, columnspan=3)

        self.canvas.bind("<Button-1>", self.pritisk_levi)
        self.canvas.bind("<B1-Motion>", self.premik_levi)
        self.canvas.bind("<ButtonRelease-1>", self.spusti_levi)
        self.canvas.bind("<Escape>", self.razveljavi)
               
        gumb_oval = Button(master, text="Oval", command=self.narisi_oval)
        gumb_oval.grid(row=1, column=0)
        
        gumb_pravokotnik = Button(master, text="Pravokotnik", command=self.narisi_pravokotnik)
        gumb_pravokotnik.grid(row=1, column=1)

        gumb_crta = Button(master, text="Črta", command=self.narisi_crto)
        gumb_crta.grid(row=1, column=2)

        self.napis_spodaj = StringVar(value="Izberi lik")
        napis = Label(master, textvariable=self.napis_spodaj)
        napis.grid(row=2, column=0, columnspan=3)

    def narisi_oval(self):
        if self.stanje == NEVTRALNO:
            self.napis_spodaj.set("Levi pritisk za 1. točko.")
            self.stanje = OVAL_ZAC
        
    def narisi_pravokotnik(self):
        print('Ni še sprogramirano ...')

    def narisi_crto(self):
        print('Ni še sprogramirano ...')

    def pritisk_levi(self, event):
        if self.stanje == OVAL_ZAC:
            self.tocka = (event.x, event.y)
            self.trenutni = self.canvas.create_oval(
                event.x, event.y,
                event.x, event.y)
            self.napis_spodaj.set("({0},{1})".format(event.x, event.y));
            self.stanje = OVAL_RISEM

    def premik_levi(self, event):
        if self.stanje == OVAL_RISEM:
            self.canvas.coords(self.trenutni, self.tocka[0], self.tocka[1],
                                 event.x, event.y)
            self.napis_spodaj.set("({0},{1})".format(event.x, event.y));

    def spusti_levi(self, event):
        if self.stanje == OVAL_RISEM:
            self.canvas.coords(self.trenutni, self.tocka[0], self.tocka[1],
                                 event.x, event.y)
            self.napis_spodaj.set("Izberi lik")
            self.stanje = NEVTRALNO

    def razveljavi(self):
        print('Ni še sprogramirano ...')
        
    def odpri(self):
        rez = filedialog.askopenfile()
        ime = rez.name
        with
        print('Ni še sprogramirano ...')

    def shrani(self):
        print('Ni še sprogramirano ...')


# Naredimo glavno okno
root = Tk()

aplikacija = Slikar(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
