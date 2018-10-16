from django.contrib import admin

from .models import Assinante, Unidade, Safra, Cultura, Ccusto, Pcontas

# Register your models here.

class AssinanteAdmin(admin.ModelAdmin):
    pass

class UnidadeAdmin(admin.ModelAdmin):
    pass

class SafraAdmin(admin.ModelAdmin):
    pass

class CulturaAdmin(admin.ModelAdmin):
    pass

class CcustoAdmin(admin.ModelAdmin):
    pass

class PcontasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Assinante, AssinanteAdmin)
admin.site.register(Unidade, UnidadeAdmin)
admin.site.register(Safra, SafraAdmin)
admin.site.register(Cultura, CulturaAdmin)
admin.site.register(Ccusto, CcustoAdmin)
admin.site.register(Pcontas, PcontasAdmin)
