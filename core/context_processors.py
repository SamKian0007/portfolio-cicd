"""Template context processor: inject lang and ui strings into every template."""
from .locale import get_ui


def lang_context(request):
    lang = request.COOKIES.get("portfolio_lang", "en")
    if lang not in ("en", "sv"):
        lang = "en"
    return {
        "lang": lang,
        "html_lang": lang,
        "ui": get_ui(lang),
    }
