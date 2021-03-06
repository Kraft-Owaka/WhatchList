import os

     

class Config:
    '''
    General configuration parent class
    '''
    
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = 'bc29199ac8b2b522fd951d97e0da5c62'
    # app.config['SECRET_KEY'] = SECRET_KEY

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kraft:moringaschool24@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}

