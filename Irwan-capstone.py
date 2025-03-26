# Ini adalah projek program data karyawan perusahaan mendang-mending
# Dibuat oleh: Irwan setio


# List data karyawan 
karyawan_list= []

# Fungsi untuk menghasilkan ID otomatis
def generate_id():
    return max([k['id'] for k in karyawan_list], default=0) + 1

# Fungsi untuk mengecek apakah nama karyawan sudah ada
def duplicate(nama):
    return any(k['nama'].lower() == nama.lower() for k in karyawan_list)

# Fungsi gaji agar angka saja dan positif
def input_gaji():
    gaji_input = input("Masukkan gaji karyawan: ")
    while not gaji_input.isdigit() or int(gaji_input) <= 0:
        print("Gaji harus berupa angka positif!")
        gaji_input = input("Masukkan gaji karyawan: ")
    return int(gaji_input)

# Fungsi untuk menambahkan karyawan mendang-mending
def tambah_karyawan():
    nama = input("Masukkan nama karyawan: ")
    while not nama:
        print("Nama tidak boleh kosong!")
        nama = input("Masukkan nama karyawan: ")
    
    if duplicate(nama):
        print("Nama karyawan sudah ada, masukan nama yang unik")
        return
    
    posisi = input("Masukkan posisi karyawan: ")
    while not posisi:
        print("Posisi tidak boleh kosong!")
        posisi = input("Masukkan posisi karyawan: ")
    
    gaji = input_gaji()
    
    karyawan = {"id": generate_id(), "nama": nama, "posisi": posisi, "gaji": gaji}
    karyawan_list.append(karyawan)
    print("Karyawan berhasil ditambahkan!")

# Fungsi untuk membaca list data karyawan mendang-mending
def read_karyawan():
    if not karyawan_list:
        print("Belum ada data karyawan.")
        return

    print("\nData Karyawan:")
    print("=" * 50)
    print(f"{'ID':<5} {'Nama':<15} {'Posisi':<15} {'Gaji':>10}")
    print("=" * 50)

    for karyawan in karyawan_list:
        print(f"{karyawan['id']:<5} {karyawan['nama']:<15} {karyawan['posisi']:<15} {karyawan['gaji']:>10,}")

    print("=" * 50)

# Fungsi untuk memperbarui data karyawan mendang-mending
def update_karyawan():
    if not karyawan_list:
        print("Tidak ada karyawan untuk diperbarui.")
        return

    read_karyawan()
    id_update = input("Masukkan ID karyawan yang ingin diperbarui: ")

    while not id_update.isdigit():
        print("ID harus berupa angka!")
        id_update = input("Masukkan ID karyawan yang ingin diperbarui: ")

    id_update = int(id_update)
    for k in karyawan_list:
        if k['id'] == id_update:
            print("Masukkan data baru (kosongkan jika tidak ingin mengubah):")

            nama_baru = input(f"Nama ({k['nama']}): ")
            if nama_baru:
                if duplicate(nama_baru):
                    print("Nama sudah digunakan! Pembaruan dibatalkan.")
                    return
                k['nama'] = nama_baru

            posisi_baru = input(f"Posisi ({k['posisi']}): ")
            if posisi_baru:
                k['posisi'] = posisi_baru

            gaji_baru = input(f"Gaji ({k['gaji']}): ")
            if gaji_baru:
                while not gaji_baru.isdigit() or int(gaji_baru) <= 0:
                    print("Gaji harus berupa angka positif!")
                    gaji_baru = input(f"Gaji ({k['gaji']}): ")
                k['gaji'] = int(gaji_baru)

            print("Karyawan berhasil diperbarui!")
            return
    
    print("ID karyawan tidak ditemukan!")

# Fungsi untuk menghapus data karyawan
def delete_karyawan():
    id_karyawan = input("Masukkan ID karyawan yang ingin dihapus: ")

    while not id_karyawan.isdigit():
        print("ID harus berupa angka!")
        id_karyawan = input("Masukkan ID karyawan yang ingin dihapus: ")

    id_karyawan = int(id_karyawan)  
    
    for k in karyawan_list:
        if k['id'] == id_karyawan:
            karyawan_list.remove(k)
            print("Data karyawan berhasil dihapus!")
            return  

    print("ID karyawan tidak ditemukan.")


# Menu utama
def main():
    while True:
        print("\n=== Sistem Manajemen Karyawan Mendang-Mending ===")
        print("1. Tambah Karyawan")
        print("2. Lihat Karyawan")
        print("3. Perbarui Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_karyawan()
        elif pilihan == "2":
            read_karyawan()
        elif pilihan == "3":
            update_karyawan()
        elif pilihan == "4":
            delete_karyawan()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

main()
