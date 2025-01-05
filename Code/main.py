from data.buku import Buku, DataBuku
from view.input_form import input_buku
from view.buku import tampilkan_buku, tampilkan_detail

def main():
    data_buku = DataBuku()

    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Cari Buku")
        print("4. Ubah Buku")
        print("5. Tampilkan Semua Buku")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            id_buku, judul, penulis = input_buku()
            buku = Buku(id_buku, judul, penulis)
            data_buku.tambah_buku(buku)
            print("Buku berhasil ditambahkan.")
        elif pilihan == "2":
            id_buku = input("Masukkan ID Buku yang ingin dihapus: ")
            data_buku.hapus_buku(id_buku)
            print("Buku berhasil dihapus.")
        elif pilihan == "3":
            id_buku = input("Masukkan ID Buku yang ingin dicari: ")
            buku = data_buku.cari_buku(id_buku)
            tampilkan_detail(buku)
        elif pilihan == "4":
            id_buku = input("Masukkan ID Buku yang ingin diubah: ")
            judul_baru = input("Masukkan Judul baru: ")
            penulis_baru = input("Masukkan Penulis baru: ")
            data_buku.ubah_buku(id_buku, judul_baru, penulis_baru)
            print("Data buku berhasil diubah.")
        elif pilihan == "5":
            buku_list = data_buku.tampilkan_semua()
            tampilkan_buku(buku_list)
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
