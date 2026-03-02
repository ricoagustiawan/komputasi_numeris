def f(x):
    return x**5 + x**3 + 3

def secant_method(x0, x1, epsilon):
    # Header Tabel
    # x0 mewakili x_{i-1}, x1 mewakili x_i, dan x_baru mewakili x_{i+1}
    print(f"{'Iterasi':<9} | {'x_i-1':<10} | {'x_i':<10} | {'f(x_i-1)':<10} | {'f(x_i)':<10} | {'x_i+1':<10} | {'Error':<10}")
    print("-" * 85)
    
    iteration = 1 # Variabel untuk menghitung iterasi
    
    # Memulai iterasi
    while True:
        fx0 = f(x0)
        fx1 = f(x1)
        
        # Cek awal untuk mencegah pembagian dengan nol
        if fx1 - fx0 == 0:
            print("Metode Secant gagal. Pembagian dengan nol karena f(x_i) - f(x_i-1) = 0.")
            return None
        
        # Rumus Metode Secant: x_i+1 = x_i - f(x_i) * [(x_i - x_i-1) / (f(x_i) - f(x_i-1))]
        x_baru = x1 - fx1 * ((x1 - x0) / (fx1 - fx0))
        
        # Menghitung batas error saat ini (nilai absolut selisih x baru dengan x sebelumnya)
        error = abs(x_baru - x1)
        
        # Print hasil iterasi saat ini ke layar
        print(f"{iteration:<9} | {x0:<10.5f} | {x1:<10.5f} | {fx0:<10.5f} | {fx1:<10.5f} | {x_baru:<10.5f} | {error:<10.5f}")
        
        # is error < epsilon?
        if error < epsilon:
            # yes -> Stop
            print("-" * 85)
            print(f"Berhenti pada iterasi ke-{iteration} karena error < epsilon")
            return x_baru
            
        # no: update nilai x0 dan x1 untuk iterasi selanjutnya
        # x1 bergeser menjadi x0, dan x_baru bergeser menjadi x1
        x0 = x1
        x1 = x_baru
        iteration += 1
        
        # Pengaman tambahan: mencegah infinite loop
        if iteration > 100:
            print("-" * 85)
            print(f"Berhenti karena mencapai batas iterasi maksimal (100).")
            return x1

# Nilai awal berdasarkan soal
x_awal_0 = -1
x_awal_1 = -1.1

# Nilai epsilon (toleransi error) berdasarkan soal (< 0.001)
epsilon = 0.001

# Menjalankan fungsi dan mencetak hasil
akar = secant_method(x_awal_0, x_awal_1, epsilon)

if akar is not None:
    print(f"Akar perkiraan untuk fungsi tersebut adalah: {akar:.5f}")
    print(f"Nilai f(x) : {f(akar):.7f}")