def machinPi(tolerans=10**-8):
    """
     Machin formülünü kullanarak Pi sayısını hesaplar.
     Girilen tolerans değeri taylor serisinin son teriminin büyüklüğünü ifade eder.

     Parametreler:
       tolerans (float): Tolerans değeri (varsayılan: 10**-8)

     Dönüş Değeri:
       float: Hesaplanan Pi değeri
     """

    def arctan(x):
        """
        Taylor serisi kullanarak arktanjant fonksiyonunu hesaplar.

        Parametreler:
          x (float): Giriş değeri

        Dönüş Değeri:
          float: Hesaplanan arktanjant değeri
        """
        toplam = x
        terim = x ** 3 / 3
        n = 1
        while abs(terim) > tolerans:
            n += 2
            toplam += terim
            terim *= -x ** 2 / n
        return toplam

    pi = 16 * arctan(1 / 5) - 4 * arctan(1 / 239)
    return pi

print(machinPi())