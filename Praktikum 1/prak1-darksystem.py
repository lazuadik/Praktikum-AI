match = int(input("Berapa match dalam 29 jam terakhir: "))
win = int(input("Berapa kali menang dalam 29 jam terakhir: "))

winrate = (win/match * 100)

if winrate <= 50:
    print("Sebaiknya isitrahat dulu")
elif winrate > 50:
    print("Silakan bermain")