from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'source_name', 'category', 'crawl_time', 'crawl_status']
    list_filter = ['category', 'source_name', 'crawl_status', 'crawl_time']
    search_fields = ['title', 'source_name']
    date_hierarchy = 'crawl_time'
    ordering = ['-crawl_time']
    
    fieldsets = (
        ('기본 정보', {
            'fields': ('title', 'url', 'category')
        }),
        ('출처 정보', {
            'fields': ('source_name', 'source_url')
        }),
        ('크롤링 정보', {
            'fields': ('crawl_time', 'crawl_status', 'error_message'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        # 관리자 페이지에서 수동으로 뉴스를 추가하지 못하도록 설정
        return False
