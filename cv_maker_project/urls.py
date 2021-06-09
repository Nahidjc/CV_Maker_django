from Cv_Maker_App import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from Cv_Maker_App.views import home
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Login_App.urls')),
    path('', views.home, name='home'),
    path('cv/', include('Cv_Maker_App.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
