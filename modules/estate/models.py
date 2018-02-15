from django.db import models


class Islem(models.Model):
    TAKAS = (
        ('Sat', 'Satılık'),
        ('Kir', 'Kiralık'),
    )
    islem_id = models.AutoField(primary_key=True)
    islem_adi = models.CharField('İşlem Durumu', max_length=20, default='Kiralık')

    class Meta:
        verbose_name = 'İşlem'
        verbose_name_plural = 'İşlemler'

    def __str__(self):
        return self.islem_adi


class Tur(models.Model):
    tur_id = models.AutoField(primary_key=True)
    tur_adi = models.CharField('Türü', max_length=50, default='Konut')

    class Meta:
        verbose_name = 'Tür'
        verbose_name_plural = 'Türler'

    def __str__(self):
        return self.tur_adi


class AltTur(models.Model):
    alt_tur_id = models.AutoField(primary_key=True)
    alt_tur_adi = models.CharField('Alt Türü', max_length=50, default='Daire')
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Alt Tür'
        verbose_name_plural = 'Alt Türler'

    def __str__(self):
        return self.alt_tur_adi


class Sehir(models.Model):
    sehir_id = models.AutoField(primary_key=True)
    sehir_adi = models.CharField('İl', max_length=50, default='Aydın')
    plaka_kodu = models.IntegerField(default=35)
    telefon_kodu = models.IntegerField(default=256)

    class Meta:
        verbose_name = 'Şehir'
        verbose_name_plural = 'Şehirler'

    def __str__(self):
        return self.sehir_adi


class Ilce(models.Model):
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE)
    ilce_id = models.AutoField(primary_key=True)
    ilce_adi = models.CharField('İlçe', max_length=50, default='Didim')

    class Meta:
        verbose_name = 'İlçe'
        verbose_name_plural = 'İlçeler'

    def __str__(self):
        return self.ilce_adi


class Mahallesemt(models.Model):
    ilce = models.ForeignKey(Ilce, on_delete=models.CASCADE)
    mahallesemt_id = models.AutoField(primary_key=True)
    semt_adi = models.CharField('Semt', max_length=200, default='Mavişehir')
    mahallesemt_adi = models.CharField('Mahalle', max_length=200, default='Sağtur')
    posta_kodu = models.IntegerField(default=35330)

    class Meta:
        verbose_name = 'Mahalle/Semt'
        verbose_name_plural = 'Mahalle/Semtler'

    def __str__(self):
        return self.mahallesemt_adi


class Kimden(models.Model):
    kimden_id = models.AutoField(primary_key=True)
    kimden_adi = models.CharField('Kimden', max_length=200,default='Emlakçıdan')

    class Meta:
        verbose_name = 'Kimden'
        verbose_name_plural = 'Kimden'

    def __str__(self):
        return self.kimden_adi


class FiyatTur(models.Model):
    fiyat_tur_id = models.AutoField(primary_key=True)
    fiyat_tur_adi = models.CharField('Para Birimi', max_length=10, default='TL')

    class Meta:
        verbose_name = 'Fiyat Türü'
        verbose_name_plural = 'Fiyat Türleri'

    def __str__(self):
        return self.fiyat_tur_adi


class Advert(models.Model):
    TAKAS = (
        (0, 'Takas Olmaz'),
        (1, 'Takas Olur'),
    )

    ilan_id = models.AutoField(primary_key=True)
    ilan_baslik = models.CharField('İlan başlığı', max_length=500, default='Giriş Katı 1+1 Yayla Evi')
    ilan_acik = models.TextField('İlan Açıklaması',default='Okula yakın ')
    fiyat_tur = models.ForeignKey(FiyatTur, on_delete=models.CASCADE)
    fiyat = models.IntegerField('Fiyatı',default=0)
    takas = models.IntegerField('Takas Durumu', choices=TAKAS, default=1)

    islem = models.ForeignKey(Islem, on_delete=models.CASCADE)
    tur = models.ForeignKey(Tur, on_delete=models.CASCADE)
    altTur = models.ForeignKey(AltTur, on_delete=models.CASCADE)
    sehir = models.ForeignKey(Sehir, on_delete=models.CASCADE)
    ilce = models.ForeignKey(Ilce, on_delete=models.CASCADE)
    mahallesemt = models.ForeignKey(Mahallesemt, on_delete=models.CASCADE)
    kimden = models.ForeignKey(Kimden, on_delete=models.CASCADE)
    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    class Meta:
        verbose_name = 'İlan'
        verbose_name_plural = 'İlanlar'

    def __str__(self):
        return self.ilan_baslik


class IcOzellik(models.Model):
    advert = models.ManyToManyField(Advert)
    ic_ozellik_id = models.AutoField(primary_key=True)
    ic_ozellik_ismi = models.CharField('İç özellik ismi', max_length=200, default='noob99')

    class Meta:
        verbose_name = 'İç Özellik'
        verbose_name_plural = 'İç Özellikler'

    def __str__(self):
        return self.ic_ozellik_ismi
