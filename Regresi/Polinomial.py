import numpy as np
import matplotlib.pyplot as plt

# 1. Menyiapkan Data Asli
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])
n = len(x)

# 2. Menghitung Elemen-Elemen Tabel
x2 = x**2
x3 = x**3
x4 = x**4
xy = x * y
x2y = x2 * y

# 3. Menampilkan Tabel Perhitungan
print("="*78)
print(f"{'xi':^5} | {'yi':^6} | {'xi^2':^6} | {'xi^3':^6} | {'xi^4':^6} | {'xi*yi':^8} | {'xi^2*yi':^8}")
print("-" * 78)

for i in range(n):
    print(f"{x[i]:5} | {y[i]:6.1f} | {x2[i]:6} | {x3[i]:6} | {x4[i]:6} | {xy[i]:8.1f} | {x2y[i]:8.1f}")

print("-" * 78)

# Menghitung Total (Sigma)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x2 = np.sum(x2)
sum_x3 = np.sum(x3)
sum_x4 = np.sum(x4)
sum_xy = np.sum(xy)
sum_x2y = np.sum(x2y)

print(f"{'SUM':5} | {sum_y:6.1f} | {sum_x2:6} | {sum_x3:6} | {sum_x4:6} | {sum_xy:8.1f} | {sum_x2y:8.1f}")
print("="*78)

# 4. Menyusun dan Menyelesaikan Matriks Persamaan Normal
# [ n     sum_x   sum_x2 ] [ a ]   [ sum_y   ]
# [ sum_x sum_x2  sum_x3 ] [ b ] = [ sum_xy  ]
# [ sum_x2 sum_x3 sum_x4 ] [ c ]   [ sum_x2y ]

A = np.array([
    [n, sum_x, sum_x2],
    [sum_x, sum_x2, sum_x3],
    [sum_x2, sum_x3, sum_x4]
])
B = np.array([sum_y, sum_xy, sum_x2y])

# Mencari koefisien a, b, dan c
a, b, c = np.linalg.solve(A, B)

print(f"\nPersamaan Hasil: y = {a:.4f} + {b:.4f}x + {c:.4f}x^2\n")

# 5. Visualisasi Grafik
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Data Asli', s=100)

# Membuat kurva
x_smooth = np.linspace(x.min(), x.max(), 100)
y_smooth = a + b*x_smooth + c*(x_smooth**2)

plt.plot(x_smooth, y_smooth, label='Kurva Polinomial Orde 2', color='blue', linewidth=2)
plt.title('Visualisasi Regresi Polinomial Orde 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()