from django.urls import path

from .site_data import (
    ARTICLE_EIGHTH_SLUG,
    ARTICLE_FIFTH_SLUG,
    ARTICLE_FOURTH_SLUG,
    ARTICLE_SECOND_SLUG,
    ARTICLE_SEVENTH_SLUG,
    ARTICLE_SIXTH_SLUG,
    ARTICLE_THIRD_SLUG,
)
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("set-language/", views.set_language, name="set_language"),
    path("projects/", views.projects_archive, name="projects_archive"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("projects/<slug:slug>/gallery/",
         views.project_gallery, name="project_gallery"),
    path("frontend-projects/", views.frontend_projects, name="frontend_projects"),
    path("articles/", views.articles_archive, name="articles_archive"),
    path(
        f"articles/{ARTICLE_SECOND_SLUG}/",
        views.article_second,
        name="article_second",
    ),
    path(
        f"articles/{ARTICLE_EIGHTH_SLUG}/",
        views.article_eighth,
        name="article_eighth",
    ),
    path(
        f"articles/{ARTICLE_SEVENTH_SLUG}/",
        views.article_seventh,
        name="article_seventh",
    ),
    path(
        f"articles/{ARTICLE_SIXTH_SLUG}/",
        views.article_sixth,
        name="article_sixth",
    ),
    path(
        f"articles/{ARTICLE_FIFTH_SLUG}/",
        views.article_fifth,
        name="article_fifth",
    ),
    path(
        f"articles/{ARTICLE_FOURTH_SLUG}/",
        views.article_fourth,
        name="article_fourth",
    ),
    path(
        f"articles/{ARTICLE_THIRD_SLUG}/",
        views.article_third,
        name="article_third",
    ),
]
