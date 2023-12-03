import customtkinter
from functions.database import *

class classeMenu(customtkinter.CTkToplevel):
  def __init__(self):
    super().__init__()
    self.minsize(340, 110)
    self.maxsize(340, 110)

    self.entry = customtkinter.CTkEntry(self, placeholder_text="Nom de la classe")
    self.entry.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew")

    self.add_class = customtkinter.CTkButton(self, text="Ajoute la classe", command=self._add_classe)
    self.add_class.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

    classes = []
    for i in get_all_classes():
      classes.append(i[1])
    if classes == []:
      classes.append('Aucune Classe')
    self.name_classe = customtkinter.CTkOptionMenu(self, dynamic_resizing=True, values=classes)
    self.name_classe.grid(row=1, column=0, padx=(20, 0), pady=(20, 20))

    self.delete_class = customtkinter.CTkButton(self, text="Supprimer la classe", command=self._remove_classe)
    self.delete_class.grid(row=1, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
  
  def _add_classe(self):
    if self.entry.get() == "":
      return self.entry.focus()

    add_classe(self.entry.get())
    self.destroy()
  
  def _remove_classe(self):
    chapitres = get_chapitres_by_classe_name(self.name_classe.get())
    for i in chapitres:
      remove_all_automatismes_by_chapitre_name_by_classe_name(self.name_classe.get(), i[1])
    remove_all_chapitres_by_classe_id(get_classe_by_name(self.name_classe.get())[0])

    remove_classe_by_name(self.name_classe.get())
    self.destroy()