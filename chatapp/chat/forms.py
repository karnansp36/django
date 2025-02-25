from django import forms
from .models import ImagePost

class imageForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['description', 'image']