#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import zipfile

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    向数据库中插入初始化博客数据
    """
    help = 'Insert blog data to database'

    def handle(self, *args, **options):
        zip_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'blogmd.zip')
        unzip_path = self.unzip_files(zip_file)

        self.stdout.write('Successfully insert blog data from "%s"' % unzip_path)

    @staticmethod
    def unzip_files(file_path):
        extract_dir = file_path.split('.')[0]
        # extract_path = os.path.abspath(os.path.dirname(file_path))
        # if os.path.exists(extract_dir):
        #     shutil.rmtree(extract_dir)
        zipfp = zipfile.ZipFile(file_path)
        for name in zipfp.namelist():
            utf8name = os.path.join(extract_dir, name.encode('cp437').decode('gbk').encode('utf-8').decode('utf-8'))
            pathname = os.path.dirname(utf8name)
            if not os.path.exists(pathname) and pathname != "":
                os.makedirs(pathname)
            data = zipfp.read(name)
            if not os.path.exists(utf8name):
                fo = open(utf8name, "w", encoding='utf-8')
                fo.write(data.decode('utf-8'))
                fo.close()
        zipfp.close()

        return extract_dir
