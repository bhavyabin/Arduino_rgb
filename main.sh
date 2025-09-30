cd Arduino_rgb

git pull

source .venv/bin/activate

pip install gunicorn

python gunicorn_config.py

nohup gunicorn app:app &
