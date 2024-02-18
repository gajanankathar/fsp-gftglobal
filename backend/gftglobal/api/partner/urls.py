from rest_framework.routers import DefaultRouter

from api.partner.views import CustomerViewSet

partner_router = DefaultRouter()
partner_router.register('partners', CustomerViewSet, basename='partner')


