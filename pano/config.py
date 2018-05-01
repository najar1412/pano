import os


class Config(object):
    app_root = os.path.dirname(os.path.abspath(__file__))
    UPLOAD_FOLDER = os.path.join(app_root, 'static', 'pano')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = 'lkjhkljh23kj4h23kj4hk23j4h'