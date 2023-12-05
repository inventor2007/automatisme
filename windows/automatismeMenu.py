import customtkinter
from functions.database import *

class automatismeMenu(customtkinter.CTkToplevel):
  def __init__(self):
    super().__init__()
    self.minsize(650, 110)
    # self.maxsize(340, 110)

    self.grid_columnconfigure((1), weight=1)
    self.grid_columnconfigure((0, 2), weight=0)

    classes = []
    for i in get_all_classes():
      classes.append(i[1])
    if classes == []:
      classes.append('Aucune Classe')
    self.name_classe = customtkinter.CTkOptionMenu(self, dynamic_resizing=True, values=classes, command=self._update_chapitres)
    self.name_classe.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))

    self.name_chapitre = customtkinter.CTkOptionMenu(self, dynamic_resizing=True, command=self._update_automatisme)
    self.name_chapitre.grid(row=1, column=0, padx=(20, 0), pady=(20, 20))
    self._update_chapitres()

    self.entry = customtkinter.CTkEntry(self, placeholder_text="Expression de l'automatisme")
    self.entry.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

    self.add_automatisme = customtkinter.CTkButton(self, text="Ajoute un automatisme", command=self._add_automatisme)
    self.add_automatisme.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

    self.name_automatismes = customtkinter.CTkOptionMenu(self, dynamic_resizing=True)
    self.name_automatismes.grid(row=1, column=1, padx=(20, 0), pady=(20, 20))
    self._update_automatisme()

    self.remove_automatisme = customtkinter.CTkButton(self, text="Supprimer un automatisme")
    self.remove_automatisme.grid(row=1, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
  
  def _add_automatisme(self):
    if self.entry.get() == "":
      return self.entry.focus()

    if self.name_classe.get() == "Aucune Classe":
      return
    
    if self.name_chapitre.get() == "Aucun chapitre":
      return
    
    chapitre = get_chapitres_by_classe_name_by_chapitre_name(self.name_classe.get(), self.name_chapitre.get())

    add_automatisme(self.entry.get().replace("\\", "\\\\"), chapitre[0])
  
  def _update_chapitres(self, *args):
    if self.name_classe.get() == "Aucune Classe":
      self.name_chapitre.configure(values=[])
      return self.name_chapitre.set("Aucun chapitre")

    chapitres = []
    for i in get_chapitres_by_classe_name(self.name_classe.get()):
      chapitres.append(i[1])
    self.name_chapitre.configure(values=chapitres)
    if len(chapitres) == 0:
      self.name_chapitre.set("Aucun chapitre")
    else:
      self.name_chapitre.set(chapitres[0])
  
  def _update_automatisme(self, *args):
    if self.name_chapitre.get() == "Aucun chapitre":
      self.name_automatismes.configure(values=[])
      return self.name_automatismes.set("Aucun Automatisme")

    chapitre = get_chapitres_by_classe_name_by_chapitre_name(self.name_classe.get(), self.name_chapitre.get())

    automatismes = []
    for i in get_automatismes_by_chapitres(int(chapitre[0])):
      automatismes.append(i[1])
    if len(automatismes) < 1:
      self.name_automatismes.configure(values=[])
      self.name_automatismes.set("Aucun chapitre")
    else:
      self.name_automatismes.configure(values=automatismes)
      self.name_automatismes.set(automatismes[0])