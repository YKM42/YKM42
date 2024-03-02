#=======================================#
#-          Adam Asmaca v2.3.17        -#
#-    Programmer: Yusuf Kerem Muştu    -#
#-            February 2024            -#
#=======================================#

import random
import time
#import os
seri=0
kazanma=0
def full_oyun():
    alfabe=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w","q","x"]
    def kelime_yazma(kelime,dogru_tahminler,tahminler,gorsel_numara):
        gorsel=[
                """ 
                  _____________
                  |          O 
                  |            
                  |
                  |
                 _|_      
                """
            
                ,
                 
                 """
                  _____________
                  |          O 
                  |          |
                  |          |  
                  |
                 _|_   
                 """
                ,
                """
                  _____________
                  |          O 
                  |          |\\
                  |          |  
                  |
                 _|_   
                 """
                ,
                """
                  _____________
                  |          O 
                  |         /|\\
                  |          |  
                  |
                 _|_
                """   
                 ,
                 """
                  _____________
                  |          O 
                  |         /|\\
                  |          |  
                  |           \\
                 _|_  
                 """
                 ,
                 """
                  _____________
                  |          O 
                  |         /|\\
                  |          |  
                  |         / \\
                 _|_
                """ 
                  ]
        print(gorsel[gorsel_numara],"\n")
        for i in range(0,len(kelime)):
            if kelime[i] in tahminler:
                print(kelime[i],end=" ")
                dogru_tahminler[i]=kelime[i]
            elif kelime[i]==" ":
                print("_",end=" ")
            else:
                print("*",end=" ")
    def bilgi():
        print("\n============================================================")
        print("""
              Adam asmaca, aklınızı ve kelime hazinenizi geliştiren bir oyundur.
              *Oyundaki amaç belirlenen kelimedeki harfleri tahmin ederek kelimeyi bulmaktır.
              *Her yanlış harf veya tahmin girdiğinizde bir canınız gider ve adamın bir kısmı asılır.
              *Canınız biterse oyunu kaybedersiniz.
              *Oyundaki \"tekrar\" komutu ile başlangıca (Oyun türü seçimi) dönebilirsiniz.
              *Oyundaki \"tahmin\" komutu ile tam kelimeyi tahmin edebilirsiniz.
              *Adam asmacayı klasik oyun ve ikili oyun olarak oynayabilirsiniz.
              Klasik Oyun:
              *Kelimeler önceden belirlenmiştir.
              *İstediğiniz kategoriden (hayvan bitki vb.) kelime seçebilirsiniz.
              *Her oyun kazandığınızda kazanma seriniz ve toplam kazanma sayınız artar. 
              *Bir oyun kaybettiğinizde kazanma sayınız değişmez fakat kazanma seriniz sıfıra iner.
              İkili Oyun:
              *İki kişi ile oynanır.
              *Sırayla bir kişi kelimeleri yazar, diğeri bilmeye çalışır.
              *En çok kelimeyi bilen kazanır.
              *Not:Kelime yazarken büyük harf kullanmayın.
              İyi eğlenceler!
              """)
        print("============================================================")        
    def ana_oyun(can,kelime,dogru_tahminler,tahminler,gorsel_numara,str_kelime,onay):
        while (can>0):
            secilen=input("\nHarf giriniz veya tam kelime tahmini için \"tahmin\" yazınız: ")
            if secilen=="bilgi":
                bilgi()
                devam=input("Oyuna devam etmek istediğinizde enter tuşuna basınız.")
                print("\n============================================================")
                if not devam:
                    kelime_yazma(kelime, dogru_tahminler, tahminler , gorsel_numara)
                    continue
            if secilen=="tekrar":
                print("\n============================================================")
                onay=input("Başlangıca dönmek istediğinizden eminseniz enter tuşuna basın. Oyuna devam etmek istiyorsanız \"-\" tuşuna basabilirsiniz. ")
                if not onay:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        baslangic()
                else:
                    continue
            if not secilen:
                print("Bu kısım boş geçilemez.")
                continue
            if secilen=="tahmin":
                print("\n============================================================")
                kelime_tahmin=input("Kelime tahmininizi yazınız: ")
                if kelime_tahmin==str_kelime:
                    break
                else:
                    can-=1
                    gorsel_numara+=1
                    print("\n============================================================")
                    print("Maaalesef doğru cevap ",kelime_tahmin," değil. Canınız:",can)
                    kelime_yazma(kelime,dogru_tahminler,tahminler,gorsel_numara)
            else:
                if secilen in tahminler:
                    print("\n============================================================")
                    print("Zaten ",secilen," harfini kullandınız")
                    kelime_yazma(kelime,dogru_tahminler,tahminler,gorsel_numara)
                else:    
                    if secilen in alfabe:
                        tahminler+=secilen
                        if secilen in kelime:
                            print("\n============================================================")
                            kelime_yazma(kelime,dogru_tahminler,tahminler,gorsel_numara)
                        else:
                            
                            can-=1
                            gorsel_numara+=1
                            print("\n============================================================")
                            print("Maaalesef ",secilen," harfi kelimede yok. Canınız:",can)
                            kelime_yazma(kelime,dogru_tahminler,tahminler,gorsel_numara)
                    else:
                        print("\n============================================================")
                        print("Geçerli bir harf ya da tahmin girin.")
                        kelime_yazma(kelime,dogru_tahminler,tahminler,gorsel_numara)
            if dogru_tahminler==kelime:
                break
                
                
        if can==0:
            return 0
        if can>0:
            return 1
    def dogru_tahminler_yapma(kelime):
        dogru_tahminler_yapma=[]
        for i in range(0,len(kelime)):
             dogru_tahminler_yapma.append(" ")
        return dogru_tahminler_yapma
    def str_kelime_yapma(kelime):
        str_kelime_yapma=""
        for i in range (0,len(kelime)):
            str_kelime_yapma+=kelime[i]
        return str_kelime_yapma
    def ikili_oyun_kazandin01(kazandin,str_kelime,kazanma12):
        if kazandin==0:
             print("\n============================================================")
             print("\nMaalesef kaybettiniz :( ")
             print("Doğru cevap: ",str_kelime)
             print("Kazanma sayınız:",kazanma12)
             while True:
                 devam=input("Devam etmek için enter tuşuna basın.")
                 if not devam:
                     break
                 else:
                     print("Enter tuşuna basmalısınız")
                     continue
             
        if kazandin==1:
             kazanma12+=1
             print("\n============================================================")
             print("\nTebrikler, bildiniz!")
             print("Kazanma sayınız:",kazanma12)
             while True:
                 devam=input("Devam etmek için enter tuşuna basın.")
                 if not devam:
                     break
                 else:
                     print("Enter tuşuna basmalısınız")
                     continue
        return kazanma12
    def adam_asmaca_ikilik(alfabe):
       kazanma1=0
       kazanma2=0
       print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
       sayi=int(input("Kaç kelimelik olsun?(3 tavsiye edilir.) "))
       bir_oyuncu=input("Birinci oyuncunun ismini giriniz: ")
       iki_oyuncu=input("İkinci oyuncunun ismini giriniz: ")
       kelimeler1=[]
       kelimeler2=[]
       for i in range (sayi):
           soru=input("{0} {1}. kelimeyi girebilirsin.(Diğer oyuncu tahmin edecek. Lütfen büyük harf kullanma.): ".format(bir_oyuncu,i+1))
           kelimeler1.append(list(soru))
       print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
       for i in range(sayi):
           kelime=list(kelimeler1[i])
           tahminler=""
           onay=""
           gorsel_numara=0
           can=5
           kazandin=0
           dogru_tahminler=dogru_tahminler_yapma(kelime)
           str_kelime=str_kelime_yapma(kelime)
           print(iki_oyuncu,"tahmin etmeye başlayabilirsin.")
           print("\n============================================================")
           kelime_yazma(kelime, dogru_tahminler, tahminler, gorsel_numara)
           print("\n")
           kazandin=ana_oyun(can, kelime, dogru_tahminler, tahminler, gorsel_numara, str_kelime, onay)
           kazanma2=ikili_oyun_kazandin01(kazandin, str_kelime, kazanma2)
           
       for i in range (sayi):
           soru=input("{0} {1}. kelimeyi girebilirsin.(Diğer oyuncu tahmin edecek. Lütfen büyük harf kullanma.): ".format(iki_oyuncu,i+1))
           kelimeler2.append(list(soru))
       print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
       for i in range(sayi):
           kelime=list(kelimeler2[i])
           tahminler=""
           onay=""
           gorsel_numara=0
           can=5
           kazandin=0
           dogru_tahminler=dogru_tahminler_yapma(kelime)
           str_kelime=str_kelime_yapma(kelime)
           print(bir_oyuncu,"tahmin etmeye başlayabilirsin.")
           print("\n============================================================")
           kelime_yazma(kelime, dogru_tahminler, tahminler, gorsel_numara)
           print("\n")
           kazandin=ana_oyun(can, kelime, dogru_tahminler, tahminler, gorsel_numara, str_kelime, onay)
           kazanma1=ikili_oyun_kazandin01(kazandin, str_kelime, kazanma1)
       if kazanma1==kazanma2:
           print("----------------------------------------")
           print("Beraberlik!")
           print("----------------------------------------")
       elif kazanma1>kazanma2:
           print("----------------------------------------")
           print(bir_oyuncu," kazandı!")
           print("----------------------------------------")
       elif kazanma2>kazanma1:
           print("----------------------------------------")
           print(iki_oyuncu," kazandı!")
           print("----------------------------------------")
       menu=input("Tekrar ikili türünde oynamak için \"enter\" tuşuna, başlangıca dönmek için \"b\" tuşuna, oyunu kapatmak için \"-\" tuşuna basın.")
       if not menu:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                adam_asmaca_ikilik(alfabe)
       elif menu=="-":
        print("İyi günler!")
        time.sleep(3)
        raise SystemExit()
       elif menu=="b":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                baslangic()     
    def adam_asmaca_klasik(seri,kazanma,alfabe):
        

        kelimeler_bilisim=["robot", "teknoloji", "bilgisayar", "kod", "yazılım", "yapay zeka", "algoritma", "değişken"]
        kelimeler_bitki=["elma", "gül", "papatya", "meşe", "patlıcan", "armut", "gürgen", "bezelye", "palamut", "akasya", "kayısı"]
        kelimeler_sehir=["konya", "kayseri", "istanbul", "ankara", "mardin", "gümüşhane", "trabzon", "izmir", "adana", "denizli", "ısparta", "çorum", "erzurum"]
        kelimeler_hayvan=["ayı", "eşek", "aslan", "martı", "arı", "kedi", "köpek", "balina", "pirana", "kaplan", "geyik", "bülbül", "zebra", "piton"]
        kelimeler_zor=["kapitülasyon", "halüsinasyon", "hissikablelvuku", "spekülasyon", "profiterol", "klostrofobi", "distribütör", "muvafakatname", "ropdöşambır"]
        kelimeler_tum=["robot", "teknoloji", "bilgisayar", "kod", "yazılım", "yapay zeka", "algoritma", "değişken","elma", "gül", "papatya", "meşe", "patlıcan", "armut", "gürgen", "bezelye", "palamut", "akasya", "kayısı","konya", "kayseri", "istanbul", "ankara", "mardin", "gümüşhane", "trabzon", "izmir", "adana", "denizli", "ısparta", "çorum", "erzurum","ayı", "eşek", "aslan", "martı", "arı", "kedi", "köpek", "balina", "pirana", "kaplan", "geyik", "bülbül", "zebra", "piton","kapitülasyon", "halüsinasyon", "hissikablelvuku", "spekülasyon", "profiterol", "klostrofobi", "distribütör", "muvafakatname", "ropdöşambır"]
        tahminler=""
        basla=""
        onay=""
        gorsel_numara=0
        can=5
        kazandin=0
        
        
        print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        #time.sleep(0.5)
        while True:
            kategori=input("Lütfen kategori seçiniz(bilişim, bitki, hayvan, şehir, zor, hepsi): ")
            if kategori=="bilişim":
                kelime=list(random.choice(kelimeler_bilisim))
                break
            elif kategori=="bitki":
                kelime=list(random.choice(kelimeler_bitki))
                break
            elif kategori=="şehir":
                kelime=list(random.choice(kelimeler_sehir))
                break
            elif kategori=="hayvan":
                kelime=list(random.choice(kelimeler_hayvan))
                break
            elif kategori=="hepsi":
                kelime=list(random.choice(kelimeler_tum))
                break
            elif kategori=="zor":
                kelime=list(random.choice(kelimeler_zor))
                break
            elif kategori=="bilgi":
                bilgi()
                devam=input("Oyuna devam etmek istediğinizde enter tuşuna basınız.")
                if not devam:
                    continue
            else:
                print("Lütfen geçerli bir kategori ismi girin.")
                continue
        dogru_tahminler=dogru_tahminler_yapma(kelime)
        str_kelime=""
        for i in range (0,len(kelime)):
            str_kelime+=kelime[i]
        print("\n============================================================")
        kelime_yazma(kelime, dogru_tahminler, tahminler, gorsel_numara) 
        print("\n")
        
        kazandin=ana_oyun(can,kelime,dogru_tahminler,tahminler,gorsel_numara,str_kelime,onay)
        
        
        if kazandin==0:
            seri=0
            print("\n============================================================")
            print("\nMaalesef kaybettiniz :( ")
            print("Doğru cevap: ",str_kelime,)
            print("Kazanma seriniz:0")
            print("Toplam kazanma sayınız:",kazanma)
            basla=input("Tekrar klasik türde oynamak için \"enter\" tuşuna, başlangıca dönmek için \"b\" tuşuna, oyunu kapatmak için \"-\" tuşuna basın.")
            if basla=="b":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                baslangic()
            elif not basla:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                #os.system('cls')
                #time.sleep(1)
               # print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                adam_asmaca_klasik(seri,kazanma,alfabe)
            elif basla=="-":
                print("İyi günler!")
                time.sleep(3)
                raise SystemExit()
            else:
                print("İyi günler!")
                time.sleep(3)
                raise SystemExit
            
        if kazandin==1:
            seri+=1
            kazanma+=1
            print("\n============================================================")
            print("\nTebrikler, bildiniz!")
            print("Kazanma seriniz:",seri)
            print("Toplam kazanma sayınız:",kazanma)
            basla=input("Tekrar klasik türde oynamak için \"enter\" tuşuna, başlangıca dönmek için \"b\" tuşuna, oyunu kapatmak için \"-\" tuşuna basın.")
            if basla=="b":
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                baslangic()
            elif not basla:
                #os.system("cls")
                #time.sleep(1)
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                adam_asmaca_klasik(seri,kazanma,alfabe)
            elif basla=="-":
                print("İyi günler!")
                time.sleep(3)
                raise SystemExit
            else:
                print("İyi günler!")
                time.sleep(3)
                raise SystemExit
    def baslangic():
        while True:
            baslangic=input("\nOyun türü seçiniz (klasik, ikili) veya \"bilgi\" yazınız: ")
            if baslangic=="bilgi":
                bilgi()
                enter=input("Devam etmek için \"enter\" tuşuna basın.")
                if not enter:
                    continue
            elif baslangic=="klasik":
                adam_asmaca_klasik(seri,kazanma,alfabe)
                break
            elif baslangic=="ikili":
                adam_asmaca_ikilik(alfabe)
                break
            else:
                print("Yanlış tür girdiniz.")
    print("Adam asmaca oyununa hoşgeldiniz! \nEğer oyun hakkında detaylı bilgi almak isterseniz \"bilgi\" yazmanız yeterlidir.")
    baslangic()
full_oyun()
