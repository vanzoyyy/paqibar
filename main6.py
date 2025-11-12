# while boolean :
#  output
#  operator assigment

# a = int (input("Masukkan angka awal "))
# b = int (input("Masukkan angka akhir "))
# while a <= b :
#     print(a)
#     a = a + 2

# Odd even generator
# buat input pilih ganjil atau genap
# jika ganjil yang terpilih
    # buat input untuk sampul angka berapa
    # looping while sesuai sampai angka berapa
# jika genap yang terpilih
    # buat input untuk sampul angka berapa
    # looping while sesuai sampai angka berapa
    
# Program menampilkan angka ganjil atau genap

print("=== Program Ganjil/Genap ===")
pilihan = input("Pilih (ganjil/genap): ").lower()
batas = int(input("Sampai angka berapa: "))

angka = 1

if pilihan == "ganjil":
    while angka <= batas:
        if angka % 2 != 0:
            print(angka)
        angka += 1

elif pilihan == "genap":
    while angka <= batas:
        if angka % 2 == 0:
            print(angka)
        angka += 1

else:
    print("Pilihan tidak valid, silakan pilih 'ganjil' atau 'genap'.")
