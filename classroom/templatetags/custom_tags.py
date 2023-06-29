from django import template
from ..models import Theory
import datetime

register = template.Library()


@register.inclusion_tag('theory.html')
def theory_list():
    theory = Theory.objects.all()
    return {'theorys': theory}
