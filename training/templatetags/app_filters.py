from django import template

register = template.Library()
@register.filter(name='pop')
def pop(value):
    return 'Hello'
