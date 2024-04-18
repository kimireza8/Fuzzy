import numpy as np
import math

class Gpa:
  
  titik1 = 0
  titik2 = 2.2
  titik3 = 3.0
  titik4 = 3.8

  def __init__(self, gpa):
    self.gpa = gpa

  def low(self):
    if(self.gpa >= self.titik1 and self.gpa <= self.titik2):
      return 1
    elif (self.gpa > self.titik2 and self.gpa < self.titik3):
      return (float)(self.titik3 - self.gpa) / (self.titik3 - self.titik2)
    else:
      return 0

  def medium(self):
    if (self.gpa > self.titik2 and self.gpa < self.titik3):
      return (float)(self.gpa - self.titik2) / (self.titik3 - self.titik2)
    elif (self.gpa >= self.titik3 and self.gpa <= self.titik4):
      return 1
    elif (self.gpa > self.titik3 and self.gpa < self.titik4):
      return (float)(self.titik4 - self.gpa) / (self.titik4 - self.titik3)
    else:
      return 0

  def high(self):
    if (self.gpa > self.titik3 and self.gpa < self.titik4):
      return (float)(self.gpa - self.titik3) / (self.titik4 - self.titik3)
    elif (self.gpa >= self.titik4):
      return 1
    else:
      return 0