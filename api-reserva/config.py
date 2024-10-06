import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/nombre_base_datos' #Esto se cambia pones tu user, password y nombre de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
