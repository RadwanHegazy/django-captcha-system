from main_app import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('session/create/',views.create_session,name='create_session'),
    path('session/start/<str:sessionuuid>/',views.session,name='session'),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
