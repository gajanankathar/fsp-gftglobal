from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.partner.serializers import CustomerSerializer
from partner.models import Customer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ('get', 'put')
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user.customer
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CustomerCreateView(CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = (permissions.AllowAny,)
