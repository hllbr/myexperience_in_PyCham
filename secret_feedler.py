def  tambolenler_bulma(sayı):
    tam_bolenler = []
    for i in range(2,sayı):
        if (sayı % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler
while True:
    sayı = input("sayı : ")
    if (sayı == "q"):
        print("program sonlanrılıyor")
        break
    else:
        sayı = int(sayı)
        print("tam bölenler : ", tambolenler_bulma(sayı))
