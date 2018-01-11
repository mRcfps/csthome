FROM python:3.5

ENV PYTHONBUFFERED 1

RUN mkdir /src
WORKDIR /src

ADD requirements.txt /src/
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

ADD . /src/

EXPOSE 8000

CMD [ "./runserver.sh" ]
