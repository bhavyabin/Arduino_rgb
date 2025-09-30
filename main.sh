

git pull

source .venv/bin/activate

pip install gunicorn

python gunicorn_config.py

nohup gunicorn app:app -w 4 -b 0.0.0.0:5000 &
