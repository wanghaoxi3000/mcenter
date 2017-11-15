#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Entry


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.name')
    timestamp = serializers.DateTimeField(format='%y-%m-%d %H:%M:%S')
    html = serializers.CharField(source='get_html_content', read_only=True)

    class Meta:
        model = Entry
        fields = ('url', 'title', 'category', 'timestamp', 'html')
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
