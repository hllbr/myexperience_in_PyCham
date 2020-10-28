print(""""*******************************
kullanucu girişi programı
*******************************
""")
sys_kullanıcı_ıd = "hllbr"
sys_parola ="123456"
grs_hak = 3

while True:
    grl_ıd = input("kullanıcı ıd giriniz : ")
    grl_prl = input("parola giriniz : ")
    if (sys_kullanıcı_ıd == grl_ıd and sys_parola != grl_prl):
        print("parola hatalıdır")
        grs_hak -=1
        print("kalan giris hakkınız : ",grs_hak)
    elif(sys_parola != grl_prl and sys_kullanıcı_ıd !=grl_ıd):
        print("kullanıcı adı ve parola hatalı")
        print("parola hatalıdır")
        grs_hak -= 1
        print("kalan giris hakkınız : ", grs_hak)
    elif (sys_parola == grl_prl and sys_kullanıcı_ıd != grl_ıd):
        print("kullanıcı adı hatalıdır ")
        print("parola hatalıdır")
        grs_hak -= 1
        print("kalan giris hakkınız : ", grs_hak)
    else:
        print("işlem başarılıdır")
        grs_hak = 3
        print("giriş resetlendir mevcut hak sayınız tekrar 3 olarak güncellendi",grs_hak)
        continue
    if(grs_hak ==0 ):
        print("giris hakkın bitti program sonlandırılıyor")
        break
