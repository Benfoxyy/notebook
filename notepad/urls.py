from django.contrib import admin
from django.urls import path,include
from django.contrib.sitemaps.views import sitemap
from stickynote.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('stickynote.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
]