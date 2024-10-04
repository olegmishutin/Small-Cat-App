from django.db import models
from django.db.models import Q, F
from django.contrib.auth import get_user_model
from .validators import check_cat_age, check_hair_color_is_hex


def upload_cat_image_to(instance, file):
    return f'{instance.owner.username}/{file}'


class Cat(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='cats', verbose_name='Хозяин', on_delete=models.CASCADE)

    name = models.CharField('Имя', max_length=128)
    age = models.PositiveSmallIntegerField('Возраст', validators=[check_cat_age])
    breed = models.CharField('Порода', max_length=128)
    hex_hair_color = models.CharField('Цвет кошки', max_length=6, validators=[check_hair_color_is_hex])
    favorite_food = models.CharField('Любимая еда', max_length=128)

    photo = models.ImageField('Фотография', upload_to=upload_cat_image_to)

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

    def __str__(self):
        return self.name
