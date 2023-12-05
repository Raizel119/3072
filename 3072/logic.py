import random

# tampilan awal game saat dijalankan
def start():
    # membuat matriks kosong dengan grid 4x4
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    # instruksi kontrol
    print("Key : ")
    print("'W' or 'w' : Up")
    print("'S' or 's' : Down")
    print("'A' or 'a' : Left")
    print("'D' or 'd' : Right")

    # memasukkan angka baru ke matriks dengan function
    add_num(mat)
    return mat

# menambah angka ke matriks
def add_num(mat):
    # memilih baris dan kolom acak
    # baris = row (r)
    r = random.randint(0, 3)
    # kolom = column (c)
    c = random.randint(0, 3)

    # jika berisi angka, pilih baris dan kolom lain yang akan dimasukkan angka baru
    while(mat[r][c] != 0):
        r = random.randint(0, 3)
        c = random.randint(0, 3)

    # memasukkan angka 3 ke dalam baris
    mat[r][c] = 3

# mengecek kondisi game
def state(mat):
    # jika terdapat 3072 di salah satu cell maka game menang
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 3072):
                return "MENANG"
            
    # jika grid masih ada 1 cell yang kosong
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == 0):
                return "BELUM BERAKHIR"
    
    # jika grid penuh, tapi terdapat angka yg bisa digabung di kanan atau bawah
    # pengecekan hanya sampai baris dan kolom ke dua terakhir, jika tidak maka akan error
    #   karena index kolom atau baris yang akan dijumlahkan melewati batas index
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "BELUM BERAKHIR"
            
    # jika grid penuh, tapi terdapat angka yg bisa digabung di kanannya (baris terakhir)
    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return "BELUM BERAKHIR"
        
    # jika grid penuh, tapi terdapat angka yg bisa digabung di bawahnya (kolom terakhir)
    for i in range(3):
        if(mat[i][3] == mat[i+1][3]):
            return "BELUM BERAKHIR"

    return "KALAH"
    
# menggeser angka ke kiri pada grid
def shift(mat):
	# variabel bool untuk perubahan pada grid
	change = False

	# matriks kosong baru dengan grid 4x4
	new = []
	for i in range(4):
		new.append([0] * 4)
	
	# looping per baris
	for i in range(4):
        # index kolom matriks baru
		x = 0
        
        # looping untuk kolom pada tiap baris
		for j in range(4):
            # menggeser angka ke kiri jika tidak ada angka di sebelah kirinya
			if(mat[i][j] != 0):
				new[i][x] = mat[i][j]
				
				# jika posisi angka matriks baru dgn matriks game berbeda,
                # maka ada perubahan
				if(j != x):
					change = True
                         
                # lanjut ke kolom matriks baru berikutnya untuk diisi nilainya
				x += 1
	return new, change

# menjumlahkan nilai yang sama ke kiri
def merge(mat, change):
    for i in range(4):
        # pengecekan hanya sampai kolom ke dua terakhir, jika tidak maka akan error
        #   karena index kolom yang akan dijumlahkan melebihi batas index
        for j in range(3):
            # memastikan nilai yang akan dijumlahkan bukan 0
            # memastikan nilai yang akan dijumlahkan sama besar di kanannya
            if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
                mat[i][j] += mat[i][j+1]
                mat[i][j+1] = 0

                # nilai angka berubah
                change = True
    return mat, change

# membalikkan nilai kiri ke kanan
def reverse(mat):
    new = []
    for i in range(4):
        new.append([])
        for j in range(3):
            new[i].append(mat[i][3 - j])
    return new

# mengganti kolom menjadi baris
def transpose(mat):
    new = []
    for i in range(4):
        new.append([])
        for j in range(4):
            new[i].append(mat[j][i])
    return new

# gerak ke kiri
def left(game):
    # gerakkan grid ke kiri
    game, change = shift(game)
    # jumlahkan nilainya ke kiri
    game, change = merge(game, change)
    # kemudian gerakkan ke kiri lagi
    game, change = shift(game)
    return game, change

# gerak ke kanan
def right(game):
    # balikkan angka kiri ke kanan
    game = reverse(game)
     # gerakkan grid ke kiri
    game, change = shift(game)
    # jumlahkan nilainya ke kiri
    game, change = merge(game, change)
    # kemudian gerakkan ke kiri lagi
    game, change = shift(game)
    # balikkan kanan ke kiri
    game = reverse(game)
    return game, change

def up(game):
    # mengganti kolom ke baris
    game = transpose(game)
     # gerakkan grid ke kiri
    game, change = shift(game)
    # jumlahkan nilainya ke kiri
    game, change = merge(game, change)
    # kemudian gerakkan ke kiri lagi
    game, change = shift(game)
    # belikkan kolom ke baris
    game = transpose(game)
    return game, change

def down(game):
    # mengganti kolom ke baris, lalu balikkan kiri ke kanan
    game = reverse(transpose(game))
     # gerakkan grid ke kiri
    game, change = shift(game)
    # jumlahkan nilainya ke kiri
    game, change = merge(game, change)
    # kemudian gerakkan ke kiri lagi
    game, change = shift(game)
    # balikkan kanan ke kiri, lalu mengganti baris ke kolom
    game = transpose(reverse(game))
    return game, change