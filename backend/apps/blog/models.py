from datetime import datetime

from django.db import models


class Category(models.Model):
    """
    每篇文章属于一个类别
    """
    name = models.CharField('名称', max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.name


class Entry(models.Model):
    """
    博客文章
    """
    owner = ((True, '原创'), (False, '转载'))
    publish = ((True, '发布'), (False, '草稿'))

    category = models.ForeignKey(Category, verbose_name='类别')
    own = models.BooleanField('属性', choices=owner, default=True)
    published = models.BooleanField('状态', choices=publish, default=False)
    title = models.CharField('标题', max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField('内容')
    timestamp = models.DateTimeField('发布时间', default=datetime.now, db_index=True)
    read_num = models.IntegerField('阅读次数', default=0, editable=False)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-timestamp', 'title']
        unique_together = ('title', 'category')

    def __str__(self):
        return '%s' % self.title
