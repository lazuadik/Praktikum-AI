harga_belanja = int(input("Harga belanja: "))

if harga_belanja > 50000:
    harga_total = harga_belanja * (127 / 100)
    print("Anda mendapatkan diskon 27%")
elif 30000 <= harga_belanja <= 50000:
    harga_total = harga_belanja * (118 / 100)
    print("Anda mendapatkan diskon 18%")
else:
    harga_total = harga_belanja
    print("Anda tidak mendapatkan diskon")

print("Harga total belanja Anda: ", harga_total)