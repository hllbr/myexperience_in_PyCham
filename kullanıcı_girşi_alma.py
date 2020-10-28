print(""""
****************************************************
KULLANICI GİRŞİ PROGRAMI
****************************************************
""")
sys_kullanıcı_ıd = "hllbr"
sys_parola ="123456"
grln_ıd =input("kullanıcı adını giriniz")
grln_prl =input("paswword pls")
if(grln_ıd == sys_kullanıcı_ıd and grln_prl == sys_parola):
    print("giriş işlemi başarılı")
elif(grln_ıd != sys_kullanıcı_ıd or grln_prl !=sys_parola ):
    print("nereye hemşerim")
else:
    print("potato qnqs yanlış emcuğa çaktun dostum")