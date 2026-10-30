
daftar_belanja = []
print("\n---------------------daftar belanja-----------------------")
banyak_barang = int(input("Banyak barang yang ingin di tambahkan: "))
for i in range(banyak_barang):
    nama_barang = input(f"Input nama barang ke {i+1}: ")
    daftar_belanja.append(nama_barang)

print("Daftar barang belanja saat ini: ", daftar_belanja)

