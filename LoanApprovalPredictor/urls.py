from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from Register import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', include("main.urls")),
    path('',include("django.contrib.auth.urls")),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

