
from django.contrib import admin
from django.urls import path, include
from Escola.views import estudantes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudantes/',estudantes),
    path('api-auth/', include('rest_framework.urls'))
]
