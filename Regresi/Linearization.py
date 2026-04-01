import numpy as np
import matplotlib.pyplot as plt

# 1. Menyiapkan Data Asli
# Menggunakan data dari gambar contoh Eksponensial Anda
x = np.array([1, 2, 3])
y = np.array([2.4, 5.0, 9.0])
n = len(x)

# 2. Menghitung Elemen-Elemen Tabel (Linearisasi)
# Mengubah y menjadi z menggunakan logaritma natural (ln)
z = np.log(y) 

x2 = x**2
xz = x * z

# 3. Menampilkan Tabel Perhitungan
print("=" * 55)
print(f"{'xi':^4} | {'yi':^5} | {'zi = ln(yi)':^12} | {'xi^2':^5} | {'xi*zi':^10}")
print("-" * 55)

for i in range(n):
    print(f"{x[i]:4} | {y[i]:5.1f} | {z[i]:12.6f} | {x2[i]:5} | {xz[i]:10.6f}")

print("-" * 55)

# Menghitung Total (Sigma)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_z = np.sum(z)
sum_x2 = np.sum(x2)
sum_xz = np.sum(xz)

print(f"{'SUM':4} | {'-':^5} | {sum_z:12.6f} | {sum_x2:5} | {sum_xz:10.6f}")
print("=" * 55)

# 4. Menyusun dan Menyelesaikan Matriks
# Persamaan Normal untuk Regresi Eksponensial (yang sudah dilinearisasi):
# [ n     sum_x  ] [ alpha ]   [ sum_z  ]
# [ sum_x sum_x2 ] [ b     ] = [ sum_xz ]

A = np.array([
    [n, sum_x],
    [sum_x, sum_x2]
])
B = np.array([sum_z, sum_xz])

# Memecahkan matriks untuk mencari alpha dan b
alpha, b = np.linalg.solve(A, B)

# Mengembalikan nilai alpha menjadi a (karena alpha = ln(a), maka a = e^alpha)
a = np.exp(alpha)

print(f"\nHasil Matriks: alpha = {alpha:.5f}, b = {b:.5f}")
print(f"Transformasi Balik: a = e^{alpha:.5f} = {a:.5f}")
print(f"\nPersamaan Kurva Nonlinear: y = {a:.5f} e^({b:.5f}x)\n")

# 5. Visualisasi Grafik
plt.figure(figsize=(8, 5))

# Plot titik data asli
plt.scatter(x, y, color='red', label='Data Asli', s=100, zorder=5)

# Membuat kurva eksponensial berdasarkan persamaan yang ditemukan
x_curve = np.linspace(min(x) - 0.5, max(x) + 0.5, 100)
y_curve = a * np.exp(b * x_curve)

plt.plot(x_curve, y_curve, color='blue', linewidth=2.5, label='Kurva Regresi Eksponensial')

# grafik
plt.title('Visualisasi Regresi Nonlinear (Model Eksponensial)', fontsize=14)
plt.xlabel('Nilai X', fontsize=12)
plt.ylabel('Nilai Y', fontsize=12)

# Menambahkan kotak teks berisi persamaan di dalam grafik
eq_text = f'$y = {a:.5f} e^{{{b:.5f}x}}$'
plt.text(1.2, 7.5, eq_text, fontsize=12, color='black', 
         bbox=dict(facecolor='white', edgecolor='blue', alpha=0.8, boxstyle='round,pad=0.5'))

plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()