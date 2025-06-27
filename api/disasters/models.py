from django.db import models

# Create your models here.
class CityCategory(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name1 = models.CharField(max_length=50)
    city_name2 = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.city_name1} {self.city_name2 or ''}".strip()
    
class DisasterCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pictogram_image = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class DisasterDetail(models.Model):
    disaster_id = models.BigAutoField(primary_key=True)
    category = models.ForeignKey(DisasterCategory, on_delete=models.CASCADE)
    city = models.ForeignKey(CityCategory, on_delete=models.CASCADE)
    occurrence_time = models.DateField()
    scale = models.CharField(max_length=20)
    casualty = models.IntegerField(default=0) 
    caused = models.CharField(max_length=30)
    status = models.CharField(max_length=20)

class DisasterProtocol(models.Model):
    protocol_id = models.BigAutoField(primary_key=True)
    disaster_category = models.ForeignKey(DisasterCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    guide_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Agency(models.Model):
    agency_id = models.BigAutoField(primary_key=True)
    protocol = models.ForeignKey(DisasterProtocol, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Responder(models.Model):
    reponder_id = models.BigAutoField(primary_key=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class AiDataset(models.Model):
    dataset_id = models.BigAutoField(primary_key=True)
    time = models.DateField()
    city = models.ForeignKey(CityCategory, on_delete=models.CASCADE)
    exmn_hmty = models.FloatField(null=True, blank=True)  # 옵션: null 허용, 빈 값 허용
    exmn_tp = models.FloatField(null=True, blank=True)  # 옵션: null 허용, 빈 값 허용
    weather = models.CharField(max_length=6)     # snow, rain, sun
    fire_check = models.BooleanField(default=False)
