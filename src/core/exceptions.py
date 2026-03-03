class ApplicationException(Exception):
    """
    Базовый класс для всех кастомных исключений в приложении.
    """
    @property
    def message(self) -> str:
        """Сообщение об ошибке по умолчанию."""
        return "Произошла непредвиденная ошибка в приложении."

    def __str__(self):
        return self.message