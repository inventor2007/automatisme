import customtkinter, tkinter
from functions.database import *

class chapitreMenu(customtkinter.CTkToplevel):
  def __init__(self):
    super().__init__()
    self.minsize(500, 110)
    self.maxsize(500, 120)

    classes = []
    for i in get_all_classes():
      classes.append(i[1])
    if classes == []:
      classes.append('Aucune Classe')
    self.name_classe = customtkinter.CTkOptionMenu(self, dynamic_resizing=True, values=classes, command=self._update_chapitres)
    self.name_classe.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))

    self.entry = customtkinter.CTkEntry(self, placeholder_text="Nom du chapitre")
    self.entry.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

    self.add_chapitre = customtkinter.CTkButton(self, text="Ajoute le chapitre", command=self._add_chapitre)
    self.add_chapitre.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

    self.name_chapitre = customtkinter.CTkOptionMenu(self, dynamic_resizing=True)
    self.name_chapitre.grid(row=1, column=1, padx=(20, 0), pady=(20, 20))
    self._update_chapitres()

    self.delete_chapitre = customtkinter.CTkButton(self, text="Supprimer le chapitre", command=self._remove_chapitre)
    self.delete_chapitre.grid(row=1, column=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
  
  def _add_chapitre(self):
    if self.entry.get() == "":
      return self.entry.focus()

    add_chapitre(self.entry.get(), get_classe_by_name(self.name_classe.get())[0])
    self.destroy()
  
  def _remove_chapitre(self):
    classe = get_classe_by_name(self.name_classe.get())

    if self.name_chapitre.get() != "Aucun chapitre":
      remove_all_automatismes_by_chapitre_name_by_classe_name(self.name_classe.get(), self.name_chapitre.get())
      remove_chapitre_by_name_by_classe_id(self.name_chapitre.get(), classe[0])
    self.destroy()

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