from django.db import models


class Tag(models.Model):
    """
    Модель Тег
    """
    name = models.CharField(max_length=128, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Модель Статья
    """
    title = models.CharField(max_length=256, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    """
    Модель Статьи-Разделы
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной', default=False)

    class Meta:
        verbose_name = 'Раздел статьи'
        verbose_name_plural = 'Разделы статей'
        unique_together = ('article', 'is_main')

    def clean(self):
        if self.is_main:
            # Проверяем, что есть только один основной раздел для каждой статьи
            main_scopes = Scope.objects.filter(article=self.article, is_main=True)
            if self.pk:
                main_scopes = main_scopes.exclude(pk=self.pk)
            if main_scopes.exists():
                raise ValidationError('У статьи может быть только один основной раздел.')
        super().clean()
