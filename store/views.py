from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import ReviewForm
from .models import CategoryProduct, Product


# Create your views here.


class CategoryList(ListView):
    model = CategoryProduct
    template_name = 'store/home.html'
    context_object_name = 'categories_product'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product_bestseller'] = Product.objects.filter(bestseller=True)
        ctx['product_new'] = Product.objects.filter(new=True)
        ctx['product_stock'] = Product.objects.filter(stock=True)
        return ctx


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'store/product.html'
    form_class = ReviewForm

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())


def about_us(request):
    data = {
    }
    return render(request, 'store/about.html', context=data)


def ship_pay(request):
    data = {
    }
    return render(request, 'store/ship_pay.html', context=data)


def contacts(request):
    data = {
    }
    return render(request, 'store/contacts.html', context=data)
