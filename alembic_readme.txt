alembic revision --autogenerate -m "comment"             Главная команда. Сравнивает модели SQLAlchemy с базой и автоматически создает файл миграции.

alembic init <directory>                                Создает структуру папок миграций в проекте (обычно alembic init migrations).
alembic upgrade head                                    Применяет все новые миграции к базе данных (обновляет до последней версии).
alembic downgrade -1                                    Откатывает последнюю примененную миграцию.
alembic history --verbose                               Показывает список всех миграций и их статусы.
alembic current                                         Показывает текущую версию (хэш) базы данных.