from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.base import View

from .forms import ReviewForm
from .models import BladesProductAttribute, BladesBrand, BladesType, BladesHandleType, BladesComposition, BladesSize, \
    RubbersProductAttribute, RubbersBrand, RubbersType, RubbersSpeedType, BallsProductAttribute, BallsBrand, BallsRank, \
    BallsPackage, BackpacksBagsProductAttribute, BackpacksBagsBrand, BackpacksBagsType, BackpacksBagsColor, \
    NetsProductAttribute, NetsBrand, NetsColor, TablesProductAttribute, TablesBrand, TablesColor, TablesSection, \
    TablesThickness, RacketsProductAttribute, RacketsBrand, RacketsType, RacketsHandleType, RacketsAverageWeight, \
    RacketsRubbersThickness, AccessoriesProductAttribute, AccessoriesBrand, AccessoriesType, AccessoriesColor, \
    CategoryProduct, Product


# Create your views here.

class BladesAttributeProduct:
    def get_attribute_blades(self):
        return BladesProductAttribute.objects.all()

    def get_brand_blades(self):
        return BladesBrand.objects.all()

    def get_type_blades(self):
        return BladesType.objects.all()

    def get_handle_type_blades(self):
        return BladesHandleType.objects.all()

    def get_composition_blades(self):
        return BladesComposition.objects.all()

    def get_size_blades(self):
        return BladesSize.objects.all()


class RubbersAttributeProduct:
    def get_attribute_rubbers(self):
        return RubbersProductAttribute.objects.all()

    def get_brand_rubbers(self):
        return RubbersBrand.objects.all()

    def get_type_rubbers(self):
        return RubbersType.objects.all()

    def get_speed_type_rubbers(self):
        return RubbersSpeedType.objects.all()


class BallsAttributeProduct:
    def get_attribute_balls(self):
        return BallsProductAttribute.objects.all()

    def get_brand_balls(self):
        return BallsBrand.objects.all()

    def get_rank_balls(self):
        return BallsRank.objects.all()

    def get_package_balls(self):
        return BallsPackage.objects.all()


class BackpacksBagsAttributeProduct:
    def get_attribute_backpacksbags(self):
        return BackpacksBagsProductAttribute.objects.all()

    def get_brand_backpacksbags(self):
        return BackpacksBagsBrand.objects.all()

    def get_type_backpacksbags(self):
        return BackpacksBagsType.objects.all()

    def get_color_backpacksbags(self):
        return BackpacksBagsColor.objects.all()


class NetsAttributeProduct:
    def get_attribute_nets(self):
        return NetsProductAttribute.objects.all()

    def get_brand_nets(self):
        return NetsBrand.objects.all()

    def get_color_nets(self):
        return NetsColor.objects.all()


class TablesAttributeProduct:
    def get_attribute_tables(self):
        return TablesProductAttribute.objects.all()

    def get_brand_tables(self):
        return TablesBrand.objects.all()

    def get_color_tables(self):
        return TablesColor.objects.all()

    def get_section_tables(self):
        return TablesSection.objects.all()

    def get_thickness_tables(self):
        return TablesThickness.objects.all()


class RacketsAttributeProduct:
    def get_attribute_rackets(self):
        return RacketsProductAttribute.objects.all()

    def get_brand_rackets(self):
        return RacketsBrand.objects.all()

    def get_type_rackets(self):
        return RacketsType.objects.all()

    def get_handle_type_rackets(self):
        return RacketsHandleType.objects.all()

    def get_average_weight_rackets(self):
        return RacketsAverageWeight.objects.all()

    def get_rubbers_thickness_rackets(self):
        return RacketsRubbersThickness.objects.all()


class AccessoriesAttributeProduct:
    def get_attribute_accessories(self):
        return AccessoriesProductAttribute.objects.all()

    def get_brand_accessories(self):
        return AccessoriesBrand.objects.all()

    def get_type_accessories(self):
        return AccessoriesType.objects.all()

    def get_color_accessories(self):
        return AccessoriesColor.objects.all()


class CategoryList(
    BladesAttributeProduct,
    RubbersAttributeProduct,
    BallsAttributeProduct,
    BackpacksBagsAttributeProduct,
    NetsAttributeProduct,
    TablesAttributeProduct,
    RacketsAttributeProduct,
    AccessoriesAttributeProduct,
    ListView
):
    model = CategoryProduct
    template_name = 'store/home.html'
    context_object_name = 'categories_product'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['product_bestseller'] = Product.objects.filter(bestseller=True)
        ctx['product_new'] = Product.objects.filter(new=True)
        ctx['product_stock'] = Product.objects.filter(stock=True)
        ctx['phone_numbers_contacts'] = [
            '+38(098)980-96-21',
            '+38(098)980-96-22',
            '+38(098)980-96-23',
        ]
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
    list_phone = [
        '+38(098)980-96-21'
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
