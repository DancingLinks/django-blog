from django import forms


class user_form(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    user_password = forms.CharField(label='user_password', widget=forms.PasswordInput, max_length=100)
    user_page = forms.CharField(label='user_page', widget=forms.Textarea)