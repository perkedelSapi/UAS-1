from prettytable import PrettyTable

def tampilkan_buku(buku_list):
    if not buku_list:
        print("Tidak ada data buku.")
        return

    
    table = PrettyTable()
    table.field_names = ["ID Buku", "Judul", "Penulis"]

    # Menambahkan data buku ke tabel
    for buku in buku_list:
        table.add_row([buku.id_buku, buku.judul, buku.penulis])

    print("\nDaftar Buku:")
    print(table)

def tampilkan_detail(buku):
    if buku:
        # Membuat objek PrettyTable untuk format tabel
        table = PrettyTable()
        table.field_names = ["ID Buku", "Judul", "Penulis"]

        # Menambahkan detail buku ke tabel
        table.add_row([buku.id_buku, buku.judul, buku.penulis])

        # Menampilkan tabel detail buku
        print("\nDetail Buku:")
        print(table)
    else:
        print("Buku tidak ditemukan.")
