import customtkinter
from functions.database import *

class automatismeMenu(customtkinter.CTkToplevel):
  def __init__(self):
    super().__init__()
    self.minsize(340, 110)
    # self.maxsize(340, 110)

    self.grid_columnconfigure((1), weight=1)
    self.grid_columnconfigure((0, 2), weight=1)

    classes = []
    for i in get_all_classes():
      classes.append(i[1])
    if classes == []:
      classes.append('Aucune Classe')
    self.name_classe = customtkinter.CTkOptionMenu(self, dynamic_resizing=True, values=classes, command=self._update_chapitres)
    self.name_classe.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))

    self.name_chapitre = customtkinter.CTkOptionMenu(self, dynamic_resizing=True)
    self.name_chapitre.grid(row=1, column=0, padx=(20, 0), pady=(20, 20))
    self._update_chapitres()

    self.entry = customtkinter.CTkEntry(self, placeholder_text="Nom de la classe")
    self.entry.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

    self.add_class = customtkinter.CTkButton(self, text="Ajoute la classe")
    self.add_class.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
  
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