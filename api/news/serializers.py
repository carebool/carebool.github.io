from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['article_id', 'title', 'url', 'source_name', 'category', 'crawl_time']
        read_only_fields = ['article_id', 'crawl_time'] 