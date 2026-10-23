nim= input("Masukan nim anda: ")
nama = input("Masukan nama anda: ")
matkul = input("Masukan mata kuliah anda: ")
absensi = int(input("Input nilai absen: "))
nilai_tugas = int(input("Input nilai tugas: "))
nilai_uts = int(input("Input nilai uts: "))
nilai_uas = int(input("Input nilai uas: "))

nilai_akhir = (absensi * 0.20) + (nilai_tugas * 0.25) + (nilai_uts * 0.25) + (nilai_uas * 0.30)

if nilai_akhir >= 80 and nilai_akhir <= 100:
    grade = "A"
    ket = "LULUS"
elif nilai_akhir  >= 70 and nilai_akhir <= 79:
    grade = "B"
    ket = "LULUS"
elif nilai_akhir  >= 60 and nilai_akhir <= 69:
    grade = "C"
    ket = "LULUS"
elif nilai_akhir  >= 31 and nilai_akhir <= 59:
    grade = "D"
    ket = "TDK LULUS"
elif nilai_akhir  >= 0 and nilai_akhir <= 30:
    grade = "E"
    ket = "TDK LULUS"

print("\n=== HASIL NILAI MAHASISWA ===")
print("NIM: ", nim)
print("NAMA: ", nama)
print("MATA KULIAH: ", matkul)
print("NILAI AKHIR: ", nilai_akhir)
print("GRADE: ", grade)
print("STATUS: ", ket)