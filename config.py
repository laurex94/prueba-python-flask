from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY', default='you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URI', default='"postgresql://postgres:postgres@flask_db:5432/postgres"')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
