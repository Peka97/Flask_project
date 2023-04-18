import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/blog.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "8f42a73054b1749f8f58848be5e6502c"
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'cosmo'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestConfig(BaseConfig):
    TESTING = True


class ProdConfig(BaseConfig):
    pass
