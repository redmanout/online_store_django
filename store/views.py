from django.shortcuts import render
from django.views.generic import ListView
from .models import *


# Create your views here.

class BladesAttributeProduct:
    def get_attribute(self):
        return BladesProductAttribute.objects.all()

    def get_brand(self):
        return BladesBrand.objects.all()

    def get_type(self):
        return BladesType.objects.all()

    def get_handle_type(self):
        return BladesHandleType.objects.all()

    def get_composition(self):
        return BladesComposition.objects.all()

    def get_size(self):
        return BladesSize.objects.all()

    def get_count_attribute(self):
        return BladesProductAttribute.objects.all()


class CategoryList(BladesAttributeProduct, ListView):
    model = CategoryProduct
    template_name = 'store/home.html'
    context_object_name = 'categories_product'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['phone_numbers_contacts'] = [
            '+38(098)980-96-21',
            '+38(098)980-96-22',
            '+38(098)980-96-23',
        ]
        return ctx


def about_us(request):
    list_phone = [
        '+38(098)980-96-21',
        '+38(098)980-96-22',
        '+38(098)980-96-23',
    ]
    data = {
        'list_phone': list_phone,
    }
    return render(request, 'store/about.html', context=data)


def ship_pay(request):
    list_phone = [
        '+38(098)980-96-21',
        '+38(098)980-96-22',
        '+38(098)980-96-23',
    ]
    data = {
        'list_phone': list_phone,
    }
    return render(request, 'store/ship_pay.html', context=data)


def contacts(request):
    list_phone = [
        '+38(098)980-96-21',
        '+38(098)980-96-22',
        '+38(098)980-96-23',
    ]
    data = {
        'list_phone': list_phone,
    }
    return render(request, 'store/contacts.html', context=data)
