"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Serie

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class QueryForm(forms.ModelForm):
    titulo=forms.CharField(max_length=20,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Titulo de la Serie'}))
    productora=forms.CharField(max_length=10,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Productora de la Serie'}))
    fecha=forms.IntegerField(
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Año de la Serie'}))
    temporada=forms.IntegerField(
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'temporada de la Serie'}))
    genero=forms.ChoiceField(choices=Serie.GENEROS,
                               widget=forms.Select({
                                   'class': 'form-control'}))
    estado=forms.ChoiceField(choices=Serie.ESTADO,
                               widget=forms.Select({
                                   'class': 'form-control'}))
    class Meta:
        model = Serie
        fields = [

            "titulo",
            "productora",
            "fecha",
            "temporada",
            "genero",
            "estado",

    ]
