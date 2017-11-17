"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Game

#class BootstrapAuthenticationForm(AuthenticationForm):
#    """Authentication form which uses boostrap CSS."""
#    username = forms.CharField(max_length=254,
#                               widget=forms.TextInput({
#                                   'class': 'form-control',
#                                   'placeholder': 'User name'}))
#    password = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Password'}))

class FormGame(forms.ModelForm):
    name=forms.CharField(max_length=50,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'name of game'}),required=True)
    publisher=forms.CharField(max_length=20,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Publisher Game'}),required=True)
    year=forms.IntegerField(
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Year game'}),required=True)
    genre=forms.ChoiceField(choices=Game.GENRES,
                               widget=forms.Select({
                                   'class': 'form-control'}),required=True)
    platform=forms.ChoiceField(choices=Game.PLATFORMS,
                               widget=forms.Select({
                                   'class': 'form-control'}),required=True)
    
    score=forms.IntegerField(
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Score Game'}),required=True)
    online=forms.BooleanField(
                               widget=forms.CheckboxInput({
                                   'class': 'form-control',
                                   'placeholder': 'Score Game'}),required=False)
    
    pegi=forms.IntegerField(
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'temporada de la Serie'}),required=True)
    class Meta:
        model = Game
        fields = [

            "name",
            "publisher",
            "year",
            "genre",
            "platform",
            "score",
            "online",
            "pegi"

    ]


class FormFilter():
    dataSearch=forms.CharField(max_length=20,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Search...'}))