angka1 = input()
operator = input()
angka2 = input()
total = eval(angka1 + operator + angka2)

if operator == "+":
    print(angka1, "ditambah", angka2, "sama dengan", total)
elif operator == "-":
    print(angka1, "dikurang", angka2, "sama dengan", total)
else:
    exit()