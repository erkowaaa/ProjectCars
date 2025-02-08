from django_filters.rest_framework import FilterSet
from .models import *


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'year': ['gt', 'lt']
        }