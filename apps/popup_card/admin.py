from django.contrib import admin

# Register your models here.
from apps.popup_card.models import Popup_card, Popup_card_catalog, Price_popup_card, Category_card, Comment

admin.site.register(Popup_card)
admin.site.register(Price_popup_card)
admin.site.register(Popup_card_catalog)
admin.site.register(Category_card)
admin.site.register(Comment)