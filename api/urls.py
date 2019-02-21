from django.urls import path
from .views import GokuLangView, IndexView
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', cache_page(60 * 1440)(IndexView.as_view()), name='index'),
    path('api/', cache_page(60 * 1440)(csrf_exempt(GokuLangView.as_view())), name='api'),
]