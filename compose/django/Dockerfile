FROM python:3.7-alpine

# Set Environment Variable
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

# Making source and static directory
RUN mkdir /src
RUN mkdir /static

# Creating Work Directory
WORKDIR /src

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg


# Installing temporary packages required for installing requirements.pip
RUN apk add --no-cache --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev

# Update pip
RUN pip install --upgrade pip

# Installing requirements.pip from project
COPY ./src/requirements.pip /scripts/
RUN pip install --no-cache-dir -r /scripts/requirements.pip

# removing temporary packages from docker and removing cache
RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

# CMD will run when this dockerfile is running
CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; gunicorn core.wsgi -b 0.0.0.0:8000 & celery --app myapp.tasks worker --loglevel=INFO"]
