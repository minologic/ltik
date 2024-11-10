# Nama : M Ilham Akbar Porindo Rahaputra
# NIM  : 2403513
# Kelas : RPL 1A

password = "Latihan"

n = 3

while n > 0:
    username = input("Masukkan username: ")
    inputPassword = input("Masukkan password: ")
    
    if inputPassword == password:
        print("Login berhasil!")
        break
    else:
        n = n-1
        if n > 0:
            print(f"Password salah, tersisa {n} kesempatan lagi.")
        else:
            print("Kesempatan habis, coba lagi nanti.")
