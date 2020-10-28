def ekstra(fonk):
    def wrapper(sayılar):
        çiftler_toplamı = 0
        tekler_toplamı=0
        çift_sayılar =0
        tek_sayılar=0
        for sayı in sayılar:
            if(sayı%2==0):
                çiftler_toplamı+=sayı
                çift_sayılar+=1
            else:
                tekler_toplamı+=sayı
                tek_sayılar+=1
        print("teklerin ortalaması : ",tekler_toplamı/tek_sayılar)
        print("çiftlerin toplamı : ",çiftler_toplamı/çift_sayılar)
        fonk(sayılar)
    return wrapper
@ekstra
def ortalamabul(sayılar):
    toplam=0
    for sayı in sayılar:
        toplam+=sayı
    print("Genel ortalama : ",toplam/len(sayılar))
ortalamabul([1,6,5,8,100,25,1,2,3,4,5,6,7,6,8,155,143,4842,99])

