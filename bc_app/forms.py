from django import forms

from .validators import bc_validator


class AddressForm(forms.Form):

    address = forms.CharField(min_length=27, max_length=35, validators=[bc_validator, ])
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
