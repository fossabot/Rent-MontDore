from django import template

register = template.Library()

@register.filter(name='get_value_from_dict')
def get_value_from_dict(dict_data, key):
    return dict_data[int(key)]

register.filter('get_value_from_dict', get_value_from_dict)
