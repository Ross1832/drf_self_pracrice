from django.contrib import admin
from django.urls import path
from women.views import WomenAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist', WomenAPIView.as_view())
]
