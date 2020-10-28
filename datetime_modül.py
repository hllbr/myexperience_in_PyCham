from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"")#SONUCU BULUNDUĞUN YERİN DİLİNE ÇEVİRMEK İÇİN KULLANABİLECEĞİN BİR YAPI
su_an =datetime.now()
print(su_an.year)
print(su_an.month)
print(su_an.microsecond)
print(su_an.hour)
print(datetime.ctime(su_an))
print(datetime.strftime(su_an,"%y "))#yıl
print(datetime.strftime(su_an,"%D"))#gün
print(datetime.strftime(su_an,"%B"))#ay
print(datetime.strftime(su_an,"%Y %B"))#AY VE YIL BİRLİKTE ALINABİLİYOR
print(datetime.strftime(su_an,"%Y %B %A"))
bu_an =datetime.now()
saniye =datetime.timestamp(bu_an)
print(saniye)
bu_an =datetime.fromtimestamp(0)
print(bu_an)
tarih = datetime(1996,3,25)
bu_an=datetime.now()
print((bu_an-tarih))

