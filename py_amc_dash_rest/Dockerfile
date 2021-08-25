# docker run --name amc_dash_rest -p 5000:5000 cnccodecreater/amc_dash_rest:0.0.2
# docker build -t cnccodecreater/amc_dash_rest:0.0.2 .

FROM python:3.9.5-alpine

LABEL MAINTAINER="Stephan Flachsbart <cnccodecreater@eclipso.email>"

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY app/ /app/
# RUN pip install gunicorn

EXPOSE 5000
# 
# CMD ["python", "app/app.py", "--host", "0.0.0.0:5000"]
CMD ["flask", "run", "--host", "0.0.0.0"]
# CMD flask run --host=0.0.0.0
# CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]