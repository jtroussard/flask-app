from .base_config import BaseConfig

class DevConfig(BaseConfig):
    DEBUG = True
    PORT = 12031
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'