from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from campaigns.views import CampaignViewSet

router = DefaultRouter()
router.register(r'campaigns', CampaignViewSet, basename='campaign')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
