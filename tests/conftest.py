import pytest

from app import create_app, db
from app.config.testing_config import TestingConfig

@pytest.fixture(scope='session')
def app():
    app = create_app(TestingConfig)
    print(f"Environment: {app.config['ENV']}")
    print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()
