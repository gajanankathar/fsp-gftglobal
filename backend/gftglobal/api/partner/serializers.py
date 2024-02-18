from rest_framework.serializers import ModelSerializer

from partner.models import Customer


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ('user',)
