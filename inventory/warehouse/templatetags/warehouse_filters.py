from django import template

register = template.Library()

@register.filter
def low_quantity(value):
    if(value.quantityLeft<=5):
        return True
    else:
        return False