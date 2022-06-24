from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *
s=serializers.Serializer
class AktyorSer(s):
    class Meta:
        model=Aktyor
        fields="__all__"

class KinoSer(s):
    class Meta:
        model=Kino
        fields="__all__"