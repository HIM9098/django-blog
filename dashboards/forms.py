from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User

class AddUserForm(UserCreationForm):
    class Meta  :
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser', 'groups', 'user_permissions')

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )