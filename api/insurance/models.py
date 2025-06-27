from django.db import models
from users.models import User

# Create your models here.
class InsuranceHistory(models.Model):
    history_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    regster_date = models.DateField()
    pub_pri = models.IntegerField()  # 0: 공공, 1: 민간 등으로 해석
    insurance_id = models.BigIntegerField()  # 실제로 연결하려면 GenericForeignKey도 가능

class PulicInsurance(models.Model):  # 오타가 있어 'PublicInsurance'로 고쳐도 됨
    insurance_id = models.BigAutoField(primary_key=True)
    insurance_name = models.CharField(max_length=50)
    coverage_type = models.CharField(max_length=30)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    city_name = models.CharField(max_length=50)
    description = models.TextField()
    gov_site = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    manage_department = models.CharField(max_length=30)     # 담당부서
    manage_phone = models.CharField(max_length=20)          # 담당자 전화번호

class PrivateInsurance(models.Model):
    insurance_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    policy_id = models.IntegerField()
    insurance_company_name = models.CharField(max_length=100)
    insurance_name = models.CharField(max_length=100)
    policy_type = models.CharField(max_length=50)
    coverage_amount = models.DecimalField(max_digits=12, decimal_places=2)
    premium = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()