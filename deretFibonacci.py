# Nama : M Ilham Akbar Porindo Rahaputra
# NIM  : 2403513
# Kelas : RPL 1A

def fibonacci(n):

    deretFibonacci = [0, 1]
    
    while len(deretFibonacci) < n:
        angka = deretFibonacci[-1] + deretFibonacci[-2]
        deretFibonacci.append(angka)
    
    return deretFibonacci[:n]

n = int(input("Masukkan panjang deret fibonacci: "))
deretAkhir = fibonacci(n)
print("Deret Fibonacci:", deretAkhir)

