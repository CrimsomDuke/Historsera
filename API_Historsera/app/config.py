

# Creamos las configuraciones para el proyecto
class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/historsera'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = '../media/images';
