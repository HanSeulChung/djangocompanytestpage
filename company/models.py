from django.db import models

# Create your models here.

class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True)
    Department_NAME = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Department_ID)


class Employer(models.Model):
    Employer_ID = models.AutoField(primary_key=True)
    Department_ID= models.ForeignKey("Department", on_delete=models.CASCADE)
    Employer_NAME = models.CharField(max_length=100)
    Employer_GENDER = models.CharField(max_length=30)
    Employer_age = models.IntegerField(default=0)
    Date_of_Join = models.DateField(null=True) #같이 쓴게 아니라 수정해서 더했기때문에 이렇게 썼음 ; 오류나서;
    Photo_Image = models.ImageField(upload_to='emp/images/%Y/%m/%d', blank=True, null=True) #같이 쓴게 아니라 수정해서 더했기때문에 이렇게 썼음 ; 오류나서;
    upload_at= models.DateTimeField(auto_now =True,null=True) #같이 쓴게 아니라 수정해서 더했기때문에 이렇게 썼음 ; 오류나서;

    def __str__(self):
        return str(f'[{self.Employer_ID}]')
