from django import template

from design.models import DescriptionPost

register = template.Library()


@register.inclusion_tag('design/include/tabgs/top_menu.html')
def get_categories():
    category = DescriptionPost.objects.all()
    return {"list_category": category}