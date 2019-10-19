from django import template

register = template.Library()

@register.filter('form_css')
def form_css(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            key, val = d.split(':')
            attrs[key] = val
    return field.as_widget(attrs=attrs)

# @register.filter('form_css1')
# def form_css1(field):
#     exmp = field.as_widget(attrs={'class': 'form-control'})
#     return exmp