import random

target = random.randint(0, 9)

for i in range(5):
    tebakan = int(input("Tebak nomor: "))
    if tebakan < target:
        print("Tebakanmu kekecilan")
    elif tebakan > target:
        print("Tebakanmu kegedean")
    else:
        print("GG gaming adick adick")
        exit()
