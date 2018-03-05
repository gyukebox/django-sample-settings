"""
리모트 개발 환경 설정입니다.
ALLOWED_HOSTS 필드를 수정 후 사용하시는걸 추천드립니다.
원격 서버에 맞게 데이터베이스 설정 또한 바꾸시면 됩니다.

Settings for production environment.
Make sure DEBUG is checked as False.
Rather than using wildcard, modify the ALLOWED_HOSTS field.
Modify DATABASES settings according to your remote server environment.
"""

from django_sample_settings.settings.base import *

DEBUG = False
# Wildcard 를 쓰기 보다는 수정하시는 것을 추천드립니다.
ALLOWED_HOSTS = ['*']

# 로컬 데이터베이스 설정을 해주시면 됩니다
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 추가로 설정이 더 필요하신 경우 아래에 추가하시면 됩니다
