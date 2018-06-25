# -*- coding: utf-8 -*-
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Tutorial, TutorialStep
from .serializers import TutorialSerializer, TutorialStepSerializer


class TutorialStepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tutorials to be viewed or edited.
    """
    queryset = TutorialStep.objects.all()
    serializer_class = TutorialStepSerializer


class TutorialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tutorials to be viewed or edited.
    """
    queryset = Tutorial.objects.all().order_by('-created_at')
    serializer_class = TutorialSerializer
