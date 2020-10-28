import random
import time
print(""""******************************
Sayı tahmin oyunu

1  ile 40 arasında sayıyı tahmin edin

(bilgilendirme 1 ve 40 işleme dahil)

oyunu tekrar oynamak için qq e basınız  

******************************
""")

tahmin_hakkı = 7


islem=input("yapılmak istenen işlemi giriniz(qq) yada q")

if(islem == "qq"):
   while True:
        rastgele_sayı = random.randint(1, 40)
        tahmin = int(input("tahmininiz : "))
        if(tahmin>rastgele_sayı):
            print("bilgiler sorgulanıyor ...")
            time.sleep(2)
            print("tahmininiz bulunması gerken sayıdan büyüktür daha küçük bir sayı giriniz...")
            tahmin_hakkı-=1
            print("tahmin hakkınız : ",tahmin_hakkı)
        elif(tahmin < rastgele_sayı):
            print("bilgiler sorgulanıyor")
            time.sleep(2)
            print("tahmininiz bulunması gerekn sayıdan küçüktür daha yüksek bir sayı giriniz...")
            tahmin_hakkı-=1
            print("tahmin hakkınız : ",tahmin_hakkı)
        else:
            print("tahmininiz doğrudur")
            print("tahmininiz = ",tahmin)
            print("bulmanız gereken sayı = ",rastgele_sayı)
            tahmin_hakkı = 7
            time.sleep(5)
            print("tahmin hakkınızı resetledik(güncel tahmin hakınız :)",tahmin_hakkı)
            print("Şehzade gaming iyi oyunlar diler :)")
            break
        if(tahmin_hakkı == 0):
            print("tahmin hakkınız bitmiştir")
            print("sistem tasarımı resetleniyor...")
            time.sleep(2)
            print("tasarım resetlendi")
            break
elif(islem =="q"):
    print("oyun kapatılıyor...")
    time.sleep(2)
    print("lütfen programı işlem sonlanana kadar kapatmayınız.")
    time.sleep(10)
    print(".....")




