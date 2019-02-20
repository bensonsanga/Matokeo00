import os


class Config:
    SECRET_KEY = '17f7be30477de40cce014c700edc75e4'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'benson.s.sanga@gmail.com'
    MAIL_PASSWORD = '3HakunaMatata7'
