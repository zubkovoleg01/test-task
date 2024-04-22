from .serializers import CinemasSerializer
from .models import Cinemas
from django_filters import rest_framework as rest_filters
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet


class CinemasView(ReadOnlyModelViewSet):
    """
    Получение всех кинотеатров
    """
    queryset = Cinemas.objects.all()
    serializer_class = CinemasSerializer


class CinemasSearchView(ReadOnlyModelViewSet):
    """
    Получение кинотеатра/кинотеатров по имени
    """
    serializer_class = CinemasSerializer
    filter_backends = [rest_filters.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'address_full']

    def get_queryset(self):
        queryset = Cinemas.objects.all()
        name_query = self.request.query_params.get('name')
        address_query = self.request.query_params.get('city')

        if name_query:
            queryset = queryset.filter(name__icontains=name_query)
        if address_query:
            queryset = queryset.filter(address_full__icontains=address_query)

        return queryset