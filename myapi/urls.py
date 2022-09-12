from django.urls import include, path
from rest_framework import routers
from myapi.views import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)

urlpatterns = [
   path('', include(router.urls)),
]