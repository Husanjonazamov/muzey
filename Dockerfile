FROM python:3.12
ENV PIP_CACHE_DIR=/root/.cache/pip

WORKDIR /code

COPY . /code/

RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

CMD sh ./scripts/entrypoint.sh
