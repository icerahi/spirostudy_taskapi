from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('courses.urls',
         'courses'), namespace='courses')),
    path('api/register/', include(('authentication.urls',
         'authentication'), namespace='authentication')),
    path('api/profile/', include(('accounts.urls',
         'acounts'), namespace='accounts')),

]
