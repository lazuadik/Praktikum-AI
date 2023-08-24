harga_belanja = int(input("Harga belanja: "))

if harga_belanja > 50000:
    harga_total = harga_belanja * (127 / 100)
elif 30000 <= harga_belanja <= 50000:
    harga_total = harga_belanja * (118 / 100)
else:
    harga_total = harga_belanja

print(harga_total)