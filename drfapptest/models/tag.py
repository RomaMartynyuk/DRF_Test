from django.db import models


class Tag(models.Model):
    """
    Model to represent a tag
    Link: Many to many post
    """
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Назва'
    )

    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Опис'
    )

    color = models.CharField(
        max_length=7,
        default='#007bff',
        help_text='Hexadecimal code',
        verbose_name='Колір тега'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        verbose_name='Тег'
        verbose_name_plural='Теги'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    @property
    def posts_count(self):
        return self.posts.count()