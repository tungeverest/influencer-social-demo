from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ops/', include('influencer.apps.demo.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('authen/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(
        "", include("influencer.apps.users.urls")
    ),
    path(
        "", include("influencer.apps.influencers.urls")
    ),
    path(
        "get-token/", obtain_jwt_token
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
