#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Category, Entry


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='get_entry_count', read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'count')


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.name')
    timestamp = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    html = serializers.CharField(source='get_html_content', read_only=True)

    class Meta:
        model = Entry
        fields = ('url', 'title', 'category', 'slug', 'timestamp', 'html')
        extra_kwargs = {
            'url': {'view_name': 'blog:entry-detail', 'lookup_field': 'slug'}
        }

    def __init__(self, *args, **kwargs):
        # Don't pass the 'detail' arg up to the superclass
        detail = kwargs.pop('detail', False)
        super(EntrySerializer, self).__init__(*args, **kwargs)

        if not detail:
            self.fields.pop('html')
        else:
            self.fields.pop('url')
