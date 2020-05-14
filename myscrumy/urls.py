from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ajayiezekiel9000scrumy/', include("ajayiezekiel9000scrumy.urls")),
    path('admin/', admin.site.urls),
]
