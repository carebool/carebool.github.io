from django.db import models

# Create your models here.
class News(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.TextField()
    url = models.TextField()
    source_name = models.CharField(max_length=255)
    source_url = models.TextField()
    category = models.CharField(max_length=100)
    crawl_time = models.DateField()
    crawl_status = models.CharField(max_length=50)
    error_message = models.TextField()
