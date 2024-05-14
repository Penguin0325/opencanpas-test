# ビルドイメージ
FROM python:3.12-slim-bookworm

# パッケージ更新
RUN apt-get -y update
RUN apt-get -y install \
    gcc 

# Flaskとuwsgiをpipで取得
RUN python -m pip install Flask uwsgi

