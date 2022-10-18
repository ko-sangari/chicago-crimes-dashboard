# backend/Dockerfile

FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/base.pip app/requirements.pip

WORKDIR /app

RUN pip install -r requirements.pip

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000" , "--reload"]
