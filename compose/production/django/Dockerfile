FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
ADD ./requirements.txt /
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r /requirements.txt

COPY ./compose/production/django/gunicorn.sh /gunicorn.sh
RUN sed -i 's/\r//' /gunicorn.sh
RUN chmod +x /gunicorn.sh

COPY ./compose/production/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /app

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
