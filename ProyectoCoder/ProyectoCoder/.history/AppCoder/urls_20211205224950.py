from django.urls import path
from AppCoder import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', views.inicio)
]