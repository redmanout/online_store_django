from django import template
from store.models import CategoryProduct, BladesProductAttribute, BladesBrand, BladesType, BladesHandleType, \
    BladesComposition, BladesSize, RubbersProductAttribute, RubbersBrand, RubbersType, RubbersSpeedType, \
    BallsProductAttribute, BallsBrand, BallsRank, BallsPackage, BackpacksBagsProductAttribute, BackpacksBagsBrand, \
    BackpacksBagsType, BackpacksBagsColor, NetsColor, NetsBrand, NetsProductAttribute, TablesProductAttribute, \
    TablesBrand, TablesColor, TablesSection, TablesThickness, RacketsProductAttribute, RacketsBrand, RacketsType, \
    RacketsHandleType, RacketsAverageWeight, RacketsRubbersThickness, AccessoriesProductAttribute, AccessoriesBrand, \
    AccessoriesType, AccessoriesColor

register = template.Library()


@register.simple_tag()
def get_phone_contacts():
    phone_numbers_contacts = [
        '+38(098)980-96-21',
        '+38(098)980-96-22',
        '+38(098)980-96-23',
    ]
    return phone_numbers_contacts


@register.simple_tag()
def get_categories():
    return CategoryProduct.objects.all()


@register.simple_tag()
def get_attribute_blades():
    return BladesProductAttribute.objects.all()


@register.simple_tag()
def get_brand_blades():
    return BladesBrand.objects.all()


@register.simple_tag()
def get_type_blades():
    return BladesType.objects.all()


@register.simple_tag()
def get_handle_type_blades():
    return BladesHandleType.objects.all()


@register.simple_tag()
def get_composition_blades():
    return BladesComposition.objects.all()


@register.simple_tag()
def get_size_blades():
    return BladesSize.objects.all()


@register.simple_tag()
def get_attribute_rubbers():
    return RubbersProductAttribute.objects.all()


@register.simple_tag()
def get_brand_rubbers():
    return RubbersBrand.objects.all()


@register.simple_tag()
def get_type_rubbers():
    return RubbersType.objects.all()


@register.simple_tag()
def get_speed_type_rubbers():
    return RubbersSpeedType.objects.all()


@register.simple_tag()
def get_attribute_balls():
    return BallsProductAttribute.objects.all()


@register.simple_tag()
def get_brand_balls():
    return BallsBrand.objects.all()


@register.simple_tag()
def get_rank_balls():
    return BallsRank.objects.all()


@register.simple_tag()
def get_package_balls():
    return BallsPackage.objects.all()


@register.simple_tag()
def get_attribute_backpacksbags():
    return BackpacksBagsProductAttribute.objects.all()


@register.simple_tag()
def get_brand_backpacksbags():
    return BackpacksBagsBrand.objects.all()


@register.simple_tag()
def get_type_backpacksbags():
    return BackpacksBagsType.objects.all()


@register.simple_tag()
def get_color_backpacksbags():
    return BackpacksBagsColor.objects.all()


@register.simple_tag()
def get_attribute_nets():
    return NetsProductAttribute.objects.all()


@register.simple_tag()
def get_brand_nets():
    return NetsBrand.objects.all()


@register.simple_tag()
def get_color_nets():
    return NetsColor.objects.all()


@register.simple_tag()
def get_attribute_tables():
    return TablesProductAttribute.objects.all()


@register.simple_tag()
def get_brand_tables():
    return TablesBrand.objects.all()


@register.simple_tag()
def get_color_tables():
    return TablesColor.objects.all()


@register.simple_tag()
def get_section_tables():
    return TablesSection.objects.all()


@register.simple_tag()
def get_thickness_tables():
    return TablesThickness.objects.all()


@register.simple_tag()
def get_attribute_rackets():
    return RacketsProductAttribute.objects.all()


@register.simple_tag()
def get_brand_rackets():
    return RacketsBrand.objects.all()


@register.simple_tag()
def get_type_rackets():
    return RacketsType.objects.all()


@register.simple_tag()
def get_handle_type_rackets():
    return RacketsHandleType.objects.all()


@register.simple_tag()
def get_average_weight_rackets():
    return RacketsAverageWeight.objects.all()


@register.simple_tag()
def get_rubbers_thickness_rackets():
    return RacketsRubbersThickness.objects.all()


@register.simple_tag()
def get_attribute_accessories():
    return AccessoriesProductAttribute.objects.all()


@register.simple_tag()
def get_brand_accessories():
    return AccessoriesBrand.objects.all()


@register.simple_tag()
def get_type_accessories():
    return AccessoriesType.objects.all()


@register.simple_tag()
def get_color_accessories():
    return AccessoriesColor.objects.all()
