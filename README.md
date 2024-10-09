# Для локального запуска

- Создайте файл .env в каталоге server со следующим наполнением:

```
SECRET_KEY = 'django-insecure-6#8&2dcr3&@reg$2$=h(o*tj1*38$472ql7%s+_934b^b#m5ae'
DB_NAME = 'cat_project'
DB_USER = 'postgres'
DB_PASSWORD = '123456'
DB_HOST = 'pgdb'
DB_PORT = '5432'
REDIS_URL = 'redis://redis:6379/1'
```

- Перейдите на каталог выше (где файл docker-compose.yml)
- Введите в консоль ``docker-compose up --build``
- Откройте в браузере http://localhost:4200/