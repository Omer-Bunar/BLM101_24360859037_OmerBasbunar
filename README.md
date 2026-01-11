# BLM101_24360859037_OmerBasbunar
BLM101 Ders Projesi
# Proje Raporu: Veri Manipülasyonu ve Mantık Kapıları

**Ders:** Bilgisayar Mimarisi
**Konu:** Mantık Kapıları ve Doğruluk Tablosu

### 1. Projenin Amacı
Bu ödevde, derste işlediğimiz temel mantık kapılarının (AND, OR, NOT, XOR) çalışma mantığını Python diliyle simüle eden bir program yazdım. Amacım, kullanıcının seçtiği kapıya göre işlem yapan ve istenilen özel bir mantıksal ifadenin doğruluk tablosunu otomatik oluşturan bir araç geliştirmekti.

### 2. Kodun Çalışma Mantığı
Programı yazarken hazır kütüphaneler kullanmak yerine, konuyu daha iyi kavramak için temel algoritma yapılarını (if-else, döngüler) tercih ettim. Program iki ana bölümden oluşuyor:

#### Bölüm A: Hesaplama Modülü
Burada kullanıcıdan iki adet giriş (0 veya 1) alıyorum. 
* **Veri Kontrolü:** Kullanıcının hatalı giriş yapmasını engellemek için, girilen değerlerin "0" veya "1" olup olmadığını `if` bloklarıyla kontrol ettim.
* **AND Kapısı:** Python'un `and` operatörünü kullandım. Mantık gereği, her iki giriş de 1 ise sonuç 1 çıkar, diğer durumlarda 0 olur.
* **OR Kapısı:** Python'un `or` operatörünü kullandım. Girişlerden en az birinin 1 olması sonucun 1 olması için yeterli.
* **XOR Kapısı:** Python'da hazır operatör olsa da, XOR'un mantığını (girişler farklıysa 1, aynıysa 0) göstermek için `if a != b` (Eşit Değilse) mantığını kurdum.
* **NOT Kapısı:** NOT kapısı tek girişli olduğu için, bu seçenek seçildiğinde program ikinci sayıyı dikkate almıyor, sadece ilk sayının tersini alıyor.

#### Bölüm B: Doğruluk Tablosu
Ödevde belirtilen **F = A AND (B OR C)** ifadesinin tablosunu oluşturmak için iç içe 3 tane `for` döngüsü kullandım.
* Bu yazdığım döngüler A, B ve C'nin alabileceği tüm değerleri (0 ve 1) sırasıyla deniyor.
* Her adımda formülü hesaplayıp sonucu ekrana tablo formatında yazdırıyor.

### 3. Neden Bu Yöntemi Seçtim?
Kodun herkes tarafından anlaşılabilir olması ve dersin içeriğine uygun olması için bit farklı operatörler veya karmaşık fonksiyonlar yerine, adım adım işleyen bir yapı kurdum. Bu sayede program hem hatasız çalışıyor hem de mantık kapılarının çalışma prensibini açıkça gösteriyor.
PROJE VİDEOSU YOUTUBE LİNKİ https://youtu.be/4w85UWltXgg
