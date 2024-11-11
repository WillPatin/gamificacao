from django import forms
from .models import Selo

class SeloForm(forms.ModelForm):
    class Meta:
        model = Selo
        fields = ["nome","descricao","imagem"]