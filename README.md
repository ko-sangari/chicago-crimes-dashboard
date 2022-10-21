# 🚨 Chicago Crimes Dashboard
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) [![Docker](https://badgen.net/badge/icon/docker?icon=docker&label)](https://https://docker.com/) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

![Screenshot from 2022-10-18 17-14-06](https://user-images.githubusercontent.com/38611172/196439960-fa6f2882-0ac3-488f-918e-577e95c1d5b8.png)

***
## Contents
- [The project's purpose](#The-project's-purpose)
- [What used to make this project](#What-used-to-make-this-project)
- [Before you begin](#Before-you-begin)
- [how to run project](#How-to-run-project)
- [how to run tests](#How-to-run-tests)
- [Final step](#Final-step)
***

## The project's purpose
This project is a visual interface for a BigQuery public dataset of Chicago's crimes. You can filter the dataset based on Crime type and Date, and check the exact location of the crimes on Chicago's map. The whole project is written in Python.
So, let's enjoy it! 
***

## What used to make this project
| Technology | 🔗 |
| ------ | ------ |
| Chicago Crime Dataset | [[Google Cloud Link](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=chicago_crime&page=dataset&project=chicagocrime-1665562906614)] [[Kaggle Link](https://www.kaggle.com/code/paultimothymooney/how-to-query-the-chicago-crime-dataset/notebook)] |
| Fastapi | [[Github Link](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#before-you-begin)] |
| Python-BigQuery | [[Github Link](https://github.com/googleapis/python-bigquery)] |
| aioredis | [[Github Link](https://github.com/aio-libs/aioredis-py)] |
| httpx | [[Github Link](https://github.com/encode/httpx)] |
| Pytest | [[Github Link](https://github.com/pytest-dev/pytest)] |
| Streamlit | [[Github Link](https://github.com/streamlit/streamlit)] |
| Docker | [[Github Link](https://github.com/docker-library/python)] |
| Docker-Compose | [[Github Link](https://github.com/docker/compose)] |
| GitHub | [[Github Link](https://github.com/)] |
***

## Before you begin
1. You need JSON Credentials for using BigQuery API.
If you don't have it, [click here](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#before-you-begin) to go to Google instructions. 
2. Where to put that JSON file?
you can put it in _backend_ directory project or anywhere you want, BUT you should add that path in _backend/.env_ variable bellow.
</br>⚠️ In project, both Backend & Frontend folders has a _.env.sample_ file, which you should rename it to _.env_ and setup your variables.
```sh
GOOGLE_CREDENTIALS=./GoogleCredentials.json
```
3. If you need to check the installed packages, they are in _requirements_ folder under Backend or Frontend folder and splited to *base.pip* & *dev.pip* .
***

## How to run project
There is a _docker-compose.dev.yml_ in root folder, which can help to run the project easily. I'll show you how to use it.
</br>⚠️ Both Backend & Frontend folders has their own _Dockerfile_.
```sh
docker-compose -f docker-compose.dev.yml up -d --build
```
And to access the dashboard, just open below link in your browser.
```sh
http://localhost:8501/
```
***

## How to run tests
Both Backend & Frontend folders have the tests folder, in which you can run _pytest_ command to run the tests separately.
<br/>And, what about Test Coverage?
```sh
pytest

coverage run -m pytest
coverage report
# Name                            Stmts   Miss  Cover
# -----------------------------------------------------
# Backend  Test Coverage TOTAL     185      5    97%
# Frontend Test Coverage TOTAL      56      0   100%

```
***

## Final step
##### Be Happy Even if Things Aren’t Perfect Now. 🎉🎉🎉

![](https://i1.wp.com/justmaths.co.uk/wp-content/uploads/2016/10/celebration-gif.gif)
