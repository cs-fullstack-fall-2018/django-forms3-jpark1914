from django import forms
from .models import NPModel

class NPForm(forms.ModelForm):
    class Meta:
        model = NPModel
        fields = {'name','address','employee_count', 'operating_budget'}