import requests
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import ReviewForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import CategoryProduct, Product, BladesType, RubbersType, BallsRank, BackpacksBagsType, NetsBrand, \
    RacketsType, TablesSection, AccessoriesType, ValueBackpacksBagsAttribute


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
    paginate_by = 6
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(name__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', )
        return context


class CatalogFilter(ListView):
    model = Product
    template_name = 'store/catalog.html'
    context_object_name = 'filter_products'
    paginate_by = 2

    def get_queryset(self, *args):
        category_id = self.request.GET.get('category')
        blades_brand_id = self.request.GET.get('blades-brand')
        blades_type_id = self.request.GET.get('blades-type')
        blades_handle_type_id = self.request.GET.get('blades-handle-type')
        blades_composition_id = self.request.GET.get('blades-composition')
        blades_size_id = self.request.GET.get('blades-size')
        rubbers_brand_id = self.request.GET.get('rubbers-brand')
        rubbers_type_id = self.request.GET.get('rubbers-type')
        rubbers_speed_type_id = self.request.GET.get('rubbers-speed-type')
        balls_brand_id = self.request.GET.get('balls-brand')
        balls_rank_id = self.request.GET.get('balls-rank')
        balls_package_id = self.request.GET.get('balls-package')
        bags_brand_id = self.request.GET.get('bags-brand')
        bags_type_id = self.request.GET.get('bags-type')
        bags_color_id = self.request.GET.get('bags-color')
        nets_brand_id = self.request.GET.get('nets-brand')
        nets_color_id = self.request.GET.get('nets-color')
        rackets_brand_id = self.request.GET.get('rackets-brand')
        rackets_type_id = self.request.GET.get('rackets-type')
        rackets_handle_type_id = self.request.GET.get('rackets-handle-type')
        rackets_average_weight_id = self.request.GET.get('rackets-average-weight')
        rackets_rubbers_thickness_id = self.request.GET.get('rackets-rubbers-thickness')
        accessories_brand_id = self.request.GET.get('accessories-brand')
        accessories_type_id = self.request.GET.get('accessories-type')
        accessories_color_id = self.request.GET.get('accessories-color')
        tables_brand_id = self.request.GET.get('tables-brand')
        tables_section_id = self.request.GET.get('tables-section')
        tables_color_id = self.request.GET.get('tables-color')
        tables_thickness_id = self.request.GET.get('tables-thickness')
        if category_id:
            products = Product.objects.filter(category=category_id)
            return products
        elif blades_brand_id:
            products = Product.objects.filter(blade_attribute__brand=blades_brand_id)
            return products
        elif blades_type_id:
            products = Product.objects.filter(blade_attribute__type=blades_type_id)
            return products
        elif blades_handle_type_id:
            products = Product.objects.filter(blade_attribute__handle_type=blades_handle_type_id)
            return products
        elif blades_composition_id:
            products = Product.objects.filter(blade_attribute__composition=blades_composition_id)
            return products
        elif blades_size_id:
            products = Product.objects.filter(blade_attribute__size=blades_size_id)
            return products
        elif rubbers_brand_id:
            products = Product.objects.filter(rubber_attribute__brand=rubbers_brand_id)
            return products
        elif rubbers_type_id:
            products = Product.objects.filter(rubber_attribute__type=rubbers_type_id)
            return products
        elif rubbers_speed_type_id:
            products = Product.objects.filter(rubber_attribute__speed_type=rubbers_speed_type_id)
            return products
        elif balls_brand_id:
            products = Product.objects.filter(ball_attribute__brand=balls_brand_id)
            return products
        elif balls_rank_id:
            products = Product.objects.filter(ball_attribute__rank=balls_rank_id)
            return products
        elif balls_package_id:
            products = Product.objects.filter(ball_attribute__package=balls_package_id)
            return products
        elif bags_brand_id:
            products = Product.objects.filter(bag_attribute__brand=bags_brand_id)
            return products
        elif bags_type_id:
            products = Product.objects.filter(bag_attribute__type=bags_type_id)
            return products
        elif bags_color_id:
            products = Product.objects.filter(bag_attribute__color=bags_color_id)
            return products
        elif nets_brand_id:
            products = Product.objects.filter(net_attribute__brand=nets_brand_id)
            return products
        elif nets_color_id:
            products = Product.objects.filter(net_attribute__color=nets_color_id)
            return products
        elif rackets_brand_id:
            products = Product.objects.filter(racket_attribute__brand=rackets_brand_id)
            return products
        elif rackets_type_id:
            products = Product.objects.filter(racket_attribute__type=rackets_type_id)
            return products
        elif rackets_handle_type_id:
            products = Product.objects.filter(racket_attribute__handle_type=rackets_handle_type_id)
            return products
        elif rackets_average_weight_id:
            products = Product.objects.filter(racket_attribute__average_weight=rackets_average_weight_id)
            return products
        elif rackets_rubbers_thickness_id:
            products = Product.objects.filter(racket_attribute__rubbers_thickness=rackets_rubbers_thickness_id)
            return products
        elif accessories_brand_id:
            products = Product.objects.filter(accessory_attribute__brand=accessories_brand_id)
            return products
        elif accessories_type_id:
            products = Product.objects.filter(accessory_attribute__type=accessories_type_id)
            return products
        elif accessories_color_id:
            products = Product.objects.filter(accessory_attribute__color=accessories_color_id)
            return products
        elif tables_brand_id:
            products = Product.objects.filter(table_attribute__brand=tables_brand_id)
            return products
        elif tables_section_id:
            products = Product.objects.filter(table_attribute__section=tables_section_id)
            return products
        elif tables_color_id:
            products = Product.objects.filter(table_attribute__color=tables_color_id)
            return products
        elif tables_thickness_id:
            products = Product.objects.filter(table_attribute__thickness=tables_thickness_id)
            return products
