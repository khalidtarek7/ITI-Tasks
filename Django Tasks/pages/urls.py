from . import views
from django.urls import path
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.pagesIndex, name = "pagesindex"),
    path('khalid', views.test, name = "renderkhalid"),
    path('base', views.returnBase),
    path('about', views.returnAbout, name = "pagesabout"),
    path('contact', views.returnContact),
    path('cars', views.viewCars)
]