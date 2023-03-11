from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from order.forms import StoreCartForm, OrderForm
from order.models import StoreCart, OrderProduct
from store.models import CategoryProduct


# Create your views here.
@login_required
def add_to_cart(request, id):
    """После проверки, есть ли такой товар в корзине, увеличивается количество товара в корзине на единицу, если такой
    товар уже есть в корзине. Если нет, то добавляется новая запись корзины с кол-вом товара = 1. Если запрос POST, то
    кол-во товара в корзине устанавливается равным сумме уже имеющегося кол-ва и кол-ву, указанному в форме."""
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    try:
        cart_item = StoreCart.objects.get(product_id=id)
        cart_item.quantity += 1
    except StoreCart.DoesNotExist:
        cart_item = StoreCart(user_id=current_user.id, product_id=id, quantity=1)

    if request.method == 'POST':
        form = StoreCartForm(request.POST)
        if form.is_valid():
            cart_item.quantity += form.cleaned_data['quantity'] - 1

    cart_item.save()
    messages.success(request, 'Product added to Storecart')
    return redirect(url)


def get_store_cart_data(request):
    """Получение корзины пользователя и связанных продуктов. Вычисление общей
    стоимости товаров в корзине с помощью агрегатной функции Sum и F объектов для выборки значений из связанных
    моделей."""
    current_user = request.user
    store_cart = StoreCart.objects.filter(user_id=current_user.id).select_related('product')
    total_price = store_cart.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price'] or 0
    category = CategoryProduct.objects.all()
    return category, store_cart, total_price, current_user


@login_required
def store_to_cart(request):
    """Отображает корзину пользователя."""
    category, store_cart, total_price, current_user = get_store_cart_data(request)

    context = {
        'category': category,
        'store_cart': store_cart,
        'total_price': total_price,
    }
    return render(request, 'order/store_card.html', context=context)


def delete_from_cart(request, id):
    """Удаление продукта из корзины. В начале функция получает текущего пользователя через объект запроса request.
    Затем она пытается найти объект StoreCart с заданным id и user, используя метод get. Если объект не найден, то
    генерируется исключение, и пользователю показывается сообщение об ошибке. Если объект найден, он удаляется с помощью
    метода delete, а пользователю показывается сообщение об успешном удалении продукта."""
    current_user = request.user
    try:
        item = StoreCart.objects.get(id=id, user=current_user)
    except StoreCart.DoesNotExist:
        messages.error(request, 'This item does not exist in your cart')
    else:
        item.delete()
        messages.add_message(request, messages.SUCCESS, 'Product removed from Storecart')
    return redirect('store_card')


def order_product(request):
    """Оформление заказа. Из корзины пользователя получаем общую сумму заказа, используя метод aggregate и функции
    Sum и F. При отправке формы методом POST, если данные формы верны, то создаем новый объект заказа (Order)
    и сохраняем его. Затем для каждого товара в корзине создаем объект OrderProduct и сохраняем его. Для каждого
    товара также уменьшаем количество товаров на складе. После успешного оформления заказа, удаляем объекты корзины
    пользователя и обновляем сессию пользователя. В случае неверных данных формы, выводим ошибки на страницу и
    перенаправляем пользователя на страницу оформления заказа (order_product)."""
    category, store_cart, total_price, current_user = get_store_cart_data(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = current_user.id
            order.total = total_price
            order.ip = request.META.get('REMOTE_ADDR')
            order.code = get_random_string(5).upper()
            order.save()

            for cart_item in store_cart:
                OrderProduct.objects.create(
                    order=order,
                    product=cart_item.product,
                    user_id=current_user.id,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,
                    amount=cart_item.amount
                )

                cart_item.product.quantity_in_stock -= cart_item.quantity
                cart_item.product.save()

            store_cart.delete()
            request.session['cart_items'] = 0
            messages.success(request, 'Your Order has been completed.')
            return render(request, 'order/order_completed.html', {'order_code': order.code, 'category': category})
        else:
            messages.warning(request, form.errors)
            return redirect('order_product')

    form = OrderForm()
    context = {
        'category': category,
        'store_cart': store_cart,
        'total_product_all': total_price,
        'form': form
    }
    return render(request, 'order/order_product.html', context=context)
