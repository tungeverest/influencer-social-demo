from django.urls import path, include
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', IndexView.as_view(),  name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
