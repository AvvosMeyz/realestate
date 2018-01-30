from django.db import models
from django.core.validators import RegexValidator


class Advert(models.Model):
    ilan_id = models.AutoField(primary_key=True)
    islem_id = models.IntegerField('Durumu',default=1)
    tur_id = models.IntegerField('Emlak Türü',default=1)
    alt_tur_id = models.IntegerField('Emlak Alt-Türü',default=1)
    ilan_baslik = models.CharField('İlan başlığı', max_length=500, default='noob')
    ilan_acik = models.TextField('İlan açıklaması',default='noob')
    fiyat_tur_id = models.IntegerField(default=0)
    fiyat = models.IntegerField('Fiyat',default=0)
    kimden_id = models.IntegerField(default=0)
    sehir_id = models.IntegerField(default=0)
    ilce_id = models.IntegerField(default=0)
    takas = models.IntegerField(default=0)
    mahallesemt_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'İlan'
        verbose_name_plural = 'İlanlar'


class Islem(models.Model):
    islem_id = models.AutoField(primary_key=True)
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    islem_adi = models.CharField(max_length=20, default='noob7')


class Tur(models.Model):
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    tur_id = models.AutoField(primary_key=True)
    tur_isim = models.CharField(max_length=50, default='noob9')


class AltTur(models.Model):
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    tur_id = models.ForeignKey(Tur, on_delete=models.CASCADE)
    alt_tur_id = models.AutoField(primary_key=True)
    alt_tur_isim = models.CharField(max_length=50, default='noob10')


class Sehir(models.Model):
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    sehir_id = models.AutoField(primary_key=True)
    sehir_isim = models.CharField(max_length=50,default='noob2')
    plaka_kodu = models.IntegerField(default=35)
    telefon_kodu = models.IntegerField(default=256)


class Ilce(models.Model):
    ilce_id = models.AutoField(primary_key=True)
    sehir_id = models.ForeignKey(Sehir, on_delete=models.CASCADE)
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    ilce_ismi = models.CharField(max_length=50, default='noob3')


class Mahallesemt(models.Model):
    mahallesemt_id = models.AutoField(primary_key=True)
    ilce_id = models.ForeignKey(Ilce, on_delete=models.CASCADE)
    sehir_id = models.ForeignKey(Sehir, on_delete=models.CASCADE)
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    mahallesemt_ismi = models.CharField(max_length=200, default='noob4')
    semt_ismi = models.CharField(max_length=200, default='noob5')
    posta_kodu = models.IntegerField(default=35330)


class Kimden(models.Model):
    kimden_id = models.AutoField(primary_key=True)
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    kimden_isim = models.CharField(max_length=200,default='noob6')


class FiyatTur(models.Model):
    fiyat_tur_id = models.AutoField(primary_key=True)
    ilan_id = models.ForeignKey(Advert, on_delete=models.CASCADE)
    fiyat_tur_name = models.CharField(max_length=10, default='TL')
