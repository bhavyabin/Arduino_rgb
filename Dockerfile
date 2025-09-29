FROM python:3.12
WORKDIR /Arduino_rgb
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]