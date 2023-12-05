import tkinter as tk
import random
import constant as c


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('3072')

        # warna background game
        self.main_grid = tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=400, height=400)
        self.main_grid.grid(pady=(80, 0))
        self.make_GUI()
        self.start_game()

        # menerima input keyboard tanpa enter
        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    # membuat tampilan GUI
    def make_GUI(self):
        # membuat tampilan grid panjang x lebar
        self.cells = []
        for i in range(c.GRID_LEN):
            row = []
            for j in range(c.GRID_LEN):
                # membuat tampilan cell (box angka)
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_BG,
                    width=100,
                    height=100)
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.EMPTY_CELL_BG)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=40, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            font=c.SCORE_LABEL_FONT).grid(
            row=0)
        self.score_label = tk.Label(score_frame, text="0", font=c.SCORE_FONT)
        self.score_label.grid(row=1)

    # tampilan awal game
    def start_game(self):
        # membuat matriks kosong dengan grid 4x4
        self.matrix = [[0] * 4 for _ in range(4)]

        # memilih baris dan kolom acak untuk memasukkan angka baru
        # baris = b
        # kolom = k
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 3
        self.cells[row][col]["frame"].configure(bg=c.BG_COLOR[3])
        self.cells[row][col]["number"].configure(
            bg=c.BG_COLOR[3],
            fg=c.NUMBER_COLOR[3],
            font=c.NUMBER_FONTS[3],
            text="3")
        
        # jika berisi angka, pilih baris dan kolom lain yang akan dimasukkan angka baru
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        # memasukkan angka 3 ke dalam matriks
        self.matrix[row][col] = 3
        self.cells[row][col]["frame"].configure(bg=c.BG_COLOR[3])
        self.cells[row][col]["number"].configure(
            bg=c.BG_COLOR[3],
            fg=c.NUMBER_COLOR[3],
            font=c.NUMBER_FONTS[3],
            text="3")

        self.score = 0

    # menggeser angka ke kiri pada grid (stack)
    def stack(self):
        # matriks kosong baru dengan grid 4x4
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):

            # index kolom matriks baru
            fill_position = 0
            for j in range(4):
                # menggeser angka ke kiri jika tidak ada angka di sebelah kirinya
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]

                    # lanjut ke kolom matriks baru berikutnya untuk digeser nilainya
                    fill_position += 1
        self.matrix = new_matrix

    # menjumlahkan nilai yang sama ke kiri
    def combine(self):
        for i in range(4):
            # pengecekan hanya sampai kolom index sebelum akhir, jika lebih maka akan error
            #   karena index kolom yang akan dijumlahkan nantinya melebihi batas index
            for j in range(3):
                # memastikan nilai yang akan dijumlahkan bukan 0
                # memastikan nilai yang akan dijumlahkan sama besar di kanannya
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    # membalikkan nilai kiri ke kanan
    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    # mengganti kolom menjadi baris
    def transpose(self):
        new_matrix = [[0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    # memasukkan angka baru
    def add_new_tile(self):
        # memilih baris dan kolom acak untuk memasukkan angka baru
        # baris = b
        # kolom = k
        row = random.randint(0, 3)
        col = random.randint(0, 3)

        # jika berisi angka, pilih baris dan kolom lain yang akan dimasukkan angka baru
        while(self.matrix[row][col] != 0):
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        # memasukkan angka 3 atau 6 ke dalam matriks
        self.matrix[row][col] = random.choice([3, 6])

    # menyesuaikan GUI agar sama dengan matrix
    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_BG)
                    self.cells[i][j]["number"].configure(
                        bg=c.EMPTY_CELL_BG, text="")
                else:
                    self.cells[i][j]["frame"].configure(
                        bg=c.BG_COLOR[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.BG_COLOR[cell_value],
                        fg=c.NUMBER_COLOR[cell_value],
                        font=c.NUMBER_FONTS[cell_value],
                        text=str(cell_value))
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    # gerak ke kiri
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    # gerak ke kanan
    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    # gerak ke atas
    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    # gerak ke bawah
    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    # mengecek apakah ada angka yang sama secara horizontal jika grid penuh
    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j + 1]:
                    return True
        return False

    # mengecek apakah ada angka yang sama secara vertikal jika grid penuh
    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i + 1][j]:
                    return True
        return False

    # mengecek kondisi game
    def game_over(self):
        if any(3072 in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="You win!",
                bg=c.WINNER_BG,
                fg=c.STATE_FONT_COLOR,
                font=c.STATE_FONT).pack()
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor="center")
            tk.Label(
                game_over_frame,
                text="Game over!",
                bg=c.LOSER_BG,
                fg=c.STATE_FONT_COLOR,
                font=c.STATE_FONT).pack()
Game()