import numpy as np
import math
from gpa import Gpa
from gre import Gre

status = ""
u_Status = np.empty(9, dtype=object)
z_Status = ["Excellent", "Good", "Fair", "Very Good", "Good", "Poor", "Fair", "Poor", "Poor"]

#RULE
def hitung_u():
  u_Status[0] = min(gpa_test.high(),gre_test.high()) #excellent
  u_Status[1]=min(gpa_test.medium(), gre_test.high()) #good
  u_Status[2]=min(gpa_test.low(), gre_test.high()) #fair
  u_Status[3]=min(gpa_test.high(), gre_test.medium()) #verygood
  u_Status[4]=min(gpa_test.medium(), gre_test.medium())  #good
  u_Status[5]=min(gpa_test.low(), gre_test.medium())  #poor
  u_Status[6]=min(gpa_test.high(), gre_test.low())  #fair
  u_Status[7]=min(gpa_test.medium(), gre_test.low())  #poor
  u_Status[8]=min(gpa_test.low(), gre_test.low())  #poor

#Max Method
def hitung_z():
  global status
  max = 0
  for i in range(len(u_Status)):
    if(max < u_Status[i]):
      max = u_Status[i]
      status = z_Status[i]

  return max

x = int(input("Masukkan GRE: "))
y = float(input("Masukkan GPA: "))
gre_test = Gre(x)
gpa_test = Gpa(y)

hitung_u()

bobot = hitung_z()

for index, value in enumerate(u_Status):
    if(value != 0):
        
        print(f"u_ke- {z_Status[index]}, Value: {value}")

print("\nMax method -> Bobot: ",bobot, "dengan Predikat: ",status)

def median_centroid(predikat):
    if predikat == 'Poor':
        return np.median(list(range(60, 70)))
    elif predikat == 'Fair':
        return np.median(list(range(60, 80)))
    elif predikat == 'Good':
        return np.median(list(range(70, 90)))
    elif predikat == 'Very Good':
        return np.median(list(range(80, 100)))
    elif predikat == 'Excellent':
        return np.median(list(range(90, 100)))

def hitung_z_centroid():
    global status
    numerator = 0
    denominator = 0
    for i in range(len(u_Status)):
        numerator += u_Status[i] * math.ceil(median_centroid(z_Status[i]))
        denominator += u_Status[i]
    res = numerator / denominator
    status = min(z_Status, key=lambda x: abs(median_centroid(x) - res))
    return res

bobot = hitung_z_centroid()

print("\nCentroid Method -> Bobot: ", bobot, "dengan predikat: ", status)