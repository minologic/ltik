# Nama : M Ilham Akbar Porindo Rahaputra
# NIM  : 2403513
# Kelas : RPL 1A

import math
r = float(input("Masukkan jari-jari: "))
t = float(input("Masukkan tinggi tabung: "))

def volumeTabung(r,t):
    volume = math.pi * r**2 * t
    return volume

volume = volumeTabung(r,t)
print(volume)
