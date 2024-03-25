from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationUserForm(forms.ModelForm):
    username = forms.CharField( max_length=20, 
                                widget=forms.TextInput(attrs={'placeholder': 'username', 
                                                              'class': 'form-control'}),
                                label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email', 
                                                            'class': 'form-control'}),
                              label='')
    password1 = forms.CharField(max_length=20,
                                 widget=forms.PasswordInput(attrs={'placeholder':'password',
                                                                   'class': 'form-control'}),
                                 label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'repeat password',
                                                                  'class': 'form-control'}),
                                label='')
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', forms.ValidationError('passwords mismatch'))
           
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username):
            self.add_error('username', forms.ValidationError('This username exists'))
        return username
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
    
        if commit:
            user.save()
        return user


   

class LoginUserForm(forms.Form):
    username = forms.CharField( max_length=20, 
                                widget=forms.TextInput(attrs={'placeholder': 'username', 
                                                              'class': 'form-control'}),
                                                            
                                label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password',
                                                                  'class': 'form-control'}),
                                label='')

