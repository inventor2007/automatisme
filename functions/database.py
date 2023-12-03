import sqlite3

connection = sqlite3.connect('./database.db')
cursor = connection.cursor()

# ##### Classe #####

def get_all_classes():
  req_classes = "SELECT * FROM classes"
  res = cursor.execute(req_classes)
  return res.fetchall()

def get_all_classes_enable():
  req_classes = "SELECT * FROM classes WHERE enable = 'true'"
  res = cursor.execute(req_classes)
  return res.fetchall()

def get_classe_by_name(classeName):
  req_classes = f"SELECT * FROM classes WHERE name = '{classeName}'"
  res = cursor.execute(req_classes)
  return res.fetchone()

def add_classe(name):
  req_classes = f"INSERT INTO classes(name) VALUES ('{name}')"
  cursor.execute(req_classes)
  connection.commit()

def remove_classe_by_name(name):
  req_classes = f"DELETE FROM classes WHERE name = '{name}'"
  cursor.execute(req_classes)
  connection.commit()

# ##### Chapitres #####

def get_chapitres_by_classe_enable(classe):
  req_chatitres = f"SELECT * FROM chapitres WHERE enable = 'true' AND classeId = {int(classe)}"
  res = cursor.execute(req_chatitres)
  return res.fetchall()

def get_chapitres_by_classe_name(classeName):
  classe = get_classe_by_name(classeName)
  req_chatitres = f"SELECT * FROM chapitres WHERE classeId = {int(classe[0])}"
  res = cursor.execute(req_chatitres)
  return res.fetchall()

def get_chapitres_by_classe_name_by_chapitre_name(classeName, chapitreName):
  classe = get_classe_by_name(classeName)
  req_chatitres = f"SELECT * FROM chapitres WHERE name = '{chapitreName}' AND classeId = {int(classe[0])}"
  res = cursor.execute(req_chatitres)
  return res.fetchone()

def add_chapitre(name, classeId):
  req_chapitres = f"INSERT INTO chapitres(name, classeId) VALUES ('{name}', '{classeId}')"
  cursor.execute(req_chapitres)
  connection.commit()

def remove_chapitre_by_name_by_classe_id(chapitreName, classeId):
  req_chapitres = f"DELETE FROM chapitres WHERE name = '{chapitreName}' AND classeId = {classeId}"
  cursor.execute(req_chapitres)
  connection.commit()

def remove_all_chapitres_by_classe_id(classeId):
  req_chapitres = f"DELETE FROM chapitres WHERE classeId = '{classeId}'"
  cursor.execute(req_chapitres)
  connection.commit()

# ##### Automatismes #####

def get_automatismes_by_chapitres_enable(chapitres):
  req_automatismes = f"SELECT * FROM automatismes WHERE enable = 'true' AND chapitreId IN ({','.join(map(str, chapitres))})"
  res = cursor.execute(req_automatismes)
  return res.fetchall()

def get_automatismes_by_id(automatismesId):
  req_automatismes = f"SELECT * FROM automatismes WHERE enable = 'true' AND id IN ({','.join(map(str, automatismesId))})"
  res = cursor.execute(req_automatismes)
  return res.fetchall()

def remove_all_automatismes_by_chapitre_name_by_classe_name(classeName, chapitreName):
  chapitre = get_chapitres_by_classe_name_by_chapitre_name(classeName, chapitreName)
  req_automatisme = f"DELETE FROM automatismes WHERE chapitreId = '{chapitre[0]}'"
  cursor.execute(req_automatisme)
  connection.commit()