from django.db import models

from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='First Name', default='Anonymous')
    last_name = models.CharField(max_length=150, verbose_name='Last Name', default='Anonymous')
    phone = models.CharField(max_length=35, verbose_name='Phone Number', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Activ')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        # abstract = True # данная модель станет абстрактным базовым классом
        # app_label = 'users' # если модель определена за пределами app., то таким образом можно ее к нему отнести
        # ordering = [-1] # изменение порядка полей в модели
        # proxy = True # модель будет рассматриваться как прокси модель
        # permissions = [] # добавляются группы пользователей, которые могут изменять сущность данной модели
        # db_table = 'my_users' # перезаписать имя таблицы в БД
        # get_latest_by = 'birth_date' # возвращает последний объект по порятку возрастания
