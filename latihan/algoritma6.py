
def hanoi(n, asal, bantuan, tujuan):
    if n == 1:
        print("Pindahkan piringan dari", asal, "ke", tujuan)
    else:
        hanoi(n - 1, asal, tujuan, bantuan)
        print("Pindahkan piringan dari", asal, "ke", tujuan)
        hanoi(n - 1, bantuan, asal, tujuan)

hanoi(3, "A", "B", "C")


def ganjil(angka, jumlah):
    if jumlah > 100:
        return
    
    print(angka, end="")
    ganjil(angka + 2, jumlah + 1)

ganjil(1,1)


def cetak_nama(jumlah):
    if jumlah > 10:
        return
    
    print("AJLA")
    cetak_nama(jumlah +1)

cetak_nama(1)