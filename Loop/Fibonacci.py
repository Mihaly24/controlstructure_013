def fibonacci(n):
    a, b = 0, 1
    hasil = []
    while a <= n:
        hasil.append(a)
        a, b = b, a + b
    return hasil
n =int (input("Masukkan angkanya: "))
print ("Hasilnya adalah: ", fibonacci(n))