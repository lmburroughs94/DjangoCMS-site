from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from . import views

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('', views.base, name='base'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),  
    path('faq', views.faq, name='faq'),  
    path('blog-home', views.blog_home, name='blog-home'), 
    path('blog-post', views.blog_post, name='blog-post'), 
    path('blog-list', views.blog_list, name='blog-list'), 
    path('portfolio-overview', views.portfolio_overview, name='portfolio-overview'), 
    path('portfolio-item', views.portfolio_item, name='portfolio-item'),
    
    path('First_Blog', views.First_Blog, name='First_Blog'), 
]


urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
