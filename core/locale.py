"""Language support for the portfolio.

Parses Swedish Version/SV-TRANSLATION.txt and provides:
  get_ui(lang)    -> flat dict of UI strings for the given language
  SV_SITE         -> Swedish copy of SITE (built once at import time)
"""
from __future__ import annotations

import copy
from pathlib import Path

# ---------------------------------------------------------------------------
# Parse the Swedish translation file
# ---------------------------------------------------------------------------

_SV_PATH = Path(__file__).resolve().parent.parent / "Swedish Version" / "SV-TRANSLATION.txt"


def _parse_translation_file(path: Path) -> dict:
    strings: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]") and len(stripped) > 2:
            if current_key is not None:
                strings[current_key] = "\n".join(current_lines).strip()
            current_key = stripped[1:-1]
            current_lines = []
        else:
            current_lines.append(line)

    if current_key is not None:
        strings[current_key] = "\n".join(current_lines).strip()

    return strings


_SV: dict[str, str] = _parse_translation_file(_SV_PATH) if _SV_PATH.exists() else {}

# ---------------------------------------------------------------------------
# UI string dictionaries
# ---------------------------------------------------------------------------

_EN_UI: dict[str, str] = {
    "skip_home": "Skip to Content",
    "skip_article": "Skip to article",
    "nav_primary_aria": "Primary",
    "nav_about": "ABOUT",
    "nav_experience": "EXPERIENCE",
    "nav_projects": "PROJECTS",
    "nav_articles": "ARTICLES",
    "section_about": "About",
    "section_experience": "Experience",
    "section_projects": "Projects",
    "section_articles": "Articles",
    "cta_resume": "View Full Résumé",
    "cta_project_archive": "View Full Project Archive",
    "cta_all_articles": "View All Articles",
    "back_home": "← Home",
    "back_all_articles": "← All Articles",
    "page_all_projects": "All Projects",
    "page_all_articles": "All Articles",
    "gallery_suffix": "- Gallery",
    "lightbox_aria": "Project screenshots gallery",
    "lightbox_close": "Close gallery",
    "lightbox_prev": "Previous image",
    "lightbox_next": "Next image",
    "lightbox_thumbs": "Thumbnails",
    "lightbox_view_screenshots": "View {title} screenshots",
    "lightbox_view_project": "View {title}",
    "gallery_viewer_aria": "{title} screenshot viewer",
    "gallery_view_image": "View image {n}",
    "gallery_thumb_nav": "Thumbnail navigation",
    "social_github_aria": "GitHub Profile",
    "social_linkedin_aria": "LinkedIn Profile",
    "social_youtube_aria": "YouTube",
    "social_youtube_title": "YouTube",
    "social_vercel_aria": "Frontend Projects",
    "social_vercel_title": "Frontend Projects",
    "page_frontend_projects": "Frontend Projects",
    "timeline_aria": "Milestone timeline from 2000 through 2025",
    "lang_en": "EN",
    "lang_sv": "SV",
    "lang_switcher_aria": "Switch language",
}

# Mapping from ui-dict key → SV translation file key
_SV_UI_MAP: dict[str, str] = {
    "skip_home": "UI.SKIP.HOME",
    "skip_article": "UI.SKIP.ARTICLE",
    "nav_primary_aria": "UI.NAV.PRIMARY_ARIA",
    "nav_about": "UI.NAV.ABOUT",
    "nav_experience": "UI.NAV.EXPERIENCE",
    "nav_projects": "UI.NAV.PROJECTS",
    "nav_articles": "UI.NAV.ARTICLES",
    "section_about": "UI.SECTION.ABOUT",
    "section_experience": "UI.SECTION.EXPERIENCE",
    "section_projects": "UI.SECTION.PROJECTS",
    "section_articles": "UI.SECTION.ARTICLES",
    "cta_resume": "UI.CTA.VIEW_RESUME",
    "cta_project_archive": "UI.CTA.VIEW_PROJECT_ARCHIVE",
    "cta_all_articles": "UI.CTA.VIEW_ALL_ARTICLES",
    "back_home": "UI.BACK.HOME",
    "back_all_articles": "UI.BACK.ALL_ARTICLES",
    "page_all_projects": "UI.PAGE.ALL_PROJECTS",
    "page_all_articles": "UI.PAGE.ALL_ARTICLES",
    "gallery_suffix": "UI.PAGE.GALLERY_SUFFIX",
    "lightbox_aria": "UI.LIGHTBOX.ARIA",
    "lightbox_close": "UI.LIGHTBOX.CLOSE",
    "lightbox_prev": "UI.LIGHTBOX.PREV",
    "lightbox_next": "UI.LIGHTBOX.NEXT",
    "lightbox_thumbs": "UI.LIGHTBOX.THUMBS",
    "lightbox_view_screenshots": "UI.LIGHTBOX.VIEW_SCREENSHOTS",
    "lightbox_view_project": "UI.LIGHTBOX.VIEW_PROJECT",
    "gallery_viewer_aria": "UI.GALLERY.VIEWER_ARIA",
    "gallery_view_image": "UI.GALLERY.VIEW_IMAGE",
    "gallery_thumb_nav": "UI.GALLERY.THUMB_NAV",
    "social_github_aria": "UI.SOCIAL.GITHUB_ARIA",
    "social_linkedin_aria": "UI.SOCIAL.LINKEDIN_ARIA",
    "social_youtube_aria": "UI.SOCIAL.YOUTUBE_ARIA",
    "social_youtube_title": "UI.SOCIAL.YOUTUBE_TITLE",
    "social_vercel_aria": "UI.SOCIAL.VERCEL_ARIA",
    "social_vercel_title": "UI.SOCIAL.VERCEL_TITLE",
    "page_frontend_projects": "UI.PAGE.FRONTEND_PROJECTS",
    "timeline_aria": "UI.ARTICLE2.TIMELINE_ARIA",
    "lang_en": "UI.LANG.SWITCHER.EN",
    "lang_sv": "UI.LANG.SWITCHER.SV",
    "lang_switcher_aria": "UI.LANG.SWITCHER.ARIA",
}

_SV_UI: dict[str, str] = {
    k: _SV.get(sv_key, _EN_UI[k])
    for k, sv_key in _SV_UI_MAP.items()
}


def get_ui(lang: str) -> dict[str, str]:
    """Return the UI string dict for *lang* ('en' or 'sv')."""
    return _SV_UI if (lang == "sv" and _SV) else _EN_UI


# ---------------------------------------------------------------------------
# Build Swedish SITE dict
# ---------------------------------------------------------------------------


def _build_sv_site(base_site: dict) -> dict:
    site = copy.deepcopy(base_site)

    # About paragraphs
    site["about"] = [
        _SV.get(f"ABOUT.P{i + 1}", p)
        for i, p in enumerate(base_site["about"])
    ]

    # Experience
    for i, exp in enumerate(site["experience"]):
        pfx = f"EXPERIENCE.{i + 1}"
        exp["date"] = _SV.get(f"{pfx}.DATE", exp["date"])
        exp["title"] = _SV.get(f"{pfx}.TITLE", exp["title"])
        exp["org"] = _SV.get(f"{pfx}.ORG", exp["org"])
        exp["bullets"] = [
            _SV.get(f"{pfx}.BULLET.{j + 1}", b)
            for j, b in enumerate(exp.get("bullets") or [])
        ]

    # Projects
    for proj in site["projects"]:
        slug = proj["slug"]
        pfx = f"PROJECT.{slug}"
        proj["title"] = _SV.get(f"{pfx}.TITLE", proj["title"])
        proj["desc"] = _SV.get(f"{pfx}.DESC", proj["desc"])
        if proj.get("highlights"):
            proj["highlights"] = [
                _SV.get(f"{pfx}.HIGHLIGHT.{j + 1}", h)
                for j, h in enumerate(proj["highlights"])
            ]
        proj["thumb_alt"] = _SV.get(f"{pfx}.THUMB_ALT", proj.get("thumb_alt", ""))
        for j, img in enumerate(proj.get("gallery_images") or []):
            if isinstance(img, dict):
                img["alt"] = _SV.get(f"{pfx}.GALLERY_ALT.{j + 1}", img.get("alt", ""))

    # Frontend-only projects (Vercel links page)
    for fp in site.get("frontend_projects") or []:
        pfx = f"FRONTEND_PROJECT.{fp['slug']}"
        fp["title"] = _SV.get(f"{pfx}.TITLE", fp["title"])
        fp["desc"] = _SV.get(f"{pfx}.DESC", fp["desc"])

    # Article 2 page
    art2_pages = site.get("article_pages") or {}
    for art2_slug, art2 in art2_pages.items():
        art2["heading"] = _SV.get("ARTICLE2.HEADING", art2.get("heading", ""))
        art2["description"] = _SV.get("ARTICLE2.DESCRIPTION", art2.get("description", ""))
        for i, item in enumerate(art2.get("items") or []):
            tpfx = f"ARTICLE2.TIMELINE.{i + 1:03d}"
            item["title"] = _SV.get(f"{tpfx}.TITLE", item.get("title", ""))
            item["description"] = _SV.get(f"{tpfx}.DESCRIPTION", item.get("description", ""))
            item["image_alt"] = _SV.get(f"{tpfx}.IMAGE_ALT", item.get("image_alt", ""))

    return site


# Build once at import time (SV strings are static for the lifetime of the process)
from .site_data import SITE as _EN_SITE  # noqa: E402  (avoids circular import at top)

SV_SITE: dict = _build_sv_site(_EN_SITE) if _SV else _EN_SITE
