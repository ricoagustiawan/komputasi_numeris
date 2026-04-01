import numpy as np
import matplotlib.pyplot as plt

# 1. Menyiapkan Data Asli (Example 4)
x = np.array([0.24, 0.65, 0.95, 1.24, 1.73, 2.01, 2.23, 2.52])
y = np.array([0.23, -0.23, -1.1, -0.45, 0.27, 0.1, -0.29, 0.24])
n = len(x)

# 2. Menghitung Fungsi Basis (Nonlinear)
f1 = np.log(x)   # ln(x)
f2 = np.cos(x)   # cos(x)
f3 = np.exp(x)   # e^x

# 3. Menampilkan Tabel Fungsi Basis
print("=" * 52)
print(f"{'xi':^6} | {'yi':^7} | {'ln(x)':^9} | {'cos(x)':^8} | {'e^x':^9}")
print("-" * 52)

for i in range(n):
    print(f"{x[i]:6.2f} | {y[i]:7.2f} | {f1[i]:9.4f} | {f2[i]:8.4f} | {f3[i]:9.4f}")

print("=" * 52)

# 4. Menghitung Total (Sigma) untuk Matriks
sum_f1_sq = np.sum(f1**2)            # Σ (ln x)^2
sum_f1_f2 = np.sum(f1 * f2)          # Σ (ln x * cos x)
sum_f1_f3 = np.sum(f1 * f3)          # Σ (ln x * e^x)
sum_y_f1  = np.sum(y * f1)           # Σ (y * ln x)

sum_f2_sq = np.sum(f2**2)            # Σ (cos x)^2
sum_f2_f3 = np.sum(f2 * f3)          # Σ (cos x * e^x)
sum_y_f2  = np.sum(y * f2)           # Σ (y * cos x)

sum_f3_sq = np.sum(f3**2)            # Σ (e^x)^2
sum_y_f3  = np.sum(y * f3)           # Σ (y * e^x)

print("\nNilai Sigma (Σ) untuk Penyusunan Matriks:")
print(f"Σ (ln x)^2        = {sum_f1_sq:8.5f}")
print(f"Σ (ln x * cos x)  = {sum_f1_f2:8.5f}")
print(f"Σ (ln x * e^x)    = {sum_f1_f3:8.5f}")
print(f"Σ (cos x)^2       = {sum_f2_sq:8.5f}")
print(f"Σ (cos x * e^x)   = {sum_f2_f3:8.5f}")
print(f"Σ (e^x)^2         = {sum_f3_sq:8.5f}")
print("-" * 35)
print(f"Σ (y * ln x)      = {sum_y_f1:8.6f}")
print(f"Σ (y * cos x)     = {sum_y_f2:8.6f}")
print(f"Σ (y * e^x)       = {sum_y_f3:8.6f}\n")

# 5. Menyusun dan Menyelesaikan Matriks
A = np.array([
    [sum_f1_sq, sum_f1_f2, sum_f1_f3],
    [sum_f1_f2, sum_f2_sq, sum_f2_f3],
    [sum_f1_f3, sum_f2_f3, sum_f3_sq]
])

B = np.array([sum_y_f1, sum_y_f2, sum_y_f3])

# Memecahkan matriks untuk mencari a1, a2, a3
a1, a2, a3 = np.linalg.solve(A, B)

print("=== HASIL REGRESI NONLINEAR ===")
print(f"a1 (untuk ln x)  = {a1:.5f}")
print(f"a2 (untuk cos x) = {a2:.5f}")
print(f"a3 (untuk e^x)   = {a3:.6f}")
print(f"Persamaan: f(x) = {a1:.5f} ln(x) {a2:.5f} cos(x) + {a3:.6f} e^x\n")

# 6. Grafik
plt.figure(figsize=(9, 6))

# Plot titik data asli
plt.scatter(x, y, color='red', label='Data Asli', s=100, zorder=5)

# Membuat kurva hasil regresi nonlinear
x_curve = np.linspace(min(x), max(x), 100)
y_curve = a1 * np.log(x_curve) + a2 * np.cos(x_curve) + a3 * np.exp(x_curve)

plt.plot(x_curve, y_curve, color='blue', linewidth=2.5, label='Kurva Fit Nonlinear')

# grafik
plt.title('Visualisasi General Linear Least Squares', fontsize=14)
plt.xlabel('Nilai X', fontsize=12)
plt.ylabel('Nilai Y', fontsize=12)
eq_text = f'$f(x) = {a1:.3f} \\ln(x) - {abs(a2):.3f} \\cos(x) + {a3:.4f} e^x$'
plt.text(1.0, 0.0, eq_text, fontsize=12, color='black', 
         bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8, boxstyle='round,pad=0.5'))

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()