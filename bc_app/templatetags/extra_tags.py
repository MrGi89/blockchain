from datetime import datetime

from django import template


register = template.Library()


@register.filter(name='time')
def time_filter(time):
    '''Filters given date to format %Y-%m-%d %H:%M:%S'''
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')


@register.filter(name='currency')
def currency_filter(value):
    return int(value) / 1000000


