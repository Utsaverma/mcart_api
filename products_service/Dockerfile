# product-service/Dockerfile

FROM python:3.8

ENV PORT=5000 \
    HOST=search-mcart-opensearch-domain-o4zce3kn7jsej2n4kwowcag7v4.ap-south-1.es.amazonaws.com \
    REGION=ap-south-1 \
    ACCESS_KEY=AKIAZI2LCXTAURHWC65W \
    SECRET_KEY=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


WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]