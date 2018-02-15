from django.contrib import admin
from .models import Advert, IcOzellik, FiyatTur, Tur, Ilce, Kimden, Mahallesemt, AltTur, Sehir, Islem


class IcOzellikAdmin(admin.ModelAdmin):
    model = IcOzellik
    filter_horizontal = ('advert',)



admin.site.register(Advert)
admin.site.register(Islem)
admin.site.register(Tur)
admin.site.register(AltTur)
admin.site.register(FiyatTur)
admin.site.register(Ilce)
admin.site.register(Kimden)
admin.site.register(Mahallesemt)
admin.site.register(Sehir)
admin.site.register(IcOzellik, IcOzellikAdmin)



