# Nama: M Ilham Akbar Porindo Rahaputra
# NIM: 2403513
# Prodi/Kelas: RPL 1A

n = 10
totalJumlah = 0


for i in range(n):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    totalJumlah = totalJumlah + angka
    print("Total sementara: ", totalJumlah)

print(f"Jumlah dari {n} angka yang diinputkan adalah: {totalJumlah}")
