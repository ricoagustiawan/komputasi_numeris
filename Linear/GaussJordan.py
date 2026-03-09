def print_equation(M):
    """Fungsi untuk mencetak matriks dalam format [A] [x] = [b]"""
    n = len(M)
    for i in range(n):
        # 1. Mengambil bagian matriks koefisien (A)
        A_row = M[i][:n]
        A_str = "  ".join([f"{val:7.2f}" for val in A_row])
        
        # 2. Membuat label variabel (x_1, x_2, dst)
        x_str = f"x_{i+1}"
        
        # 3. Mengambil bagian hasil konstanta (b)
        b_val = M[i][n]
        b_str = f"{b_val:7.2f}"
        
        # 4. Menempatkan tanda '='
        eq_sign = " = " if i == n // 2 else "   "
        
        # 5. Mencetak gabungan semuanya dengan kurung siku
        print(f"[ {A_str} ]  [{x_str}] {eq_sign} [ {b_str} ]")
    print("-" * 75)

def gauss_jordan(A, b):
    n = len(b)
    
    # Membuat Matriks Augmented M = [A | b]
    M = []
    for i in range(n):
        row = A[i].copy()
        row.append(b[i])
        M.append(row)
        
    print("Persamaan Matriks Awal:")
    print_equation(M)
    
    # Proses Eliminasi Gauss-Jordan
    for i in range(n):
        if M[i][i] == 0.0:
            print("Peringatan: Elemen pivot bernilai nol.")
            return None
        
        # Langkah A: Membagi baris pivot agar elemen diagonalnya menjadi 1
        pivot = M[i][i]
        for j in range(n + 1):
            M[i][j] = M[i][j] / pivot
            
        # Langkah B: Eliminasi baris LAIN (di atas dan di bawah pivot) agar menjadi 0
        for k in range(n):
            if k != i:
                pengali = M[k][i]
                for j in range(n + 1):
                    M[k][j] = M[k][j] - pengali * M[i][j]
                    
        print(f"Persamaan setelah proses pivot baris/kolom ke-{i+1}:")
        print_equation(M)
        
    # Solusi langsung diambil dari kolom paling kanan
    x = [M[i][n] for i in range(n)]
    return x

# --- Bagian Input Soal 3x3 ---
A = [
    [ 2.0, -2.0,  2.0],
    [ 4.0,  2.0, -1.0],
    [ 2.0, -2.0,  4.0]
]

b = [0.0, 7.0, 2.0]

# Menjalankan fungsi
hasil_x = gauss_jordan(A, b)

# Menampilkan hasil akhir
if hasil_x is not None:
    print("=== HASIL AKHIR GAUSS-JORDAN ===")
    for i in range(len(hasil_x)):
        print(f"x_{i+1} = {hasil_x[i]:.2f}")