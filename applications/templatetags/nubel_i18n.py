from django import template
from nubel_project.translations import tr as _tr, status_label as _status

register = template.Library()


def _lang(context):
    request = context.get("request")
    if request is not None:
        return request.session.get("lang", "uz")
    return "uz"


@register.simple_tag(takes_context=True)
def t(context, key, **kwargs):
    return _tr(key, _lang(context), **kwargs)


@register.simple_tag(takes_context=True)
def status_label(context, value):
    return _status(value, _lang(context))
