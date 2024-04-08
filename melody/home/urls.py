from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('genre/happy/', views.genre_happy, name='genre_happy'),
    path('genre/lofi/', views.genre_lofi, name='genre_lofi'),
    path('genre/romantic/', views.genre_romantic, name='genre_romantic'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)