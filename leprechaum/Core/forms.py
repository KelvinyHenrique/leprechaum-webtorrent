from django import forms
from .models import Torrents

class TorrentsForms(forms.ModelForm):
    class Meta:
        model = Torrents
        fields = ['nome', 'magnet', 'type']
        widgets = {
            'magnet': forms.TextInput()
        }
