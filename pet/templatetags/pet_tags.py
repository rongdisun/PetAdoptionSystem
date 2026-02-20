from django import template

from pet.models import PetCategory

register = template.Library()


@register.simple_tag
def get_all_cate():
    return PetCategory.objects.all()
