import os, shutil
from fpdf import FPDF
from fpdf.enums import Align
import matplotlib.pyplot as plt
from functions.database import *
from functions.replaceText import replaceText

def create_automatisme(nombre, automatismesId, nombreParPage):
  automatismes = get_automatismes_by_id_enable(automatismesId)
  print(automatismes)

  if not os.path.exists("temp"):
    os.makedirs("temp")
  else:
    shutil.rmtree("temp")
    os.makedirs("temp")

  pdf = FPDF("P", "mm", "A4")
  pdf.add_page()

  if nombre == 5:
    yPoints = [37.4, 58.1, 78.7, 99.2, 119.8]
    add_header(pdf)

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(10, 7, " ", border=False)
    pdf.cell(90, 7, "Enoncé", border=True)
    pdf.cell(90, 7, "Réponse", border=True, ln=True)

    for i in automatismes:
      latex_to_png(replaceText(i[1]).text, i[0])

    exNum = 1
    for i in range(5):
      pdf.cell(10, 20.6, f"{str(exNum)}.", border=True)
      pdf.cell(90, 20.6, " ", border=True)
      pdf.cell(90, 20.6, " ", border=True, ln=True)
      pdf.image(f'temp/{automatismes[i][0]}.png', 20.5, yPoints[i], w=89)
      exNum += 1
    
    if nombreParPage == 2:
      pdf.cell(90, 5, " ", ln=True)
      add_header(pdf)

      pdf.set_font("Helvetica", "", 12)
      pdf.cell(10, 7, " ", border=False)
      pdf.cell(90, 7, "Enoncé", border=True)
      pdf.cell(90, 7, "Réponse", border=True, ln=True)

      exNum = 1
      for i in range(5):
        pdf.cell(10, 20.6, f"{str(exNum)}.", border=True)
        pdf.cell(90, 20.6, " ", border=True)
        pdf.cell(90, 20.6, " ", border=True, ln=True)
        pdf.image(f'temp/{automatismes[i][0]}.png', 20.5, yPoints[i] + 136.1, w=89)
        exNum += 1
  
  elif nombre == 10:
    yPoints = [37.4, 58.1, 78.7, 99.2, 120, 141, 161.8, 182, 202.5, 223]

    add_header(pdf)

    pdf.set_font("Helvetica", "", 12)
    pdf.cell(10, 7, " ", border=False)
    pdf.cell(90, 7, "Enoncé", border=True)
    pdf.cell(90, 7, "Réponse", border=True, ln=True)

    for i in automatismes:
      latex_to_png(i[1], i[0])

    exNum = 1
    for i in range(10):
      pdf.cell(10, 20.6, f"{str(exNum)}.", border=True)
      pdf.cell(90, 20.6, " ", border=True)
      pdf.cell(90, 20.6, " ", border=True, ln=True)
      pdf.image(f'temp/{automatismes[i][0]}.png', 20.5, yPoints[i], w=89)
      exNum += 1

  pdf.output("automatisme.pdf")
  
def add_header(pdf):
  pdf.set_font("Helvetica", "", 12)

  pdf.cell(50, 7, "Nom :", )
  pdf.cell(40, 7, "Prénom :", ln=True)

  pdf.set_font("Helvetica", "U", 15)
  pdf.cell(190, 13, "Automatisme", align=Align.C, ln=True)

def latex_to_png(latec, name):
  fig = plt.figure(figsize=(35, 7.8), facecolor="red")

  plt.axis("off")
  expression = f"${latec}$" if "\\" in latec or "{" in latec else f"{latec}"
  plt.text(0.5, 0.5, expression.replace("\\\\", "\\"), size=100, ha="center", va="center")


  plt.savefig(f"temp/{name}.png", format="png", bbox_inches="tight", pad_inches=0, transparent=True)
  plt.close()