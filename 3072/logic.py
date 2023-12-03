import random

# awal game saat dijalankan
def start():
    # membuat matriks kosong dengan 4 baris dan kolom
    mat = []
    for i in range(4):
        mat.append([0] * 4)

    # instruksi kontrol
    print("Key : ")
    print("'W' or 'w' : Up")
    print("'S' or 's' : Down")
    print("'A' or 'a' : Left")
    print("'D' or 'd' : Right")

    # memasukkan angka 3 ke matriks dengan function
    add_3(mat)
    return mat

# menambah angka ke matriks
def add_3(mat):
    # memilih angka dari 0 sampai 3 ke baris dan kolom
    b = random.randint(0, 3)
    k = random.randint(0, 3)

    # jika berisi angka, pilih baris dan kolom lain yang akan dimasukkan angka baru
    while(mat[b] != 0):
        b = random.randint(0, 3)
        k = random.randint(0, 3)

    # memasukkan angka 3 ke dalam baris
    mat[b] = 3

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
    # pengecekan hanya sampai baris ke 3, jika lebih maka akan error karena saat
    # baris index 4 ditambah, index 5 tidak terdapat dalam matriks (akan error)
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "BELUM BERAKHIR"
            
    # jika grid penuh, tapi terdapat angka yg bisa digabung di kanannya (baris 4)
    for j in range(3):
        if(mat[3][j] == mat[3][j+1]):
            return "BELUM BERAKHIR"
        
    # jika grid penuh, tapi terdapat angka yg bisa digabung di bawahnya (kolom 4)
    for i in range(3):
        if(mat[i][3] == mat[i+1][3]):
            return "BELUM BERAKHIR"

    return "KALAH"
    
# kompress matriks untuk nanti nilainya di jumlahkan
def compress(mat):
    change = False

# mengganti baris ke kolom matriks x di matriks baru
def transpose(mat):
    new = []
    for i in range(4):
        new.append([])
        for j in range(4):
            new[i].append(mat[j][i])
    return new