FROM python:latest
MAINTAINER Matthew Barr "mbarr@mbarr.net"
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["person-redis.py"]