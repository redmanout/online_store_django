from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import CategoryProduct, Product, BladesType, RubbersType, BallsRank, BackpacksBagsType, NetsBrand, \
    RacketsType, TablesSection, AccessoriesType


# Create your views here.


class CategoryList(ListView):
    model = CategoryProduct
    template_name = 'store/home.html'
    context_object_name = 'categories_product'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category_catalog_card'] = CategoryProduct.objects.filter(visibility_catalog_cards=True)
        ctx['product_bestseller'] = Product.objects.filter(bestseller=True)
        ctx['product_new'] = Product.objects.filter(new=True)
        ctx['product_stock'] = Product.objects.filter(stock=True)
        ctx['blades_type'] = BladesType.objects.all()
        ctx['rubbers_type'] = RubbersType.objects.all()
        ctx['balls_rank'] = BallsRank.objects.all()
        ctx['backpacks_bags_type'] = BackpacksBagsType.objects.all()
        ctx['nets_brand'] = NetsBrand.objects.all()
        ctx['rackets_type'] = RacketsType.objects.all()
        ctx['tables_section'] = TablesSection.objects.all()
        ctx['accessories_type'] = AccessoriesType.objects.all()
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
            form.ip = request.META.get('REMOTE_ADDR')
            form.product = product
            current_user = request.user
            form.user_id = current_user.id
            form.save()
            messages.success(request, 'Your review has been sent')
        return redirect(product.get_absolute_url())


class SearchView(ListView):
    template_name = 'store/search.html'
    paginate_by = 2
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')
        return context
