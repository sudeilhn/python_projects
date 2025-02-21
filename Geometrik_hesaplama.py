PI = 3.14

def help():
    print("""
    Program Kullanımı:
    1.Kare Hesaplama: Karenin kenar uzunluğunu girerek alan ve çevresini hesaplayın.
    2.Daire Hesaplama: Dairenin yarıçapını girerek alan ve çevresini hesaplayın.
    3.Dikdörtgen Hesaplama: Uzun ve kısa kenarlarını girerek alan ve çevresini hesaplayın.
    4.Küre Hesaplama: Yarıçapını girerek yüzey alanı ve hacmini hesaplayın.
    5.Yardım Menüsü: Bu menüyü tekrar gösterir.
    6.Çıkış: Programdan çıkış yapar.""")

def kare_hesaplama():
    kenar = input("Karenin bir kenar uzunluğunu  girin:")
    if not kenar.isdigit() or float(kenar) <= 0:
        print("Kenar uzunluğu pozitif bir sayı olmalıdır.")
        return
    kenar=float(kenar)
    kare_alan = kenar * kenar
    kare_cevre = kenar * 4

    print(f"Karenin alanı:{kare_alan}")
    print(f"Krenin çevresi:{kare_cevre}")


def daire_hesaplama():
    r = input("Dairenin yarıçapını girin (r):")
    if not r.isdigit() or float(r) <=0:
        print("Hata: Yarıçap pozitif bir sayı olmalıdır.")
        return
    r=float(r)
    daire_alan = PI * r * r
    daire_cevre = 2 * PI * r

    print(f"Dairenin alanı:{daire_alan}")
    print(f"Dairenin çevresi:{daire_cevre}")


def dikdortgen_hesaplama():
    ukenar = input("Dikgörtgenin uzun kenarını giriniz:")
    kkenar = input("Dikdörtgenin kısa kenarını giriniz:")
    if not ukenar.isdigit() or not kkenar.isdigit() or float(ukenar) <= 0 or float(kkenar) <= 0:
        print("Hata: Kenar uzunlukları pozitif bir sayı olmalıdır.")
        return
    else:
        ukenar=float(ukenar)
        kkenar=float(kkenar)
        dikdörtgen_alan= ukenar * kkenar
        dikdörtgen_cevre= 2 * (ukenar+kkenar)

    print(f"Dikdörtgenin alanı:{dikdörtgen_alan}")
    print(f"Dikdörtgenin çevresi:{dikdörtgen_cevre}")

def kure_hesaplama():
    x = input("Kürenin yarıçapını giriniz:")
    if not x.isdigit() or float(x) <= 0:
        print("Hata: Yarıçap pozitif bir sayı olmalıdır.")
        return
    x=float(x)
    yuzey_alan= 4 * PI * x * x
    hacim= (4/3) * PI * x ** 3

    print(f"Kürenin yüzey alanı:{yuzey_alan}")
    print(f"Kürenin hacmi:{hacim}")

def main_menü():
    help()
    while True:
        print("\n1.Kare Hesaplama"
              "\n2.Daire Hesaplama"
              "\n3.Dikdörtgen Hesaplama"
              "\n4.Küre Hesaplama"
              "\n5.Yardım Menüsü"
              "\n6.Çıkış")
        secim=input("Bir seçim yapınız:")
        if not secim.isdigit() or int(secim) not in range(1,7):
            print("Hata: Lütfen 1 ile 6 arasında bir sayı giriniz: ")
            continue
        secim=int(secim)
        if secim==1:
            kare_hesaplama()
        elif secim==2:
            daire_hesaplama()
        elif secim==3:
            dikdortgen_hesaplama()
        elif secim==4:
            kure_hesaplama()
        elif secim==5:
            help()
        elif secim==6:
            print("---------"
                  "---------"
                  "\nçıkış yapılıyor...")
            break

main_menü()
