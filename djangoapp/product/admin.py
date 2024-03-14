from django.contrib import admin
from .models import Product, VariationPrice
from .utils.report import report_price_variation

def report_price_variation_action(modeladmin, request, queryset):
    report_price_variation()
report_price_variation_action.short_description = "Gerar relatório de variação de preços"

class PriceVariationAdmin(admin.ModelAdmin):
    list_display = ('data', 'price')
    actions = [report_price_variation_action]
    
admin.site.register(Product)
# admin.site.register(VariationPrice)
admin.site.register(VariationPrice, PriceVariationAdmin)