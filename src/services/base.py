from src.core.db_manager import DBManager


class BService:
    def __init__(self, db: DBManager):
        self.db = db