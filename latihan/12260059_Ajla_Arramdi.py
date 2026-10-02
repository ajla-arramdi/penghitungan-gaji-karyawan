print("\n ---program penghitungan gaji karyawan")

nama = input("nama karyawan: ")
jumlahjamkerja = int(input("jumlah jam kerja: "))
jamlembur = int(input("jumlah jam lembur: "))

gaji = jumlahjamkerja * 20000
lembur = jamlembur * 25000
gajikotor = gaji + lembur
pajak = gajikotor * 6 / 100
gajibersih = gajikotor - pajak

print("\n ---slipgaji---")
print("nama karyawan: ", nama)
print("total gaji: ", f"RP: {gajibersih: ,.0f}")

