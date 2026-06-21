from django.contrib import admin
from django.utils.html import format_html
from core.models import News, AboutProducts, MoneyByPhone, WorkAsLeader, FamilyShopping
from django_summernote.admin import SummernoteModelAdmin

class BaseItemAdmin(SummernoteModelAdmin):
    list_display = ('title', 'image_preview', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('image_preview_large',)
    field = ('title', 'image', 'image_preview_large', 'description')
    summernote_fields = ('description',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return 'Нет фото'

    image_preview.short_description = 'Фото'

    class Media:
        js = ('admin/js/dynamic_image_preview.js',)

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 300px; border-radius: 10px;" />', obj.image.url)
        return 'Нет фото'

    image_preview_large.short_description = 'Предпросмотр фото'

class BaseInfoAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_at')
    search_fields = ('title',)
    readonly_fields = ('image_preview_large',)
    field = ('title', 'image', 'image_preview_large', 'description')
    summernote_fields = ('description',)

    class Media:
        js = ('admin/js/dynamic_image_preview.js',)

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 300px; border-radius: 10px;" />', obj.image.url)
        return 'Нет фото'

    image_preview_large.short_description = 'Предпросмотр фото'

@admin.register(News)
class NewsAdmin(BaseItemAdmin):
    pass

@admin.register(AboutProducts)
class AboutProductsAdmin(BaseItemAdmin):
    pass

@admin.register(MoneyByPhone)
class MoneyByPhoneAdmin(BaseInfoAdmin):
    pass

@admin.register(WorkAsLeader)
class WorkAsLeaderAdmin(BaseInfoAdmin):
    pass

@admin.register(FamilyShopping)
class FamilyShoppingAdmin(BaseInfoAdmin):
    pass