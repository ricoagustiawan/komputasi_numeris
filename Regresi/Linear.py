import numpy as np
import matplotlib.pyplot as plt

# 1. Menyiapkan Data Asli
x = np.array([1, 2, 3])
y = np.array([5.1, 5.9, 6.3])
n = len(x)

# 2. Menghitung Elemen-Elemen Tabel
x2 = x**2
xy = x * y

# 3. Menampilkan Tabel Perhitungan
print("=" * 38)
print(f"{'xi':^5} | {'yi':^5} | {'xi^2':^5} | {'xi*yi':^7}")
print("-" * 38)

for i in range(n):
    print(f"{x[i]:5} | {y[i]:5.1f} | {x2[i]:5} | {xy[i]:7.1f}")

print("-" * 38)

# Menghitung Total (Sigma)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x2)
sum_xy = np.sum(xy)

print(f"{'SUM':5} | {sum_y:5.1f} | {sum_x2:5} | {sum_xy:7.1f}")
print("=" * 38)

# 4. Menyusun dan Menyelesaikan Matriks
# Persamaan Normal untuk Linear Regression:
# [ n     sum_x  ] [ a ]   [ sum_y  ]
# [ sum_x sum_x2 ] [ b ] = [ sum_xy ]

A = np.array([
    [n, sum_x],
    [sum_x, sum_x2]
])
B = np.array([sum_y, sum_xy])

# Memecahkan matriks untuk mencari a (intercept) dan b (slope/gradien)
a, b = np.linalg.solve(A, B)

print(f"\nPersamaan Hasil: y = {a:.4f} + {b:.4f}x\n")

# 5. Visualisasi Grafik
plt.figure(figsize=(8, 5))

# Plot titik data asli
plt.scatter(x, y, color='red', label='Data Asli', s=100, zorder=5)

# Membuat garis lurus berdasarkan persamaan yang ditemukan
x_line = np.linspace(min(x) - 0.5, max(x) + 0.5, 100)
y_line = a + b * x_line

plt.plot(x_line, y_line, color='blue', linewidth=2.5, label='Garis Regresi Linear')

# grafik
plt.title('Visualisasi Regresi Linear (Least Squares)', fontsize=14)
plt.xlabel('Nilai X', fontsize=12)
plt.ylabel('Nilai Y', fontsize=12)
eq_text = f'$y = {a:.4f} + {b:.4f}x$'
plt.text(1.2, 6.1, eq_text, fontsize=12, color='black', 
         bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8, boxstyle='round,pad=0.5'))

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()