import numpy as np
import math

class Gre:
  
  titik1 = 0
  titik2 = 800
  titik3 = 1200
  titik4 = 1800

  def __init__(self, gre):
    self.gre = gre

  def low(self):
    if(self.gre >= self.titik1 and self.gre <= self.titik2):
      return 1
    elif (self.gre > self.titik2 and self.gre < self.titik3):
      return (float)(self.titik3 - self.gre) / (self.titik3 - self.titik2)
    else:
      return 0

  def medium(self):
    if (self.gre > self.titik2 and self.gre < self.titik3):
      return (float)(self.gre - self.titik2) / (self.titik3 - self.titik2)
    elif (self.gre >= self.titik3 and self.gre <= self.titik4):
      return 1
    elif (self.gre > self.titik3 and self.gre < self.titik4):
      return (float)(self.titik4 - self.gre) / (self.titik4 - self.titik3)
    else:
      return 0

  def high(self):
    if (self.gre > self.titik3 and self.gre < self.titik4):
      return (float)(self.gre - self.titik3) / (self.titik4 - self.titik3)
    elif (self.gre >= self.titik4):
      return 1
    else:
      return 0