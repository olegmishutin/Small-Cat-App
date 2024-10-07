import os
from django.db import models
from django.db.models import Q, F
from django.contrib.auth import get_user_model
from .validators import check_cat_age


def upload_cat_image_to(instance, file):
    return f'{instance.owner.username}/{file}'


class Cat(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='cats', verbose_name='Хозяин', on_delete=models.CASCADE)

    name = models.CharField('Имя', max_length=128)
    age = models.PositiveSmallIntegerField('Возраст', validators=[check_cat_age])
    breed = models.CharField('Порода', max_length=128)
    color = models.CharField('Цвет', max_length=96)
    favorite_food = models.TextField('Любимая еда', null=True, blank=True)

    _photo = models.ImageField('Фотография', upload_to=upload_cat_image_to, db_column='photo', null=True, blank=True)

    class Meta:
        db_table = 'Cat'
        verbose_name = 'Кошка'
        verbose_name_plural = 'Кошки'
        constraints = [
            models.CheckConstraint(
                check=Q(age__lte=30) | Q(age__gte=1),
                name='cat_age_between_1_and_30',
                violation_error_message='Возраст не может быть меньше 1 и больше 30'
            )
        ]

    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, file):
        if file:
            if self._photo and os.path.exists(self._photo.path):
                os.remove(self._photo.path)
            self._photo = file

    def delete(self, using=None, keep_parents=False):
        if self._photo and os.path.exists(self._photo.path):
            os.remove(self._photo.path)

        return super().delete(using, keep_parents)

    def __str__(self):
        return self.name
