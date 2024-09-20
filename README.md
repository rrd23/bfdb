# Проект Telegram бота с веб-интерфейсом

Этот проект включает в себя Telegram бота и веб-приложение на Flask с интеграцией Telegram.

## Структура проекта

- `bot_app/`: Код Telegram бота
- `flask_app/`: Веб-приложение на Flask
- `data/`: Данные для nginx и certbot
- `docker-compose.yml`: Конфигурация Docker Compose

## Запуск проекта

1. Установите Docker и Docker Compose
2. Заполните `.env` файл необходимыми данными
3. Запустите проект командой: `docker-compose up -d`

## Настройка

- Настройте Telegram бота в `bot_app/main.py`
- Настройте веб-приложение в `flask_app/app.py`
- Настройте nginx в `data/nginx/default.conf`
