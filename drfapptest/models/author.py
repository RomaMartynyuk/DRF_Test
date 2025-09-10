from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Author(models.Model):
    """
    Model to represent an author
    Link: One-to-Many relationship to a Post
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Користувач'
    )
    bio = models.TextField(
        max_length=500,
        blank=True,
        verbose_name='Біографія'
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        verbose_name='Аватар'
    )
    website = models.URLField(
        blank=True,
        verbose_name='Вебсайт'
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Дата народження'
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
        verbose_name = 'Автор'
        verbose_name_plural = 'Автори'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" or self.user.username

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username

    @property
    def posts_count(self):
        return self.posts.count()