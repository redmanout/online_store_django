from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import ReviewForm
from django.contrib import messages
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
        ctx['rubbers_type'] = RubbersType.objects.all().order_by('title')
        ctx['balls_rank'] = BallsRank.objects.all().order_by('title')
        ctx['backpacks_bags_type'] = BackpacksBagsType.objects.all().order_by('title')
        ctx['nets_brand'] = NetsBrand.objects.all().order_by('title')
        ctx['rackets_type'] = RacketsType.objects.all().order_by('title')
        ctx['tables_section'] = TablesSection.objects.all().order_by('title')
        ctx['accessories_type'] = AccessoriesType.objects.all().order_by('title')
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
    paginate_by = 3
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

    def get_queryset(self):
        queryset = super().get_queryset()

        attribute_filters = {
            'blade': {
                'brand': 'blade_attribute__brand',
                'type': 'blade_attribute__type',
                'handle_type': 'blade_attribute__handle_type',
                'composition': 'blade_attribute__composition',
                'size': 'blade_attribute__size',
            },
            'rubber': {
                'brand': 'rubber_attribute__brand',
                'type': 'rubber_attribute__type',
                'speed_type': 'rubber_attribute__speed_type',
            },
            'ball': {
                'brand': 'ball_attribute__brand',
                'rank': 'ball_attribute__rank',
                'package': 'ball_attribute__package',
            },
            'bag': {
                'brand': 'bag_attribute__brand',
                'type': 'bag_attribute__type',
                'color': 'bag_attribute__color',
            },
            'net': {
                'brand': 'net_attribute__brand',
                'color': 'net_attribute__color',
            },
            'racket': {
                'brand': 'racket_attribute__brand',
                'type': 'racket_attribute__type',
                'handle_type': 'racket_attribute__handle_type',
                'average_weight': 'racket_attribute__average_weight',
                'rubbers_thickness': 'racket_attribute__rubbers_thickness',
            },
            'accessory': {
                'brand': 'accessory_attribute__brand',
                'type': 'accessory_attribute__type',
                'color': 'accessory_attribute__color',
            },
            'table': {
                'brand': 'table_attribute__brand',
                'section': 'table_attribute__section',
                'color': 'table_attribute__color',
                'thickness': 'table_attribute__thickness',
            }
        }

        """В переменную filters будет сохраняться словарь, содержащий фильтры, которые будут использоваться
        для фильтрации продуктов. Перебор параметров GET-запроса и их значений. Если ключ является "category",
        то сохраняем его значение в словарь фильтров. Если ключ не является "category", то проходим по списку
        атрибутов, определенных в переменной attribute_filters. Если ключ начинается с типа атрибута, то проверяем
        каждый атрибут в этом типе. Если ключ оканчивается конкретным атрибутом, то сохраняем его значение в словарь
        фильтров, используя соответствующий ключ фильтра. Мы также добавляем 'available_status' в словарь,
        чтобы показать, что мы ищем только товары, которые доступны в наличии. Если словарь фильтров не пуст,
        то используем его для фильтрации объектов модели Product и сохраняем результат в переменную queryset."""
        filters = {}

        for key in self.request.GET:
            value = self.request.GET.get(key)
            if key == 'category':
                filters['category'] = value
            else:
                for attribute_type, attribute_map in attribute_filters.items():
                    if key.startswith(attribute_type):
                        for attribute, filter_key in attribute_map.items():
                            if key.endswith(attribute):
                                filters[filter_key] = value
                                filters['available_status'] = True
        if filters:
            queryset = Product.objects.filter(**filters)

        return queryset


class Probe(ListView):
    model = Product
    template_name = 'store/probe.html'
    context_object_name = 'probe'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
