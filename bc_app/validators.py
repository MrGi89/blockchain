from django.core.exceptions import ValidationError
from blockchain import blockexplorer
from blockchain.exceptions import APIException


def bc_validator(value):
    '''Searches if given address exists in API. If not raises ValidationError.'''
    try:
        blockexplorer.get_address(value)
    except APIException:
        raise ValidationError("BitCoin address {} is wrong. Please add correct address.".format(value))
