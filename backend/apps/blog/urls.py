#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from .views import EntryViewSet

router = DefaultRouter()
router.register(r'articles', EntryViewSet, 'entry')

urlpatterns = router.urls
