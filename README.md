# Django 샘플 환경설정 예시

django 샘플 환경설정 예시입니다.  
파이썬 3.6 버전, 그리고 장고 2.0+ 버전과 호환됩니다.

## 사용방법

1. 이 레포를 클론하세요

```
$ git clone https://github.com/gyukebox/django-sample-settings
```

2. 가상환경을 활성화하고, 의존성을 설치하세요

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

가상환경(=`virtualenv`) 이 설치되어 있지 않으시다면, 다음 명령어로 설치하세요.

```
$ pip3 install virtualenv
```

3. 새로운 앱을 만들고, 장고 개발을 시작하세요!

```
$ python manage.py startapp APP_NAME
```

## 설정방법

`settings` 폴더에는 `base.py`, `dev.py`, `prod.py` 이렇게 세 가지의 파일이 있습니다.  
`base.py` 는 기본 설정 파일입니다.  
`dev.py` 에는 로컬 환경 혹은 개발 시 환경에 대한 설정을 추가하시면 됩니다. 가령, `DEBUG=True` 같은 설정들은 `dev.py` 에서만 활성화되어야 합니다.  
`prod.py` 에는 실제 서비스 환경에서의 설정을 추가하시면 됩니다. 가령, 데이터베이스 설정값이 담긴 환경변수들을 여기서 포함하시면 됩니다.

## 블로그 포스팅

해당 레포지토리는 [이 블로그 글](https://gyukebox.github.io/2018/03/05/django-multiple-settings/) 의 예제 코드를 담은 것입니다. 자세한 내용 참고용으로 사용하세요!

## License
MIT