def f(x):
    return x**3 - 2*x**2 + x - 3

def f_prime(x):
    h = 1e-7  # Nilai h yang sangat kecil
    return (f(x + h) - f(x)) / h

def newton_raphson(x0, epsilon):
    # Membuat header tabel untuk merapikan output
    print(f"{'Iterasi':<9} | {'x_i':<10} | {'f(x_i)':<10} | {'f_prime(x_i)':<12} | {'x_i+1':<10} | {'Error':<10}")
    print("-" * 80)
    
    iteration = 1 # Variabel untuk menghitung iterasi
    x = x0        # Inisialisasi tebakan awal
    
    # Memulai iterasi
    while True:
        fx = f(x)
        fpx = f_prime(x)
        
        # Cek awal apakah turunan nol (syarat Newton-Raphson tidak boleh f'(x) = 0)
        if fpx == 0:
            print("Metode Newton-Raphson gagal. Turunan f'(x) bernilai nol.")
            return None
        
        # x_i+1 = x_i - f(x_i)/f'(x_i)
        x_baru = x - (fx / fpx)
        
        # Menghitung batas error saat ini (nilai absolut selisih)
        error = abs(x_baru - x)
        
        # Print hasil iterasi saat ini ke layar
        print(f"{iteration:<9} | {x:<10.5f} | {fx:<10.5f} | {fpx:<12.5f} | {x_baru:<10.5f} | {error:<10.5f}")
        
        # is error < epsilon?
        if error < epsilon:
            # yes -> Stop
            print("-" * 80)
            print(f"Berhenti pada iterasi ke-{iteration} karena error < epsilon")
            return x_baru
            
        # no: update x untuk iterasi selanjutnya
        x = x_baru
        iteration += 1
        
        # Pengaman tambahan: mencegah infinite loop jika fungsi tidak konvergen
        if iteration > 100:
            print("-" * 80)
            print(f"Berhenti karena mencapai batas iterasi maksimal (100).")
            return x

# Nilai awal berdasarkan soal gambar pertama
x_awal = 4

# Nilai epsilon (toleransi error) disamakan dengan bisection
epsilon = 0.001

# Menjalankan fungsi dan mencetak hasil
akar = newton_raphson(x_awal, epsilon)

if akar is not None:
    print(f"Akar perkiraan untuk fungsi tersebut dengan tebakan awal {x_awal} adalah: {akar:.5f}")
    print(f"Nilai f(x) : {f(akar):.7f}")