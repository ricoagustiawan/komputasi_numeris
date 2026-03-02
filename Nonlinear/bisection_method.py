def f(x):
    return x**3 - 3*x + 1

def bisection_method(a, b, epsilon):
    u = f(a)
    v = f(b)
    
    # Syarat Bisection
    if u * v >= 0:
        print("Metode bagi dua mungkin tidak berhasil. f(a) dan f(b) harus berbeda tanda.")
        return None

    # Header Tabel
    print(f"{'Iterasi':<9} | {'a':<9} | {'b':<9} | {'c':<9} | {'f(c)':<10} | {'Error':<9}")
    print("-" * 70)
    
    iteration = 1 
    
    # Memulai iterasi
    while True:
        # c = (a+b)/2 ; w = f(c)
        c = (a + b) / 2
        w = f(c)
        
        # Menghitung batas error saat ini
        error = (b - a) / 2
        
        # Print hasil iterasi saat ini ke layar
        print(f"{iteration:<9} | {a:<9.5f} | {b:<9.5f} | {c:<9.5f} | {w:<10.5f} | {error:<9.5f}")
        
        # is u*w < 0?
        if u * w < 0:
            # yes: b = c ; v = w
            b = c
            v = w
        else:
            # no: a = c ; u = w
            a = c
            u = w
            
        # is (b-a)/2 < epsilon?
        if error < epsilon:
            # yes -> Stop
            print("-" * 70)
            print(f"Berhenti pada iterasi ke-{iteration} karena error < epsilon")
            return c
            
        iteration += 1 # Tambah penghitung iterasi untuk langkah selanjutnya

# Nilai awal berdasarkan soal di gambar kedua
a = 0
b = 1

# Nilai epsilon (toleransi error)
epsilon = 0.001

# Menjalankan fungsi dan mencetak hasil
akar = bisection_method(a, b, epsilon)

if akar is not None:
    print(f"Akar perkiraan untuk fungsi tersebut pada interval [{a}, {b}] adalah: {akar:.5f}")
    print(f"Nilai f(x) : {f(akar):.7f}")