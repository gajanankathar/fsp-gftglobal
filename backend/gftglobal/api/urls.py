from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.partner.views import CustomerCreateView
from api.partner.urls import partner_router

router = DefaultRouter()

router.registry.extend(partner_router.registry)

urlpatterns = [
    path('account/', include('api.account.urls')),
    path('create/partner/', CustomerCreateView.as_view(), name="create-partner")
] + router.urls
