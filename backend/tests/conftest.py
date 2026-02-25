import os
import sys
import pytest

# Add backend directory to sys.path to allow importing app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app as flask_app
from database.storage_manager import FaceDataStorage

@pytest.fixture
def app():
    # Set environment to testing
    os.environ['BCC_ENV'] = 'testing'
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def clean_storage():
    # TestingConfig defines a separate test DB path
    storage = FaceDataStorage()
    # Ensure it's clean (or at least initialized)
    # Since sqlite is file based, we could delete the file if we wanted absolute clean state
    if os.path.exists(storage.storage_path):
        os.remove(storage.storage_path)
    storage._init_db()
    return storage
