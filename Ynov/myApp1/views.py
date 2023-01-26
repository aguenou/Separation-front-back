from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Artiste,Chanson
from .serializers import ArtisteSerializer

# Create your views here.
class ArtisteAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Artiste.objects.all()
        serializer = ArtisteSerializer(categories, many=True)
        return Response(serializer.data)

class ArtisteViewset(ModelViewSet):
    serializer_class = ArtisteSerializer

    def get_queryset(self):
        queryset = Artiste.objects.all()

        nomT = self.request.GET.get('nom')

        if nomT is not None:
            queryset = queryset.filter(nom=nomT)

        return queryset