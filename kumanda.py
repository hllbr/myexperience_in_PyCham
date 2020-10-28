import random
import time
class kumanda():
    def __init__(self,tv_durum ="kapalı",tv_ses = 0,kanal_listesi=["trt"],kanal="trt"):
        self.tv_durum =tv_durum
        self.tv_ses =tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum =="AÇIK" or self.tv_durum=="açık" or self.tv_durum=="Açık"):
            print("Tv zaten açık durumda")
        else:
            print("Tv açılıyor")
            self.tv_durum ="açık"
    def tv_kapat(self):
        if (self.tv_durum == "KAPALI" or self.tv_durum == "kapalı" or self.tv_durum == "Kapalı"):
            print("televizyon zaten kapalı")
        else:
            print("Tv kapanıyor")
            self.tv_durum="kapalı"
    def ses_ayarları(self):
        while True:
            cevap =input("Sesi azalt(-) arttırmak için (+) çıkış için ise ck yazınız : ")
            if(cevap =="-"):
                if(self.tv_ses !=0):
                    self.tv_ses-=1
                    print("Ses : ",self.tv_ses)
            elif(cevap =="+"):
                if(self.tv_ses!=31):
                    self.tv_ses+=1
            else:
                print("Ses güncellendi",self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("kanal ekleniyor....")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal : ",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return  "Tv Durumu : {}\nTV ses : {}\nKanal listesi : {}\nŞu anki kanal : {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda1 =kumanda()



print(
"""
TV UYGULAMASI
1.TV AÇ
2.TV KAPAT
3.SES AYARALRI
4.KANAL EKLEME
5.KANAL SAYISI ÖĞRENME
6.RASTGELE KANALA GEÇME
7.KUMANDA BİLGİLERİ
8.ÇIKMAK İÇİN Q YADA q YA BASINIZ


""")
while True:
    işlem =input("işlemi seçiniz : ")
    if(işlem =="q" or işlem =="Q"):
        print("program sonlandırılıyor")
        break
    elif(işlem =="1"):
        kumanda1.tv_ac()
    elif(işlem=="2"):
        kumanda1.tv_kapat()
    elif(işlem=="3"):
        kumanda1.ses_ayarları()
    elif(işlem=="4"):
        kanal_isimleri= input("kanal isimlerini ',' ile yazınız : ")
        kanal_listesi =kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda1.kanal_ekle(eklenecekler)
    elif(işlem =="5"):
        print("Kanal Sayısı : ",len(kumanda1))
    elif(işlem =="6"):
        kumanda1.rastgele_kanal()
    elif(işlem=="7"):
        print(kumanda1)
    else:
        print("Geçersiz işlem girişi :(")