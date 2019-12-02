from tutorials.models import Comment
# from django.contrib.auth.models import User
from django import forms
# from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')


# class RegisterForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ('fullname', 'email', 'username', 'password1', 'password2')
#
#
# class LoginForm(forms.ModelForm):
