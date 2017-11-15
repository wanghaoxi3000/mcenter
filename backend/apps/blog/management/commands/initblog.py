#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from django.core.management.base import BaseCommand

from backend.settings import BASE_DIR
from blog.models import Category, Entry


class Command(BaseCommand):
    """
    向数据库中插入初始化博客数据
    """
    help = 'Insert blog data to database'

    def handle(self, *args, **options):
        data_path = os.path.join(BASE_DIR, 'init')
        for dirpath, dirnames, filenames in os.walk(data_path):
            if len(filenames) > 0:
                if len(dirnames) == 0:
                    cate, created = Category.objects.get_or_create(name=dirpath.split(os.sep)[-1])
                    published = True
                else:
                    cate = None
                    published = False

                for item in filenames:
                    own = True if item.find('[转载]') < 0 else False
                    with open(os.path.join(dirpath, item), encoding='utf8') as f:
                        time = os.path.getmtime(os.path.join(dirpath, item))
                        timestamp = datetime.utcfromtimestamp(time)
                        Entry.objects.create(category=cate, own=own, published=published, timestamp=timestamp,
                                             title=item, content=f.read())

        self.stdout.write('Successfully insert blog data')
