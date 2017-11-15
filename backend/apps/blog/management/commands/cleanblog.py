#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand

from blog.models import Category, Entry


class Command(BaseCommand):
    """
    清空博客数据
    """
    help = 'Clean blog database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Entry.objects.all().delete()
