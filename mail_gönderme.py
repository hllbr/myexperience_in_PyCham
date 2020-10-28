import smtpd
import smtplib
from email.mime.multipart import MIMEMultipart
#üst kısım mesaj gövdemizi oluşturuyor
from email.mime.text import MIMEText
#mailde ne yazacağıı belirleyeceğimiz kısım iste üst satırdaki komut ile oluyor
import sys
#ekrana hata mesajlarımızı sys ile yazdırıyoruz
mesaj = MIMEMultipart()
#BİR MAİL YAPISI OLUŞTURDUK
mesaj["From"] = "halibrahim.kocak@gmail.com"
#kim gönderiyor mesajı
mesaj["To"]= "halibrahim.kocak@gmail.com"
#kime gidecek
mesaj["Subject"]= "Stmp ile  Mail gönderme"
#mailin konusunu oluşturduk bu yapıyla
#gövde oluşturuyoruz şimdide
yazı ="""
Stmp ile mail gönderiyorum 
 I am a developer 
 ı need a business case of ı will be champion's world
 ı hope I'll be best of one in the earth
 maybe you need not me yet however you have been need me case of ı am hllbr 
 HLLBR is price of OE
 hllbr is a prince of sultan second ABDULHAMİT

 
  
"""
#mesajımızın gövdesi =
mesaj_gövdesi = MIMEText(yazı,"plain")
mesaj.attach(mesaj_gövdesi)
#şimdi gmail serverlerına bağlanmamız gerekiyor lakin bazı sorunlar meydana gelebilir
#sunucuya bağlanamama sunucu çökmesi mesajın gitmemesi gibi
#bu durumlar için try yapısı kullanmak iyi oluyor
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("mail","şifre")
    #buraya kadar mesajı oluşturk kime gidecek konusu ne içeriği yazıldı kimden gideceği yazıldı
    #burdan sonra maili gönderme işlemi için gereken clic işlemlerini gerçekleştiriyor olucaz
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print(("mail başarıyla gönderildi"))
    mail.close()
except:
    sys.stderr.write("bir hata oluştu ")
    sys.stderr.flush()

