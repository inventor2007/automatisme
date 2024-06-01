import tkinter, customtkinter, random
import tkinter.messagebox
from functions.database import *
from functions.createPDF import *
from windows.classeMenu import *
from windows.chapitreMenu import *
from windows.automatismeMenu import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()
  
    # configure window
    self.title("CustomTkinter")
    self.geometry(f"{1400}x{580}")

    # configure grid layout (4x4)
    self.grid_columnconfigure((3), weight=3)
    self.grid_columnconfigure((2), weight=1)
    self.grid_columnconfigure((2), weight=1)
    self.grid_rowconfigure((0), weight=1)

    # create sidebar frame with widgets
    self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
    self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
    self.sidebar_frame.grid_rowconfigure((1), weight=1)

    # class menu
    self.open_classe_menu_button = customtkinter.CTkButton(self.sidebar_frame, command=classeMenu, text="Menu Classe")
    self.open_classe_menu_button.grid(row=2, column=0, padx=20, pady=(20, 0))

    self.open_chapitre_menu_button = customtkinter.CTkButton(self.sidebar_frame, command=chapitreMenu, text="Menu Chapitre")
    self.open_chapitre_menu_button.grid(row=3, column=0, padx=20, pady=(20, 0))

    self.open_chapitre_menu_button = customtkinter.CTkButton(self.sidebar_frame, command=automatismeMenu, text="Menu Automatisme")
    self.open_chapitre_menu_button.grid(row=4, column=0, padx=20, pady=20)

    # Logs
    self.logsbox = customtkinter.CTkTextbox(self.sidebar_frame)
    self.logsbox.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="nsew")
    self.logsbox.insert("0.0", "Voici les logs du programme")

    # Select class
    self.class_frame = customtkinter.CTkScrollableFrame(self, label_text="Classe")
    self.class_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.class_frame.grid_columnconfigure(0, weight=1)
    self.class_frame_radio = []
    self.class_var = tkinter.IntVar(value=0)
    for i in get_all_classes_enable():
      radio = customtkinter.CTkRadioButton(master=self.class_frame, variable=self.class_var, value=i[0], text=i[1], command=self.update_chapitres)
      radio.grid(row=i[0], column=0, padx=10, pady=(0, 20))
      self.class_frame_radio.append(radio)

    # Select Chapitre
    self.chapitre_frame = customtkinter.CTkScrollableFrame(self, label_text="Chapitres")
    self.chapitre_frame.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.chapitre_frame.grid_columnconfigure(0, weight=1)
    self.chapitre_frame_switches = []

    # Select Automatisme
    self.automatisme_frame = customtkinter.CTkScrollableFrame(self, label_text="Automatisme")
    self.automatisme_frame.grid(row=0, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
    self.automatisme_frame.grid_columnconfigure(0, weight=1)
    self.automatisme_frame_switches = []

    # Nombre d'automatisme
    self.nombre_automatisme = customtkinter.CTkOptionMenu(self, dynamic_resizing=True, values=["5 Automatismes", "10 Automatismes"])
    self.nombre_automatisme.grid(row=1, column=1, padx=20, pady=(20, 10))

    # Create automatisme
    self.create_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Crée l'automatisme", command=self.create_automatisme_button)
    self.create_button.grid(row=1, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

    self.add_class_window = None
  
  def update_chapitres(self):
    chapitres = get_chapitres_by_classe_enable(self.class_var.get())

    if self.chapitre_frame_switches != []:
      for i in self.chapitre_frame_switches:
        i.grid_remove()
      self.chapitre_frame_switches.clear()
    
    if self.automatisme_frame_switches != []:
      for i in self.automatisme_frame_switches:
        i.grid_remove()
      self.automatisme_frame_switches.clear()

    for i in chapitres:
      switch = customtkinter.CTkSwitch(master=self.chapitre_frame, text=i[1], command=self.update_automatismes)
      switch.grid(row=i[0], column=0, padx=10, pady=(0, 20))
      
      self.chapitre_frame_switches.append(switch)
  
  def update_automatismes(self):
    switchOn = []
    for i in self.chapitre_frame_switches:
      if i.get():
        switchOn.append(i.grid_info()['row'])

    automatismes = get_all_automatismes_by_chapitres_enable(switchOn)

    if self.automatisme_frame_switches != []:
      for i in self.automatisme_frame_switches:
        i.grid_remove()
      self.automatisme_frame_switches.clear()

    for i in automatismes:
      switch = customtkinter.CTkSwitch(master=self.automatisme_frame, text=i[1])
      switch.select()
      switch.grid(row=i[0], column=0, padx=10, pady=(0, 20))
      
      self.automatisme_frame_switches.append(switch)
  
  def create_automatisme_button(self):
    switchOn = []
    for i in self.automatisme_frame_switches:
      if i.get():
        switchOn.append(i.grid_info()['row'])

    random.shuffle(switchOn)

    if self.nombre_automatisme.get() == "5 Automatismes":
      if len(switchOn) < 5:
        return self.logsbox.insert("0.0", "Vous n'avez pas sélectionné assez d'automatismes !\n")

      automatismeId = random.sample(switchOn, 5)
      create_automatisme(5, automatismeId, 2)

    elif self.nombre_automatisme.get() == "10 Automatismes":
      if len(switchOn) < 10:
        return self.logsbox.insert("0.0", "Vous n'avez pas sélectionné assez d'automatismes !\n")
      
      automatismeId = random.sample(switchOn, 10)
      create_automatisme(10, automatismeId, 1)
  
  def open_class_menu(self):
    classeMenu(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()