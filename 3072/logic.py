import random

def start():
    mat = []
    matx = []
    for i in range(4):
        matx.append(0)

    for i in range(4): 
        mat.append(matx)
    

    # instruksi kontrol
    print("Key : ")
    print("'W' or 'w' : Up")
    print("'S' or 's' : Down")
    print("'A' or 'a' : Left")
    print("'D' or 'd' : Right")

    # memasukkan angka 2 ke matriks dengan function
    add_2(mat)
    return mat

# menambah angka ke matriks
def add_2(mat):
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
    
    # jika grid penuh, tapi terdapat angka yang bisa digabung disekitarnya
    for i in range(4):
        for j in range(4):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return "BELUM BERAKHIR"
            
    # 

    return "KALAH"
    