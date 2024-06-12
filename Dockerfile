FROM python:3.12

WORKDIR /WORKDIR

COPY ./requirements.txt /WORKDIR/requirements.txt

RUN apt-get update && apt-get install -y netcat-openbsd \
    && pip install --no-cache-dir -r requirements.txt

COPY . /WORKDIR

COPY ./entrypoint.sh /WORKDIR/entrypoint.sh

RUN chmod +x /WORKDIR/entrypoint.sh

CMD ["/WORKDIR/entrypoint.sh"]
