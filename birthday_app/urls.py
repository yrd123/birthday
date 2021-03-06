from django.urls import path
from . import views,urls
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('wish', views.wish,name="wish"),
    path('photos', views.photos,name="photos"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)