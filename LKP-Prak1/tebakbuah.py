import random
list = ["apel", "jeruk", "mangga", "pisang", "durian", "rambutan", "anggur"]

while(True):
    target = random.choice(list)

    nyawa = 5

    for i in range(nyawa):
        tebakan = input("Tebak: ")
        if tebakan == target:
            print("Selamat, jawaban Anda benar!")
            break
        elif tebakan != target:
            print("Salah cuy")
            print("Nyawa Anda tersisa: ", nyawa - 1, "lagi")
            nyawa -= 1
            if nyawa != 0:
                print("Gas maen lagi!")