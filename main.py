import string
# Tahtadaki yatay çizgilerin sayısı ve sütunların etiketlenmesinde kullanılan harfler için sabitler
EN_AZ_YATAY_CIZGI = 4
EN_FAZLA_YATAY_CIZGI = 8
HARFLER = list(string.ascii_uppercase[:EN_FAZLA_YATAY_CIZGI + 1])

OYUNCU_YOK_TAS = " "
TABLO_SATIR_CIZGI = "-------"
TABLO_SUTUN_CIZGI = "|"


def satir_sutun_hesapla(tahta_matris):# Tahtadaki satır ve sütun sayısını hesapla
    satir_sayi = len(tahta_matris)
    sutun_sayi = len(tahta_matris[0])
    return satir_sayi, sutun_sayi

# Tahtayı çiz
def tahta_ciz(oyun_matris):
    satir_sayisi, sutun_sayisi = satir_sutun_hesapla(oyun_matris)
    print(" " * 6, end="")
    for harf in HARFLER[:sutun_sayisi]:
        print(harf, end="")
        print(" " * 6, end="")
    print()
    for satir in range(satir_sayisi):
        print("  ", TABLO_SATIR_CIZGI * satir_sayisi)
        print(satir + 1, TABLO_SUTUN_CIZGI, end="")

        for sutun in range(sutun_sayisi):
            print(" ", oyun_matris[satir][sutun], " ", TABLO_SUTUN_CIZGI, end="")

        print(" ", satir + 1)

    print("  ", TABLO_SATIR_CIZGI * satir_sayisi)
    print(" " * 6, end="")
    for harf in HARFLER[:sutun_sayisi]:
        print(harf, end="")
        print(" " * 6, end="")
    print()


def tas_yerlestir(oyun_matris, oyuncu1tas, oyuncu2tas):#oyun tahtasına başlangıç konumuna taşları yerleştirirme
    for i in range(len(oyun_matris[0])):
        for j in range(len(oyun_matris[0])):
            if i == 0:
                oyun_matris[i][j] = oyuncu1tas
            if i == len(oyun_matris[0]) - 1:
                oyun_matris[i][j] = oyuncu2tas


def konuma_cevir(harf_kodu, oyun_matris): #girilen konumu sayı olan konuma çevirme
    satir_sayisi, sutun_sayisi = satir_sutun_hesapla(oyun_matris)
    try:
        satir_no = int(harf_kodu[0]) - 1
        sutun_no = HARFLER.index(harf_kodu[1])
        if 0 <= satir_no <= satir_sayisi and 0 <= sutun_no <= sutun_sayisi and len(harf_kodu) == 2:
            return satir_no, sutun_no
    except(ValueError, TypeError, IndexError):
        print("Lütfen geçerli bir konum giriniz! ")


def hareket_konum_al_tas_ekle(oyun_matris, oyuncu):#hareket konumunu alıp taşları hareket ettirme fonksiyonu
    while True:
        try:
            konum = input(f"{oyuncu} için hareket ettirilecek taşın konumunu ve hedef konumu giriniz: ").upper().split(
                " ")
            mevcut_konum = konuma_cevir(konum[0], oyun_matris)
            hedef_konum = konuma_cevir(konum[1], oyun_matris)

            if oyun_matris[mevcut_konum[0]][mevcut_konum[1]] != oyuncu:
                print("Kendi taşınızı oynatanilirsiniz!")
                continue

            if len(mevcut_konum) != 2 or len(hedef_konum) != 2:
                print("Geçersiz konum girişi")
                continue
            else:

                if mevcut_konum[0] == hedef_konum[0]:

                    if mevcut_konum[1] > hedef_konum[1]:
                        for i in range(mevcut_konum[1] - 1, hedef_konum[1] - 1, -1):
                            if oyun_matris[mevcut_konum[0]][i] != OYUNCU_YOK_TAS:
                                print("Yerleştirmek istediğiniz taşın konumu dolu!")
                                break
                        else:
                            oyun_matris[mevcut_konum[0]][mevcut_konum[1]] = OYUNCU_YOK_TAS
                            oyun_matris[hedef_konum[0]][hedef_konum[1]] = oyuncu
                            break

                    else:
                        for i in range(mevcut_konum[1] + 1, hedef_konum[1] + 1):
                            if oyun_matris[mevcut_konum[0]][i] != OYUNCU_YOK_TAS:
                                print("Yerleştirmek istediğiniz taşın konumu dolu!")
                                break
                        else:
                            oyun_matris[mevcut_konum[0]][mevcut_konum[1]] = OYUNCU_YOK_TAS
                            oyun_matris[hedef_konum[0]][hedef_konum[1]] = oyuncu
                            break

                elif mevcut_konum[1] == hedef_konum[1]:

                    if mevcut_konum[0] > hedef_konum[0]:
                        for i in range(mevcut_konum[0] - 1, hedef_konum[0] - 1, -1):
                            if oyun_matris[i][mevcut_konum[1]] != OYUNCU_YOK_TAS:
                                print("Yerleştirmek istediğiniz taşın konumu dolu!")
                                break
                        else:
                            oyun_matris[mevcut_konum[0]][mevcut_konum[1]] = OYUNCU_YOK_TAS
                            oyun_matris[hedef_konum[0]][hedef_konum[1]] = oyuncu
                            break

                    else:
                        for i in range(mevcut_konum[0] + 1, hedef_konum[0] + 1):
                            if oyun_matris[i][mevcut_konum[1]] != OYUNCU_YOK_TAS:
                                print("Yerleştirmek istediğiniz taşın konumu dolu!")
                                break
                        else:
                            oyun_matris[mevcut_konum[0]][mevcut_konum[1]] = OYUNCU_YOK_TAS
                            oyun_matris[hedef_konum[0]][hedef_konum[1]] = oyuncu
                            break
                else:
                    print("Çapraz hareket yok")

        except(IndexError, TypeError, ValueError):
            print("Geçersiz konum girişi!")
    return hedef_konum


def tas_sil(oyun_matris, satir_sutun, oyuncu):#taş silme fonksiyonu
    for i in range(satir_sutun):
        for j in range(satir_sutun - 2):
            if oyun_matris[i][j] == oyuncu == oyun_matris[i][j + 2] and oyun_matris[i][j + 1] != oyuncu and oyun_matris[i][j + 1] != OYUNCU_YOK_TAS:
                oyun_matris[i][j + 1] = OYUNCU_YOK_TAS
                print(i + 1, HARFLER[j + 1], " konumundaki taş kitlendi")
                tahta_ciz(oyun_matris)
    for i in range(satir_sutun - 2):
        for j in range(satir_sutun):
            if oyun_matris[i][j] == oyuncu == oyun_matris[i + 2][j] and oyun_matris[i + 1][j] != oyuncu and oyun_matris[i + 1][j] != OYUNCU_YOK_TAS:
                oyun_matris[i + 1][j] = OYUNCU_YOK_TAS
                print(i + 1, HARFLER[j + 1], " konumundaki taş kitlendi")
                tahta_ciz(oyun_matris)
    for i in range(satir_sutun):
        for j in range(satir_sutun):
            if i == 0 and j == 0:
                if oyun_matris[i][j] != OYUNCU_YOK_TAS and oyun_matris[i][j] != oyuncu and oyun_matris[i][j + 1] == oyuncu and oyun_matris[i + 1][j] == oyuncu:
                    oyun_matris[i][j] = OYUNCU_YOK_TAS
                    print(i + 1, HARFLER[j + 1], " konumundaki taş kitlendi")
                    tahta_ciz(oyun_matris)
            if i == 0 and j == satir_sutun - 1:
                if oyun_matris[i][j] != OYUNCU_YOK_TAS and oyun_matris[i][j] != oyuncu and oyun_matris[i][j - 1] == oyuncu and oyun_matris[i + 1][j] == oyuncu:
                    oyun_matris[i][j] = OYUNCU_YOK_TAS
                    print(i+1, HARFLER[j+1], " konumundaki taş kitlendi")
                    tahta_ciz(oyun_matris)
            if i == satir_sutun - 1 and j == 0:
                if oyun_matris[i][j] != OYUNCU_YOK_TAS and oyun_matris[i][j] != oyuncu and oyun_matris[i - 1][j] == oyuncu and oyun_matris[i][j + 1] == oyuncu:
                    oyun_matris[i][j]=OYUNCU_YOK_TAS
                    print(i+1, HARFLER[j+1], " konumundaki taş kitlendi")
                    tahta_ciz(oyun_matris)
            if i == satir_sutun - 1 and j == satir_sutun - 1:
                if oyun_matris[i][j] != OYUNCU_YOK_TAS and oyun_matris[i][j] != oyuncu and oyun_matris[i][j - 1] == oyuncu and oyun_matris[i - 1][j] == oyuncu:
                    oyun_matris[i][j] = OYUNCU_YOK_TAS
                    print(i+1, HARFLER[j+1], " konumundaki taş kitlendi")
                    tahta_ciz(oyun_matris)
def tas_hesapla(oyun_matris,oyuncu,satir_sutun):# rakip oyuncuncunun taşlarını hesaplama fonksiyonu
    rakip_tas_say = 0
    for i in range(satir_sutun):
        for j in range(satir_sutun):
            if oyun_matris[i][j] != oyuncu and oyun_matris[i][j] != OYUNCU_YOK_TAS:
                rakip_tas_say +=1
    return rakip_tas_say


def main():
    devam = "e"
    while devam == "e" or devam == "E":
        while True:
            try:
                satir_sutun = int(input("Lütfen tablonun satır/sutun sayısını girin: "))#satır sutun sayısının alınması
                if satir_sutun >= EN_AZ_YATAY_CIZGI and satir_sutun <= EN_FAZLA_YATAY_CIZGI:
                    break
                else:
                    print("Lütfen 4 ila 8 arasında bir sayı girin: ")
            except(ValueError):
                print("Lütfen geçerli bir sayı girin! ")

        oyun_matris = [[OYUNCU_YOK_TAS for i in range(satir_sutun)] for j in range(satir_sutun)]
        while True:
            try:
                # oyuncu 1 için harf alın
                oyuncu1 = input("Lütfen oyuncu 1 için bir harf girin: ")
                if len(oyuncu1) == 1 and oyuncu1.isalpha() and oyuncu1.isupper():
                    break
                else:
                    print("Lütfen geçerli bir harf girin!")
            except(ValueError):
                print("Lütfen geçerli bir harf girin!")
        while True:
            try:
                # oyuncu 2 için harf alın
                oyuncu2 = input("Lütfen oyuncu 2 için bir harf girin: ")

                # girilen değerin tek harf olduğunu ve büyük harf olduğunu kontrol edin
                if len(oyuncu2) == 1 and oyuncu2.isalpha() and oyuncu2.isupper() and oyuncu2 != oyuncu1:
                    break
                else:
                    print("Lütfen geçerli bir harf girin!")
            except ValueError:
                print("Lütfen geçerli bir harf girin!")
        satir_sutun_hesapla(oyun_matris)
        tas_yerlestir(oyun_matris, oyuncu2, oyuncu1)
        tahta_ciz(oyun_matris)
        oyun_devam = True

        genel_oyuncu = oyuncu1

        while oyun_devam:
            hareket_konum_al_tas_ekle(oyun_matris, genel_oyuncu)
            tahta_ciz(oyun_matris)
            tas_sil(oyun_matris, satir_sutun, genel_oyuncu)
            rakip_tas_say = tas_hesapla(oyun_matris,genel_oyuncu,satir_sutun)
            if rakip_tas_say<2:
                print(f"Oyunu kazanan oyuncu: {genel_oyuncu}")
                while True:
                    try:
                        devam = input("Oyuna devam etmek istiyor musunuz? (E,e,H,h) ")
                        if devam not in ["E", "e", "H", "h"]:
                            raise ValueError
                        break
                    except ValueError:
                        print("Geçersiz değer girdiniz! ")
                    if devam == "h" or devam == "H":
                        break

                if devam == "h" or devam == "H":
                    break


            else:
                if genel_oyuncu == oyuncu1:
                    genel_oyuncu = oyuncu2
                else:
                    genel_oyuncu = oyuncu1

        if devam == "h" or devam == "H":
            break

if __name__ == '__main__':
    main()