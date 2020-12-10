from django import forms
from Home.models import *

class HikeChoiceField(forms.Form):
    Hikes = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Hikes'].choices= [(Hike.id, Hike.name) for Hike in Hike.objects.all()]
