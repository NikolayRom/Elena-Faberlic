from django.contrib import admin
from django.utils.html import format_html
from core.models import News, AboutProducts, MoneyByPhone, WorkAsLeader, FamilyShopping, HomeDealOffer, HomeGiftsSection, HomeStarterSection
from django_summernote.admin import SummernoteModelAdmin

class SingletonModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

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

class BaseInfoAdmin(SummernoteModelAdmin, SingletonModelAdmin):
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

@admin.register(HomeGiftsSection)
class GiftsSectionAdmin(SingletonModelAdmin):
    pass

@admin.register(HomeStarterSection)
class StarterSectionAdmin(SingletonModelAdmin):
    pass

@admin.register(HomeDealOffer)
class DealOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'created_at')

    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="height: 50px; border-radius: 4px;" />', obj.image.url)
        return ""

    image_preview.short_description = 'Фото'