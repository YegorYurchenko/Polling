from django import template

register = template.Library()

@register.filter(name='split')
def split(value: str) -> list[str]:
    return value.split('\n')

@register.filter
def split_space_for_result(value: str) -> list[str]:
    """ Преобразование количества голосов в проценты """
    value_list = list(map(int, value.split(' ')))
    sum_value_list = sum(value_list)

    if sum_value_list > 0:
        value_list = list(map(lambda x: round((x / sum_value_list * 100), 1), value_list))
        
    value_list = list(map(lambda x: str(x) + '%', value_list))
    return value_list
