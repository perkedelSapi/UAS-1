class Buku:
    def __init__(self, id_buku, judul, penulis):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis

    def __str__(self):
        return f"ID Buku: {self.id_buku}, Judul: {self.judul}, Penulis: {self.penulis}"


class DataBuku:
    def __init__(self):
        self.buku_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)

    def hapus_buku(self, id_buku):
        self.buku_list = [b for b in self.buku_list if b.id_buku != id_buku]

    def cari_buku(self, id_buku):
        for buku in self.buku_list:
            if buku.id_buku == id_buku:
                return buku
        return None

    def ubah_buku(self, id_buku, judul_baru, penulis_baru):
        buku = self.cari_buku(id_buku)
        if buku:
            buku.judul = judul_baru
            buku.penulis = penulis_baru

    def tampilkan_semua(self):
        return self.buku_list