from django import template
from django.utils.safestring import mark_safe
from django.template.loader import get_template
from ..models import Category, SubCategory
# from ..views import html_path
from decouple import config


# def get_banner_data():
#     banner = Banner.objects.all().order_by('banner_type')
#     return {
#         "banner":banner
#     }
register = template.Library()

@register.simple_tag
def get_category():
    category = Category.objects.all()
    data = ''
    for i in category:
        # if i.image:
        #     data += f"<li><a href='{i.slug}'><img src='{i.image.url}' alt=''>{i.name}</a></li>"
        # else:
        data += f"<li><a href='{i.slug}'><img src='/static/home/images/mega-store/header-category/1.png' alt=''>{i.name}</a></li>"
    
    if not category:
        data += f"<li><a href='#'><img src='/static/home/images/mega-store/header-category/1.png' alt=''>Not found!</a></li>"

    return mark_safe(data)

@register.simple_tag
def get_sub_category():
    sub_category = SubCategory.objects.all().values('name').distinct()
    data = ''
    # print(sub_category)
    for i in sub_category:
        data += f"""<option value={i['name']}>{i['name']}</option>"""
    return mark_safe(data)

@register.simple_tag
def currency():
    return config('CURRENCY')
