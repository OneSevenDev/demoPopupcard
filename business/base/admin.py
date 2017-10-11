from django.contrib import admin

# Register your models here.
from business.base.models import Status_general, Type_general, Tag_general, MenuSetting

admin.site.register(Status_general)
admin.site.register(Type_general)
admin.site.register(Tag_general)
admin.site.register(MenuSetting)