# order_service/Dockerfile

FROM python:3.8

ENV PORT=5001 \
    TABLE_NAME=mcart-order-details \
    REGION=ap-south-1 \
    ACCESS_KEY=<ACCESS_KEY> \
    SECRET_KEY=<SECRET_KEY>


WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5001
CMD ["python", "app.py"]