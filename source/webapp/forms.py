from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]

BROWSER_DATETIME_FORMAT = '%Y-%m-%d'


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Описание')
    more = forms.CharField(max_length=3000, required=False, label='Подробное описание',
                           widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус',
                               initial=default_status)
    date = forms.DateTimeField(required=False, label='Время выполнения',
                                     input_formats=['%Y-%m-%dT%H:%M', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))