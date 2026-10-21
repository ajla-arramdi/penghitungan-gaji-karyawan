nama_konsumen = input("Input Nama Konsumen: ")
kode_kasir = input("Input Kode Kasir SF/RMD: ")
jenis_paket = input("Input Jenis Paket [A/B]: ")
jumlah_beli = int(input("Input Jumlah Pesanan: "))

if kode_kasir == "SF" or kode_kasir == "sf":
    namakasir = "Sifa"
elif kode_kasir== "RMD" or kode_kasir == "rmd":
    namakasir = "Ramdhan"
else:
    namakasir = "tidak ditemukan"

if jenis_paket == "A" or jenis_paket == "a":
    paket = "Reguler"
    menu = "Nasi Putih, Ayam goreng, Tahu, Tempe, Lalapan, dan Sambal"
    harga = 15000
elif jenis_paket == "B" or jenis_paket == "b":
    paket = "Deluxe"
    menu = "Nasi Putih, Ayam goreng, Tahu, Tempe, Bakwan udang, Lalapan, dan Sambal"
    harga = 20000
else:
    paket = "salah kode"
    menu = "tidak ada"
    harga = 0

total_harga = jumlah_beli * harga


print("\n                  CAFE ONES GLATE              ")
print("\n-----------------------------------------------")
print("Nama Konsumen:", nama_konsumen)
print("Nama Kasir:", namakasir)
print("\n-----------------------------------------------")
print("Paket:", paket)
print("Menu:", menu)
print("Harga Rp.", harga)
print("Jumlah Pesanan:",jumlah_beli)
print("\n-----------------------------------------------")
print("SUBTOTAL HARGA RP.",total_harga)