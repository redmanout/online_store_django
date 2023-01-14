from django.shortcuts import render


# Create your views here.

def home(request):
    list_phone = [
        '+38(098)980-96-21',
        '+38(098)980-96-22',
        '+38(098)980-96-23',
    ]
    data = {
        'list_phone': list_phone,
    }
    return render(request, 'store/home.html', context=data)


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
