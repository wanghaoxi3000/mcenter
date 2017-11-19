from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Entry
from .serializers import CategorySerializer, EntrySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    文章类别ViewSet
    """
    pagination_class = None
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EntryViewSet(viewsets.ModelViewSet):
    """
    博客文章ViewSet
    """
    serializer_class = EntrySerializer
    queryset = Entry.objects.all().filter(published=True)
    lookup_field = 'slug'
    lookup_value_regex = r'\w+'

    def get_queryset(self):
        """
        根据参数过滤文章条目
        """
        category = self.request.query_params.get('category', None)
        if category is not None:
            print(category)
            return super().get_queryset().filter(category__slug=category)
        else:
            return super().get_queryset()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, detail=True)
        return Response(serializer.data)
