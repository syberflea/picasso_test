# Тестовое задание: Загрузка и обработка файлов

## Технологии
 - Python 3.9
 - Django 3.2.3
 - Django REST framework 3.12.4
 - Celery 5.2.7
 - Redis

## Локальное развертывание проекта
1. Клонируйте репозиторий git@github.com:syberflea/picasso_test.git.
2. В каталоге с проектом  запустите docker compose в режиме демона:
```
sudo docker compose -f docker-compose.production.yml up -d`
```

3. Выполните миграции:
```
sudo docker compose -f docker-compose.yml exec web python manage.py migrate
```

4. Соберите статику:
```
sudo docker compose -f docker-compose.yml exec web python manage.py collectstatic --no-input
```

5. После завершения сборки откройте браузур и перейдите к http://127.0.0.1:8000

(с) Евгений Андронов, 2023