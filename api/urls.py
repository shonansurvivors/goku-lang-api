from django.urls import path
from .views import GokuLangView, IndexView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', csrf_exempt(GokuLangView.as_view()), name='api'),
]