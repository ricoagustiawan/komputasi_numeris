import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def run_newton_with_steps_and_plot():
    # 1. DATA (Sesuai gambar: x=0,1,2,3,4 | y=1,3,2,5,4)
    x_data = np.array([0, 1, 2, 3, 4], dtype=float)
    y_data = np.array([1, 3, 2, 5, 4], dtype=float)
    n = len(x_data)
    
    print("="*80)
    print(" LANGKAH PERHITUNGAN SELISIH TERBAGI NEWTON ")
    print("="*80)

    # 2. HITUNG TABEL SELISIH TERBAGI (DENGAN PRINT LOG)
    tabel = np.zeros([n, n])
    tabel[:, 0] = y_data
    
    for j in range(1, n):
        print(f"\n--- Menghitung Kolom Orde-{j} (f[{','*j}]) ---")
        for i in range(n - j):
            pembilang = tabel[i+1][j-1] - tabel[i][j-1]
            penyebut = x_data[i+j] - x_data[i]
            tabel[i][j] = pembilang / penyebut
            
            # Format tampilan pecahan untuk log terminal
            f_pembilang = Fraction(pembilang).limit_denominator()
            f_penyebut = Fraction(penyebut).limit_denominator()
            f_hasil = Fraction(tabel[i][j]).limit_denominator()
            
            print(f"  f[{i}...{i+j}] = ({f_pembilang}) / ({f_penyebut}) = {f_hasil}")

    # 3. TAMPILKAN TABEL FINAL (FORMAT PECAHAN)
    print("\n" + "="*80)
    print("TABEL SELISIH TERBAGI AKHIR (Sesuai Gambar 1):")
    header = "x\t| f(x)\t| " + " | ".join([f"Orde-{i}\t" for i in range(1, n)])
    print(header)
    print("-" * 80)
    for i in range(n):
        row = f"{int(x_data[i])}\t| "
        for j in range(n - i):
            val = tabel[i][j]
            # Menampilkan sebagai pecahan jika bukan angka bulat
            if val % 1 == 0:
                row += f"{int(val)}\t| "
            else:
                row += f"{Fraction(val).limit_denominator()}\t| "
        print(row)

    # 4. RAKIT PERSAMAAN (Sesuai Gambar 2)
    koef = tabel[0, :]
    print("\n" + "="*80)
    print("PERSAMAAN POLINOMIAL NEWTON:")
    
    # Ambil baris teratas sebagai koefisien (a0, a1, a2...)
    eq_parts = []
    for i in range(n):
        c = Fraction(koef[i]).limit_denominator()
        if i == 0:
            eq_parts.append(f"{c}")
        else:
            term_x = "".join([f"(x-{int(x_data[j])})" for j in range(i)])
            tanda = "+" if c >= 0 else "-"
            eq_parts.append(f"{tanda} {abs(c)}{term_x}")
            
    print(f"f_4(x) = {' '.join(eq_parts)}")

    # 5. VISUALISASI GRAFIK
    x_plot = np.linspace(min(x_data), max(x_data), 100)
    
    def eval_newton(x_val):
        res = koef[0]
        for i in range(1, n):
            temp = koef[i]
            for j in range(i):
                temp *= (x_val - x_data[j])
            res += temp
        return res

    y_plot = [eval_newton(x) for x in x_plot]

    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_plot, 'r-', label='Polinomial Newton $f_4(x)$', linewidth=2)
    plt.scatter(x_data, y_data, color='black', s=100, label='Titik Data (Gambar)', zorder=5)
    
    # Tambahkan anotasi pada titik agar jelas
    for i, txt in enumerate(y_data):
        plt.annotate(f"({int(x_data[i])},{int(txt)})", (x_data[i], y_data[i]), 
                     textcoords="offset points", xytext=(0,10), ha='center')

    plt.title('Grafik Interpolasi Newton (Selisih Terbagi)')
    plt.xlabel('Sumbu X')
    plt.ylabel('Sumbu Y / f(x)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    print("\n[INFO] Menampilkan Grafik...")
    plt.show()

if __name__ == "__main__":
    run_newton_with_steps_and_plot()