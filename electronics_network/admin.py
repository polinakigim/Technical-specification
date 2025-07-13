from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronics_network.models import Network


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt_to_supplier(modeladmin, request, queryset):
    queryset.update(debt_to_supplier=0)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "supplier_link", "debt_to_supplier")
    list_filter = ("city",)
    actions = [clear_debt_to_supplier]

    def supplier_link(self, obj):
        # если поставщик не указан
        if not obj.supplier:
            return "-"
        # если сеть ссылается сама на себя — показываем просто имя
        if obj.supplier == obj:
            return obj.supplier.name
        # иначе — делаем ссылку
        url = reverse(
            "admin:electronics_network_network_change", args=[obj.supplier.id]
        )
        return format_html('<a href="{}">{}</a>', url, obj.supplier.name)

    supplier_link.short_description = "Поставщик"
