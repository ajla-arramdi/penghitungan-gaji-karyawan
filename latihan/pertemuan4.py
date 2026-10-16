#pernyataaniftunggal
# angka  = 5 
# if angka > 0:
#     print(angka, "adalah bilangan positif")

#ifmajemuk
# angka  = -2 
# if angka > 0:
#     print(angka, "adalah bilangan positif")
# else:
#     print(angka"adalah bilangan negatif")

#pernyataan if elif else
# nis = input("Masukan NIS anda:")
# name = input("Maasukan nama anda:")
# jurusan = input("Masukan jurusan anda [ti/si]: ")

# if jurusan == "ti":
#     nama_prodi = "Teknik Informatika"
#     biaya = 2400000
# elif jurusan == "si":
#     nama_prodi = "sistem informasi"
#     biaya = 2000000
# else:nama_prodi = "tidak ada"
#     biaya = 0
#     print("kode jurusan tidak sesuai")
# print("\n ------------------")
# print("jurusan: ",jurusan)
# print("nama prodi: ",nama_prodi)
# print("biaya kuliah: ",biaya)

#percabangan 5 statement
# pembeli = input("Masukan Nama Pembeli: ")
# no_handphone = input("Masukan no handphone: ")
# jurusan = input("masukan tujuan [sby/jkt/bdg]")

# if jurusan == "sby":
#     nama_jurusan = "surabaya"
#     harga = 150000
# elif jurusan == "jkt":
#     nama_jurusan = "jakarta"
#     harga = 260000
# else :
#     nama_jurusan = "bandung"
#     harga = 310000

# #proses perhitungan total harga
# jumlah = int(input("masukan jumlah beli: "))

# if jumlah>= 3:
#     potongan = (total_harga * jumlah )*0.1
# else:
#     potongan = 0

# total = (jumlah*harga)-potongan

# print("\n----------------------------------------")
# print("            penjualan tiket bus")
# print("                    xyz")
# print("\n----------------------------------------")
# print("Nama pembeli: ", pembeli)
# print("no handphone: ", no_handphone)
# print("kode tujuan yang dipilih: "+str(jurusan))
# print("nama kota tujuan: "+str(nama_jurusan))
# print("harga: ", +(harga))
# print("jumlah: ", +(jumlah))
# print("\n----------------------------------------")
# print("potongan yang didapat: ", +(potongan))
# print("total pembayaran: ", +(total))

# ubay = int(input("uang bayar: Rp. "))
# uangkembali = ubay-total
# print("uang kembali: ",+ (uangkembali))

# Tugas 1
nama = input("Masukan nama: ")
jabatan = int(input("masukan jabatan: "))
pendidikan = input("pendidikan: ")
jumlah_jam = int(input("jumlah jam kerja: "))

#inisialisasi
gapok = 3000000

#percabgan
if jabatan == 1:
    tunjangan == 0.05 * gapok
elif jabatan == 2:
    tunjangan = 0.1 * gapok
elif jabatan == 3:
    tunjangan = 0.15 * gapok
else:
    tunjangan = 0

#percabgan
if pendidikan =="smk":
    tjg_pendidikan = 0.025 * gapok
elif pendidikan == "d1":
    tjg_pendidikan =  0.05 * gapok
elif pendidikan == "d3":
    tjg_pendidikan =  0.2 * gapok
elif pendidikan == "s1":
    tjg_pendidikan =  0.3 * gapok
else:
    tjg_pendidikan = 0

if jumlah_jam>=8:
    gaji_lembur = (jumlah_jam - 8) *3500
else:
    gaji_lembur = 0

total_gaji = gapok + tunjangan + tjg_pendidikan + gaji_lembur

print("\n----------------------------------------")
print("            pt dingin damai")
print("\n----------------------------------------")
print("Nama karyawan: ", nama)
print("honor yang diterima: ")
print("tunjangan jabatan rp: ", int(tunjangan))
print("tunjangan pendidikan: ",int(tjg_pendidikan))
print("gaji lembur Rp.", +int(gaji_lembur))
print("------------------------------------------")
print("total gaji Rp. ", int(total_gaji))