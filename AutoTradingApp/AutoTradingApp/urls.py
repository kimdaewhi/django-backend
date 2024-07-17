from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login')
]
