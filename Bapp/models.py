from django.db import models
from django.contrib.auth.models import User

# Create your models here.


Blood_groups=(
    ("O+ ive","O POSITIVE"),
    ("O- ive","O NEGATIVE"),
    ("A+ ive","A POSITIVE"),
    ("A- ive","A NEGATIVE"),
    ("B+ ive","B POSITIVE"),
    ("B- ive","B NEGATIVE"),
    ("AB+ ive","AB POSITIVE"),
    ("AB- ive","AB NEGATIVE")
)

class Doner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=15,default="Doner")
    Doner_name = models.CharField(max_length=25)
    Doner_place = models.CharField(max_length=25)
    Doner_address = models.CharField(max_length=50)
    Doner_blood_type = models.CharField(max_length=20,choices=Blood_groups)
    Doner_contact_number = models.IntegerField()
    def __str__(self):
        return self.Doner_name


class Buser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=15,default="Buser")
    Buser_name = models.CharField(max_length=25)
    Buser_place = models.CharField(max_length=25)
    Buser_address = models.CharField(max_length=50)
    Buser_blood_type = models.CharField(max_length=20,choices=Blood_groups)
    Buser_contact_number = models.IntegerField()

    def __str__(self):
        return self.Buser_name