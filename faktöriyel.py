from time import sleep

print("faktöriyel bulma prigramı")
print("hoş geldiniz")
print("""yapabileceğiniz işlemler çıkış için 2
      *******************
      faktöriyel alma işlemi için ise 1 tuşuna basınız
      """)
while True:
    print("program başlatılıyor...")
    print("program başlatıldı")
    a = int(input("yapılacak işlemi seciniz"))
    if(a == 2):
        print("program sonlandırılıyor")
        sleep(2.4)
        print("program sonlandırıldı")
        break
    elif(a == 1):
        sayı =int(input("faktöriyelini alma istediğiniz sayıyı giriniz : "))
        fakto = 1
        for i in range(2,sayı+1):
            print("Faktoriyel : ",fakto,"İ :",i)
            fakto*=i
            sleep(1.14)
            print("Faktoriyel sonucunuz : ",fakto)
    else:
        print("hatalı veya yanlış işlem girişi yaptınız lütfen input değerlerinizi kontrol ediniz")
        print("iyi günler dileriz")
        sleep(5.10)
        print("program sonlandırıldı")
        continue