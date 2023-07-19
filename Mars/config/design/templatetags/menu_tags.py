from django import template

from design.models import Category

register = template.Library()


#@register.simple_tag()#передача контекста в шаблон
#def get_categories():
#    return Category.objects.all()

@register.inclusion_tag('design/include/tags/top_menu.html')#рендерит  контекста в шаблон
def get_categories():
    category = Category.objects.all()
    #category = Category.objects.filter()
    return {"list_category": category}