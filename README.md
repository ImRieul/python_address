# 공공데이터 청년인턴 데이터 분류를 위한 프로그램


## 개발 환경
- Python 3.9.2


## 실행 전 세팅
### setting.py

---
> 저장되어있는 변수
> - KAKAO_TOKEN
> - ROOT_PROJECT

KAKAO_TOKEN은 노춛되면 위험하기 때문에 이 파일을 Github에 올려놓지 않았습니다.
(토큰이 없으면 address.py를 사용할 수 없습니다.)

필요한 변수 값으로는

    ROOT_PROJECT = os.path.dirname(os.path.abspath(__file__))

이 있습니다.


### sample.xlsx

---
마찬가지로 보안상 올려놓지 않았습니다.

추후에 샘플 데이터를 넣을 예정입니다.


### pyvenv.cfg

---
Python Interpreter에 관한 설정 파일입니다.

이 파일을 수정하지 않으면 코드가 작동하지 않습니다.

- window 
    ```
    home = {PATH}
    implementation = CPython
    version_info = 3.9.2.final.0
    include-system-site-packages = false
    base-prefix = {PATH}
    prefix = {PATH}
    base-executable = {PATH}\python.exe
    ```
- Mac
    ```
    home = {PATH}
    include-system-site-packages = false
    version = 3.9.2
    ```

PATH : 파이썬이 설치된 폴더


### Python Interpreter

- [window 3.9.2](https://www.python.org/downloads/release/python-392/)
- mac

  ``` pyenv install 3.9.2```

### 외부 라이브러리

---
윈도우와 맥 venv가 서로 연동되지 않아 따로 설치해줘야 합니다.

바로바로 설치하고 있으나, 읽지 못하는 경우는 아래를 참고해서 설치하면 됩니다.

    pip install [libray name] (가상환경 진입 후)
> - requests
> - openpyxl
> - pandas
