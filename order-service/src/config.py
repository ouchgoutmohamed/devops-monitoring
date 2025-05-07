class Config:
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///orders.db'
    SECRET_KEY = 'your_secret_key_here'
    JSON_SORT_KEYS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:'