from tkinter import *

# Stanja
NEVTRALNO = 0
CRTA_ZAC = 1
CRTA_RISANJE = 2

class Slikar():
    def __init__(self, master):

        self.stanje = NEVTRALNO
        self.tocka = None
        self.trenutni_lik = None
        
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
        file_menu.add_command(label="Quit", command=master.destroy)


               
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.canvas.bind("<Button-1>", self.levi_pritisni)
        self.canvas.bind("<B1-Motion>", self.levi_premikaj)
        self.canvas.bind("<ButtonRelease-1>", self.levi_spusti)
        master.bind("<Escape>", self.opusti) 

        gumb_crta = Button(master, text="Črta", command=self.narisi_crto)
        gumb_crta.grid(row=1, column=0)

        gumb_oval = Button(master, text="Oval", command=self.narisi_oval)
        gumb_oval.grid(row=1, column=1)

        gumb_pravokotnik = Button(master, text="Pravokotnik", command=self.narisi_pravokotnik)
        gumb_pravokotnik.grid(row=1, column=2)

        self.napis = StringVar(value="Izberi lik.")
        label = Label(master, textvariable=self.napis)
        label.grid(row=2, column=0, columnspan=3)

    def odpri(self):
        ime = filedialog.askopenfilename()
        with open(ime, encoding="utf8") as f:
            for v in f:
                print(v)

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        with open(ime, "wt", encoding="utf8") as f:
            f.write("Evo, smo shranili")

    def levi_pritisni(self, event):
        if self.stanje == CRTA_ZAC:
            self.tocka = (event.x, event.y)
            self.trenutni_lik = self.canvas.create_line(event.x, event.y, event.x, event.y)
            self.napis.set("({0},{1})".format(event.x, event.y))
            self.stanje = CRTA_RISANJE

    def levi_premikaj(self, event):
        if self.stanje == CRTA_RISANJE:
            self.canvas.coords(self.trenutni_lik,
                               self.tocka[0], self.tocka[1],
                               event.x, event.y)
            self.napis.set("({0},{1})".format(event.x, event.y))            
            

    def levi_spusti(self, event):
        if self.stanje == CRTA_RISANJE:
            self.canvas.coords(self.trenutni_lik,
                               self.tocka[0], self.tocka[1],
                               event.x, event.y)
            self.napis.set("Izberi lik.")            
            self.stanje = NEVTRALNO
        
    def narisi_crto(self):
        if self.stanje == NEVTRALNO:
            self.napis.set("Pritisni za 1. točko črte.")
            self.stanje = CRTA_ZAC

    def opusti(self, event):
        if self.stanje == CRTA_ZAC:
            self.napis.set("Izberi lik.")
            self.stanje = NEVTRALNO           
        elif self.stanje == CRTA_RISANJE:
            self.canvas.delete(self.trenutni_lik)
            self.napis.set("Izberi lik.")
            self.stanje = NEVTRALNO
            
    def narisi_oval(self):
        print("Rišem oval ...")

    def narisi_pravokotnik(self):
        print("Rišem pravokotnik ...")





# Naredimo glavno okno
root = Tk()

aplikacija = Slikar(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
