from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class PlanForm(forms.Form):
    description = forms.CharField(max_length=200, label='Description', required=True)
    status = forms.ChoiceField(label='Status', required=True, choices=STATUS_CHOICES)
    deadline = forms.DateField(label='Deadline',required='True', widget=widgets.SelectDateWidget)
    full_description = forms.CharField(max_length=3000, label='Full_description', required=True,
                           widget=widgets.Textarea)