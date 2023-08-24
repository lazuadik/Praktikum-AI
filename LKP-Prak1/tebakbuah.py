import random
list = ["apel", "jeruk", "mangga", "pisang", "durian", "rambutan", "anggur"]

target = random.choice(list)

nyawa = 5

for i in range(nyawa):
    tebakan = input("Tebak: ")
    if tebakan == target:
        print("Selamat, jawaban Anda benar!")
        exit()
    elif tebakan != target:
        print("Masih salah nih")
        print("Nyawa Anda tersisa: ", nyawa - 1)
        nyawa -= 1
        if nyawa != 0:
            print("Ayo tebak lagi!")
        else:
            exit()