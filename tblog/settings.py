# coding:utf-8


"""
Django settings for tblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# import ugettext_lazy for location
from django.utils.translation import ugettext_lazy as _

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y_+j79%qw9t(jy4aql)8=$ozdgt!^m41+m9b8yq$vdvw%__^+2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagination',
    # django-wmd-editor,markdown editor(used in admin)
    'wmd',
    # markdown_deux,convert markdown to html(used in template).
    'markdown_deux',
    # My apps
    'apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.common.commonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',

)

ROOT_URLCONF = 'tblog.urls'

WSGI_APPLICATION = 'tblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh'
#LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# Begin added for suit by Tulpar,20140908
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request"
)

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': _(u'T-Blog'),
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        #    'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'blog': 'icon-leaf',
    },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        # 'sites',
        # 'auth',
        # Rename app and set icon
        # {'app': 'auth', 'label': 'Authorization', 'icon':'icon-lock'},
        #
        # {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
        # {'label': _('Auth'), 'icon':'icon-lock', 'models': ('auth.user', 'auth.group')},

        # {'app': 'apps.blog', 'icon':'icon-leaf', 'models': ('Article', 'Category')},
        # {'label': _('Blog'), 'icon':'icon-leaf', 'models': ('apps.blog.Article', 'apps.blog.Category')},
        #{'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    ),

    # misc
    # 'LIST_PER_PAGE': 15
}
# End

# Begin. Settings for MEDIA, STATIC, TEMPLATE
MEDIA_ROOT = os.path.join(BASE_DIR, 'public/media'),
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'public/static/blog/'),
    ("css", os.path.join(STATIC_ROOT,'css')),
    ("js", os.path.join(STATIC_ROOT,'js')),
    ("images", os.path.join(STATIC_ROOT,'images')),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'public/templates/'),
)

# End
# For django-wmd-editor,the markdown editor
WMD_ADMIN_SHOW_PREVIEW = True
