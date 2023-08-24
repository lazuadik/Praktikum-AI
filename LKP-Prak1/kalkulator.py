while(True):
    angka1 = input()
    operator = input()
    angka2 = input()
    
    angka1 = int(angka1)
    angka2 = int(angka2)

    if operator == "+":
        print(angka1, "ditambah", angka2, "sama dengan", angka1 + angka2)
    elif operator == "-":
        print(angka1, "dikurang", angka2, "sama dengan", angka1 - angka2)