from .base_config import BaseConfig

class TestingConfig(BaseConfig):
    TESTING = True
    PORT = 9999
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'