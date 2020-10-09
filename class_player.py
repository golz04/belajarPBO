class Player():
    def __init__(self, nama):
        self.nama = nama

    def get_aksi(self, kondisi):
        return self.kondisi
    def set_aksi(self, kondisi):
        self.kondisi = kondisi

player1 = Player("Player 1")
# player1.aksi("Menyerang")

player2 = Player("Player 2")
# player2.aksi("Bertahan")

print(player1.get_aksi("Menyerang"))