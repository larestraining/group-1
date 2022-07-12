from random import choice
from django.db import models

from rest_framework import viewsets, serializers
from django.contrib.auth.models import User


choice = (
    ('single', 'single'),
    ('maried', 'married'),
    ('divorced', 'divorced'),
)


   

