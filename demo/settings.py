import pathlib
import views, errors

BASE_DIR = pathlib.Path(__file__).parent.resolve()

# ADDRESS AND PORT
ADDRESS = ''
PORT = 80

# VIEWS
urls = {
    '/welcome': views.welcome,
}
errors = {
    404: errors.not_found,
}

# CORS
CORS_ALLOWED_ORIGINS = [
    'http://localhost',
    'https://localhost',
    'http://localhost:3001'
]
CORS_ALLOW_CREDENTIALS = False

# STATIC FILES
STATIC_URL_BASE = '/static/'
STATIC_FILES_DIR = BASE_DIR / 'static/'

# MEDIA FILES
MEDIA_URL_BASE = '/media/'
MEDIA_FILES_DIR = BASE_DIR / 'media/'

# HTTPS
USE_HTTPS = False
CERTIFICATE_PATH = ''
PRIVATE_KEY_PATH = ''
PRIVATE_KEY_PASSWD = ''
