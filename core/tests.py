"""Automated tests for the portfolio website.

The site has no database, so every test is a SimpleTestCase: Django's test client
opens the pages like a browser would and the tests check the answers.
"""

from django.templatetags.static import static
from django.test import SimpleTestCase
from django.urls import reverse

from .site_data import SITE
from .views import _project_with_assets

ARTICLE_PAGES = [
    "article_second",
    "article_third",
    "article_fourth",
    "article_fifth",
    "article_sixth",
    "article_seventh",
    "article_eighth",
]

MAIN_PAGES = ["home", "projects_archive", "frontend_projects", "articles_archive"]

# Projects that have screenshots get their own detail and gallery pages.
PROJECTS_WITH_PAGES = [
    _project_with_assets(project)
    for project in SITE["projects"]
    if _project_with_assets(project)["gallery_images"]
]


def all_page_urls():
    urls = [reverse(name) for name in MAIN_PAGES + ARTICLE_PAGES]
    for project in PROJECTS_WITH_PAGES:
        urls.append(reverse("project_detail", args=[project["slug"]]))
        urls.append(reverse("project_gallery", args=[project["slug"]]))
    return urls


class PagesOpenTests(SimpleTestCase):
    """Every page must open (status 200) in both languages."""

    def test_there_are_pages_to_test(self):
        # Guards against an empty list, which would make
        # the tests below pass without testing anything.
        self.assertGreaterEqual(len(PROJECTS_WITH_PAGES), 1)
        self.assertGreaterEqual(len(all_page_urls()), 20)

    def test_every_page_opens_in_english(self):
        for url in all_page_urls():
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_every_page_opens_in_swedish(self):
        self.client.cookies["portfolio_lang"] = "sv"
        for url in all_page_urls():
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)


class LanguageTests(SimpleTestCase):
    """The EN | SV switch must change the language and send the visitor back."""

    def test_english_is_the_default(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<html lang="en">')

    def test_switch_to_swedish(self):
        response = self.client.get(reverse("set_language"), {"lang": "sv", "next": "/projects/"})
        self.assertRedirects(response, "/projects/", fetch_redirect_response=False)
        self.assertEqual(response.cookies["portfolio_lang"].value, "sv")

        page = self.client.get(reverse("home"))
        self.assertContains(page, '<html lang="sv">')
        self.assertContains(page, "Om mig")

    def test_unknown_language_falls_back_to_english(self):
        response = self.client.get(reverse("set_language"), {"lang": "xx"})
        self.assertEqual(response.cookies["portfolio_lang"].value, "en")

    def test_switch_never_sends_the_visitor_to_another_site(self):
        # "//other-site.example" starts with "/" but a browser reads it as another website.
        for next_url in ["https://other-site.example/", "//other-site.example/"]:
            with self.subTest(next_url=next_url):
                response = self.client.get(
                    reverse("set_language"), {"lang": "en", "next": next_url}
                )
                self.assertEqual(response["Location"], "/")


class ProjectPageTests(SimpleTestCase):
    """A project page must show the project's own screenshots."""

    def test_project_page_shows_its_images(self):
        project = PROJECTS_WITH_PAGES[0]
        response = self.client.get(reverse("project_detail", args=[project["slug"]]))
        self.assertContains(response, project["title"])
        for image in project["gallery_images"]:
            # static() gives the real address, including the file's content hash.
            self.assertContains(response, static(image["src"]))


class NotFoundTests(SimpleTestCase):
    """Unknown addresses must answer 404 (not found), not crash with 500."""

    def test_unknown_page(self):
        self.assertEqual(self.client.get("/this-page-does-not-exist/").status_code, 404)

    def test_unknown_project(self):
        url = reverse("project_detail", args=["no-such-project"])
        self.assertEqual(self.client.get(url).status_code, 404)
