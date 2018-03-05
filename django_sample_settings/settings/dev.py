"""
로컬 개발 환경 설정입니다.
"""

from django_sample_settings.settings.base import *

DEBUG = True

# 로컬 데이터베이스 설정을 해주시면 됩니다
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 추가로 설정이 더 필요하신 경우 아래에 추가하시면 됩니다
