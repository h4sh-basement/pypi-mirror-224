from django.contrib.auth import get_user_model
from django.core.validators import MaxLengthValidator
from django.db import models

from badi_utils.dynamic_models import BadiModel
from badi_utils.validations import BadiValidators

User = get_user_model()


class BlogCategory(models.Model, BadiModel):
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        permissions = (
            ('can_category', 'مدیریت دسته بندی ها'),
        )
        ordering = ['index_order']

    SHOW_TYPES = (
        ('1', 'نمایش نوع 1'),
        ('2', 'نمایش نوع 2'),
        ('3', 'نمایش نوع 3'),
        ('4', 'نمایش نوع 4'),
    )
    title = models.CharField(max_length=30, unique=True, verbose_name='عنوان', )
    father = models.ForeignKey('BlogCategory', verbose_name='زیرمجموعه', on_delete=models.CASCADE, blank=True,
                               null=True,
                               related_name='children')
    index_show = models.BooleanField(default=False, null=True, verbose_name='ترتیب')
    index_order = models.IntegerField(default=0, null=True, blank=True, verbose_name='ترتیب نمایش')
    title_show_type = models.CharField(max_length=2, verbose_name="چیدمان عنوان", choices=SHOW_TYPES, blank=True,
                                       null=True)
    post_show_type = models.CharField(max_length=2, verbose_name="چیدمان پست ها", choices=SHOW_TYPES, blank=True,
                                      null=True)
    # ads = models.ForeignKey(Ads, related_name='categories', on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return self.father.__str__() + ' ' + self.title if self.father else self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.father:
            father = self.father
            while father.father:
                if father == self:
                    ValueError("یک دسته بندی نمی تواند زیر مجموعه یکی از زیرمجموعه های خودش باشد.")
                father = father.father
        else:
            super().save(force_insert, force_update, using, update_fields)


class BlogTag(models.Model, BadiModel):
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'
        permissions = (
            ('can_category', 'مدیریت تگ ها'),
        )
        ordering = ['-pk']

    title = models.CharField(max_length=30, unique=True, verbose_name='عنوان', )
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return self.title


class BlogPost(models.Model, BadiModel):
    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'اخبار'
        permissions = (
            ('can_blog_post', 'مدیریت اخبار'),
        )
        ordering = ['-pk', ]

    title = models.CharField(max_length=200, verbose_name="تیتر")
    pre_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="پیش تیتر")
    picture = models.FileField(upload_to='blog_post/', blank=True, null=True, verbose_name="تصویر")
    slug = models.CharField(max_length=256, verbose_name="متن Slug خبر", validators=[BadiValidators.slug])
    slider_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="تیتر اسلایدر")
    slider_picture = models.FileField(upload_to='blog_post/', blank=True, null=True, verbose_name="تصویر اسلایدر")
    breaking_title = models.CharField(max_length=200, blank=True, null=True, verbose_name="تیتر فوری")
    categories = models.ManyToManyField(BlogCategory, related_name='news', verbose_name="دسته بندی ها")
    tags = models.ManyToManyField(BlogTag, related_name='news', verbose_name="تگ ها")
    is_recommend = models.BooleanField(default=False, verbose_name='پیشنهادی', blank=True)
    short = models.TextField(verbose_name="خلاصه خبر", validators=[MaxLengthValidator(1200)])
    description = models.TextField(verbose_name="شرح خبر", blank=True, validators=[])
    view = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    source_title = models.CharField(max_length=200, null=True, blank=True, verbose_name="عنوان منبع")
    source_link = models.URLField(null=True, blank=True, verbose_name="لینک منبع")
    writer = models.ForeignKey(User, verbose_name='نویسنده', related_name='news', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='زمان ایجاد')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='زمان آخرین ویرایش')

    def __str__(self):
        return self.title


class BlogComment(models.Model, BadiModel):
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
        permissions = (
            ('can_comment', 'مدیریت نظرات'),
        )
        ordering = ['-id']

    description = models.TextField(validators=[MaxLengthValidator(500)], verbose_name="متن دیدگاه")
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده", blank=True, null=True)
    writer_name = models.CharField(max_length=40, blank=True, verbose_name="نام نویسنده")
    writer_phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="شماره تماس نویسنده")
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="خبر", related_name="comments")
    replay = models.ForeignKey('BlogComment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="پاسخ به",
                               related_name='replies')
    is_accepted = models.BooleanField(default=False, blank=True, verbose_name="تایید شده")
    is_rejected = models.BooleanField(default=False, blank=True, verbose_name="رد شده")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='زمان ایجاد')

    def __str__(self):
        return self.writer_name + ' - ' + self.post.__str__()

    @staticmethod
    def get_serializer_fields():
        return ['id', 'description', 'writer', 'writer_name', 'writer_phone', 'post', 'replies', 'replay',
                'created_at', ]

    @staticmethod
    def get_datatable_verbose():
        return ['id',
                "متن دیدگاه",
                "نویسنده",
                "نام نویسنده",
                "شماره تماس نویسنده",
                "فیلم",
                "پاسخ به",
                "تایید شده",
                "رد شده",
                'زمان ایجاد',
                ]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_accepted:
            self.is_rejected = False
        if self.is_rejected:
            self.is_accepted = False
        super().save(force_insert, force_update, using, update_fields)
