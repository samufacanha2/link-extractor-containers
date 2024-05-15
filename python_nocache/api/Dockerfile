FROM       python:3.9
LABEL      maintainer="Sawood Alam <@ibnesayeed>"

ENV        REDIS_URL="redis://localhost:6379"

WORKDIR    /app
COPY       requirements.txt /app/
COPY       openssl.cnf /app/
RUN        pip install -r requirements.txt

COPY       *.py /app/
RUN        chmod a+x *.py
RUN        export OPENSSL_CONF=openssl.cnf

CMD        ["./main.py"]
