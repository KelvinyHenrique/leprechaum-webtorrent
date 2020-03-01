from django import forms
from .models import Torrents

class TorrentsForms(forms.ModelForm):
    class Meta:
        model = Torrents
        fields = ['nome', 'magnet', 'type']
        widgets = {
            'nome': forms.TextInput({'class':'col form-control'}),
            'magnet': forms.TextInput({'class':'col form-control'}),
            'type': forms.Select({'class':'col form-control'})
        }
