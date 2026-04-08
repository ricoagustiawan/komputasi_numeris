import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# ==========================================
# 1. SETUP DATA (Sesuai Gambar)
# ==========================================
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1, 3, 2, 5, 4])
x_smooth = np.linspace(min(x_data), max(x_data), 100)

def run_full_interpolation():
    print("="*80)
    print(" PROSES PERHITUNGAN INTERPOLASI: NEWTON VS LAGRANGE ")
    print("="*80)

    # --- BAGIAN A: METODE NEWTON (TABEL & PERSAMAAN) ---
    n = len(x_data)
    tabel = np.zeros([n, n])
    tabel[:, 0] = y_data
    
    for j in range(1, n):
        for i in range(n - j):
            tabel[i][j] = (tabel[i+1][j-1] - tabel[i][j-1]) / (x_data[i+j] - x_data[i])

    print("\n[1] TABEL SELISIH TERBAGI NEWTON (Seperti Gambar 1):")
    header = "x\t| f(x)\t| " + " | ".join([f"f[{','*i}]\t" for i in range(1, n)])
    print(header)
    print("-" * 80)
    for i in range(n):
        row = f"{x_data[i]}\t| "
        for j in range(n - i):
            val = tabel[i][j]
            row += f"{Fraction(val).limit_denominator()}\t| " if val % 1 != 0 else f"{int(val)}\t| "
        print(row)

    # Susun String Persamaan Newton (Seperti Gambar 2)
    koef = tabel[0, :]
    eq_newton = f"f(x) = {int(koef[0])}"
    for i in range(1, n):
        term = f"({Fraction(koef[i]).limit_denominator()})" if koef[i] % 1 != 0 else f"{int(koef[i])}"
        if koef[i] >= 0: term = f"+ {term}"
        
        parts = "".join([f"(x-{x_data[j]})" for j in range(i)])
        eq_newton += f" {term}{parts}"
    print(f"\nPersamaan Newton:\n{eq_newton}")


    # --- BAGIAN B: METODE LAGRANGE (BASIS & PERSAMAAN) ---
    print("\n" + "="*80)
    print("[2] LANGKAH BASIS LAGRANGE (Seperti Gambar 3):")
    
    eq_lagrange_base = "f(x) = " + " + ".join([f"{y_data[i]}l_{i}(x)" for i in range(n)])
    print(f"Bentuk Umum: {eq_lagrange_base}\n")

    for i in range(n):
        pembilang = "".join([f"(x-{x_data[j]})" for j in range(n) if i != j])
        penyebut_val = np.prod([x_data[i] - x_data[j] for j in range(n) if i != j])
        print(f"l_{i}(x) = {pembilang} / {penyebut_val}")

    # --- BAGIAN C: VISUALISASI GRAFIK ---
    # Fungsi Evaluasi untuk Plotting
    def eval_newton(x):
        res = koef[0]
        for i in range(1, n):
            p = 1
            for j in range(i): p *= (x - x_data[j])
            res += koef[i] * p
        return res

    def eval_lagrange(x):
        res = 0
        for i in range(n):
            li = 1
            for j in range(n):
                if i != j: li *= (x - x_data[j]) / (x_data[i] - x_data[j])
            res += y_data[i] * li
        return res

    y_newton = [eval_newton(xi) for xi in x_smooth]
    y_lagrange = [eval_lagrange(xi) for xi in x_smooth]

    plt.figure(figsize=(10, 6))
    plt.plot(x_smooth, y_lagrange, 'b-', lw=4, alpha=0.3, label='Kurva Lagrange (Garis Tebal)')
    plt.plot(x_smooth, y_newton, 'r--', lw=2, label='Kurva Newton (Garis Putus-putus)')
    plt.scatter(x_data, y_data, color='black', zorder=5, label='Titik Data (Waypoint)')
    
    plt.title('Newton vs Lagrange: Dua Jalan, Satu Tujuan')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    print("\n[3] Menampilkan Grafik... (Tutup jendela grafik untuk mengakhiri)")
    plt.show()

if __name__ == "__main__":
    run_full_interpolation()