

# Creamos las configuraciones para el proyecto
class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROJECT_ABS_PATH = 'C:/Users/PC/Desktop/CrimsomDuke/tareas/Semestre_5/Web_I/Final_Project/Historsera/'  # absolute path


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/historsera'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROJECT_ABS_PATH = 'C:/MediaTemp'  # absolute path
    STATIC_FOLDER = PROJECT_ABS_PATH + 'media/images' #Path relative to the app folder
