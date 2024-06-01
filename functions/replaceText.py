import random
import re

class replaceText:
  def __init__(self, text):
    self.text = text
    self.text = re.sub(r"%rand_(\d+)_(\d+)%", self.rand, self.text)
    
  def rand(self, match):
    limite_inf, limite_sup = map(int, match.groups())
    nombre_aleatoire = random.randint(limite_inf, limite_sup)
    return str(nombre_aleatoire)