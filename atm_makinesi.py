print(""""
*************************
ATM PROJESİNE HOŞGELDİNİZ
*************************
YAPABİLECEĞİNİZ İŞLEMLER =
1) BAKİYE SORGULAMA 
2) PARA YATIRMA 
3) PARA ÇEKME 
4) PROGRAMDAN ÇIKIŞ VE KART İADESİ(5) İLE ÇIKIŞ YAPABİLİRSİNİZ
6) FAİZ ORANLARI GÖRNTÜLE
*************************

""")
bakiye = 5500
while True:
    islem =int(input("YAPILACAK İŞLEMİN KOD NUMARASINI GİRİNİZ :"))
    if(islem == 1 ):
        print("bakiye sorgulama",bakiye)
    elif(islem ==2):
        print("yapılan işlem para yatırmadır : ")
        a =int(input("yatırılacak tutaru tl cinsinden giriniz :"))
        bakiye+=a
        print("güncel bakiye : ",bakiye)
    elif(islem == 3):
        print("toplam bakiyeniz 2500 türk lirasının altına inemez...(sözleşme şartı)")
        print("mevcur bakiyeniz : ",bakiye)
        b = int(input("hesabınızdan çekmek istediniz miktarı tl cinsinden yazınız"))
        bakiye -=b
        if(bakiye <=1000):
            print("işlem hacminizi aştınız ")
            bakiye+=b
            continue
        print("güncel bakiye",bakiye)
    elif (islem == 6):
        print("konut kredisi için faiz oranı  %1.1")
        print("araç kredisi için faiz oranı %1.12")
        print("breysel ihtiyaç kredisi için faiz oranı %2,14")

    elif(islem == 5 ):
        print("çıkış yapılıyor")
        break
    else:
        print("hatalı yada yanlış bir tuşlama yaptınız sistem kapatıldı")
        break
