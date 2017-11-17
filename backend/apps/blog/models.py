import re
from datetime import datetime

from django.db import models
from markdown import markdown
from pypinyin import lazy_pinyin


class Category(models.Model):
    """
    每篇文章属于一个类别
    """
    name = models.CharField('名称', max_length=255, unique=True)
    slug = models.SlugField(unique=True, max_length=100)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.name

    def save(self, *args, **kwargs):
        """
        自动生成拼音slug
        """
        name_pinyin = lazy_pinyin(self.name)
        self.slug = '_'.join(name_pinyin)[:100]
        super(Category, self).save(*args, **kwargs)


class Entry(models.Model):
    """
    博客文章
    """
    owner = ((True, '原创'), (False, '转载'))
    publish = ((True, '发布'), (False, '草稿'))

    category = models.ForeignKey(Category, null=True, verbose_name='类别')
    own = models.BooleanField('属性', choices=owner, default=True)
    published = models.BooleanField('状态', choices=publish, default=False)
    title = models.CharField('标题', max_length=255)
    slug = models.SlugField(unique=True, max_length=100)
    content = models.TextField('内容')
    timestamp = models.DateTimeField('时间戳', default=datetime.now, db_index=True)
    read_num = models.IntegerField('阅读次数', default=0, editable=False)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-timestamp', 'id']
        unique_together = ('title', 'category')

    def __str__(self):
        return '%s' % self.title

    def save(self, *args, **kwargs):
        """
        自动生成拼音slug
        """
        # 空格转下划线
        title = self.title.replace(' ', '_').lower()
        # 去除转载等标识
        type_index = title.find(']')
        if type_index > 0:
            title = title[type_index+1:]
        # 删除非单词字符
        title = re.sub(r'\W+', '', title)
        # 汉字转拼音
        name_pinyin = lazy_pinyin(title)
        self.slug = '_'.join(name_pinyin)[:100]
        super(Entry, self).save(*args, **kwargs)

    def get_html_content(self):
        return markdown(self.content,
                        extensions=['markdown.extensions.tables',
                                    'markdown.extensions.fenced_code',
                                    'markdown.extensions.codehilite']
                        )

    def get_synopsis(self):
        synopsis = self.content[:100]
        last_section_index = synopsis.rfind('\n')
        if last_section_index > 0:
            synopsis = synopsis[:last_section_index]
        return markdown(synopsis)
