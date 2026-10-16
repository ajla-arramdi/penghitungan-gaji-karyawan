# Tempat menyimpan data akun
akun = {}


# =========================
# REGISTER
# =========================
def register():
    print("\n===== REGISTER =====")

    username = input("Buat username: ")
    password = input("Buat password: ")

    if username in akun:
        print("Username sudah digunakan!")
    else:
        akun[username] = password
        print("Register berhasil!")


# =========================
# LOGIN
# =========================
def login():
    print("\n===== LOGIN =====")

    username = input("Username: ")
    password = input("Password: ")

    if username in akun and akun[username] == password:
        print("Login berhasil!")
        print("Selamat datang,", username)
    else:
        print("Username atau password salah!")


# =========================
# MENU
# =========================
while True:

    print("\n======================")
    print("   SISTEM LOGIN")
    print("======================")
    print("1. Register")
    print("2. Login")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        register()

    elif pilihan == "2":
        login()

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")