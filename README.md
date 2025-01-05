# Manajemen Perpustakaan

Program ini adalah aplikasi sederhana untuk mengelola data perpustakaan. Dibangun dengan pendekatan **Object-Oriented Programming (OOP)** dan menggunakan struktur modular untuk mempermudah pengelolaan kode.

## Fitur
1. **Tambah Buku**: Menambahkan buku baru ke dalam daftar.
2. **Hapus Buku**: Menghapus buku dari daftar berdasarkan ID.
3. **Cari Buku**: Mencari buku berdasarkan ID.
4. **Ubah Buku**: Mengubah informasi buku (judul dan penulis).
5. **Tampilkan Semua Buku**: Menampilkan daftar semua buku yang ada.
6. **Keluar**: Mengakhiri program.

## Struktur Program

### Direktori dan File
```
Program/
├── data/
│   ├── __init__.py
│   └── buku.py  # Berisi kelas Buku dan DataBuku
├── view/
│   ├── __init__.py
│   ├── input_form.py  # Berisi fungsi untuk input data buku
│   └── buku.py  # Berisi fungsi untuk menampilkan data buku
└── main.py  # Program utama
```

### Modul dan Kelas
1. **data/buku.py**
   - **Kelas Buku**: Merepresentasikan entitas buku dengan atribut ID, judul, dan penulis.
   - **Kelas DataBuku**: Mengelola daftar buku, seperti menambah, menghapus, mencari, dan mengubah data buku.

2. **view/input_form.py**
   - **Fungsi input_buku()**: Meminta input dari pengguna untuk ID, judul, dan penulis buku.

3. **view/buku.py**
   - **Fungsi tampilkan_buku()**: Menampilkan daftar buku.
   - **Fungsi tampilkan_detail()**: Menampilkan detail buku tertentu.

4. **main.py**
   - Program utama yang menyediakan menu interaktif untuk pengguna.


## Contoh Penggunaan

### Menambahkan Buku
```
Menu:
1. Tambah Buku
2. Hapus Buku
3. Cari Buku
4. Ubah Buku
5. Tampilkan Semua Buku
6. Keluar
Pilih menu: 1
Masukkan ID Buku: 101
Masukkan Judul Buku: Pemrograman Python
Masukkan Penulis Buku: John Doe
Buku berhasil ditambahkan.
```

### Menampilkan Semua Buku
```
Menu:
1. Tambah Buku
2. Hapus Buku
3. Cari Buku
4. Ubah Buku
5. Tampilkan Semua Buku
6. Keluar
Pilih menu: 5

Daftar Buku:
ID Buku: 101, Judul: Pemrograman Python, Penulis: John Doe
```



