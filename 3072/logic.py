import random
import constant as c

# tampilan awal game
def new_game(n):
    # membuat matriks kosong dengan grid panjang x lebar
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix

# memilih baris dan kolom acak untuk memasukkan angka baru
def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)

    # jika cell berisi angka, pilih cell lain yang akan dimasukkan angka baru
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)

    # memasukkan angka 3 ke dalam matriks
    mat[a][b] = 3
    return mat

# kondisi game
def game_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 3072:
                return 'win'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'

# menggeser ke kiri cell yang kosong pada grid
def cover_up(mat):
    # matriks kosong baru dengan panjang x lebar
    new = []
    for j in range(c.GRID_LEN):
        partial_new = []
        for i in range(c.GRID_LEN):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    
    for i in range(c.GRID_LEN):
        # index kolom matriks baru
        count = 0
        for j in range(c.GRID_LEN):
            # menggeser angka ke kiri
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True

                # lanjut ke kolom matriks baru berikutnya untuk digeser nilainya
                count += 1
    return new, done

# menjumlahkan nilai yang sama ke kiri
def merge(mat, done):
    for i in range(c.GRID_LEN):
        # pengecekan hanya sampai kolom index sebelum akhir, jika lebih maka akan error
        #   karena index kolom yang akan dijumlahkan nantinya melebihi batas index
        for j in range(c.GRID_LEN-1):
            # memastikan nilai yang akan dijumlahkan bukan 0
            # memastikan nilai yang akan dijumlahkan sama besar di kanannya
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done

# membalikkan nilai kiri ke kanan
def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new

# mengganti kolom menjadi baris
def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

# gerak ke kiri
def left(game):
    print("left")
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done

# gerak ke kanan
def right(game):
    print("right")
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done

# gerak ke atas
def up(game):
    print("up")
    game = transpose(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(game)
    return game, done

# gerak ke bawah
def down(game):
    print("down")
    game = reverse(transpose(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return game, done
