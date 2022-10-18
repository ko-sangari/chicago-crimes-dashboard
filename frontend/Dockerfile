FROM python:3.9

COPY requirements/base.pip app/requirements.pip

WORKDIR /app

RUN pip install -r requirements.pip

COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "src/main.py", "--logger.level=debug"]
