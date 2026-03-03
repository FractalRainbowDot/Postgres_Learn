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