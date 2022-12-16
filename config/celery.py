import os

from celery import Celery

# Путь к настройкам
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Название celery приложения
celery_app = Celery("braniac")

# Путь, откуда будет забираться конфигурация для celery приложения
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Автоподрузка задач
celery_app.autodiscover_tasks()

# celery -A Braniac worker -l info -- консольная команда для запуска celery, инфо- уровень вывода логов celery в консоль
