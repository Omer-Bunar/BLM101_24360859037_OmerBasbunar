# MANTIK KAPILARI VE DOĞRULUK TABLOSU PROJESİ
print("--- SANAL MANTIK DEVRESİ SİMÜLATÖRÜ ---")
print("1. Mantık Kapısı Hesapla (AND, OR, NOT, XOR)")
print("2. Doğruluk Tablosu Oluştur")
print("---------------------------------------------")

secim = input("Yapmak istediğiniz işlemi seçin (1 veya 2): ")

# --- 1. Seçenek: Mantık kapısı hesaplama ---
if secim == "1":
    print("\n--- MANTIK KAPISI HESAPLAMA MODU ---")
    
    # Girişleri alıyoruz
    giris1 = input("Birinci değeri girin (0 veya 1): ")
    giris2 = input("İkinci değeri girin (0 veya 1): ")
    
    # Girilen değerlerin 0 veya 1 olup olmadığına bakın
    if (giris1 == "0" or giris1 == "1") and (giris2 == "0" or giris2 == "1"):
        # İşlem yapabilmek için sayıya çeviriyorum
        a = int(giris1)
        b = int(giris2)
        
        kapi = input("Kapı türünü yazın (AND, OR, NOT, XOR): ")
        
        # Sonuç değişkenini başlangıçta sıfır yaptım.
        sonuc = 0
        
        if kapi == "AND" or kapi == "and":
            sonuc = a and b
            print("SONUÇ:", a, "AND", b, "=", sonuc)
            
        elif kapi == "OR" or kapi == "or":
            sonuc = a or b
            print("SONUÇ:", a, "OR", b, "=", sonuc)
            
        elif kapi == "XOR" or kapi == "xor":
            # XOR kapısı mantığı: Girişler farklıysa 1, aynıysa 0 olur
            if a != b:
                sonuc = 1
            else:
                sonuc = 0
            print("SONUÇ:", a, "XOR", b, "=", sonuc)

        elif kapi == "NOT" or kapi == "not":
            # NOT kapısı sadece tek girişle çalışır (Tersini alır.1 ise 0 gösterir. 0 ise 1.)
            # Bu yüzden sadece 1. sayıya (a) bakarız.
            if a == 0:
                sonuc = 1
            else:
                sonuc = 0
            print("SONUÇ: NOT", a, "=", sonuc, "(İkinci sayı kullanılmaz)")
            
        else:
            print("HATA: Geçersiz kapı ismi! (AND, OR, NOT, XOR yazın)")
            
    else:
        print("HATA: Lütfen sadece 0 veya 1 giriniz!")


# ---2. Seçenek: Doğruluk tablosu (A AND (B OR C)) ---
elif secim == "2":
    print("\n--- 3 Değişkenli Doğruluk Tablosu ---")
    print("İfade: F = A AND (B OR C)") 
    print("-----------------------------------")
    print(" A | B | C | SONUÇ ")
    print("-----------------------------------")

    # Tüm ihtimaller için iç içe döngüler
    for a in range(2):
        for b in range(2):
            for c in range(2):
                
                # Ödevde istenen formül: A AND (B OR C)
                islem_sonucu = a and (b or c)
                
                # Sonuçları ekrana yazdırma (Virgüllü yöntem)
                print(" ", a, "|", b, "|", c, "|   ", int(islem_sonucu))

else:
    print("Yanlış seçim yaptınız. Lütfen programı tekrar çalıştırın.")