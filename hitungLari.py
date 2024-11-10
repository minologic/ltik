# Nama : M Ilham Akbar Porindo Rahaputra
# NIM  : 2403513
# Kelas : RPL 1A

jamMulai = int(input("Jam mulai: "))
menitMulai = int(input("Menit mulai: "))
detikMulai = int(input("Detik mulai: "))

jamSelesai = int(input("Jam selesai: "))
menitSelesai = int(input("Menit selesai: "))
detikSelesai = int(input("Detik selesai: "))

totaldetikMulai = jamMulai * 3600 + menitMulai * 60 + detikMulai
totaldetikSelesai = jamSelesai * 3600 + menitSelesai * 60 + detikSelesai

selisih = totaldetikSelesai - totaldetikMulai

jam = selisih// 3600
sisaDetik = selisih % 3600
menit = sisaDetik // 60
detik = sisaDetik % 60

print(f"Selisih waktu: {jam} jam - {menit} menit - {detik} detik")
