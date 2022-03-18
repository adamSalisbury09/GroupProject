from rest_framework import generics

from dogWalkers import models
from api.serializers import walkerSerializer

class ListWalkers(generics.ListCreateAPIView):
    queryset = models.DogWalker.objects.all()
    serializer_class = walkerSerializer
    filterset_fields = ['name', 'acpt_pup']


class DetailWalkers(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DogWalker.objects.all()
    serializer_class = walkerSerializer

