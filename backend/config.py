import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'bcc-secret-key-12345')
    DATABASE_PATH = os.path.join(BASE_DIR, 'data', 'faces.db')
    MODEL_NAME = 'antelopev2'
    MODEL_ROOT = os.path.join(BASE_DIR, 'backend', 'models', 'cache')
    DEBUG = False
    TESTING = False
    CORS_ORIGINS = "*"

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    BCC_ENV = "development"

class ProductionConfig(Config):
    """Production configuration."""
    BCC_ENV = "production"
    # In production, we might want to specify strict CORS
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:4200')

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    BCC_ENV = "testing"
    DATABASE_PATH = os.path.join(BASE_DIR, 'data', 'test_faces.db')
    DEBUG = True

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

def get_config():
    env = os.environ.get('BCC_ENV', 'development').lower()
    return config_by_name.get(env, DevelopmentConfig)
