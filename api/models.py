from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Role(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'


class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name='E-mail',
        help_text='Введите e-mail',
        unique=True,
        db_index=True
    )

    role = models.CharField(
        verbose_name='Роль',
        help_text='Выберите роль',
        max_length=30,
        choices=Role.choices,
        default=Role.USER
    )

    bio = models.TextField(
        blank=True,
        verbose_name='Описание',
        help_text='Добавьте описание'
    )

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == Role.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == Role.MODERATOR


User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Наименование',
        help_text='Введите имя'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Введите идентификатор',
        db_index=True
    )

    class Meta:
        ordering = ['slug']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Наименование',
        help_text='Введите имя'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Идентификатор',
        help_text='Введите идентификатор',
        db_index=True
    )

    class Meta:
        ordering = ['slug']
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name


class Title(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles'
    )
    genre = models.ManyToManyField(Genre)
    name = models.CharField(
        verbose_name='Наименование',
        help_text='Введите имя',
        max_length=100
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
        help_text='Введите год',
        validators=[MaxValueValidator(datetime.today().year)],
        db_index=True
    )
    description = models.CharField(
        max_length=50,
        verbose_name='Описание',
        help_text='Введите описание',
        blank=True
    )

    class Meta:
        ordering = ['pk']
        verbose_name = 'title'
        verbose_name_plural = 'titles'

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(max_length=500)
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Введите дату',
        auto_now_add=True
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Оценка',
        help_text='Поставьте оценку',
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'
        unique_together = ['author', 'title']

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите комментарий',
        max_length=200
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        help_text='Введите дату',
        auto_now_add=True
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text
