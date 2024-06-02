from django.db import models

# Create your models here.

class Tbl_Employee(models.Model):
    id   = models.AutoField(primary_key=True, serialize=True)
    name = models.CharField(max_length = 250, null=False)
    email = models.CharField(max_length = 250, null=False)
    mobile_no = models.CharField(max_length = 50, null=False)

    class Meta:
        db_table = 'tbl_employee'
