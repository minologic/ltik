# Nama: M Ilham Akbar Porindo R
# Kelas: RPL 1A
# NIM: 2403513

x = int(input("Masukkan bilangan bulat: "))

if (x > 0):
    print(f"{x} adalah bilangan bulat positif.")
    if (x % 2 == 0 ):
        print(f"{x} adalah bilangan bulat genap")
    else:
        print(f"{x} adalah bilangan bulat ganjil")

elif ( x < 0 ):
    print(f"{x} adalah bilangan bulat negatif")
    if (x % 2 == 0 ):
        print(f"{x} adalah bilangan bulat genap")
    else:
        print(f"{x} adalah bilangan bulat ganjil")

else:
    print(f"{x} adalah bilangan netral")