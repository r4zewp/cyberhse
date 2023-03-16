from django import forms
from .models import Participant, Partner


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email', 'telegram', 'name']

    labels = {
        'email': 'E-mail',
        'telegram': 'Telegram',
        'Name': 'Name',
    }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['email', 'company_name', 'name']

        labels = {
            'email': 'E-mail',
            'company_name': 'Company name',
            'name': 'Name',
        }