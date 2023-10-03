from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




Blood_groups = (
    ("O+ ive", "O POSITIVE"),
    ("O- ive", "O NEGATIVE"),
    ("A+ ive", "A POSITIVE"),
    ("A- ive", "A NEGATIVE"),
    ("B+ ive", "B POSITIVE"),
    ("B- ive", "B NEGATIVE"),
    ("AB+ ive", "AB POSITIVE"),
    ("AB- ive", "AB NEGATIVE")
)


class Doner_registration(UserCreationForm):
    Doner_name = forms.CharField(max_length=25)
    Doner_place = forms.CharField(max_length=25)
    Doner_address = forms.CharField(max_length=50)
    Doner_blood_type = forms.ChoiceField(choices=Blood_groups)
    Doner_contact_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['Doner_name', 'Doner_place',
                  'Doner_address', 'Doner_blood_type',
                  'Doner_contact_number', 'username','email',
                  'password1', 'password2']


class Buser_registration(UserCreationForm):
    Buser_name = forms.CharField(max_length=25)
    Buser_place = forms.CharField(max_length=25)
    Buser_address = forms.CharField(max_length=50)
    Buser_blood_type = forms.ChoiceField(choices=Blood_groups)
    Buser_contact_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['Buser_name', 'Buser_place',
                  'Buser_address', 'Buser_blood_type', 
                  'Buser_contact_number', 'username','email',
                    'password1', 'password2']



