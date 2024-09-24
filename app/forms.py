from django import forms
from .models import CustomUser, user

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'is_admin', 'is_banker', 'is_customeruser']  
        widgets = {
            'password': forms.PasswordInput(), 
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = "__all__"
        exclude = ['user_id'] 
