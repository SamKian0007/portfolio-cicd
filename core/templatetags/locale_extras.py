"""Custom template filters for locale string interpolation."""
from django import template

register = template.Library()


@register.filter
def locfmt(fmt_string, value):
    """Replace {title} or {n} placeholder in a UI format string with *value*.

    Usage:
        {{ ui.lightbox_view_screenshots|locfmt:p.title }}
        {{ ui.gallery_view_image|locfmt:forloop.counter }}
    """
    try:
        return str(fmt_string).replace("{title}", str(value)).replace("{n}", str(value))
    except Exception:
        return fmt_string
