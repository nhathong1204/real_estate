from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
# from core.views import serve_media
from real_estate.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = i18n_patterns(
    path("i18n/", include("django.conf.urls.i18n")),
    path("admin/", admin.site.urls),
    path("rosetta/", include("rosetta.urls")),
    path("user/", include("userauths.urls")),
    path("", include("core.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # re_path(r"^media/(?P<path>.*)$", serve_media),
    prefix_default_language=False,
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)