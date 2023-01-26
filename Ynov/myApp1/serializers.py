from rest_framework.serializers import ModelSerializer
from .models import Artiste,Chanson

class ArtisteSerializer(ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['nom', 'style']

