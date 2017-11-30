from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.decorators import list_route

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
        query_set = super().get_queryset()
        category = self.request.query_params.get('category', None)
        archive = self.request.query_params.get('archive', None)
        if category is not None:
            query_set = query_set.filter(category__slug=category)
        if archive is not None:
            print('123123', archive)
            if len(archive) != 6:
                raise ParseError
            query_set = query_set.filter(timestamp__year=archive[:4], timestamp__month=archive[4:6])
        return query_set

    def retrieve(self, request, *args, **kwargs):
        """
        获取到文章详情后设置detail=True，排除部分序列化数据
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, detail=True)
        return Response(serializer.data)

    @list_route(url_path='date-archive')
    def date_archive(self, request):
        """
        获取博客归档数据
        """
        archives = []
        timestamp_month = self.queryset.dates('timestamp', 'month', 'DESC')
        for pub in timestamp_month:
            num = self.queryset.filter(timestamp__year=pub.year, timestamp__month=pub.month).count()
            archives.append({'record': '{:d}-{:d}'.format(pub.year, pub.month),  'num': num})

        return Response(archives)
