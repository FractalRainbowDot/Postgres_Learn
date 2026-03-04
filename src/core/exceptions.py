class ApplicationException(Exception):
    """
    Базовый класс для всех кастомных исключений в приложении.
    """
    status_code: int = 500

    @property
    def message(self) -> str:
        """Сообщение об ошибке по умолчанию."""
        return "Произошла непредвиденная ошибка в приложении."

    def __str__(self):
        return self.message

class CounterNahryukError(ApplicationException):
    status_code: int = 403

    @property
    def message(self) -> str:
        return "There's no place for dirty pigs!"

class DataNotFound(ApplicationException):
    def __init__(self, filter_kwargs: dict = None):
        self.filter_kwargs =  filter_kwargs
    status_code: int = 404

    @property
    def message(self) -> str:
        return f"Not found {self.filter_kwargs}"