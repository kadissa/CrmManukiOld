from django import forms

from webhooks.models import Guest


class GuestEditForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = (
            'people_count', 'prepayment', 'rotenburo_1', 'birch_broom',
            'oak_broom', 'bed_sheet', 'towel', 'robe', 'slippers')
