# FROM : base image 지정 / 이번 장고 컨테이너에서는 애초에 파이썬3.9.0이 설치되어있는 환경을 베이스 이미지로 사용할 계획
FROM python:3.9.0

# 우선 홈을 경로로 지정
WORKDIR /home/

# 깃허브내용가져오기
RUN git clone https://github.com/ae-min/pinterest.git

# 홈 경로 하위로 내 프로젝트 주소 생김
WORKDIR /home/pinterest/

# requirements.txt 파일에 적힌 모든 라이브러리를 설치한다
RUN pip install -r requirements.txt

# 민감정보를 제외하고 깃허브에 업로드되게 했으므로, 깃허브에는 시크릿 키 정보가 없어서 정상적으로 실행이 안됨.
# 그래서 일단 임시적으로 이곳에 시크릿키 적어둠. 나중에 이 문제는 다시 해결 예정
# > .env : 이렇게 적어두면 실제 이미지 안에서도 시크릿키가 들어있는 env 파일이 생성됨.
RUN echo "SECRET_KEY=django-insecure-!s^vkv!)-v6t5&-2*y29vc*c)5ja$!j&!lu&gu6qx$s^!q6(qa" > .env

# migrate : DB랑 연동시키는 작업
RUN python manage.py migrate

# 포트 번호 지정 / 8000번 포트를 통해 접속 가능하도록 설정
EXPOSE 8000

# 장고 컨테이너가 생성될 때마다 실행될 커맨드 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
