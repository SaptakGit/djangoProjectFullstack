from django import forms
from .models import ChaiVaraity

class ChaiVarityForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVaraity.objects.all(), label="Select chai variety")
