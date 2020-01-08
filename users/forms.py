from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class LogupForm(forms.Form):
    user_first_name = forms.CharField(max_length=100, required=True)
    user_last_name = forms.CharField(max_length=100, required=True)
    user_aka = forms.CharField(max_length=100, required=True)
    user_email = forms.EmailField(widget=forms.EmailInput, required=True)
    user_password = forms.EmailField(widget=forms.PasswordInput, required=True)