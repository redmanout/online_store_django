from django import template
from store.models import Product

register = template.Library()


@register.simple_tag()
def get_phone_contacts():
    phone_numbers_contacts = [
        '+38(098)980-96-21',
        '+38(098)980-96-22',
        '+38(098)980-96-23',
    ]
    return phone_numbers_contacts
