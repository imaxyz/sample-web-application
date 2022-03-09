import os


def main():
    import logging
    logging.basicConfig()

    os.environ["DJANGO_SETTINGS_MODULE"] = "django.conf.global_settings"

    from django.conf import global_settings
    global_settings.SECRET_KEY = "SECRET"
    global_settings.INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'sample_app.django.my_modules',
    )
    global_settings.DEBUG = True
    global_settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }

    logging.log(100, 'sample test message!')

    pass


if __name__ == '__main__':
    main()
