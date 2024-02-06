import os

# Flask settings
FLASK_SERVER_NAME = 'localhost:5001'
FLASK_SERVER_PORT = 5001
FLASK_DEBUG = False  # Do not use debug mode in production


# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False


def _version_build():
    dpath = os.path.dirname(__file__)
    try:
        with open(os.path.join(dpath, 'VERSION'), encoding="utf-8") as filereader:
            version = filereader.read().strip()
    except IOError:
        version = '1.0.1a'
    try:
        with open(os.path.join(dpath, 'BUILD'), encoding="utf-8") as filereader:
            build = filereader.read().strip()
    except IOError:
        build = '0'

    return f'{version}.{build}'


MCART_API_VERSION = _version_build()
