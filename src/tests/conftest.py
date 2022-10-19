import pytest
from src import create_app, db  # updated


@pytest.fixture(scope='module')
def test_app():
    app = create_app()
    app.config.from_object('src.config.TestingConfig')
    with app.app_context():
        yield app #Testing happens here

@pytest.fixture(scope='module')
def test_database():
    db.create_all()
    yield db #Testing happens here
    db.session.remove()
    db.drop_all()
