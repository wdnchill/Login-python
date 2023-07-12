import json
import getpass
import webbrowser

def save_registered_users():
    # Fungsi untuk menyimpan data pengguna terdaftar ke dalam file
    with open("registered_users.json", "w") as file:
        json.dump(registered_users, file)

def register():
    # Fungsi untuk melakukan proses registrasi pengguna
    print("Anda belum punya akun. Silahkan register terlebih dahulu.")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username in registered_users:
        print("Username sudah terdaftar. Silakan gunakan username lain.")
    else:
        registered_users[username] = password
        print("Registrasi berhasil. Silakan login dengan username dan password Anda.")
        save_registered_users()
        login()

def login():
    # Fungsi untuk melakukan proses login pengguna
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in registered_users and registered_users[username] == password:
        print("Login berhasil. Selamat datang, " + username + "!")
        main_menu()
    else:
        print("Username atau password salah. Silakan coba lagi.")
        register()

# Fungsi untuk menampilkan menu utama
def main_menu():
    print("Menu utama:")
    url = "https://github.com/wdnchill"
    webbrowser.open(url)
    # Tambahkan pilihan menu dan logika lainnya sesuai kebutuhan Anda

# Program Utama
registered_users = {}

# Memeriksa apakah file pengguna terdaftar sudah ada
try:
    with open("registered_users.json", "r") as file:
        registered_users = json.load(file)
except FileNotFoundError:
    pass

# Memanggil fungsi login untuk memulai program
login()
