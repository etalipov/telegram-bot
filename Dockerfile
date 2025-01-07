FROM python:3.12.0

WORKDIR /app

COPY . .

RUN pip install -r k8s/requirements.txt

CMD ["python", "main.py"]