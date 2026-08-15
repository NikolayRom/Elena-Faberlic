from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class DynamicPagesSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['home', 'news', 'about-products']

    def location(self, item):
        return reverse(item)

class StaticInfoPagesSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return ['money-by-phone', 'work-as-leader', 'family-shopping']

    def location(self, item):
        return reverse(item)