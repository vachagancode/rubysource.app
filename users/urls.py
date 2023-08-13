from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'users'
urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name='logout'),
    path('registration_user/', views.registration_user, name='registration')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)