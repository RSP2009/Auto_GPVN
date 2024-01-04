from django import template  # импортируем модуль template для работы с шаблонами
from auto.models import *   # импортируем наши модели из приложения auto

register = template.Library()   # создаем экземпляр класса Library(), через который происходит регистрация
# собственных шаблонных тегов

@register.simple_tag(name = 'getcats')  # декоратор @register.simple_tag превращает функцию get_categories в тег
def get_categories(filter=None):   # создали простой тег, возвращающий список наших категорий
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)  # применили фильтр, с помощью которого возвращается категория
    # c определенным pk


@register.inclusion_tag('auto/list_categories.html')  # декоратор @register.simple_tag
def show_categories(sort=None, cat_selected=0):   # создали включающий тег, который возвращает фрагмент html-страницы
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}
