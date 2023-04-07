from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.UsersTable.as_view()),
    path('delete/<int:pk>/', views.UsersDelete.as_view()),
    path('', include('client_config.urls'))
]
