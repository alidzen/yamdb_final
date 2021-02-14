from django_filters.rest_framework import CharFilter, FilterSet, NumberFilter

from .models import Title


class TitleFilter(FilterSet):
    category = CharFilter(field_name='category__slug')
    genre = CharFilter(field_name='genre__slug')
    name = CharFilter(field_name='name', lookup_expr='icontains')
    year = NumberFilter()

    class Meta:
        model = Title
        fields = ['category', 'genre', 'name', 'year']
