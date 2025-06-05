from django.contrib import admin
from .models import GPUBrand, GPU, Order, OrderItem


class GPUBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year', 'active')
    search_fields = ('name', 'country')


class GPUAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'price', 'memory_gb',
                    'core_clock_mhz', 'boost_clock_mhz', 'is_available')
    list_filter = ('brand', 'memory_type', 'is_available')
    search_fields = ('model', 'brand__name')
    ordering = ['price']


admin.site.register(GPUBrand, GPUBrandAdmin)
admin.site.register(GPU, GPUAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
