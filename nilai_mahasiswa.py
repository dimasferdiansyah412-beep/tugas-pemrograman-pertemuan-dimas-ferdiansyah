# Dictionary untuk menyimpan data mahasiswa
data_mahasiswa = {}

# ============================
#   OPERASI TAMBAH DATA
# ============================
def tambah_data():
    nama = input("Masukkan Nama Mahasiswa : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    data_mahasiswa[nama] = {
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }

    print(">>> Data berhasil ditambahkan!\n")


# ============================
#   OPERASI UBAH DATA
# ============================
def ubah_data():
    nama = input("Masukkan nama yang akan diubah : ")

    if nama in data_mahasiswa:
        print("Masukkan nilai baru:")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))

        akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

        data_mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "akhir": akhir
        }
        print(">>> Data berhasil diubah!\n")
    else:
        print(">>> Nama tidak ditemukan!\n")


# ============================
#   OPERASI HAPUS DATA
# ============================
def hapus_data():
    nama = input("Masukkan nama yang akan dihapus : ")

    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(">>> Data berhasil dihapus!\n")
    else:
        print(">>> Nama tidak ditemukan!\n")


# ============================
#   OPERASI TAMPILKAN DATA
# ============================
def tampil_data():
    if not data:
        print("\nDaftar Nilai'")
    if not data_mahasiswa:
        print(">>> Belum ada data!\n")
        return

    print("\nDaftar Nilai Mahasiswa")
    print("-" * 50)
    print(f"{'Nama':10} {'Tugas':6} {'UTS':6} {'UAS':6} {'Akhir':6}")
    print("-" * 50)

    for nama, nilai in data_mahasiswa.items():
        print(f"{nama:10} {nilai['tugas']:6} {nilai['uts']:6} {nilai['uas']:6} {nilai['akhir']:.2f}")

    print()


# ============================
#   OPERASI CARI DATA
# ============================
def cari_data():
    nama = input("Masukkan nama yang dicari : ")

    if nama in data_mahasiswa:
        nilai = data_mahasiswa[nama]
        print(f"\nData ditemukan:")
        print(f"Nama  : {nama}")
        print(f"Tugas : {nilai['tugas']}")
        print(f"UTS   : {nilai['uts']}")
        print(f"UAS   : {nilai['uas']}")
        print(f"Akhir : {nilai['akhir']:.2f}\n")
    else:
        print(">>> Nama tidak ditemukan!\n")


# ============================
#   MENU UTAMA
# ============================
while True:
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        ubah_data()
    elif pilih == "3":
        hapus_data()
    elif pilih == "4":
        tampil_data()
    elif pilih == "5":
        cari_data()
    elif pilih == "0":
        print("Program selesai.")
        break
    else:
        print(">>> Pilihan tidak valid!\n")