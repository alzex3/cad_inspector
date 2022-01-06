from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Facility, List, FacilityType
from .serializers import FacilityTypeSerializer, FacilitySerializer
from .main import main, api


class FacilityTypeViewSet(ModelViewSet):
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer


class FacilityViewSet(ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


@api_view(['GET'])
def hello(request):
    get_extra_actions = []
    print(request)
    if request.method == 'GET':
        return Response({"message": "Got some data!"})
    return Response({"message": "Hello, world!"})
