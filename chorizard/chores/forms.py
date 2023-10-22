from django.forms import forms

from .models import Chore


class NewChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = ["name", "created_on", "score"]
