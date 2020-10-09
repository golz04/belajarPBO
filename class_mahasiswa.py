class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    # def get_nama(self):
    #     return self.nama
    def set_nama(self, ganti_nama):
        self.nama = ganti_nama

    def belajar(self, kondisi):
        self.kondisi = kondisi
        print("Kondisi dari",self.nama,"dengan nim",self.nim,self.kondisi)
    
    def get_kehadiran(self, jenis_kehadiran):
        self.jenis_kehadiran = jenis_kehadiran
        return self.jenis_kehadiran
    

siswa = Mahasiswa("Haidar", "192410103002")
siswa2 = Mahasiswa("Agus", "3003")
siswa3 = Mahasiswa("Windi", "3009")
print('''
Nama    : {}
NIM     : {}
=============================='''.format(siswa.nama, siswa.nim))
siswa.set_nama("Amiroh")
kondisi = input("Mau Kondisi Apa ?")
siswa.belajar(kondisi)
siswa2.belajar("Malas malas")
siswa3.belajar("Gak Niat")
print("==============================")
print("Kehadiran", siswa.nama,"adalah",siswa.get_kehadiran("Alpha"))
print("Kehadiran", siswa2.nama,"adalah",siswa2.get_kehadiran("Ijin"))
print("Kehadiran", siswa3.nama,"adalah",siswa3.get_kehadiran("Hadir"))