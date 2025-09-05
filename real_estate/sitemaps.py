from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        # List of static URL names
        return ["core:index", "core:about", "core:contact"]

    def location(self, item):
        return reverse(item)