from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import CusOrders, CusRatingFeedback
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        
class CusOrdersUpd(forms.ModelForm):
    class Meta:
        model = CusOrders
        fields = ['quantity']
    
    quantity = forms.IntegerField(
        validators=[
            MinValueValidator(1, message='Quantity must be at least 1.'),
            MaxValueValidator(10, message='Quantity cannot be more than 10.')
        ]
    )      
        
        
class CusRatFeedForm(forms.ModelForm):
    class Meta:
        model = CusRatingFeedback
        fields = ['ratings','feedback']
        
            
        ratings = forms.IntegerField(
            validators=[
                MinValueValidator(1, message='Ratings must be at least 1.'),
                MaxValueValidator(10, message='Ratings cannot be more than 10.')
            ]
        )
        feedback = forms.CharField(
            validators=[
                RegexValidator(
                    regex='^[a-zA-Z]+$',
                    message='Feedback must contain only alphabets.',
                ),
            ],
        )


    
        
                      

 