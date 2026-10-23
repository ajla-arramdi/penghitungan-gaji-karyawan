
#buat kelongkapan 
# for i in range(1,100, 5):
#     print(i)

# buat perulangan penyebutan nama
# for i in range(2):
#     nama = input("masukan nama mahasiswa: ")
#     print("nama mahasiswa ke ", i+1, "adalah", nama)

# nested for

# angka = 1
# for i in range(10):
#     for j in range(10):
#         print(angka, end=" ")
#         angka +=1
#     print()

# matrix
# for i in range(3):
#     for j in range(5):
#         print(f"({i},{j})", end=" ")
#     print()

# while biar behenti kalo salah
# i = 1
# while i <= 5:
#     print(i)
#     i +=1

# # while unlimited infinit
# i = 1
# while i <= 5:
#     print(i)

# break
# x = 1
# while x <=10:
#     print(x)
#     if x == 8:
#         break
#     x += 1


# break skip angka
# x = 1 #pakai 0 kalo mao dari
# while x <= 10:
#     x += 1
#     if x == 5:
#         continue
#     print(x)


# x = 1 
# while x <= 5:
#     print(x)
#     if x == 3:
#         break
#     x += 1
# else:
#     print("perulangan kelar")


# x = 1 
# while x <= 5:
#     print(x)
#     x += 1
# else:
#     print("perulangan kelar")

banyak_jenis = int(input("Banyak jenis pelanggan: "))
total_bayar = 0
daftar_pembelian = []


for i in range(banyak_jenis):
    print(f"(jenis ke- {i+1})")


    kode_potongan = input("kode potongan D/S/P: ").upper()
    jml_potong = int(input("Banyak potongan: "))

    if kode_potongan == "D":
        jenis_potongan = "dada"
        harga = 8000
    elif kode_potongan == "S":
        jenis_potongan = "sayap"
        harga = 7000
    elif kode_potongan == "P":
        jenis_potongan = "paha"
        harga = 7500
    else:
        jenis_potongan = "kesalahan"
        harga = 0
        continue    

    jumlah_harga = harga * jml_potong

    daftar_pembelian.append(
        [jenis_potongan, jml_potong, harga, jumlah_harga]
    )

    total_bayar += jumlah_harga

    pajak = total_bayar * 0.1
    total_pembayaran = total_bayar + pajak

print("\n========================= DAFTAR PEMBELIAN =========================")

for i, item in enumerate(daftar_pembelian, start=1):
    print(f"{i:<3} {item[0]:<14} Rp.{item[1]:<13}{item[2]:<13} Rp.{item[3]}")
print("=====================================================================")
print(f"Jumlah bayar    Rp. {int(total_bayar)}")
print(f"Pajak 10%       Rp. {int(pajak)}")
print(f"Total bayar     Rp. {int(total_pembayaran)}")
print("=====================================================================")



