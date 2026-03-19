def print_persamaan(A, b):
    """Fungsi untuk mencetak persamaan dalam format [A] [x] = [b]"""
    n = len(A)
    for i in range(n):
        A_str = "  ".join([f"{val:7.2f}" for val in A[i]])
        x_str = f"x_{i+1}"
        b_str = f"{b[i]:7.2f}"
        
        eq_sign = " = " if i == n // 2 else "   "
        
        print(f"[ {A_str} ]  [{x_str}] {eq_sign} [ {b_str} ]")
    print("-" * 65)

def urutkan_diagonally_dominant(A, b):
    n = len(A)
    A_baru = [[0.0] * n for _ in range(n)]
    b_baru = [0.0] * n
    posisi_terisi = [False] * n

    for i in range(n):
        max_val = -1
        max_idx = -1
        # Mencari nilai absolut terbesar di baris i
        for j in range(n):
            if abs(A[i][j]) > max_val:
                max_val = abs(A[i][j])
                max_idx = j
        
        # Menempatkan baris ke posisi diagonal yang sesuai
        if not posisi_terisi[max_idx]:
            A_baru[max_idx] = A[i].copy()
            b_baru[max_idx] = b[i]
            posisi_terisi[max_idx] = True
        else:
            print("Peringatan: Matriks tidak bisa diurutkan menjadi Diagonally Dominant sempurna.")
            return A, b
            
    return A_baru, b_baru

def jacobi_iteration(A, b, tebakan_awal, epsilon, max_iter=100):
    n = len(b)
    x_lama = tebakan_awal.copy()
    x_baru = [0.0 for _ in range(n)]
    
    # Membuat header tabel
    header_x = " | ".join([f"x_{i+1:<8}" for i in range(n)])
    print(f"\n{'Iterasi':<9} | {header_x} | {'Error':<10}")
    print("-" * (25 + 11 * n))
    
    # Cetak tebakan awal
    awal_str = " | ".join([f"{val:10.2f}" for val in x_lama])
    print(f"{0:<9} | {awal_str} | {'-':<10}")
    
    # Memulai perulangan iterasi Jacobi
    for iterasi in range(1, max_iter + 1):
        for i in range(n):
            if A[i][i] == 0:
                print(f"Metode gagal: Elemen diagonal A[{i}][{i}] bernilai nol.")
                return None
                
            sum_ax = 0.0
            for j in range(n):
                if i != j:
                    sum_ax += A[i][j] * x_lama[j]
                    
            # Rumus Iterasi Jacobi: hitung dan simpan di x_baru
            x_baru[i] = (b[i] - sum_ax) / A[i][i]
            
        # Menghitung error
        error = max([abs(x_baru[i] - x_lama[i]) for i in range(n)])
        
        # Cetak hasil iterasi
        x_str = " | ".join([f"{val:10.2f}" for val in x_baru])
        print(f"{iterasi:<9} | {x_str} | {error:10.2f}")
        
        # Kondisi berhenti
        if error < epsilon:
            print("-" * (25 + 11 * n))
            print(f"Berhenti pada iterasi ke-{iterasi} karena error < epsilon")
            return x_baru
            
        # Update nilai x_lama secara SERENTAK untuk iterasi selanjutnya
        x_lama = x_baru.copy()
        
    print("-" * (25 + 11 * n))
    print("Peringatan: Iterasi mencapai batas maksimal tanpa konvergensi.")
    return x_baru

A_mentah = [
    [  1.0,  8.0, -2.0],
    [ -2.0,  4.0, -9.0],
    [ 10.0, -3.0,  6.0]
]

b_mentah = [-9.0, -50.0, 24.5]

print("=== PERSAMAAN SEBELUM DIURUTKAN ===")
print_persamaan(A_mentah, b_mentah)

# 1. Memanggil fungsi pengurut otomatis
A_urut, b_urut = urutkan_diagonally_dominant(A_mentah, b_mentah)

# 2. Cetak persamaan yang sudah diurutkan
print("\n=== PERSAMAAN SETELAH DIURUTKAN (Diagonally Dominant) ===")
print_persamaan(A_urut, b_urut)

# 3. Menjalankan fungsi Iterasi Jacobi
tebakan_awal = [0.0, 0.0, 0.0]
batas_error = 1e-5
hasil_x = jacobi_iteration(A_urut, b_urut, tebakan_awal, batas_error)

if hasil_x is not None:
    print("\n=== HASIL AKHIR ITERASI JACOBI ===")
    print(f"x_1 = {hasil_x[0]:.2f}")
    print(f"x_2 = {hasil_x[1]:.2f}")
    print(f"x_3 = {hasil_x[2]:.2f}")