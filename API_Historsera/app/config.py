

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
    PROJECT_MEDIA_PATH = 'C:/MediaTemp/'  # absolute path
    IMAGES_FOLDER = PROJECT_MEDIA_PATH + 'images' #Path relative to the app folder
    PDFS_FOLDER = PROJECT_MEDIA_PATH + 'pdfs' #Path relative to the app folder
