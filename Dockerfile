FROM python:3.5

ENV PYTHONBUFFERED 1

# RUN apt-get update \
#     && apt-get install -y sqlite3 \
#     && rm -rf /var/lib/apt/lists/*

RUN mkdir /csthome
WORKDIR /csthome
ADD . /csthome/

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
    -r requirements.txt \
    && python manage.py migrate

EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
