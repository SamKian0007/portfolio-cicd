from datetime import date
from pathlib import Path

from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.templatetags.static import static
from .locale import SV_SITE, get_ui
from .site_data import (
    ARTICLE_EIGHTH_SLUG,
    ARTICLE_FIFTH_SLUG,
    ARTICLE_FOURTH_SLUG,
    ARTICLE_SECOND_SLUG,
    ARTICLE_SEVENTH_SLUG,
    ARTICLE_SIXTH_SLUG,
    ARTICLE_THIRD_SLUG,
    SITE,
)


def _get_lang(request) -> str:
    lang = request.COOKIES.get("portfolio_lang", "en")
    return lang if lang in ("en", "sv") else "en"


def _get_site(lang: str) -> dict:
    return SV_SITE if lang == "sv" else SITE


def set_language(request):
    """Set the language cookie and redirect back to the referring page."""
    lang = request.GET.get("lang", "en")
    if lang not in ("en", "sv"):
        lang = "en"
    next_url = request.GET.get("next") or "/"
    if not next_url.startswith("/"):
        next_url = "/"
    response = HttpResponseRedirect(next_url)
    response.set_cookie(
        "portfolio_lang",
        lang,
        max_age=365 * 24 * 3600,
        samesite="Lax",
        httponly=False,
    )
    return response

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}

# Article 2 horizontal axis only - fixed range (inclusive) for scale and point math.
ARTICLE2_AXIS_START = date(2000, 1, 1)
ARTICLE2_AXIS_END = date(2025, 12, 31)


def _article2_axis_span_days():
    return (ARTICLE2_AXIS_END - ARTICLE2_AXIS_START).days


def _clamp_article2_axis_date(d):
    if d < ARTICLE2_AXIS_START:
        return ARTICLE2_AXIS_START
    if d > ARTICLE2_AXIS_END:
        return ARTICLE2_AXIS_END
    return d


def _article2_date_to_position_pct(d, *, inset_pct=3.0):
    inner = max(0.0, 100.0 - (2 * inset_pct))
    span = _article2_axis_span_days()
    if span <= 0:
        return round(inset_pct + inner / 2.0, 4)
    dc = _clamp_article2_axis_date(d)
    ratio = (dc - ARTICLE2_AXIS_START).days / span
    ratio = max(0.0, min(1.0, ratio))
    return round(inset_pct + inner * ratio, 4)


def _article2_year_axis_ticks(*, inset_pct=3.0):
    """One tick per calendar year 2000–2025 at Jan 1 on the same scale as milestones."""
    ticks = []
    for year in range(2000, 2026):
        ticks.append({
            "year": year,
            "position_pct": _article2_date_to_position_pct(date(year, 1, 1), inset_pct=inset_pct),
        })
    return ticks


# Vertical lanes for crowded milestones (0-based index; horizontal % unchanged).
# Default is 0 for indices not listed. Extra separation added for: Google App Engine (4),
# Elasticsearch (11), Zero Trust Architecture (14), Linkerd 2.0 (42) per layout passes.
ARTICLE2_MARKER_TRANSLATE_Y_PX = {
    4: -18,
    5: -18,
    9: -18,
    10: -36,
    11: -34,
    12: -18,
    14: -12,
    20: -18,
    21: -36,
    23: -18,
    26: -18,
    27: -36,
    28: -54,
    31: -18,
    32: -36,
    34: -18,
    38: -18,
    39: -36,
    40: -54,
    42: -36,
    43: -36,
    44: -54,
    46: -18,
    47: -36,
    50: -18,
    51: -36,
    54: -18,
}


def _parse_article2_timeline_date(raw):
    """Map Article 2 `date` strings to calendar dates for axis positioning (Article 2 only).

    Supported: `YYYY` (Jan 1 of that year), `YYYY-MM` (first day of that month).
    Month may be one or two digits after split (e.g. 2006-03 or normalized 2006-3 in data).
    """
    if raw is None:
        return None
    s = str(raw).strip()
    if not s:
        return None
    if len(s) == 4 and s.isdigit():
        y = int(s)
        if 1 <= y <= 9999:
            return date(y, 1, 1)
        return None
    parts = s.split("-", 2)
    if len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
        y, m = int(parts[0]), int(parts[1])
        if 1 <= y <= 9999 and 1 <= m <= 12:
            return date(y, m, 1)
    return None


def _article2_plain_description(text):
    """Strip Markdown bold markers from milestone blurbs (legacy ** around Example sections)."""
    if not text or not isinstance(text, str):
        return text
    return text.replace("**", "")


def _article2_items_axis_positions(items, *, inset_pct=3.0):
    """Place each milestone on fixed 2000-01-01 .. 2025-12-31 axis (Article 2 only)."""
    inner = max(0.0, 100.0 - (2 * inset_pct))
    mid = inset_pct + inner / 2.0
    out = []
    for idx, item in enumerate(items):
        row = dict(item)
        row["description"] = _article2_plain_description(
            row.get("description"))
        d = _parse_article2_timeline_date(item.get("date"))
        if d is None:
            pct = mid
        else:
            pct = _article2_date_to_position_pct(d, inset_pct=inset_pct)
        nudge = item.get("position_pct_nudge")
        if nudge is not None:
            try:
                pct = pct + float(nudge)
            except (TypeError, ValueError):
                pass
        row["position_pct"] = round(max(0.0, min(100.0, pct)), 4)
        y_px = ARTICLE2_MARKER_TRANSLATE_Y_PX.get(idx, 0)
        dy = item.get("marker_translate_y_delta_px")
        if dy is not None:
            try:
                y_px += int(dy)
            except (TypeError, ValueError):
                pass
        row["marker_translate_y_px"] = y_px
        try:
            row["marker_translate_x_px"] = int(
                item.get("marker_translate_x_px", 0))
        except (TypeError, ValueError):
            row["marker_translate_x_px"] = 0
        out.append(row)
    return out


def _project_gallery_images(project):
    explicit_images = project.get("gallery_images")
    if explicit_images:
        images = []
        for image in explicit_images:
            src = image.get("src")
            if not src:
                continue
            images.append({
                "src": src,
                "alt": image.get("alt") or f"{project['title']} screenshot",
            })
        return images

    gallery_dir = project.get("gallery_dir")
    if not gallery_dir:
        return []

    gallery_path = Path(settings.BASE_DIR) / "static" / gallery_dir
    if not gallery_path.exists() or not gallery_path.is_dir():
        return []

    images = []
    for image_path in sorted(gallery_path.iterdir()):
        if image_path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        if "copy" in image_path.stem.lower():
            continue
        relative_path = image_path.relative_to(
            Path(settings.BASE_DIR) / "static").as_posix()
        images.append({
            "src": relative_path,
            "alt": f"{project['title']} screenshot",
        })
    return images


def _project_with_assets(project):
    item = dict(project)
    item["gallery_images"] = _project_gallery_images(project)
    return item


def _projects_with_gallery_data(site_data=None, *, featured_only=False, limit=None):
    if site_data is None:
        site_data = SITE
    projects = [_project_with_assets(project) for project in site_data["projects"]]
    if featured_only:
        projects = [p for p in projects if p.get("featured")]
    if limit is not None:
        projects = projects[:limit]
    gallery_data = []
    for p in projects:
        if p.get("gallery_images"):
            gallery_data.append([
                {"url": static(img["src"]), "alt": img.get(
                    "alt") or "Screenshot"}
                for img in p["gallery_images"]
            ])
        else:
            gallery_data.append(None)
    return projects, gallery_data


def _featured_writing(site_data=None, *, limit=4):
    if site_data is None:
        site_data = SITE
    items = site_data.get("writing", [])
    featured = [w for w in items if w.get("featured")]
    return featured[:limit]


def home(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    projects, gallery_data = _projects_with_gallery_data(site, featured_only=True, limit=4)

    ctx = {
        "profile": site["profile"],
        "social": site["social"],
        "about_paragraphs": site["about"],
        "experience": site["experience"],
        "projects": projects,
        "gallery_data": gallery_data,
        "writing": _featured_writing(site, limit=4),
        "resume_path": site.get("resume_sv") if lang == "sv" else site.get("resume"),
        "article_second": (site.get("article_pages") or {}).get(ARTICLE_SECOND_SLUG),
        "article_third": (site.get("article_documents") or {}).get(ARTICLE_THIRD_SLUG),
        "article_fourth": (site.get("article_documents") or {}).get(ARTICLE_FOURTH_SLUG),
    }
    return render(request, "core/home.html", ctx)


def projects_archive(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    projects, gallery_data = _projects_with_gallery_data(site)
    return render(request, "core/projects_archive.html", {
        "profile": site["profile"],
        "projects": projects,
        "gallery_data": gallery_data,
    })


def frontend_projects(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    return render(request, "core/frontend_projects.html", {
        "profile": site["profile"],
        "frontend_projects": site.get("frontend_projects", []),
    })


def articles_archive(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    return render(request, "core/articles_archive.html", {
        "profile": site["profile"],
        "writing": site.get("writing", []),
        "article_second": (site.get("article_pages") or {}).get(ARTICLE_SECOND_SLUG),
        "article_third": (site.get("article_documents") or {}).get(ARTICLE_THIRD_SLUG),
        "article_fourth": (site.get("article_documents") or {}).get(ARTICLE_FOURTH_SLUG),
        "article_fifth": (site.get("article_documents") or {}).get(ARTICLE_FIFTH_SLUG),
        "article_sixth": (site.get("article_documents") or {}).get(ARTICLE_SIXTH_SLUG),
        "article_seventh": (site.get("article_documents") or {}).get(ARTICLE_SEVENTH_SLUG),
        "article_eighth": (site.get("article_documents") or {}).get(ARTICLE_EIGHTH_SLUG),
    })


def article_third(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    docs = site.get("article_documents") or {}
    article = docs.get(ARTICLE_THIRD_SLUG)
    if not article:
        raise Http404("Article not found")

    return render(request, "core/article3.html", {
        "profile": site["profile"],
        "article": article,
    })


def article_fourth(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    docs = site.get("article_documents") or {}
    article = docs.get(ARTICLE_FOURTH_SLUG)
    if not article:
        raise Http404("Article not found")

    return render(request, "core/article4.html", {
        "profile": site["profile"],
        "article": article,
    })


def article_fifth(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    docs = site.get("article_documents") or {}
    article = docs.get(ARTICLE_FIFTH_SLUG)
    if not article:
        raise Http404("Article not found")

    return render(request, "core/article5.html", {
        "profile": site["profile"],
        "article": article,
    })


def article_sixth(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    docs = site.get("article_documents") or {}
    article = docs.get(ARTICLE_SIXTH_SLUG)
    if not article:
        raise Http404("Article not found")

    return render(request, "core/article6.html", {
        "profile": site["profile"],
        "article": article,
    })


def article_seventh(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    docs = site.get("article_documents") or {}
    article = docs.get(ARTICLE_SEVENTH_SLUG)
    if not article:
        raise Http404("Article not found")

    return render(request, "core/article7.html", {
        "profile": site["profile"],
        "article": article,
    })


def article_eighth(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    docs = site.get("article_documents") or {}
    article = docs.get(ARTICLE_EIGHTH_SLUG)
    if not article:
        raise Http404("Article not found")

    return render(request, "core/article8.html", {
        "profile": site["profile"],
        "article": article,
    })


def article_second(request):
    lang = _get_lang(request)
    site = _get_site(lang)
    pages = site.get("article_pages") or {}
    article = pages.get(ARTICLE_SECOND_SLUG)
    if not article:
        raise Http404("Article not found")

    items_raw = article.get("items") or []
    timeline_items = _article2_items_axis_positions(items_raw)
    article_horizontal_payload = []
    for item in timeline_items:
        row = {
            "date": item.get("date", "") or "",
            "title": item.get("title", "") or "",
            "description": item.get("description", "") or "",
            "image_alt": item.get("image_alt", "") or "",
        }
        img = item.get("image")
        row["image"] = static(img) if img else ""
        article_horizontal_payload.append(row)

    return render(request, "core/article_timeline_horizontal.html", {
        "profile": site["profile"],
        "article": article,
        "timeline_items": timeline_items,
        "article_horizontal_payload": article_horizontal_payload,
        "article2_year_ticks": _article2_year_axis_ticks(),
    })


def project_detail(request, slug):
    lang = _get_lang(request)
    site = _get_site(lang)
    project = next(
        (item for item in site["projects"] if item.get("slug") == slug), None)
    if not project:
        raise Http404("Project not found")

    project = _project_with_assets(project)
    if not project["gallery_images"]:
        raise Http404("Project gallery not found")

    return render(request, "core/project_detail.html", {
        "profile": site["profile"],
        "project": project,
    })


def project_gallery(request, slug):
    """Dedicated gallery viewer for projects with ordered screenshots (e.g. LogInsight)."""
    lang = _get_lang(request)
    site = _get_site(lang)
    project = next(
        (item for item in site["projects"] if item.get("slug") == slug), None)
    if not project:
        raise Http404("Project not found")

    project = _project_with_assets(project)
    if not project["gallery_images"]:
        raise Http404("Project gallery not found")

    return render(request, "core/project_gallery.html", {
        "profile": site["profile"],
        "project": project,
    })
