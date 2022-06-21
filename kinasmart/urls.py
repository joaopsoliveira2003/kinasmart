from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from website.views import home, services, about, contacts, products, lang
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('services/', services, name='services'),
    path('products/', products, name='products'),
    path('products/category/<int:id>/', products, name='products'),
    path('lang/', lang, name='language'),
    path('admin/', admin.site.urls, name='admin'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True), name='favicon')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
