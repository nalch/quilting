# from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Tutorial, TutorialStep


class TutorialStepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TutorialStep
        fields = '__all__'
        lookup_field = 'title'


class TutorialSerializer(serializers.HyperlinkedModelSerializer):
    steps = TutorialStepSerializer(many=True, read_only=True)

    class Meta:
        model = Tutorial
        fields = '__all__'
