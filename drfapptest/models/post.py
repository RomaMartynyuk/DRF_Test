from django.db import models


class Post(models.Model):
    """
    Model of a post.
    Link:
    - Many to One Author
    - Many to Many Tag
    """

    STATUS_CHOICES = [
        ('draft', 'Чорновик'),
        ('published', 'Опублікований'),
        ('archived', 'Архівований'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Slug'
    )
    content = models.TextField(
        verbose_name='Вміст'
    )
    excerpt = models.TextField(
        max_length=300,
        blank=True,
        verbose_name='Короткий опис'
    )

    # Many to One Author
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )

    # Many to Many Tag
    tags = models.ManyToManyField(
        'Tag',
        blank=True,
        related_name='posts',
        verbose_name='Теги'
    )

    featured_image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name='Зображення'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft',
        verbose_name='Статус'
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Кількість перглядів'
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name='Рекомендують'
    )

    published_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата публікації'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата оновлення'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'
        ordering = ['-published_ad', '-created_at']
        indexes = [
            models.Index(fields=['status', 'published_at']),
            models.Index(fields=['author', 'status']),
        ]

    def __str__(self):
        return self.title