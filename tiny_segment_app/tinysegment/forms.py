from django import forms

from . import models

class LoginForm(forms.Form):
    email = forms.CharField(label="Email", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    
    class Meta:
        model = models.User
        fields = ['email', 'password', 'name']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'password': 'Password',
        }


class CodeComponentForm(forms.ModelForm):
    class Meta:
        model = models.CodeComponent
        fields = ['name', 'description', 'source_event', 'source_div_id', 'html_code', 'code_placement', 'status']
    
    def __init__(self, *args, **kwargs):
        super(CodeComponentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'