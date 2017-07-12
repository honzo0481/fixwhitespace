FROM python:3.6

ENV PYTHONBUFFERED 1

WORKDIR /code

RUN pip install pytest

ENTRYPOINT ["python", "trimwhitespace.py"]
