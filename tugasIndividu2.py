# Nama: M Ilham Akbar Porindo R
# Kelas: RPL 1A
# NIM: 2403513

print("Cek apakah kamu bisa menjadi seorang model catwalk!\n")

jenisKelamin = str(input("Masukkan jenis kelamin anda (Pria/Wanita): "))
umur = int(input("Masukkan umur anda: "))
iq = int(input("Masukkan IQ anda: "))
tinggiBadan = int(input("Masukkan tinggi badan: "))


if (umur >= 18 and umur <=25):
    if (jenisKelamin == "Pria"):
        if (iq >= 130):
            if (tinggiBadan == 175):
                print("Kamu berhak menjadi seorang model catwalk!")
            else:
                print("Tinggi badan belum sesuai dengan persyaratan!")
        else:
                print("IQ yang dibutuhkan minimal 130!")
    
    elif (jenisKelamin == "Wanita"):
        if (iq >= 130):
            if (tinggiBadan == 170):
                print("Kamu berhak menjadi seorang model catwalk")
            else:
                print("Tinggi badan belum sesuai dengan persyaratan!")
        else:
                print("IQ yang dibutuhkan minimal 130!")
    else:
         print("Jenis kelamin tidak sesuai! Masukkan Pria atau Wanita!")
else:
     print("Syarat harus berumur 18-25 tahun!")