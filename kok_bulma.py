print("""""""""""""""""""""*********************************
      hesap makinesi programı 
isemler:
1)TOPLAMA
2)ÇIKARMA
3)ÇARPMA
4)BÖLME
5)bölümden kalanın bulunması 
*********************************
""""""""""""""""""""""")

a = int(input("BİRNİCİ SAYIYI GİRİNİZ : "))
b = int(input("İKİNCİ SAYIYI GİRİNİZ : "))
c = input("YAPILMAK İSTENEN İŞLEM BUMARASI")
if c == "1":
 print ("{} il {} in toplamı {} dır.".format(a,b,a+b))
elif c == "2":
     print("{} il {} in sonucu {} dır.".format(a, b, a - b))
elif c == "3":
         print("{} il {} in sonucu {} dır.".format(a, b, a * b))
elif c == "4":
             print("{} il {} in bölümü {} dır.".format(a, b, a / b))
elif c =="5":
    print("{} il {} in kalanı {} dır.".format(a, b, a % b))
else:
    print("hatalı işlem girişi")
