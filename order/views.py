from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from order.forms import StoreCartForm
from order.models import StoreCart
from store.models import CategoryProduct


# Create your views here.
@login_required
def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')  # get last url
    current_user = request.user

    check_product = StoreCart.objects.filter(product_id=id)  # check product in store cart
    if check_product:
        control = 1
    else:
        control = 0

    if request.method == 'POST':
        form = StoreCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # update store cart
                data = StoreCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:  # insert to store cart
                data = StoreCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Product added to Storecart')
        return redirect(url)

    # if there is no post
    else:
        if control == 1:
            data = StoreCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = StoreCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, 'Product added to Storecart')
        return redirect(url)


def storecart(request):
    category = CategoryProduct.objects.all()
    current_user = request.user
    store_cart = StoreCart.objects.filter(user_id=current_user.id)


    total_product_all = 0
    for el in store_cart:
        total_product_all += el.product.price * el.quantity

    context = {
        'category': category,
        'store_cart': store_cart,
        'total_product_all': total_product_all,
    }
    return render(request, 'order/store_card.html', context=context)


@login_required()
def delete_from_cart(request, id):
    StoreCart.objects.filter(id=id).delete()
    messages.success(request, 'Your product deleted from Storecart')
    return redirect('store_card')
