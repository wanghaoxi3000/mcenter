from django.contrib import admin

from .models import Category, Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'own', 'category', 'timestamp', 'read_num')
    list_filter = ('own', 'category')
    # 时间过滤器 修改好后，页面中的列表顶端会有一个逐层深入的导航条，它从可用的年份开始，然后逐层细分到月乃至日
    date_hierarchy = 'timestamp'


admin.site.register(Category)
admin.site.register(Entry, EntryAdmin)
