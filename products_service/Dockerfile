# product-service/Dockerfile

FROM python:3.8

ENV PORT=5000 \
    HOST=<HOST_END_POINT: OPEN_SEARCH> \
    REGION=ap-south-1 \
    ACCESS_KEY=<ACCESS_KEY> \
    SECRET_KEY=<SECRET_KEY>


WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]