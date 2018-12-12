from django import template
from transaction.models import *

register = template.Library()


@register.filter
def mult(value1, value2):
    return float(value1)*float(value2)

@register.filter
def check_item(value):
    try:
        Re