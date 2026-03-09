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
        
        # 5. Mencetak kurung siku
        print(f"[ {A_str} ]  [{x_str}] {eq_sign} [ {b_str} ]")
    print("-" * 75)

def gauss_elimination(A, b):
    n = len(b)
    
    # Membuat Matriks Augmented M = [A | b]
    M = []
    for i in range(n):
        row = A[i].copy()
        row.append(b[i])
        M.append(row)
        
    print("Persamaan Matriks Awal:")
    print_equation(M)
    
    # Proses Forward Elimination
    for i in range(n):
        if M[i][i] == 0.0:
            print("Peringatan: Elemen pivot bernilai nol.")
            return None
            
        for j in range(i+1, n):
            ratio = M[j][i] / M[i][i]
            
            for k in range(n+1):
                M[j][k] = M[j][k] - ratio * M[i][k]
                
        if i < n - 1:
            print(f"Persamaan setelah eliminasi kolom ke-{i+1}:")
            print_equation(M)
        
    # Proses Back Substitution
    x = [0 for _ in range(n)]
    
    x[n-1] = M[n-1][n] / M[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += M[i][j] * x[j]
        x[i] = (M[i][n] - sum_ax) / M[i][i]
        
    return x

# --- Bagian Input Soal Matriks ---
A = [
    [ 6.0,  -2.0,   2.0,   4.0],
    [12.0,  -8.0,   6.0,  10.0],
    [ 3.0, -13.0,   9.0,   3.0],
    [-6.0,   4.0,   1.0, -18.0]
]

b = [16.0, 26.0, -19.0, -34.0]

# Menjalankan fungsi
hasil_x = gauss_elimination(A, b)

# Menampilkan hasil akhir
if hasil_x is not None:
    print("=== HASIL AKHIR ELIMINASI GAUSS ===")
    for i in range(len(hasil_x)):
        print(f"x_{i+1} = {hasil_x[i]:.2f}")