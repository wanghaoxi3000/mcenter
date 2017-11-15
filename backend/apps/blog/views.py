from rest_framework import viewsets
from rest_framework.response import Response

from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
    lookup_field = 'slug'
    lookup_value_regex = r'\w+'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, detail=True)
        return Response(serializer.data)
